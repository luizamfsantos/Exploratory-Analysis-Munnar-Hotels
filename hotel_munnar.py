# %% [markdown]
# Dataset: Hotels in Munnar, Kerala
# 
# Columns:
# - Hotel Name: Name of the hotel
# - Rating: Rating value
# - Rating Description: Short Description of the given rating
# - Reviews: No. of reviews
# - Star rating: Star rating of the hotel
# - Location: Place were the hotel is located
# - Nearest Landmark: Landmark near to hotel
# - Distance to the Landmark: Distance to the landmark from the hotel(m/km)
# - Price: Price(rupees) for 1 Night stay(in Rupees)
# - Tax: Tax(rupees) payable for the booking amount
# 
# Please Note:
# 
# Price given here is for one night (base room).
# Tax given here is slapped on top of the price payable. Therefore, total amount = Price + Tax

# %% [markdown]
# # import libraries

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns  
import scipy.stats as stats


# %% [markdown]
# # import data

# %%
data = pd.read_csv('munnar.csv')

# %%
data.head()

# %% [markdown]
# # clean data

# %% [markdown]
# ### handle missing data

# %%
data.isnull().sum()

# %%
data.shape[0]

# %%
data[data.isnull().any(axis=1)]

# %%
# drop star rating column
data.drop(['Star Rating'], axis=1, inplace=True)
data.head()

# %%
data.isnull().sum()

# %%
data.dropna(inplace=True)

# %% [markdown]
# ### check duplicates

# %%
# count duplicate rows
data.duplicated().sum()

# %% [markdown]
# ### rename columns

# %%
data.rename(columns={
    'Rating Description': 'Rating_Description',
    'Star rating': 'Star_Rating',
    'Nearest Landmark': 'Nearest_Landmark',
    'Distance to Landmark': 'Distance_to_Landmark',
    'Price': 'Price_Rupees',
    'Tax': 'Tax_Rupees'
}, inplace=True)
data.head()

# %% [markdown]
# ### convert types

# %%
data.dtypes

# %%
data['Price_Rupees'] = data['Price_Rupees'].str.replace(',', '').astype(float)

# %%
data['Tax_Rupees'] = data['Tax_Rupees'].str.replace(',', '').astype(float)

# %%
# some of the distances have 'km' in them, remove it and multiply by 1000
# if they have 'm' in them, just remove the 'm'

for row, col in data.iterrows():
    dist = data.loc[row, 'Distance_to_Landmark']
    if 'km' in dist:
        dist = dist.replace('km', '')
        dist = float(dist) * 1000
    elif 'm' in dist:
        dist = dist.replace('m', '')
    data.at[row, 'Distance_to_Landmark'] = str(dist)
data.head()

# %%
# change type of distance column to float
data['Distance_to_Landmark'] = data['Distance_to_Landmark'].astype(float)
data.head()

# %%
data['Reviews'] = pd.to_numeric(data['Reviews'])

# %%
data.dtypes

# %%
# rename column distance_to_landmark to distance_to_landmark_meters
data.rename(columns={'Distance_to_Landmark': 'Distance_to_Landmark_meters'}, inplace=True)
data.head()

# %% [markdown]
# # exploratory analysis

# %%
data.columns

# %%
# display basic information about the dataset
data.info()

# %%
data.describe()

# %% [markdown]
# ### Data visualization

# %%
# Data Visualization
plt.figure(figsize=(12, 6))

# Define a custom color palette
custom_order = ["Average", "Good", "Very Good", "Excellent"]
custom_palette = sns.color_palette("Blues", len(custom_order))

# Histogram of Ratings
plt.subplot(2, 2, 1)
sns.histplot(data['Rating'], bins=20, kde=True)
plt.title('Distribution of Ratings')

# Countplot of Rating Descriptions with custom order and colors
plt.subplot(2, 2, 2)
sns.countplot(data=data, x='Rating_Description', order=custom_order, palette=custom_palette)
plt.xticks(rotation=45)
plt.title('Count of Ratings by Description (Custom Order)')

# Distribution of Prices
plt.subplot(2, 2, 3)
sns.histplot(data['Price_Rupees'], bins=30, kde=True)
plt.title('Distribution of Prices (Rupees)')

# Distribution of Taxes
plt.subplot(2, 2, 4)
sns.histplot(data['Tax_Rupees'], bins=30, kde=True)
plt.title('Distribution of Taxes (Rupees)')

plt.tight_layout()
plt.show()



