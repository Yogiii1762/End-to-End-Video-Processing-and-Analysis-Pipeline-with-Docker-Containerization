import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns

def plot_bird_detection(db_file):
    
    engine = create_engine(f'sqlite:///{db_file}')
    
    
    query = """
    SELECT 
       duration_in_minutes,
        COUNT(*) AS bird_count
    FROM 
        detection_results
    WHERE 
        Class='bird'
    GROUP BY 
        duration_in_minutes
    ORDER BY 
        duration_in_minutes
    """

    
    df_birds = pd.read_sql(query, engine)

   
    engine.dispose()

    
    if df_birds.empty:
        print("Warning: No data found for plotting.")
        return

   
    sns.lineplot(data=df_birds, x='duration_in_minutes', y='bird_count')
    plt.xlabel('Time (Minutes)')
    plt.ylabel('Number of Birds Detected')
    plt.title('Bird Detection Over Time')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('bird_detection_plot.png')
    plt.show()
    print("Plot saved as bird_detection_plot.png")

if __name__ == "__main__":
    db_file = "detection_results.db"
    plot_bird_detection(db_file)