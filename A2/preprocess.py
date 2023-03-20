import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

population = pd.read_csv('./world_population.csv', encoding = 'unicode_escape')
gdp = pd.read_csv('./gdp_per_capita.csv')

years = ['1970','1980','1990','2000','2010','2020']
gdp_year = gdp[['Country', 'Code']]

for year in years:
    gdp_year[year+'gdp'] = gdp[year]
    population.rename(columns={year:year+'population'}, inplace = True)

merged = pd.merge(gdp_year, population, on = 'Code')
print(merged.columns)

data = pd.DataFrame()
print(len(merged))
merged.dropna(inplace = True)
print(len(merged))
countries = merged['Code']
merged.rename(columns={'Country_x':'Country'}, inplace = True)

for i, country in enumerate(countries):
    for year in years:
        row = merged.iloc[i]
        newrow = row[['Country','Code','Rank','Capital','Continent','Growth Rate','World Population Percentage']]
        newrow['gdp'] = row[year+'gdp']
        newrow['population'] = row[year+'population']
        newrow['year'] = year
        data = data.append(newrow)
data.to_csv('data.csv')