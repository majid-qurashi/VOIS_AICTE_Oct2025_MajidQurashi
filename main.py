import pandas as pd

# Load the Excel file
df = pd.read_excel('data_analysis.xlsx')

# Preview the data
print(df.head())

#Q1
print(df.columns)
property_types = df['room type'].unique()
print(f"1. Different Property/Room Types:\n{property_types}")

#Q2
highest_listings = df['neighbourhood group'].value_counts().nlargest(1)
print(f"\n2. Neighborhood Group with Highest Number of Listings:\n{highest_listings}")

#Q3
highest_avg_prices = (
    df.groupby('neighbourhood group')['price']
    .mean()
    .sort_values(ascending=False)
    .head()
)
print(f"\n3. Neighborhood Groups with Highest Average Prices:\n{highest_avg_prices}")

#Q4
correlation_year_price = df[['Construction year', 'price']].corr().loc['Construction year', 'price']
print(f"\n4. Correlation between Construction Year and Price: {correlation_year_price:.4f}")

#Q5
top_hosts = df['host id'].value_counts().nlargest(10)
print(f"\n5. Top 10 Hosts by Calculated Host Listing Count (host id):\n{top_hosts}")

#Q6
avg_scores = (
    df.groupby('host_identity_verified')['review rate number']
    .mean()
)
print(f"\n6. Average Review Rate by Host Identity Verification Status:\n{avg_scores}")
# A higher average rate for 't' (or 'True') suggests they are more likely to receive positive reviews.

#Q7
# Note: Ensure both columns are numeric.
correlation_price_fee = df[['price', 'service fee']].corr().loc['price', 'service fee']
print(f"\n7. Correlation between Price and Service Fee: {correlation_price_fee:.4f}")

#Q8
# Average for all listings
overall_avg_rating = df['review rate number'].mean()
print(f"\n8a. Overall Average Review Rate Number: {overall_avg_rating:.2f}")

# Variation by neighborhood group and room type
avg_rating_by_groups = (
    df.groupby(['neighbourhood group', 'room type'])['review rate number']
    .mean()
    .unstack()
)
print(f"\n8b. Average Review Rate by Neighborhood Group and Room Type:\n{avg_rating_by_groups}")

#Q9
# Check the correlation between 'calculated host listings count' and 'availability 365'
# Note: Ensure both columns are numeric.
correlation_count_availability = (
    df[['calculated host listings count', 'availability 365']]
    .corr()
    .loc['calculated host listings count', 'availability 365']
)
print(f"\n9. Correlation between Host Listing Count and Availability 365: {correlation_count_availability:.4f}")
# A positive correlation would suggest that hosts with more listings also tend to have higher overall availability.