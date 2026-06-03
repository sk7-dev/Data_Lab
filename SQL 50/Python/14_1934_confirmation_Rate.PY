import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    df = signups.merge(confirmations, on="user_id", how="left")

    result = (
        df.groupby("user_id")["action"]
        .apply(lambda x: round((x == "confirmed").sum() / x.notna().sum(), 2) if x.notna().sum() > 0 else 0)
        .reset_index(name="confirmation_rate")
    )

    return result