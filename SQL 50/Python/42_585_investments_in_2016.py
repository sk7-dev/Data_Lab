import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    mask1 = ~insurance.duplicated(subset = ['lat','lon'],keep = False)
    mask2 = insurance.duplicated(subset = ['tiv_2015'],keep = False)
    ins_f = insurance[mask1 & mask2]
    return pd.DataFrame({"tiv_2016":round(ins_f['tiv_2016'].sum(),2)},index=[0])