import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.copy()
    df=df[
        (df['activity_date'] > '2019-06-27') &
        (df['activity_date'] <= '2019-07-27')
    ]
    return df.groupby('activity_date')['user_id'].nunique().reset_index().rename(columns={'activity_date': 'day', 'user_id':'active_users'})