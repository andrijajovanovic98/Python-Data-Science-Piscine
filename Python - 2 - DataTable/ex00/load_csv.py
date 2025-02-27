import pandas as pd


def load(path: str) -> pd.DataFrame:
    """ Loads a CSV file into a Pandas DataFrame."""
    try:
        data = pd.read_csv(path)

        print(f"Loading dataset of dimensions {data.shape}")

        return data
    except FileNotFoundError:
        print("Error: File not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
    except pd.errors.ParserError:
        print("Error: Bad file format.")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return pd.DataFrame()
