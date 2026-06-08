import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    total=seat['id'].max()
    def swap(x):
        if x%2==0:
            return x-1
        elif x==total:
            return x
        else:
            return x+1
    seat['id']=seat['id'].apply(swap)
    return seat.sort_values('id').reset_index(drop=True)