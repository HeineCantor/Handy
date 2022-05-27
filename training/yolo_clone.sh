if [ -z "$(ls -A yolov5)" ]; then

    git clone https://github.com/ultralytics/yolov5  # clone
    cd yolov5
    pip install -r requirements.txt  # install
    cd ..

fi
