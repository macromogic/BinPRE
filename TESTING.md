# TESTING INSRUCTIONS

It is recommended to use `docker-compose` to build and launch the
container. Or refer to `compose.yml` for execution options.

## Setup

``` bash
docker-compose up -d --build testbench
```

## Connect to the container

``` bash
docker-compose exec testbench /bin/bash
```

If the shell does not show up, the container might not be running.
Make sure you are right under the project directory. and
`-d` is used to start the container in the background.

## Run scripts

Under `/BinPRE/Artifact_Evaluation/BinPRE_scripts` you will find 
`server.sh` and `client.sh`. You can run them as follows:

``` bash
./server.sh [protocol]
```

``` bash
./client.sh [protocol]
```

## Keeping tools up-to-date

Inside the container:

``` bash
./update.sh # use -p to pull from remote before building
```

