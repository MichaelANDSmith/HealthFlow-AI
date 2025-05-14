import pandas as pd
from sklearn.preprocessing import MinMaxScaler  # [Incremental]
import numpy as np  # [Incremental]

def preprocess_data(raw_data):
    """
    Preprocess raw data into a clean format.
    :param raw_data: The raw data input
    :return: Cleaned and processed data
    """
    df = pd.DataFrame(raw_data)

    # Drop missing values
    df.dropna(inplace=True)

    # [Incremental] Convert data types where possible
    df = df.convert_dtypes()

    # [Incremental] Remove numeric outliers using z-score method
    numeric_cols = df.select_dtypes(include=['number']).columns
    for col in numeric_cols:
        z_scores = (df[col] - df[col].mean()) / df[col].std()
        df = df[(z_scores > -3) & (z_scores < 3)]

    # [Incremental] Normalize numeric columns
    scaler = MinMaxScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    # [Incremental] Encode categorical columns using one-hot encoding
    categorical_cols = df.select_dtypes(include=['string', 'category']).columns
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    return df
