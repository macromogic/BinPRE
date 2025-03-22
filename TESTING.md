# TESTING INSRUCTIONS

It is recommended to use `docker-compose` to build and launch the
container. Or refer to `compose.yml` for execution options.

## Setup

``` bash
docker-compose up -d --build
```

## Connect to the container

``` bash
docker-compose exec testbench /bin/bash
```

If the shell does not show up, the container might not be running.
Make sure `-d` is used to start the container in the background.
