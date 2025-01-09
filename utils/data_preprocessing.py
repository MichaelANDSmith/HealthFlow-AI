import pandas as pd

def preprocess_data(raw_data):
    """
    Preprocess raw data into a clean format.
    :param raw_data: The raw data input
    :return: Cleaned and processed data
    """
    df = pd.DataFrame(raw_data)
    # Data cleaning process (e.g., remove NaNs, normalize values)
    df.dropna(inplace=True)
    return df
