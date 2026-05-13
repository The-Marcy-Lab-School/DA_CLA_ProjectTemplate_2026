import pandas as pd


def create_time_features(df: pd.DataFrame, date_column: str) -> pd.DataFrame:
    """
    Creates basic time-based features.

    Example:
    - day of week
    - month
    - weekend flag
    """
    df = df.copy()

    df[date_column] = pd.to_datetime(df[date_column], errors="coerce")

    df["day_of_week"] = df[date_column].dt.dayofweek
    df["month"] = df[date_column].dt.month
    df["is_weekend"] = df["day_of_week"].isin([5, 6]).astype(int)

    return df


def create_target_placeholder(df: pd.DataFrame) -> pd.DataFrame:
    """
    Placeholder for target creation.

    YOU should define their own target based on stakeholder decision.
    """
    df = df.copy()

    # Example only:
    # df["target"] = ...

    return df
