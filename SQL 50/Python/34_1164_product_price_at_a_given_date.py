import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    product = pd.DataFrame({'product_id': products['product_id'].unique()})
    products = products[pd.to_datetime(products['change_date']) <='2019-08-16'].sort_values('change_date').groupby('product_id', as_index = False)['new_price'].last()
    product = product.merge(products, on='product_id', how = 'left')
    product['price'] = product['new_price'].fillna(10)
    return product[['product_id', 'price']]