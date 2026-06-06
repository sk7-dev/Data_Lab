import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    total_products = product["product_key"].nunique()

    bought_counts = (
        customer.drop_duplicates(["customer_id", "product_key"])
        .groupby("customer_id")["product_key"]
        .nunique()
        .reset_index(name="products_bought")
    )

    result = bought_counts[bought_counts["products_bought"] == total_products]

    return result[["customer_id"]]