import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import warnings
warnings.filterwarnings('ignore')

# --- Cell ---

df=pd.read_excel('../DataSets/WIID_19Dec2018.xlsx')
df

# --- Cell ---

df.columns

# --- Cell ---

df.isnull().sum()

# --- Cell ---

df.country.unique()

# --- Cell ---

df['c3'].unique()

# --- Cell ---

df['c2'].unique()

# --- Cell ---

df['c2'].fillna('Unknown',inplace=True)

# --- Cell ---

df.year.unique()

# --- Cell ---

df=df.dropna(subset=['gini_reported'])

# --- Cell ---

quintiles=['q1','q2','q3','q4','q5']

for col in quintiles:
    df[col].fillna(df[col].median(),inplace=True)

# --- Cell ---

deciles = ['d1','d2','d3','d4','d5','d6','d7','d8','d9','d10']

for dec in deciles:
    df[dec].fillna(df[dec].median(),inplace=True)

# --- Cell ---

df.drop(['bottom5','top5'], axis=1, inplace=True)

# --- Cell ---

df.sharing_unit.unique()

# --- Cell ---

df['sharing_unit'].fillna(df['sharing_unit'].mode()[0], inplace=True)

# --- Cell ---

df.scale.unique()

# --- Cell ---

df.scale_detailed.unique()

# --- Cell ---

df['scale'].fillna(df['scale'].mode()[0], inplace=True)
df['scale_detailed'].fillna(df['scale_detailed'].mode()[0], inplace=True)

# --- Cell ---

df.reference_unit.unique()

# --- Cell ---

df['reference_unit'].fillna(df['reference_unit'].mode()[0], inplace=True)

# --- Cell ---

df['mean'].fillna(df['mean'].median(), inplace=True)
df['median'].fillna(df['median'].median(), inplace=True)

# --- Cell ---

df.currency.unique()

# --- Cell ---

df['currency'].fillna("Unknown", inplace=True)

# --- Cell ---

df.reference_period.unique()

# --- Cell ---

df['reference_period'].fillna("Unknown", inplace=True)

# --- Cell ---

df['exchangerate'].fillna(df['exchangerate'].median(), inplace=True)

# --- Cell ---

df.drop(['mean_usd','median_usd'], axis=1, inplace=True)

# --- Cell ---

df['gdp_ppp_pc_usd2011'].fillna(df['gdp_ppp_pc_usd2011'].median(), inplace=True)

# --- Cell ---

df['population'].fillna(df['population'].median(), inplace=True)

# --- Cell ---

df.revision.unique()

# --- Cell ---

df['revision'].fillna("Unknown", inplace=True)

# --- Cell ---

df.source_comments.unique()

# --- Cell ---

df['source_comments'].fillna("No comments", inplace=True)

# --- Cell ---

df.survey.unique()

# --- Cell ---

df['survey'].fillna("Unknown", inplace=True)

# --- Cell ---

df.resource.unique()

# --- Cell ---

df['resource'].fillna("Unknown", inplace=True)

# --- Cell ---

df.dtypes

# --- Cell ---

plt.figure(figsize=(10,5))
sb.histplot(df['gini_reported'], bins=30, kde=True,color='Teal')
plt.title("Global Distribution of Gini Coefficient")
plt.xlabel("Gini Coefficient")
plt.ylabel("Frequency")
plt.show()

# --- Cell ---

country_gini = df.groupby('country')['gini_reported'].mean().reset_index()

# --- Cell ---

plt.figure(figsize=(10,5))
sb.histplot(country_gini['gini_reported'], bins=30, kde=True,color='Teal')
plt.title("Distribution of Income Inequality Across Countries")
plt.xlabel("Average Gini Coefficient")
plt.ylabel("Number of Countries")
plt.show()

# --- Cell ---

top10 = country_gini.sort_values(by='gini_reported', ascending=False).head(10)

plt.figure(figsize=(18,5))

plt.subplot(1,2,1)
sb.barplot(x=top10.country, y=top10.gini_reported,palette="BrBG",edgecolor='black')
plt.title("Top 10 Countries with Highest Inequality")
plt.xlabel("Gini Coefficient")
plt.ylabel("Country")
plt.xticks(rotation=45)

bottom10 = country_gini.sort_values(by='gini_reported').head(10)

plt.subplot(1,2,2)
sb.barplot(x=bottom10.country, y=bottom10.gini_reported,palette="BrBG",edgecolor='black')
plt.title("Top 10 Countries with Lowest Inequality")
plt.xlabel("Gini Coefficient")
plt.ylabel("Country")
plt.xticks(rotation=45)

plt.show()

# --- Cell ---

region_avg = df.groupby('region_un')['gini_reported'].mean().reset_index().sort_values(by='gini_reported', ascending=False)

plt.figure(figsize=(10,5))
sb.barplot(x=region_avg.gini_reported, y=region_avg.region_un,palette="BrBG",edgecolor='black')
plt.title("Average Income Inequality Across Regions")
plt.xlabel("Average Gini Coefficient")
plt.ylabel("Region")
plt.show()

# --- Cell ---

highest_region = region_avg.iloc[0]
print("Highest Inequality Region:\n", highest_region)

# --- Cell ---

lowest_region = region_avg.iloc[-1]
print("Lowest Inequality Region:\n", lowest_region)

# --- Cell ---

plt.figure(figsize=(15,7))
sb.boxplot(x=df.region_un, y=df.gini_reported,palette="BrBG")
plt.title("Distribution of Inequality Across Regions")
plt.xlabel("Region")
plt.ylabel("Gini Coefficient")
plt.show()

# --- Cell ---

plt.figure(figsize=(10,5))
sb.scatterplot(x=df.gdp_ppp_pc_usd2011,y=df.gini_reported,color='Teal',edgecolor='black')
plt.title("GDP per Capita vs Income Inequality")
plt.xlabel("GDP per Capita (PPP USD 2011)")
plt.ylabel("Gini Coefficient")
plt.show()

# --- Cell ---

income_avg = df.groupby('incomegroup')['gini_reported'].mean().reset_index().sort_values(by='gini_reported', ascending=False)

plt.figure(figsize=(12,5))
sb.barplot(x=income_avg.incomegroup, y=income_avg.gini_reported,palette="BrBG",edgecolor='black')
plt.title("Inequality Comparison Across Income Groups")
plt.xlabel("Income Group")
plt.ylabel("Average Gini Coefficient")
plt.show()

# --- Cell ---

variation = df.groupby('incomegroup')['gini_reported'].std().reset_index().sort_values(by='gini_reported', ascending=False)

highest_variation = variation.iloc[0]

print("Income group with highest inequality variation:\n")
print(highest_variation)

# --- Cell ---

plt.figure(figsize=(12,5))
sb.boxplot(x=df.incomegroup, y=df.gini_reported,palette="BrBG")
plt.title("Inequality Across Income Groups")
plt.xlabel("Income Group")
plt.ylabel("Gini Coefficient")
plt.show()

# --- Cell ---

country_std = df.groupby('country')['gini_reported'].std().reset_index()

country_stats = pd.merge(country_gini, country_std, on='country')
country_stats.columns = ['country', 'avg_gini', 'std_gini']

high_inequality = country_stats[(country_stats['avg_gini'] > 45) & (country_stats['std_gini'] < 5)]
high_inequality = high_inequality.sort_values(by='avg_gini', ascending=False)

top_countries = high_inequality.head(10)

plt.figure(figsize=(10,5))
sb.barplot(x=top_countries.avg_gini, y=top_countries.country,palette="BrBG",edgecolor='black')
plt.title("Countries with Consistently High Inequality")
plt.xlabel("Average Gini Coefficient")
plt.ylabel("Country")
plt.show()

# --- Cell ---

equal_countries = country_gini.sort_values(by='gini_reported').head(10)

plt.figure(figsize=(10,4))
plt.scatter(equal_countries['gini_reported'], equal_countries['country'],color='Teal',edgecolor='black')
plt.title("Top 10 Countries with Most Equal Income Distribution")
plt.xlabel("Gini Coefficient")
plt.ylabel("Country")
plt.show()

# --- Cell ---

country_fluctuation = df.groupby('country')['gini_reported'].std().reset_index().sort_values(by='gini_reported', ascending=False)

top_fluctuating = country_fluctuation.head(5)['country']

fluct_data = df[df['country'].isin(top_fluctuating)]

plt.figure(figsize=(12,5))
sb.lineplot(x=fluct_data.year, y=fluct_data.gini_reported, hue=fluct_data.country,marker='x',markeredgecolor='black',palette="BrBG")
plt.title("Countries with High Inequality Fluctuations Over Time")
plt.xlabel("Year")
plt.ylabel("Gini Coefficient")
plt.legend(title='Country',bbox_to_anchor=(1.17,1.0))
plt.grid(True)
plt.show()

# --- Cell ---

global_trend = df.groupby('year')['gini_reported'].mean().reset_index()

plt.figure(figsize=(12,5))
sb.lineplot(x=global_trend.year, y=global_trend.gini_reported,marker='x',markeredgecolor='black',color='Teal')
plt.title("Global Income Inequality Trend Over Time")
plt.xlabel("Year")
plt.ylabel("Average Gini Coefficient")
plt.grid(True)
plt.show()

# --- Cell ---

plt.figure(figsize=(12,6))

sb.scatterplot(x=df.population,y=df.gini_reported,color='Teal',edgecolor='black')
plt.title("Population vs Income Inequality")
plt.xlabel("Population")
plt.ylabel("Gini Coefficient")
plt.show()

# --- Cell ---

