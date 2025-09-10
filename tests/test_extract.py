import os
import pandas as pd
from extract import extract

def test_extract_creates_file():
    extract()
    assert os.path.exists("extracted.csv")
    df = pd.read_csv("extracted.csv")
    assert "id" in df.columns
    assert "name" in df.columns

print("ETL Done!")
