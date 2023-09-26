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

    # make sure path is a csv file
    assert path.endswith(".csv"), "path must be a valid csv file"

    try:
        # open the csv file
        df = pd.read_csv(path)

        # print the shape of the data frame
        print(f"Loading dataset of dimensions {df.shape}")

        # return the data frame
        return df
    except FileNotFoundError:
        raise AssertionError("path must be an existing file") from None
    except PermissionError:
        raise AssertionError("path must be an accessible file") from None
    except pd.errors.EmptyDataError:
        raise AssertionError("path must not be an empty file") from None
    except pd.errors.ParserError:
        raise AssertionError("path must have valid csv format") from None
