FROM python:3.10

ARG DEBIAN_FRONTEND=noninteractive
ARG NJOBS=8
RUN apt update && apt install -y \
build-essential make gcc g++ cmake git vim \
net-tools wget tar tcpdump less strace dnsutils \
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
COPY <<EOT /dev.init.sh
cd /BinPRE/src
git checkout dev
git pull
./run compile taint
EOT

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
listen-address=10.1.0.1
dhcp-range=lan.hzsogood.net,10.1.0.100,10.1.0.250,255.255.255.0,12h
local=/lan.hzsogood.net/
domain=lan.hzsogood.net
expand-hosts
no-negcache
resolv-file=/etc/resolv.conf
dhcp-authoritative
dhcp-leasefile=/etc/dhcp.leases
read-ethers
dhcp-host=00:14:A4:60:73:66,kong,infinite
dhcp-host=00:1d:d9:45:1f:8a,theharlequin,infinite
dhcp-host=00:01:e6:4e:64:47,printer,infinite
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
cd /Mirai-Source-Code/mirai
sed -i '52,55d' build.sh
sed -i '2i set -ex' build.sh
sed -i 's/^ipv4_t/extern ipv4_t/g' bot/includes.h
sed -i '26i ipv4_t LOCAL_ADDR;' bot/main.c
sed -i '18s/"[^"]*", [0-9]\+/"NMACNJMQV\\"", 10/g' bot/table.c
sed -i '21s/"[^"]*", [0-9]\+/"NMACNJMQV\\"", 10/g' bot/table.c
sed -i '2i USE mirai;' ../scripts/db.sql
echo "INSERT INTO users VALUES (NULL, 'anna-senpai', 'p455w', 0, 0, 0, 0, -1, 1, 30, '');" >> ../scripts/db.sql
sed -i '11s/"[^"]*"/"anna-senpai"/g' cnc/main.go
sed -i '12s/"[^"]*"/"p455w"/g' cnc/main.go
go mod init mirai
go get -u github.com/go-sql-driver/mysql github.com/mattn/go-shellwords
go mod tidy
mkdir -p debug
./build.sh debug telnet
service mariadb start
mysql -u root < ../scripts/db.sql
EOR

WORKDIR /BinPRE/Artifact_Evaluation/BinPRE_scripts
