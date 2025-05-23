FROM python:3.10

ARG DEBIAN_FRONTEND=noninteractive
ARG NJOBS=8
RUN apt update && apt install -y \
build-essential make gcc g++ cmake git vim \
net-tools wget tar tcpdump less strace dnsutils telnet \
libcap-dev mariadb-server mariadb-client
COPY <<EOT /root/.vimrc
set nocompatible
syntax on
set number
set mouse=a
set autoindent
set tabstop=4
set shiftwidth=4
set expandtab
set smarttab
set smartindent
set hlsearch
EOT

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

## BinaryInferno

RUN git clone https://github.com/binaryinferno/binaryinferno.git
RUN cd /binaryinferno && git apply /BinPRE/testdata/binaryinferno.patch
ENV BINARYINFERNO_PATH="/binaryinferno"

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
ENV BINPRE_TFTP_SERVER="/tftp-hpa/tftpd/tftpd"

## DNS

RUN git clone https://github.com/infinet/dnsmasq.git
RUN make -C /dnsmasq -j ${NJOBS}
COPY <<EOT /dnsmasq.conf
domain-needed
bogus-priv
filterwin2k
localise-queries
dhcp-range=lan.hzsogood.net,10.1.0.100,10.1.0.250,255.255.255.0,12h
local=/lan.hzsogood.net/
domain=lan.hzsogood.net
expand-hosts
no-negcache
resolv-file=/etc/resolv.conf
interface=lo
interface=eth0
dhcp-authoritative
dhcp-leasefile=/etc/dhcp.leases
dhcp-host=00:14:A4:60:73:66,kong,infinite
dhcp-host=00:1d:d9:45:1f:8a,theharlequin,infinite
dhcp-host=00:01:e6:4e:64:47,printer,infinite
user=root
EOT
ENV BINPRE_DNS_SERVER="/dnsmasq/src/dnsmasq"

## Mirai

RUN wget https://go.dev/dl/go1.24.2.linux-amd64.tar.gz
RUN tar -C /usr/local -xzf go1.24.2.linux-amd64.tar.gz
ENV GOROOT=/usr/local/go
ENV GOPATH=/go
ENV PATH=$GOPATH/bin:$GOROOT/bin:$PATH
RUN rm /go1.24.2.linux-amd64.tar.gz

RUN git clone https://github.com/jgamblin/Mirai-Source-Code.git
RUN <<EOR
set -e
cd /BinPRE
git pull

cd /Mirai-Source-Code
git apply /BinPRE/testdata/mirai.patch
cd mirai
go mod init mirai
go get -u github.com/go-sql-driver/mysql github.com/mattn/go-shellwords
go mod tidy
mkdir -p debug

./build.sh debug telnet
service mariadb start
mysql -uroot < ../scripts/db.sql
EOR
ENV BINPRE_MIRAI_SERVER=/Mirai-Source-Code/mirai/debug/mirai.dbg

WORKDIR /BinPRE/Artifact_Evaluation/BinPRE_scripts