# Handy - AISchools UNIMORE Project

Lo scopo di questo progetto è quello di voler realizzare un sistema di Hand Tracking e Gesture Recognition basato su rete neurale per implementare una procedura di controllo interattivo real-time da webcam.

La documentazione relativa ai processi di sviluppo, di studio e di benchmark della soluzione è disponibile in questo stesso repository.

## Uso dei File

Nella cartella **training** è presente tutto l'esssenziale all'installazione dei requisiti per l'utilizzo dei programmi e per predisporre un training custom:

- **all_in_one_init.sh:** script per eseguire in automatico l'inizializzazione dei requisiti e il download del dataset. In particolare chiamerà in sequenza **init.sh** e **dataset_downloader.sh**.
- **dataset_downloader.sh:** script per scaricare il dataset e eseguire il preprocessing. Se chiamandolo non si specifica nessun parametro, scaricherà automaticamente il dataset _HANDS_. Altrimenti è possibile specificare _egohands_.
- **init.sh:** installa (apt-get e pip) i requisiti. Chiama inoltre **yolo_clone.sh** per installare anche i requisiti di YOLO.
- **yolo_clone.sh:** si occupa di clonare la repository ufficiale di YOLO e di installare i suoi requisiti.
- **yolo_custom_train.sh:** uno script per facilitare il training custom della rete, specificando i pesi di partenza (rete pre-trained) e se eseguire su una singola GPU o su 2 GPU in parallelo.

Nella cartella **preprocessing** all'interno di **training** ci sono i vari programmi Python per l'esecuzione del preprocessing sulle immagini del dataset. Verranno elencati i principali:

- **gaussian_noise.py:** aggiunge un rumore gaussiano sui canali RGB delle immagini del dataset.
- **luminance_randomizer.py:** randomizza le curve RGB dell'immagine per ottenere immagini più luminose o meno luminose e far generalizzare questo concetto alla rete.
- **train_valid_test_splitter.py:** suddivide le immagini del dataset nei vari set (Test, Validation e Training).

Nella cartella principale è presente sia una documentazione della realizzazione del progetto sia vari programmi Python per la detection. In particolare abbiamo:

- **webcam_detector.py:** script per la detection diretta da webcam. Il file di pesi da usare è da specificare come parametro, ad esempio facendo 'python3 webcam_detector.py yoloM10.pt'.
- **video_detector.py:** script per la detection su un video pre-registrato. Il file di pesi e il video da usare sono da specificare come parametri, ad esempio facendo 'python3 video_detector.py yoloM10.pt video.mp4'.
- **video_recorder.py:** una semplice utility per registrare un video su cui effettuare un detection test.

I vari pesi utilizzabili per la detection sono disponibili su [Google Drive](https://drive.google.com/file/d/1zDABYJ889kYYUN2gqmcZ95gfHlrcM0w8/view?usp=sharing).




