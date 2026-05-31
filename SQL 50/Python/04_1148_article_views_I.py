import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    result = views[views["author_id"] == views["viewer_id"]][["author_id"]]
    result = result.drop_duplicates()
    result = result.rename(columns={"author_id": "id"})
    return result.sort_values(by="id")