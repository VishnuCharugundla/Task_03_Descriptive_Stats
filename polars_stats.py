import polars as pl

def load_and_summarize(filepath):
    df = pl.read_csv(filepath)
    print("\n--- Overall ---")
    print(df.describe())

    print("\n--- Value counts for categorical fields ---")
    for col in df.columns:
        if df[col].dtype == pl.Utf8:
            vc = df[col].value_counts().sort("counts", descending=True).limit(5)
            print(f"\n{col}:\n{vc}")

if __name__ == "__main__":
    load_and_summarize("data/2024_fb_ads_president_scored_anon.csv")
