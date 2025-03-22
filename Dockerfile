FROM python:3.10

ARG DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y \
build-essential make gcc g++ cmake \
samba git vim net-tools wget tar tcpdump less \
strace smbclient

## Pin

RUN wget https://software.intel.com/sites/landingpage/pintool/downloads/pin-3.28-98749-g6643ecee5-gcc-linux.tar.gz
RUN tar -xzf pin-3.28-98749-g6643ecee5-gcc-linux.tar.gz
ENV PIN_ROOT="/pin-3.28-98749-g6643ecee5-gcc-linux"
ENV PATH="/pin-3.28-98749-g6643ecee5-gcc-linux:${PATH}"

## BinPRE

WORKDIR /
RUN git clone https://github.com/macromogic/BinPRE.git
RUN pip install -r /BinPRE/requirements.txt
RUN cd /BinPRE/src && git checkout dev && ./run compile taint

## SMB2

RUN mkdir -p /shared && chmod 777 /shared
RUN echo "\
[global]\n\
    map to guest = Bad User\n\
    security = user\n\
[shared]\n\
    path = /shared\n\
    read only = no\n\
    browsable = yes\n\
    guest ok = yes\n\
    min protocol = SMB2\n\
" >> /etc/samba/smb.conf

## HTTP

RUN git clone https://github.com/avih/miniweb.git
RUN make -C /miniweb -j4

## DNP3

RUN git clone https://github.com/dnp3/opendnp3.git
RUN cmake -B /opendnp3/build -S /opendnp3 && make -C /opendnp3/build -j4

## TFTP

RUN git clone https://git.kernel.org/pub/scm/network/tftp/tftp-hpa.git
RUN make -C /tftp-hpa -j4

WORKDIR /BinPRE/Artifact_Evaluation/BinPRE_scripts
