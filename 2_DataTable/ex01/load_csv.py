import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    A function that opens a csv file at the given path,
    prints its dimensions and returns it as a pandas DataFrame

    Arguments:
        path (str): path of csv file to load

    Returns:
        a DataFrame containing the data
    """

    # make sure path is a string
    assert type(path) is str, "path must be a string"

    # open the csv file
    df = pd.read_csv(path)

    # print the shape of the data frame
    print(f"Loading dataset of dimensions {df.shape}")

    # return the data frame
    return df
