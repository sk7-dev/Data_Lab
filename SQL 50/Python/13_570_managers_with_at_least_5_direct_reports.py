import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    direct_reports = (
        employee
        .groupby("managerId")
        .size()
        .reset_index(name="reports")
    )

    managers = direct_reports[direct_reports["reports"] >= 5]

    result = employee[employee["id"].isin(managers["managerId"])]

    return result[["name"]]