import pandas as pd

def extract():
    # Sample data
    data = {
        "id": [1, 2, 3],
        "name": ["Alice", "Bob", "Charlie"]
    }
    df = pd.DataFrame(data)
    
    # Intentional break: writing wrong file name
    df.to_csv("wrong_file.csv", index=False)
    
    print("Extraction complete (but file name is wrong!)")

if __name__ == "__main__":
    extract()
