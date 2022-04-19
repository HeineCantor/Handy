echo "YoloV5 Git Clone"

NET="yolov5s.pt"

case $1 in
        S) NET="yolov5s.pt"
        ;;
        N) NET="yolov5n.pt"
        ;;
        M) NET="yolov5m.pt"
        ;;
        L) NET="yolov5l.pt"
        ;;
        XL) NET="yolov5xl.pt"
        ;;
        *) echo "Nessuna rete specificata per pesi di pretrain. Di default c'è 'yolov5s.pt'."
esac

if [ -z "$(ls -A yolov5)" ]; then

git clone https://github.com/ultralytics/yolov5  # clone
cd yolov5
pip install -r requirements.txt  # install
cd ..

fi

cd yolov5

python3 train.py --img 640 --batch 32 --epochs 100 --data '../dataset/data.yaml' --weights $NET
