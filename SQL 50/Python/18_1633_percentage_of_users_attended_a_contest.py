import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    total_users = users["user_id"].nunique()

    result = (
        register.groupby("contest_id", as_index=False)["user_id"]
        .nunique()
        .rename(columns={"user_id": "percentage"})
    )

    result["percentage"] = round((result["percentage"] / total_users) * 100, 2)

    result = result.sort_values(
        by=["percentage", "contest_id"],
        ascending=[False, True]
    )

    return result