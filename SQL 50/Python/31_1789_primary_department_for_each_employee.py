import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    # Count how many departments each employee belongs to
    employee["dept_count"] = employee.groupby("employee_id")["department_id"].transform("count")

    # Keep rows where:
    # 1. employee has only one department, or
    # 2. department is marked as primary
    result = employee[
        (employee["dept_count"] == 1) | (employee["primary_flag"] == "Y")
    ]

    return result[["employee_id", "department_id"]]