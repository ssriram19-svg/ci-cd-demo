import os
import sys
import pandas as pd

# Add parent folder to sys.path so extract.py can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from extract import extract

def test_extract_creates_file():
    extract()
    assert os.path.exists("extracted.csv")
    df = pd.read_csv("extracted.csv")
    assert "id" in df.columns
    assert "name" in df.columns
