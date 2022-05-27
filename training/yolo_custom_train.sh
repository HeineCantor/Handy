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

./yolo_clone.sh

cd yolov5

if [ -z "$2" ]; then
    MODE="SINGLE"
else
    MODE="MULTI"
fi

if [ $MODE = "SINGLE" ]; then
    python3 train.py --img 640 --batch 2 --epochs 15 --data '../dataset/data.yaml' --weights $NET
else
    python3 -m torch.distributed.launch --nproc_per_node 2 train.py --img 640 --batch 32 --epochs 50 --data '../dataset/data.yaml' --weights $NET
fi
