FROM python:3
 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
 
 
WORKDIR /code
 
RUN pip install pip==19.2
COPY requirements.txt .
 
RUN pip3 install -r requirements.txt
 
RUN apt-get update
RUN apt-get install python3-pyqt5 -y
RUN apt-get install qt5-default -y
RUN apt-get install x11-apps -y
RUN apt-get install -y apt-utils
RUN apt-get install 'ffmpeg'\
    'libsm6'\ 
    'libxext6'  -y
RUN mkdir -p /tmp/runtime-circleci
RUN apt-get install libglu1-mesa-dev freeglut3-dev mesa-common-dev -y
COPY . .
 
CMD ["python", "./main.py"]
