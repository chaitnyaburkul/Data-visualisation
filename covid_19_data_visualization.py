import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('country_wise_latest.csv')

# Basic data cleaning
df.fillna(0, inplace=True)

# Set style for plots
sns.set_style('whitegrid')
plt.figure(figsize=(12, 8))

# 1. Top 20 Countries by Confirmed Cases
plt.subplot(2, 2, 1)
top_confirmed = df.sort_values('Confirmed', ascending=False).head(20)
sns.barplot(x='Confirmed', y='Country/Region', data=top_confirmed, palette='viridis')
plt.title('Top 20 Countries by Confirmed Cases')
plt.xlabel('Confirmed Cases')
plt.ylabel('Country')

# 2. Death Rate vs Recovery Rate Scatter Plot
plt.subplot(2, 2, 2)
sns.scatterplot(x='Recovered / 100 Cases', y='Deaths / 100 Cases', 
                data=df, hue='WHO Region', size='Confirmed', sizes=(20, 200))
plt.title('Death Rate vs Recovery Rate by Region')
plt.xlabel('Recovery Rate (%)')
plt.ylabel('Death Rate (%)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# 3. Cases Distribution by WHO Region
plt.subplot(2, 2, 3)
region_stats = df.groupby('WHO Region')[['Confirmed', 'Deaths', 'Recovered', 'Active']].sum()
region_stats.plot(kind='bar', stacked=True, ax=plt.gca())
plt.title('COVID-19 Cases Distribution by WHO Region')
plt.xlabel('WHO Region')
plt.ylabel('Number of Cases')
plt.xticks(rotation=45)

# 4. Weekly Increase Percentage Heatmap
plt.subplot(2, 2, 4)
top_weekly_increase = df.sort_values('1 week % increase', ascending=False).head(10)
heatmap_data = top_weekly_increase[['Country/Region', '1 week % increase', 'Confirmed']]
heatmap_data = heatmap_data.set_index('Country/Region')
sns.heatmap(heatmap_data[['1 week % increase']], annot=True, fmt='.1f', cmap='YlOrRd')
plt.title('Top 10 Countries by Weekly % Increase')
plt.ylabel('Country')

plt.tight_layout()
plt.show()

# Additional Visualizations
# 5. Deaths per 100 Cases Distribution
plt.figure(figsize=(10, 6))
sns.boxplot(x='WHO Region', y='Deaths / 100 Cases', data=df)
plt.title('Distribution of Death Rates by WHO Region')
plt.xticks(rotation=45)
plt.show()

# 6. Active Cases vs New Cases
plt.figure(figsize=(10, 6))
sns.regplot(x='Active', y='New cases', data=df, scatter_kws={'alpha':0.5})
plt.xscale('log')
plt.yscale('log')
plt.title('Active Cases vs New Cases (Log Scale)')
plt.show()

# 7. Top 10 Countries by Deaths
plt.figure(figsize=(12, 6))
top_deaths = df.sort_values('Deaths', ascending=False).head(10)
sns.barplot(x='Deaths', y='Country/Region', data=top_deaths, palette='magma')
plt.title('Top 10 Countries by Deaths')
plt.xlabel('Total Deaths')
plt.ylabel('Country')
plt.show()