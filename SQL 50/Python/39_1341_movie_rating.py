import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    mfs = movie_rating['user_id'].mode()
    mf = users.loc[users['user_id'].isin(mfs), 'name'].min()
    movie_rating = movie_rating[(movie_rating['created_at'].dt.month == 2) & (movie_rating['created_at'].dt.year == 2020)]
    a = movie_rating.groupby('movie_id')['rating'].mean()
    max_rating_ids = a[a == a.max()].index
    best_movie = movies.loc[movies['movie_id'].isin(max_rating_ids), 'title'].min()
    return pd.DataFrame({'results': [mf, best_movie]})