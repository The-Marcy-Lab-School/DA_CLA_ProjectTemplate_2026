import pandas as pd


def check_required_columns(df: pd.DataFrame, required_columns: list) -> None:
    """
    Checks whether all required columns exist.
    """
    missing = [col for col in required_columns if col not in df.columns]

    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def check_null_rates(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    """
    Returns columns with null rates above the selected threshold.
    """
    null_rates = df.isna().mean()
    return null_rates[null_rates > threshold].sort_values(ascending=False)


def check_duplicate_count(df: pd.DataFrame) -> int:
    """
    Returns duplicate row count.
    """
    return df.duplicated().sum()
