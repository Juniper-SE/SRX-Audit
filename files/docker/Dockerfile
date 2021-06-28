FROM python:slim-buster

### -------------------------------------------------
### Metadata information
### -------------------------------------------------
LABEL name="juniper-automation-container"
LABEL maintainer="cremsburg@protonmail.com"
LABEL description="nornir container to manage Juniper devices"
LABEL license="GPLv3"
LABEL url="https://gitlab.com/cremsburg/juniper-automation-container/container_registry"
LABEL build-date="20210321"

### -------------------------------------------------
### Change directory to /var/tmp
### -------------------------------------------------
WORKDIR /var/tmp

### -------------------------------------------------
### Add and install python packages
### -------------------------------------------------
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install --upgrade pip

### -------------------------------------------------
### Change directory to /home/nornir
### -------------------------------------------------
WORKDIR /home/nornir

### -------------------------------------------------
### Environmentals
### -------------------------------------------------
# ENV NORNIR_CONFIG /home/nornir/config.cfg
