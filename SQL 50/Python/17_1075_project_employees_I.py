import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    merged = project.merge(employee, on="employee_id")

    result = (
        merged.groupby("project_id", as_index=False)["experience_years"]
        .mean()
        .round(2)
    )

    result = result.rename(columns={"experience_years": "average_years"})

    return result