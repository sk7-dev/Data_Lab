import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    employee["dept_count"] = employee.groupby("employee_id")["department_id"].transform("count")

    result = employee[
        (employee["dept_count"] == 1) | (employee["primary_flag"] == "Y")
    ]

    return result[["employee_id", "department_id"]]