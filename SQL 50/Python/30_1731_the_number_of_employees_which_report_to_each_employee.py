import pandas as pd
import numpy as np

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    reports = (
        employees.groupby("reports_to")
        .agg(
            reports_count=("employee_id", "count"),
            average_age=("age", "mean")
        )
        .reset_index()
    )

    reports["average_age"] = np.floor(reports["average_age"] + 0.5).astype(int)

    result = reports.merge(
        employees[["employee_id", "name"]],
        left_on="reports_to",
        right_on="employee_id"
    )

    return (
        result[["employee_id", "name", "reports_count", "average_age"]]
        .sort_values("employee_id")
    )