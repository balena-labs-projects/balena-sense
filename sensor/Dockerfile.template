FROM balenalib/%%BALENA_MACHINE_NAME%%-python:3-build

ARG BSEC_FILENAME=BSEC_1.4.7.3_Generic_Release_20190410.zip

RUN install_packages \
        unzip

WORKDIR /usr/src/app
RUN git clone https://github.com/balena-io-playground/bsec_bme680_linux.git
RUN wget https://ae-bst.resource.bosch.com/media/_tech/media/bsec/$BSEC_FILENAME
RUN unzip -d bsec_bme680_linux/src $BSEC_FILENAME

WORKDIR /usr/src/app/bsec_bme680_linux
RUN chmod +x make.sh
RUN ./make.sh

RUN pip install smbus

WORKDIR /usr/src/app
COPY ./scripts ./scripts
COPY ./entry.sh /usr/src/app/
RUN chmod +x /usr/src/app/entry.sh

CMD ./entry.sh
