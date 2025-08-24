import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/colors.csv')

# Return the unique values of the row and colunm
# print(df.nunique())

# Run around the DataFrame
# for index in range(len(df)):
#     print(f"the color {df['name'].loc[index]} is transparent: {df['is_trans'].loc[index]}")

# Counting the values in the column by item
# print(df.is_trans.value_counts())

# Or you can use this way
# print(df.groupby('is_trans ').count())

df_sets = pd.read_csv("data/sets.csv")

# Collecting data
print('First year: ')
print(df_sets['year'].min())
print(f"the index of the first set lego by year is: {df_sets['year'].idxmin()}")

print(df_sets['name'].loc[df_sets['year'].idxmin()])

# The 5 set in the first year
print('The 5 set in the first year')
print(df_sets.sort_values('year').head())

print("The five sets the first year with other metodh ")
print(df_sets[df_sets['year'] == 1949])
# print(df_sets.name.value_counts())

# Find the top 5 LEGO sets with the most number of parts.
print('The top 5 LEGO sets with the most number of parts.')
print(df_sets.sort_values('num_parts', ascending=False).head())

print('The number of sets by year')
sets_by_years = df_sets.groupby('year').count()

print(sets_by_years['set_num'])


# Create a column Themes by year
themes_by_year = df_sets.groupby('year').agg( {'theme_id': pd.Series.nunique})

themes_by_year.rename(columns={'theme_id': 'nr_themes'},inplace=True)
print(themes_by_year.head())

# ax1 = plt.gca() # get the axis
# ax2 = ax1.twinx() # create another axis that shares the same x-axis
# # Printing the Graph
# # Add styling
# ax1.plot(sets_by_years['set_num'], color='g')
# ax2.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2],'b')

# Add a label
# ax1.set_xlabel('Year')
# ax1.set_ylabel('Number of Sets', color='green')
# ax2.set_ylabel('Number of theme', color='blue')
# plt.show()

# Printing a Graph with the number of parts by year
# num_of_parts_by_year = df_sets.groupby('year').agg({'num_parts':pd.Series.nunique})
# print(num_of_parts_by_year.tail())
# print(num_of_parts_by_year.count())
# plt.scatter(num_of_parts_by_year.index, num_of_parts_by_year)

# Counting the sets themes by id
set_theme_count = df_sets['theme_id'].value_counts()

# Changing the structure of DataFrame and creating a column ID and  SET_COUNT
set_theme_count = pd.DataFrame({'id':set_theme_count.index, 'set_count': set_theme_count.values} )
print(set_theme_count[:5])
# plt.show()

df_theme = pd.read_csv('data/themes.csv')
print(df_theme.head())

# Printing the Theme by name
print("Themes by name")
print(df_theme[df_theme.name == 'Star Wars'])

# Printing Sets by id
print("Sets by Id")
print(df_sets[df_sets.theme_id == 18])

# Join two DATAFRAME by a column that have a same name we`ll use the pandas.merge methods, don`t forget 'on' must set with the column
merged_df = pd.merge(set_theme_count, df_theme, on='id')

print('Merged DataFrame')
print(merged_df[:3])



# Customizing the graph
plt.figure(figsize=(14,8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.xlabel('Theme name', fontsize=14)
plt.ylabel('Num of Sets', fontsize=14)
# Printing the graph
plt.bar(merged_df.name[:10], merged_df.set_count[:10])
plt.show()