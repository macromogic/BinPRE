#!/bin/bash

set -u
DEV_CXXFLAGS=
DO_PULL=0
case ${1:-} in
    --pull|-p)
        DO_PULL=1
        ;;
    --testhook|-t)
        DEV_CXXFLAGS="${DEV_CXXFLAGS} -DTESTHOOK"
        ;;
    --verbose-debug|-d)
        DEV_CXXFLAGS="${DEV_CXXFLAGS} -DBINPRE_DEBUG"
        ;;
    *)
        echo "Usage: $0 [--pull|-p] [--testhook|-t] [--verbose-debug|-d]"
        echo "  --pull|-p:           Pull the latest changes from the repository"
        echo "  --testhook|-t:       Build with -DTESTHOOK"
        echo "  --verbose-debug|-d:  Build with -DBINPRE_DEBUG"
        exit 1
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
