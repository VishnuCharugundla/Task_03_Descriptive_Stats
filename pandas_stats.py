import pandas as pd

def load_and_summarize(filepath):
    df = pd.read_csv(filepath)
    print("\n--- Overall ---")
    print(df.describe(include='all'))

    print("\n--- Value counts for categorical fields ---")
    categorical = df.select_dtypes(include=['object']).columns
    for col in categorical:
        print(f"\n{col}:\n{df[col].value_counts().head(5)}")

if __name__ == "__main__":
    load_and_summarize("data/2024_fb_ads_president_scored_anon.csv")
