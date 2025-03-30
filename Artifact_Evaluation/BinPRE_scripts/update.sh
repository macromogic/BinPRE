#!/bin/bash

set -u
DEV_CXXFLAGS=
DO_PULL=0
case ${1:-} in
    --verbose-debug)
        DEV_CXXFLAGS="${DEV_CXXFLAGS} -DBINPRE_DEBUG"
        ;;
    --testhook)
        DEV_CXXFLAGS="${DEV_CXXFLAGS} -DTESTHOOK"
        ;;
    --pull)
        DO_PULL=1
        ;;
esac

BINPRE_PATH=$(dirname $(dirname $(dirname $(realpath $0))))
cd $BINPRE_PATH/src
if [ $DO_PULL -eq 1 ]
then
    git pull
fi

export DEV_CXXFLAGS
./run compile taint
