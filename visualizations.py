import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

os.makedirs("plots", exist_ok=True)

df = pd.read_csv("data/2024_fb_ads_president_scored_anon.csv")

# Estimated Spend Distribution
plt.figure()
sns.histplot(df['estimated_spend'], bins=50, kde=True, color='skyblue')
plt.title('Distribution of Estimated Spend')
plt.xlabel('Spend ($)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('plots/estimated_spend_distribution.png')
plt.close()

# Top 10 Political Advertisers
plt.figure()
top_bylines = df['bylines'].value_counts().head(10)
sns.barplot(y=top_bylines.index, x=top_bylines.values, palette="viridis")
plt.title('Top 10 Political Advertisers')
plt.xlabel('Number of Ads')
plt.ylabel('Byline')
plt.tight_layout()
plt.savefig('plots/top_advertisers.png')
plt.close()

# Top 10 Platform Combinations
plt.figure()
platform_counts = df['publisher_platforms'].value_counts().head(10)
sns.barplot(y=platform_counts.index, x=platform_counts.values, palette="magma")
plt.title('Top 10 Platform Combinations')
plt.xlabel('Number of Ads')
plt.ylabel('Platforms')
plt.tight_layout()
plt.savefig('plots/platform_usage.png')
plt.close()

# Political Topics
topic_cols = [col for col in df.columns if '_topic_illuminating' in col]
topic_sums = df[topic_cols].sum().sort_values(ascending=False)
plt.figure()
sns.barplot(y=topic_sums.index, x=topic_sums.values, palette='coolwarm')
plt.title('Total Mentions of Political Topics')
plt.xlabel('Total Count')
plt.ylabel('Topic')
plt.tight_layout()
plt.savefig('plots/topic_mentions.png')
plt.close()

# CTA Types
cta_cols = [col for col in df.columns if 'cta_' in col and 'illuminating' in col]
cta_sums = df[cta_cols].sum().sort_values(ascending=False)
plt.figure()
sns.barplot(y=cta_sums.index, x=cta_sums.values, palette='Set2')
plt.title('CTA Types Across All Ads')
plt.xlabel('Total Count')
plt.ylabel('CTA Type')
plt.tight_layout()
plt.savefig('plots/cta_distribution.png')
plt.close()

print("Visualizations saved in 'plots/' directory.")
