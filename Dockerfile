FROM nikolaik/python-nodejs:python3.9-nodejs16

# Updating Packages
RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y

# Installing Requirements
RUN cd /
RUN pip3 install --upgrade pip
RUN pip3 install -U -r requirements.txt

RUN mkdir /DCXPlayer 
WORKDIR /DCXPlayer 

CMD python3 -m main.py
