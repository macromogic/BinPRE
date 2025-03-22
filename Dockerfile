FROM python:3.10

ARG DEBIAN_FRONTEND=noninteractive
ARG NJOBS=8
RUN apt update && apt install -y \
acl attr autoconf bind9utils bison build-essential cmake make \
debhelper dnsutils docbook-xml docbook-xsl flex gdb libjansson-dev krb5-user \
libacl1-dev libaio-dev libarchive-dev libattr1-dev libblkid-dev libbsd-dev \
libcap-dev libcups2-dev libgnutls28-dev libgpgme-dev libjson-perl \
libldap2-dev libncurses5-dev libpam0g-dev libparse-yapp-perl \
libpopt-dev libreadline-dev nettle-dev perl pkg-config \
xsltproc zlib1g-dev liblmdb-dev lmdb-utils gcc g++ libdbus-1-dev \
git vim net-tools wget tar tcpdump less strace smbclient

## Pin

RUN wget https://software.intel.com/sites/landingpage/pintool/downloads/pin-3.28-98749-g6643ecee5-gcc-linux.tar.gz
RUN tar -xzf pin-3.28-98749-g6643ecee5-gcc-linux.tar.gz
ENV PIN_ROOT="/pin-3.28-98749-g6643ecee5-gcc-linux"
ENV PATH="/pin-3.28-98749-g6643ecee5-gcc-linux:${PATH}"
RUN rm /pin-3.28-98749-g6643ecee5-gcc-linux.tar.gz

## BinPRE

WORKDIR /
RUN git clone https://github.com/macromogic/BinPRE.git
RUN pip install -r /BinPRE/requirements.txt
RUN cd /BinPRE/src && git checkout dev && ./run compile taint

## SMB2

RUN wget https://download.samba.org/pub/samba/stable/samba-4.21.4.tar.gz
RUN pip install markdown crypto dnspython
RUN tar -xzf samba-4.21.4.tar.gz
RUN cd samba-4.21.4 && ./configure --enable-debug && make -j ${NJOBS} && make install
RUN rm /samba-4.21.4.tar.gz
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
RUN make -C /miniweb -j ${NJOBS}

## DNP3

RUN git clone https://github.com/dnp3/opendnp3.git
RUN cmake -B /opendnp3/build -S /opendnp3 && make -C /opendnp3/build -j ${NJOBS}

## TFTP

RUN git clone https://git.kernel.org/pub/scm/network/tftp/tftp-hpa.git
RUN make -C /tftp-hpa -j ${NJOBS}

WORKDIR /BinPRE/Artifact_Evaluation/BinPRE_scripts
