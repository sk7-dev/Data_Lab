import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    low_salary_df = employees[(employees['salary'] < 30000) & (employees['manager_id'].notna())]
    result = low_salary_df[~low_salary_df['manager_id'].isin(employees['employee_id'])]
    return result[['employee_id']].sort_values('employee_id')