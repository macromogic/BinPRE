#!/bin/bash

set -u
BINPRE_PATH=$(dirname $(dirname $(dirname $(realpath $0))))
cd $BINPRE_PATH/src
case ${1:-} in
    modbus)
        ./run run taint ./freemodbus/tcpmodbus
        ;;
    s7)
        export LD_LIBRARY_PATH=$PWD/s7/release/Linux/X86_64/glibc_2.21:${LD_LIBRARY_PATH:-}
        ./run run taint ./s7/examples/cpp/x86_64-linux/server
        ;;
    ftp)
        ./run run taint ./ftp/Source/Release/fftp ./ftp/Bin/fftp.conf
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
        killall $BINPRE_DNS_SERVER
        sleep 1
        ./run run taint $BINPRE_DNS_SERVER -C /BinPRE/testdata/dnsmasq.conf -d -i lo
        ;;
    eip)
        ./run run taint $BINPRE_EIP_SERVER lo
        ;;
    mirai)
        ./run run taint $BINPRE_MIRAI_SERVER
        ;;
    *)
        echo "Usage: $0 [modbus|s7|ftp|http|tftp|dnp3|dns|eip|mirai]"
        exit 1
        ;;
esac