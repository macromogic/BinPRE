#!/bin/bash

set -u
cd ../../Analyzer
case $1 in
    modbus)
        python3 fsend_split.py modbus 0 0 oa xx big 0
        ;;
    http)
        python3 fsend_split.py http 0 0 oa index big 0
        ;;
    tftp)
        echo TFTP not supported yet
        exit 1
        # python3 fsend_split.py tftp 0 0 oa index big 0
        ;;
    dnp3)
        python3 fsend_split.py dnp3 0 0 oa index big 0
        ;;
    dns)
        python3 fsend_split.py dnp3 0 0 oa index big 0
        ;;
    *)
        echo "Usage: $0 [modbus|http|tftp|dnp3|dns]"
        ;;
esac