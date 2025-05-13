#!/bin/bash

set -u
SCRIPTS_PATH=$(dirname $(realpath $0))
BINPRE_PATH=$(dirname $(dirname $SCRIPTS_PATH))
BINARYINFERNO_PATH=${BINARYINFERNO_PATH:-$BINPRE_PATH/../binaryinferno}

PROTO=${1:-}
DETECTOR=BE

case $PROTO in
    modbus|s7|ftp|http|tftp|dns|mirai)
        ;;
    dnp3|eip)
        DETECTOR=LE
        ;;
    *)
        echo "Usage: $0 [modbus|s7|ftp|http|tftp|dnp3|dns|eip|mirai]"
        exit 1
        ;;
esac

cd $BINARYINFERNO_PATH/binaryinferno
python3 $SCRIPTS_PATH/mock_client.py $PROTO -d - | python3 blackboard.py --detector $DETECTOR > $PROTO.log 2> >(tee $PROTO.err >&2)
awk '/INFERRED DESCRIPTION/,/SPECEND/' $PROTO.log