import pandas as pd

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    first_years = (
        sales.groupby("product_id", as_index=False)["year"]
        .min()
        .rename(columns={"year": "first_year"})
    )

    result = sales.merge(
        first_years,
        left_on=["product_id", "year"],
        right_on=["product_id", "first_year"]
    )

    return result[["product_id", "first_year", "quantity", "price"]]