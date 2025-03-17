FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y \
python3-dev python3-dbg python3-crypto python3-dnspython python3-gpg python3-markdown python3-pip \
samba git vim net-tools wget tar

RUN mkdir -p /shared && chmod 777 /shared

RUN echo "[shared]\n\
    path = /shared\n\
    read only = no\n\
    browsable = yes\n\
    guest ok = yes\
" >> /etc/samba/smb.conf

WORKDIR /
RUN git clone https://github.com/macromogic/BinPRE.git

RUN wget https://software.intel.com/sites/landingpage/pintool/downloads/pin-3.28-98749-g6643ecee5-gcc-linux.tar.gz
RUN tar -xzf pin-3.28-98749-g6643ecee5-gcc-linux.tar.gz
ENV PATH="/pin-3.28-98749-g6643ecee5-gcc-linux:${PATH}"

WORKDIR /BinPRE
RUN pip install -r requirements.txt