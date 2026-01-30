import pandas as pd

def profile_dataframe(df: pd.DataFrame) -> dict:
    profile = {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "column_profiles": {}
    }

    for col in df.columns:
        col_data = df[col]

        col_profile = {
            "dtype": str(col_data.dtype),
            "null_count": int(col_data.isnull().sum()),
            "null_percentage": round(float(col_data.isnull().mean() * 100), 2),
            "unique_count": int(col_data.nunique(dropna=True))
        }

        if pd.api.types.is_numeric_dtype(col_data):
            col_profile.update({
                "min": float(col_data.min()),
                "max": float(col_data.max()),
                "mean": round(float(col_data.mean()), 2),
                "std": round(float(col_data.std()), 2)
            })

        profile["column_profiles"][col] = col_profile

    return profile
