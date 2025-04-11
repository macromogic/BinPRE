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
        ./run run taint $BINPRE_TFTP_SERVER -L --secure /BinPRE/testdata/tftp/
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
    mirai)
        ./run run taint $BINPRE_MIRAI_SERVER
    *)
        echo "Usage: $0 [modbus|http|tftp|dnp3|dns|eip|mirai]"
        ;;
esac