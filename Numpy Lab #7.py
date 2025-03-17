import numpy as np

#Boolean mask 
rand_numbers = np.random.randint(1, 101, 100)
mask = (rand_numbers % 3 == 0)
rand_numbers[mask] = -1

#Fancy Indexing
matrix = np.random.randint(1, 101, (5, 5))
alternate_rows = matrix[::2]

#Sorting
matrix = np.random.randint(1, 101, (10, 10))
sorted_matrix = matrix[matrix[:, 0].argsort()]

np.random.seed(42)
rainfall = np.random.gamma(shape=2.0, scale=2.0, size=365)  # Synthetic daily rainfall data
rainfall[np.random.choice(365, 100, replace=False)] = 0  # 100 dry days

# Basic rainy day count
rainy_count = np.sum(rainfall > 0)
print(f"Number of rainy days: {rainy_count}\n")

# Heavy rainy day count
heavy_percent = np.sum(rainfall > 5) / len(rainfall)*100
print(f"Percentage of heavy rain days: {heavy_percent:.2f}%\n")

# Dry spell count
dry_days = rainfall == 0
dry_spells = np.diff(np.where(dry_days)[0])
longest = np.max(np.concatenate(([0], dry_spells)))
print(f"Longest dry spell: {longest}\n")

# Top rain fall
top_ten_rain = np.sort(rainfall)[-10:]  # 10 wettest days
print(f"Top 10 rainiest days: \n{top_ten_rain}\n")

# Monthly avg
days = np.array([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
month_index = np.cumsum(np.insert(days, 0, 0))[:-1]
month_avg = [np.mean(rainfall[start:start + length]) for start, length in zip(month_index, days)]
print(f"Monthly average rainfall:")
for month, avg in enumerate(month_avg, start=1):
    print(f"Month {month}: {avg:.2f} mm")

# Sorting & Median
sorted_rainfall = np.sort(rainfall)
median_rainfall = np.median(rainfall)
print(f"\nMedian rainfall: {median_rainfall:.2f} mm\n")

# Percentile
percentile_90 = np.percentile(rainfall, 90)
print(f"90th percentile of rainfall: {percentile_90:.2f} mm\n")

# Creating a structured array
dtype = [('day', 'i4'), ('rainfall', 'f4'), ('is_rainy', 'bool')]
days = np.arange(1, 366)
is_rainy = rainfall > 0
structured_array = np.array(list(zip(days, rainfall, is_rainy)), dtype=dtype)

# Filtering rainy days
rain_data = structured_array[structured_array['is_rainy']]
avg_rain = np.mean(rain_data['rainfall'])
print(f"Average rainfall on rainy days: {avg_rain:.2f} mm\n")

# Sorting by rainfall
sorted_rainfall = np.sort(structured_array, order='rainfall')
top_5 = sorted_rainfall[-5:]
print("Top 5 rainiest days:")
for day in top_5:
    print(f"Day {day['day']} - Rainfall: {day['rainfall']:.2f} mm")
