import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = products.merge(orders, on='product_id', how='inner')
    df = df[(df['order_date']>= '2020-02-01')&(df['order_date']<='2020-02-29')]
    result = df.groupby('product_name')['unit'].sum().reset_index()
    return result[result['unit']>=100]