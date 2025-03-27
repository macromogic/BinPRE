FROM python:3.10

ARG DEBIAN_FRONTEND=noninteractive
ARG NJOBS=8
RUN apt update && apt install -y \
build-essential make gcc g++ cmake \
git vim net-tools wget tar tcpdump less strace \
libcap-dev

## Pin

RUN wget https://software.intel.com/sites/landingpage/pintool/downloads/pin-3.28-98749-g6643ecee5-gcc-linux.tar.gz
RUN tar -xzf pin-3.28-98749-g6643ecee5-gcc-linux.tar.gz
ENV PIN_ROOT="/pin-3.28-98749-g6643ecee5-gcc-linux"
ENV PATH="/pin-3.28-98749-g6643ecee5-gcc-linux:${PATH}"
RUN rm /pin-3.28-98749-g6643ecee5-gcc-linux.tar.gz

## BinPRE

RUN git clone https://github.com/macromogic/BinPRE.git
RUN pip install -r /BinPRE/requirements.txt
RUN cd /BinPRE/src && ./run compile taint
RUN mkdir -p /pcaps
RUN echo "\
cd /BinPRE/src\n\
git checkout dev\n\
git pull\n\
./run compile taint" > /dev.init.sh

## EIP

RUN git clone https://github.com/EIPStackGroup/OpENer.git
RUN cd /OpENer/bin/posix && ./setup_posix.sh && make -j ${NJOBS}
ENV BINPRE_EIP_SERVER="/OpENer/bin/posix/src/ports/POSIX/OpENer"

## HTTP

RUN git clone https://github.com/avih/miniweb.git
RUN make -C /miniweb -j ${NJOBS}
ENV BINPRE_HTTP_SERVER="/miniweb/miniweb"

## DNP3

RUN git clone https://github.com/dnp3/opendnp3.git
RUN cmake -B /opendnp3/build -S /opendnp3 -DDNP3_EXAMPLES=ON && make -C /opendnp3/build -j ${NJOBS}
ENV BINPRE_DNP3_SERVER="/opendnp3/build/cpp/examples/outstation/outstation-demo"

## TFTP

RUN git clone https://git.kernel.org/pub/scm/network/tftp/tftp-hpa.git
RUN make -C /tftp-hpa -j ${NJOBS} && make -C /tftp-hpa install
ENV BINPRE_TFTP_SERVER="/tftp-hpa/tftpd"

## DNS

RUN git clone https://github.com/infinet/dnsmasq.git
RUN make -C /dnsmasq -j ${NJOBS}
RUN echo "\
domain-needed\n\
bogus-priv\n\
filterwin2k\n\
localise-queries\n\
listen-address=10.1.0.1\n\
dhcp-range=lan.hzsogood.net,10.1.0.100,10.1.0.250,255.255.255.0,12h\n\
local=/lan.hzsogood.net/\n\
domain=lan.hzsogood.net\n\
expand-hosts\n\
no-negcache\n\
resolv-file=/etc/resolv.conf\n\
dhcp-authoritative\n\
dhcp-leasefile=/etc/dhcp.leases\n\
read-ethers\n\
dhcp-host=00:14:A4:60:73:66,kong,infinite\n\
dhcp-host=00:1d:d9:45:1f:8a,theharlequin,infinite\n\
dhcp-host=00:01:e6:4e:64:47,printer,infinite" > /dnsmasq.conf
ENV BINPRE_DNS_SERVER="/dnsmasq/src/dnsmasq"

WORKDIR /BinPRE/Artifact_Evaluation/BinPRE_scripts
