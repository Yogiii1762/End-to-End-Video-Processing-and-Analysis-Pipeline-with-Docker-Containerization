import cv2
import os
from datetime import timedelta

Video_path = "Pigeon.mp4"
output_folder = "Frames"

def frame_capture(video_path):

    output_folder = "Frames"


    if not os.path.exists(output_folder):
        os.makedirs(output_folder)


    cap = cv2.VideoCapture(video_path)
    count = 0
    fps = cap.get(cv2.CAP_PROP_FPS)
    timestamps=[]

    while True:
        ret,frame = cap.read()

        if not ret:
            break
        
        timestamp = count / fps
        timestamp_format = str(timedelta(seconds=timestamp))
        timestamps.append(timestamp_format)

        name = output_folder + "/frame" + str(count) + ".jpg"
        
        cv2.imwrite(name, frame)
        count += 1
    
    cap.release()
    cv2.destroyAllWindows()
    return timestamps, output_folder

if __name__ == "__main__":
    video_path = "Pigeon.mp4"
    timestamps, output_folder = frame_capture(video_path)
