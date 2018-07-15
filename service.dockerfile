FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y software-properties-common vim
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update

RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv
RUN apt-get install -y git

# update pip
RUN python3.6 -m pip install pip --upgrade
RUN python3.6 -m pip install wheel


RUN python3.6 -m pip install flask

RUN python3.6 -m pip install pyopenssl

RUN python3.6 -m pip install numpy scipy
RUN python3.6 -m pip install scikit-learn
RUN python3.6 -m pip install Pillow

COPY flaskapp /src/

EXPOSE 5000

ENTRYPOINT ["python3.6", "/src/app.py"]