from pathlib import Path

import pandas as pd

RAW_PATH = Path("data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")
OUT_PATH = Path("data/processed/clean.csv")


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.drop(columns=["customerID"])
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce").fillna(0.0)
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
    return df


if __name__ == "__main__":
    df = clean_data(pd.read_csv(RAW_PATH))
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)
    print(f"Saved {df.shape} to {OUT_PATH}")