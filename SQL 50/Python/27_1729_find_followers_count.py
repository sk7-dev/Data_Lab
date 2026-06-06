import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    result = (
        followers.groupby("user_id")
        .size()
        .reset_index(name="followers_count")
        .sort_values("user_id")
    )

    return result