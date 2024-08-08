
from Detection import detect_objects
from Create_db import store_results_in_db
from Plot import plot_bird_detection

def main(video_path):
    csv_file = detect_objects(video_path)
    db_file = store_results_in_db(csv_file)
    plot_bird_detection(db_file)

if __name__ == "__main__":
    video_path = "Pigeon.mp4"
    main(video_path)
