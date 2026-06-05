import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery_sorted = delivery.sort_values(by='order_date').drop_duplicates(subset='customer_id',keep='first')
    delivery_immediate = delivery_sorted[delivery_sorted['order_date']==delivery_sorted['customer_pref_delivery_date']]
    immediate_percentage = round((len(delivery_immediate) / len(delivery_sorted)) * 100 , 2)
    return pd.DataFrame({'immediate_percentage':[immediate_percentage]})