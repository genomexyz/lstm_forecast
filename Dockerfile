FROM tensorflow/tensorflow:latest-gpu

WORKDIR /usr/src/app
COPY . .
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install -r requirements.txt
RUN python3 PyEMD/setup.py install

