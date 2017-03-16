import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

#read csv data
country_data = 'data/raw/API_ILO_country_YU.csv'
df = pd.read_csv(country_data)


#create a new list for Asian Countries
asian_countries_list = ['Afghanistan','Armenia','Azerbaijan','Bahrain','Bangladesh','Bhutan','Brunei','Cambodia','China','Cyprus',
'Georgia','India','Indonesia','Iran','Iraq','Israel','Japan','Jordan','Kazakhstan','Kuwait','Kyrgyzstan','Laos','Lebanon',
'Malaysia','Maldives','Mongolia','Myanmar','Nepal','North Korea','Oman','Pakistan','Palestine','Philippines','Qatar','Russia',
'Saudi Arabia','Singapore','South Korea','Sri Lanka', 'Syria','Taiwan','Tajikistan','Thailand','Timor-Leste','Turkey','Turkmenistan'
'United Arab Emirates','Uzbekistan','Vietnam','Yemen']

#create a new data frame for asian countries
asian_countries = df[df['Country Name'].isin(asian_countries_list)]

print(asian_countries)