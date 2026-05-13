import pandas as pd


def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardizes column names for consistency.
    CUSTOMIZE these docstrings aka comments for YOUR project
    """
    df = df.copy()
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(" ", "_")
    )
    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes exact duplicate rows.
    """
    return df.drop_duplicates()


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Main cleaning function.

    """
    df = standardize_column_names(df)
    df = remove_duplicates(df)

    return df
