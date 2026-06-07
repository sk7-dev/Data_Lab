import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    df = prices.merge(units_sold, on="product_id", how="left")

    df = df[
        (df["purchase_date"] >= df["start_date"]) &
        (df["purchase_date"] <= df["end_date"])
    ]

    df["total_price"] = df["price"] * df["units"]

    sales = (
        df.groupby("product_id")
        .agg(
            total_price=("total_price", "sum"),
            total_units=("units", "sum")
        )
        .reset_index()
    )

    sales["average_price"] = (sales["total_price"] / sales["total_units"]).round(2)

    result = prices[["product_id"]].drop_duplicates().merge(
        sales[["product_id", "average_price"]],
        on="product_id",
        how="left"
    )

    result["average_price"] = result["average_price"].fillna(0)

    return result