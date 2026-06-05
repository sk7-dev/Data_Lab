import pandas as pd
import datetime as dt

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['month'] = transactions['trans_date'].dt.strftime('%Y-%m')
    transactions['approved_count'] = (transactions['state'] == 'approved')
    transactions['trans_total_amount'] = transactions['amount']
    transactions['approved_total_amount'] = transactions['amount'] * (transactions['state'] == 'approved')
    return (transactions.groupby(['month', 'country'], dropna = False).agg({'trans_date': 'size', 'approved_count':'sum', 'trans_total_amount':'sum', 'approved_total_amount':'sum'}).rename(columns = {'trans_date': 'trans_count'}).reset_index())
    