from preprocessing import (Read_data_file,Drop_unnecessary_features,check_data_type)
from config.config import cols_to_drop
file_path = r"D:\mahmoud\depi\CA-R5-S2S2-AI\src\DA\preprocessing\assighnent 9\project\data\raw\Titanic.csv"
df = Read_data_file(file_path)
if df is None:
    print("Error: no DataFrame provided.")
else:
    print("Original Dataset:")
    print(df.head())

    # Check data type
    print("\nData Quality Report:")
    print(check_data_type(df))

    # Remove unnecessary features
    df = Drop_unnecessary_features(df, cols_to_drop)

    print("\nDataset after removing unnecessary features:")
    print(df.head())
    