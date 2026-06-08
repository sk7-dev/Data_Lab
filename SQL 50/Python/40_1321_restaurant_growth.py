import pandas as pd

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
  daily_amount = customer.groupby("visited_on")["amount"].sum().reset_index()
  daily_amount["amount"] = daily_amount["amount"].rolling(window = 7).sum()
  daily_amount["average_amount"] = (daily_amount["amount"]/7).round(2)
  result = daily_amount.dropna()
  return result