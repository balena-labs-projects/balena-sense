KERNEL_TREE_PATH?=/lib/modules/$(shell uname -r)/build
EXTRA_CFLAGS="-DDEBUG"

obj-m+=bme680_core.o
obj-m+=bme680_i2c.o

all: bme680_core.ko bme680_i2c.ko

bme680_core.ko: bme680_core.c
	make -C $(KERNEL_TREE_PATH) M=$(PWD) modules

bme680_i2c.ko: bme680_i2c.c
	make -C $(KERNEL_TREE_PATH) M=$(PWD) modules

clean:
	make -C $(KERNEL_TREE_PATH) M=$(PWD) clean

.PHONY: all clean
