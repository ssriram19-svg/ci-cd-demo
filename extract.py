import pandas as pd

def extract():
    # Sample data
    data = {
        "id": [1, 2, 3],
        "name": ["Alice", "Bob", "Charlie"]
    }
    df = pd.DataFrame(data)
    
    # Correct file name as expected by test_extract.py
    df.to_csv("extracted.csv", index=False)
    
    print("Extraction complete and saved to extracted.csv")

if __name__ == "__main__":
    extract()
