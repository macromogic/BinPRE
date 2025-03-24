#!/bin/bash

set -u
cd ../../src
case $1 in
    modbus)
        ./run run taint ./freemodbus/tcpmodbus
        ;;
    http)
        ./run run taint $BINPRE_HTTP_SERVER -r /BinPRE/httpdata/
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
        ./run run taint $BINPRE_DNS_SERVER -C /dnsmasq.conf -d -i lo
        ;;
    *)
        echo "Usage: $0 [modbus|http|tftp|dnp3|dns]"
        ;;
esac