import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    con_cat = pd.concat([request_accepted['requester_id'],request_accepted['accepter_id']])
    m = con_cat.value_counts()
    m = m.sort_values(ascending = False)
    return pd.DataFrame({"id":m.index[0],"num":m.iloc[0]},index = [0])