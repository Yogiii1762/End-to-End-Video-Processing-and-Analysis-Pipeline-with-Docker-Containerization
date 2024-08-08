from ultralytics import YOLO
import cv2
import pandas as pd
import os




def detect_objects(video_path):
    from Frames_extraction import frame_capture
    timestamps, output_folder = frame_capture(video_path)

    model = YOLO("yolov8n.pt")  
    all_detections = []

    for count, filename in enumerate(sorted(os.listdir(output_folder))):
        if filename.endswith(".jpg"):
            frame_path = os.path.join(output_folder, filename)
            img = cv2.imread(frame_path)
            results = model(img)  

            for result in results:  #check the loop Once again!!(Read the documentation)
                boxes = result.boxes 
                for box in boxes:
                    
                    x1, y1, x2, y2 = box.xyxy[0].numpy()  
                    confidence = box.conf[0].numpy()      
                    class_id = int(box.cls[0].numpy())   
                    class_name = result.names[class_id]          
                    
                    all_detections.append({
                        'class': class_name,
                        'Timestamp': timestamps[count],
                        'frame_number': count,
                        'BoundingBox_Coordinate_0': x1,
                        'BoundingBox_Coordinate_1': y1,
                        'BoundingBox_Coordinate_2': x2,
                        'BoundingBox_Coordinate_3': y2,
                        'confidence': confidence,
                        
                    })


    df = pd.DataFrame(all_detections)
    csv_file = "Detection_Results.csv"
    df.to_csv(csv_file, index=False)
    return csv_file
    
if __name__ == "__main__":
    video_path = "Pigeon.mp4"
    detect_objects(video_path)