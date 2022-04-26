pip install gdown

apt-get install git unzip curl ffmpeg libsm6 libxext6 -y

pip install opencv-python

pip uninstall torch torchvision torchaudio -y

pip install torch==1.10.1+cu111 torchvision==0.11.2+cu111 torchaudio==0.10.1 -f https://download.pytorch.org/whl/torch_stable.html
