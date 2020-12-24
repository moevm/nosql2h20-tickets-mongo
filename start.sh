docker-compose up --build
apt-get update
apt-get install python3-pyqt5 -y
apt-get install qt5-default -y
apt-get install x11-apps -y
apt-get install -y apt-utils
apt-get install 'ffmpeg'\
   'libsm6'\ 
   'libxext6'  -y
mkdir -p /tmp/time-circleci
apt-get install libglu1-mesa-dev freeglut3-dev mesa-common-dev -y
apt install software-properties-common -y
add-apt-repository ppa:deadsnakes/ppa -y
apt-get update
apt-get install python3.6 -y
python3 --version
apt install python3-pip -y
pip3 install pymongo
pip3 install matplotlib
pip3 install numpy
pip3 install python-dateutil 
 
python3 app/api/main.py
