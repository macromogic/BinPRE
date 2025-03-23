FROM python:3.10

ARG DEBIAN_FRONTEND=noninteractive
ARG NJOBS=8
RUN apt update && apt install -y \
build-essential make gcc g++ cmake \
git vim net-tools wget tar tcpdump less

## Pin

RUN wget https://software.intel.com/sites/landingpage/pintool/downloads/pin-3.28-98749-g6643ecee5-gcc-linux.tar.gz
RUN tar -xzf pin-3.28-98749-g6643ecee5-gcc-linux.tar.gz
ENV PIN_ROOT="/pin-3.28-98749-g6643ecee5-gcc-linux"
ENV PATH="/pin-3.28-98749-g6643ecee5-gcc-linux:${PATH}"
RUN rm /pin-3.28-98749-g6643ecee5-gcc-linux.tar.gz

## BinPRE

RUN git clone https://github.com/macromogic/BinPRE.git
RUN pip install -r /BinPRE/requirements.txt
RUN cd /BinPRE/src && git checkout dev && ./run compile taint
RUN mkdir -p /pcaps

## HTTP

RUN git clone https://github.com/avih/miniweb.git
RUN make -C /miniweb -j ${NJOBS}

## DNP3

RUN git clone https://github.com/dnp3/opendnp3.git
RUN cmake -B /opendnp3/build -S /opendnp3 && make -C /opendnp3/build -j ${NJOBS}

## TFTP

RUN git clone https://git.kernel.org/pub/scm/network/tftp/tftp-hpa.git
RUN make -C /tftp-hpa -j ${NJOBS}

## DNS

RUN git clone https://github.com/infinet/dnsmasq.git
RUN make -C /dnsmasq -j ${NJOBS}

WORKDIR /BinPRE/Artifact_Evaluation/BinPRE_scripts
