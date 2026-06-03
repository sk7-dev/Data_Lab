import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    df = prices.merge(units_sold, on="product_id", how="left")

    df = df[
        (df["purchase_date"].isna()) |
        (
            (df["purchase_date"] >= df["start_date"]) &
            (df["purchase_date"] <= df["end_date"])
        )
    ]

    df["total_price"] = df["price"] * df["units"]

    result = (
        df.groupby("product_id")
        .agg(
            total_price=("total_price", "sum"),
            total_units=("units", "sum")
        )
        .reset_index()
    )

    result["average_price"] = (
        result["total_price"] / result["total_units"]
    ).fillna(0).round(2)

    return result[["product_id", "average_price"]]