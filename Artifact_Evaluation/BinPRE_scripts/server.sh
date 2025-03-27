#!/bin/bash

set -u
BINPRE_PATH=$(dirname $(dirname $(dirname $(realpath $0))))
cd $BINPRE_PATH/src
case ${1:-} in
    modbus)
        ./run run taint ./freemodbus/tcpmodbus
        ;;
    http)
        ./run run taint $BINPRE_HTTP_SERVER -r /BinPRE/testdata/http/
        ;;
    tftp)
        echo TFTP not supported yet
        exit 1
        # ./run run taint $BINPRE_TFTP_SERVER
        ;;
    dnp3)
        ./run run taint $BINPRE_DNP3_SERVER
        ;;
    dns)
        ./run run taint $BINPRE_DNS_SERVER -C /BinPRE/testdata/dnsmasq.conf -d -i lo
        ;;
    eip)
        ./run run taint $BINPRE_EIP_SERVER lo
        ;;
    *)
        echo "Usage: $0 [modbus|http|tftp|dnp3|dns|eip]"
        ;;
esac