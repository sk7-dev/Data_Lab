import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    queue.sort_values(by = 'turn', inplace = True)
    queue['Total_Weight'] = queue['weight'].cumsum()
    queue = queue[queue['Total_Weight']<=1000]
    result = queue.tail(1)
    return result[['person_name']]