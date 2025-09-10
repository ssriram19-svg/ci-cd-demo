import pandas as pd

def extract():
    data = {
        "id": [1, 2, 3],
        "name": ["Alice", "Bob", "Charlie"]
    }
    df = pd.DataFrame(data)
    df.to_csv("extracted.csv", index=False)
    print("Extraction complete!")

if __name__ == "__main__":
    extract()
