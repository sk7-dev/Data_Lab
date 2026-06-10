import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee['emp_sal'] = employee.groupby('departmentId')['salary'].rank(method = 'dense', ascending = False)
    emp = employee.sort_values(by = 'emp_sal', ascending = False)
    emp = emp[emp['emp_sal'] <= 3]
    emp = emp.merge(department, how = 'left', left_on = 'departmentId', right_on = 'id')

    return pd.DataFrame({"Department": emp['name_y'], "Employee": emp["name_x"] , "Salary": emp["salary"]})