#!/bin/bash

files_url='https://files.balena-cloud.com' # URL exporting S3 XML
s3_xml=$(curl -L -s $files_url)

# From https://stackoverflow.com/a/7052168
read_dom () {
    local IFS=\>
    read -d \< ENTITY CONTENT
}
s3_bucket=$(while read_dom; do if [[ $ENTITY = "Name" ]] ; then  echo $CONTENT; fi; done <<<"$s3_xml")

# Output arguments to stderr.
function err()
{
	echo "$@">&2
}

# Output arguments to stderr and halt with non-zero exit code.
function fatal()
{
	err "$@"
	exit 1
}

# Output usage and halt.
function usage()
{
	err   "usage: $0 <device type> <version> <module path>"
	fatal "   or: $0 --list - list available devices and versions"
}

function push()
{
	pushd $1 >/dev/null
}

function pop()
{
	popd >/dev/null
}

# Retrieves all available kernel header archives.
# args: $1 - device search pattern (default .*)
#       $2 - version search pattern (default .*)
function get_header_paths()
{
	local dev_pat="${1:-.*}"
	local ver_pat="${2:-.*}"
	list_kernels=$(aws s3api list-objects --no-sign-request --bucket $s3_bucket  --output text  --query 'Contents[]|[?contains(Key, `kernel`)]' | cut -f2)

	while read -r line; do
		if echo "$line" | grep -q "images/$dev_pat/$ver_pat"; then
			device=$(echo "$line" | cut -f2 -d/)
			version=$(echo "$line" | cut -f3 -d/)
			echo "$line"
		fi
	done <<< "$list_kernels"
}

# List available devices and versions.
function list_versions()
{
	list_kernels=$(aws s3api list-objects --no-sign-request --bucket $s3_bucket  --output text  --query 'Contents[]|[?contains(Key, `kernel`)]|[?contains(Key,`images`)]' | cut -f2)

	while read -r line; do
		var1=$(echo "$line" | cut -f1 -d/)
		device=$(echo "$line" | cut -f2 -d/)
		version=$(echo "$line" | cut -f3 -d/)
		printf "%-30s %-30s\n" "$device" "$version"
	done <<< "$list_kernels"
}

# Retrieve kernel module headers from the specified remote path and build kernel
# module against them, generating a new copy of the kernel module with
# ..._<device>_<version> suffix.
function get_and_build()
{
	local path="$1"
	local pattern="^images/(.*)/(.*)/"
	[[ "$path" =~ $pattern ]] || fatal "Invalid path '$path'?!"

	local device="${BASH_REMATCH[1]}"
	local version="${BASH_REMATCH[2]}"
	local output_dir="${module_dir}_${device}_${version}"

	filename=$(basename $path)
	url="$files_url/$path"

	tmp_path=$(mktemp --directory)
	push $tmp_path

	# Workaround for the nuc image. Tools compiled expecting /lib/ld-linux-x86-64.so.2 while it is in /lib64
	if [ -f /lib64/ld-linux-x86-64.so.2 ]; then
		if [ ! -f /lib/ld-linux-x86-64.so.2 ]; then
			ln -s /lib64/ld-linux-x86-64.so.2  /lib/ld-linux-x86-64.so.2
		fi
	fi

	if ! wget $(echo "$url" | sed -e 's/+/%2B/g'); then
		pop
		rm -rf "$tmp_path"

		err "ERROR: $path: Could not retrieve $url, skipping."
		return
	fi

	if ! tar -xf $filename --strip 1; then
		pop
		rm -rf "$tmp_path"

		err "ERROR: $path: Unable to extract $tmp_path/$filename, skipping."
		return
	fi

	# Check if we have fetched the kernel_source tarball
	if [[ $filename == *"source"* ]]; then
		# Prepare tools
		make -C "$tmp_path" modules_prepare
	fi

	pop

	# Now create a copy of the module directory.
	rm -rf "$output_dir"
	mkdir "$output_dir"
	cp -R "$module_dir"/* "$output_dir"

	push "$output_dir"
	make -C "$tmp_path" M="$PWD" modules
	pop

	rm -rf "$tmp_path"

  mkdir compiled
  cp "$output_dir"/*.ko compiled
}

if [[ "$1" = "--list" ]]; then
	echo "Fetching list from servers"
	list_versions
	exit
elif [[ $# -lt 3 ]]; then
	usage
fi

device="$1"
version="$2"
module_dir="$3"

[[ -d "$module_dir" ]] || fatal "ERROR: Cannot find module directory $module_dir"

seen=''

echo "Fetching list from servers"
for path in $(get_header_paths "$device" "$version"); do
	echo "Building $path..."

	get_and_build $path

	seen='y'
done

[[ -n "$seen" ]] || fatal "Could not find headers for '$device' at version '$version', run $0 --list"
