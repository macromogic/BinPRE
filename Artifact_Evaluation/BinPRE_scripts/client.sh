#!/bin/bash

set -u
BINPRE_PATH=$(dirname $(dirname $(dirname $(realpath $0))))
cd $BINPRE_PATH/Analyzer

PROTO=${1:-}
BASELINE_MODE=${2:-oa}
EVAL_MODE=index
ENDIAN=big

case $PROTO in
    modbus)
        EVAL_MODE=xx
        ;;
    http|dns)
        ;;
    tftp)
        export SET_TIMEOUT=10
        ;;
    dnp3|eip)
        ENDIAN=little
        ;;
    mirai)
        service mariadb restart
        netstat -tuln | grep '0.0.0.0:55' || /dnsmasq/src/dnsmasq -C /dnsmasq.conf -i lo -p 55
        ;;
    *)
        echo "Usage: $0 [modbus|http|tftp|dnp3|dns|eip|mirai]"
        exit 1
        ;;
esac

echo 0 | python3 fsend_split.py $PROTO 0 0 $BASELINE_MODE $EVAL_MODE $ENDIAN 0