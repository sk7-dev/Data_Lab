import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    df = users
    df['name'] = df['name'].str.capitalize()
    return df.sort_values(by='user_id') 