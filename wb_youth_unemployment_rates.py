import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

#read csv data
country_data = 'data/raw/API_ILO_country_YU.csv'
df = pd.read_csv(country_data)

#create new data frame from the raw data
new_df = df.copy()


"""
CREATE LISTS FOR EACH CONTINENT TO FILTER FROM THE DATA SET
"""

#create a new list fo African Countries
african_countries_list = ['Algeria','Angola','Benin','Botswana','Burkina','Burundi','Cameroon','Cape Verde','Central African Republic',
'Chad','Comoros','Congo, Rep.','Cote d\'Ivoire','Djibouti','Egypt','Equatorial Guinea','Eritrea','Ethiopia','Gabon','Gambia','Ghana',
'Guinea','Guinea-Bissau','Kenya','Lesotho','Liberia','Libya','Madagascar','Malawi','Mali','Mauritania','Mauritius','Mayotte','Morocco',
'Mozambique','Namibia','Niger','Nigeria','Rwanda','Saint Helena','Sao Tome and Principe','Senegal','Seychelles','Sierra Leone',
'Somalia','South Africa','Sudan','Swaziland','Tanzania','Togo','Tunisia','Uganda','Western Sahara','Zambia','Zimbabwe']

#create a new list for Asian Countries
asian_countries_list = ['Afghanistan','Armenia','Azerbaijan','Bahrain','Bangladesh','Bhutan','Brunei','Cambodia','China','Cyprus',
'Georgia','India','Indonesia','Iran','Iraq','Israel','Japan','Jordan','Kazakhstan','Kuwait','Kyrgyzstan','Laos','Lebanon',
'Malaysia','Maldives','Mongolia','Myanmar','Nepal','North Korea','Oman','Pakistan','Palestine','Philippines','Qatar','Russia',
'Saudi Arabia','Singapore','South Korea','Sri Lanka', 'Syria','Taiwan','Tajikistan','Thailand','Timor-Leste','Turkey','Turkmenistan'
'United Arab Emirates','Uzbekistan','Vietnam','Yemen']

#create a new list for European Countries
european_countries_list = ['Albania','Andorra','Austria','Belarus','Belgium','Bosnia and Herzegovina','Bulgaria','Croatia','Czech Republic',
'Denmark','Estonia','Faroe Islands','Finland','France','Germany','Gibraltar','Greece','Hungary','Iceland','Ireland','Italy','Kosovo','Latvia',
'Liechtenstein','Lithuania','Luxembourg','Malta','Moldova','Monaco','Montenegro','Netherlands','Norway','Poland','Portugal','Romania','Russia',
'San Marino','Serbia','Slovakia','Slovenia','Spain','Sweden','Switzerland','Ukraine','United Kingdom','Vatican City']

#create a new list for North American Countries
north_american_countries_list = ['Antigua and Barbuda','Bahamas','Barbados','Belize','Bermuda','British Virgin Islands','Canada','Cayman Islands',
'Costa Rica','Cuba','Dominica','Dominican Republic','El Salvador','Greenland','Grenada','Guadeloupe','Guatemala','Haiti','Honduras','Jamaica',
'Martinique','Mexico','Nicaragua','Panama','Puerto Rico','Trinidad and Tobago','United States']

#create new list for South American Countries
south_american_countries_list = ['Argentina','Bolivia','Brazil','Chile','Colombia','Ecuador','Guyana','Paraguay','Peru','Suriname','Uruguay','Venezuela']

#create new list for Oceanian Countries
oceanian_countries_list = ['Australia','Fiji','Guam','Kiribati','Marshall Islands','Micronesia','Nauru','New Zealand','Palau','Papua New Guinea',
'Samoa','Solomon Islands','Tonga','Tuvalu','Vanuatu',]


"""
CREATE NEW DATA FRAME FOR EACH CONTINENT BASED FROM THE COUNTRY LIST
"""

#create a new data frame for African countries and add a new column for Continent
african_countries = new_df[new_df['Country Name'].isin(african_countries_list)]
african_countries.insert(0, 'Continent', 'Africa')

#create a new data frame for Asian countries and add a new column for Continent
asian_countries = df[df['Country Name'].isin(asian_countries_list)]
asian_countries.insert(0, 'Continent', 'Asia')

#create a new data frame for European countries and add a new column for Continent
european_countries = df[df['Country Name'].isin(european_countries_list)]
european_countries.insert(0, 'Continent', 'Europe')

#create a new data frame for North American countries and add a new column for Continent
north_american_countries = df[df['Country Name'].isin(north_american_countries_list)]
north_american_countries.insert(0, 'Continent', 'North America')

#create a new data frame for South American countries and add a new column for Continent
south_american_countries = df[df['Country Name'].isin(south_american_countries_list)]
south_american_countries.insert(0, 'Continent', 'South America')

#create a new data frame for Oceanian countries and add a new column for Continent
oceanian_countries = df[df['Country Name'].isin(oceanian_countries_list)]
oceanian_countries.insert(0, 'Continent', 'Oceania')

#create list of continents
continents_list = [african_countries, asian_countries, european_countries, north_american_countries,
              south_american_countries, oceanian_countries]

"""
PLOT A GRAPH FOR EACH CONTINENT WHICH COMPARES EACH COUNTRY'S DATA FROM 2010-2014
2010 AS THE LIGHTEST COLOR AND 2014 AS THE DARKEST TO SHOW EACH COUNTRY'S PROGRESS
OVER THE PAST 5 YEARS
"""

sb.set_context("notebook", font_scale=.9)
sb.set_style("whitegrid")
palette_2013= sb.color_palette("hls",5)
palette_2014= sb.hls_palette(5,l=.3,s=.8)
palette_2012 = sb.hls_palette(5,l=.5,s=.6)
palette_2011 = sb.hls_palette(5,l=.7,s=.5)
palette_2010 = sb.hls_palette(5,l=.8,s=.4)

#function for plotting the graph using stripplot
def plot_continent_graph(continent):
    sb.stripplot(x='Country Name', y='2010',hue='Country Name',data=continent, palette=palette_2010,jitter=True)
    sb.stripplot(x='Country Name', y='2011',data=continent, palette=palette_2011)
    sb.stripplot(x='Country Name', y='2012',data=continent, palette=palette_2012)
    sb.stripplot(x='Country Name', y='2013',data=continent, palette=palette_2013)
    sb.stripplot(x='Country Name', y='2014',data=continent, palette=palette_2014)

def select_highest_rate(continent, year):
    highest_rate_idx = continent[year].idxmax()
    return continent.loc[highest_rate_idx]

def select_lowest_rate(continent, year):
    lowest_rate_idx = continent[year].idxmin()
    return continent.loc[lowest_rate_idx]

def select_highest_countries(continents_list):
    df_highest_countries = pd.concat(continents_list)
    #melt for Year values in column
    df_highest_countries = pd.melt(df_highest_countries, id_vars=['Continent', 'Country Name', 'Country Code'], var_name='Year')
    #aggregate highest value and merge back to original set
    df_highest_countries = df_highest_countries.groupby(['Year', 'Continent'])['value'].max().reset_index().\
        merge(df_highest_countries, on=['Year', 'Continent', 'value'])
    return df_highest_countries
        
"""def show_highest_countries(continents_list):
    df_highest_countries = {}
    years_list = ['2010','2011','2012','2013','2014']
    for continent in continents_list:
        for year in years_list:
            highest_country = select_highest_rate(continent, year)
            highest_countries = highest_country[['Continent','Country Name',year]]
            df_highest_countries[year] = pd.DataFrame(highest_countries)
    return df_highest_countries"""

"""def show_highest_countries(continents_list):
    highest_countries = {}
    for continent in continents_list:
        highest_country = select_highest_rate(continent, '2010')
        highest_countries[highest_country['Country Name']] = highest_country['2010']
    df_highest_countries = pd.DataFrame(list(highest_countries.items()), columns=['Country', 'Rate'])
    return df_highest_countries"""

def show_lowest_countries(continents_list):
    lowest_countries = {}
    for continent in continents_list:
        lowest_country = select_lowest_rate(continent, '2010')
        lowest_countries[lowest_country['Country Name']] = lowest_country['2010']
    df_lowest_countries = pd.DataFrame(list(lowest_countries.items()), columns=['Country Name','Rate'])
    return df_lowest_countries        

#print(oceanian_countries)
print(select_highest_countries(continents_list))
#print(show_lowest_countries(continents_list))
#print(select_highest_rate(african_countries, '2014'))
#print(select_lowest_rate(oceanian_countries, '2010'))
#plot_continent_graph(oceanian_countries)
#plot_continent_graph(asian_countries)