# OPENER_PATH=$HOME/OpENer/bin/posix/src/ports/POSIX/
if [ -z "$OPENER_PATH" ]; then
    echo "OPENER_PATH is not set"
    exit 1
fi
./run run taint $OPENER_PATH/OpENer lo
