import pandas as pd
import seaborn as sns
import plotly
import matplotlib.pyplot as plt

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

sns.set_context("notebook", font_scale=.9)
sns.set_style("whitegrid")
palette_2013= sns.color_palette("hls",5)
palette_2014= sns.hls_palette(5,l=.3,s=.8)
palette_2012 = sns.hls_palette(5,l=.5,s=.6)
palette_2011 = sns.hls_palette(5,l=.7,s=.5)
palette_2010 = sns.hls_palette(5,l=.8,s=.4)

#function for plotting the graph using stripplot
def plot_continent_graph(continent):
    ax = sns.stripplot(x='Country Name', y='2010',hue='Country Name',data=continent, palette=palette_2010,jitter=True)
    ax = sns.stripplot(x='Country Name', y='2011',data=continent, palette=palette_2011)
    ax = sns.stripplot(x='Country Name', y='2012',data=continent, palette=palette_2012)
    ax = sns.stripplot(x='Country Name', y='2013',data=continent, palette=palette_2013)
    ax = sns.stripplot(x='Country Name', y='2014',data=continent, palette=palette_2014)
    ax.legend().set_visible(False)
    return ax

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
    df_highest_countries = sns.barplot(x='Year', y='value', hue='Continent', data=df_highest_countries)
    return df_highest_countries

#select_highest_countries(continents_list)
#plt.xticks(rotation=90)

def select_lowest_countries(continents_list):
    df_lowest_countries = pd.concat(continents_list)
    #melt for Year values in column
    df_lowest_countries = pd.melt(df_lowest_countries, id_vars=['Continent', 'Country Name', 'Country Code'], var_name='Year')
    #aggregate highest value and merge back to original set
    df_lowest_countries = df_lowest_countries.groupby(['Year', 'Continent'])['value'].min().reset_index().\
        merge(df_lowest_countries, on=['Year', 'Continent', 'value'])
    df_lowest_countries = sns.barplot(x='Year', y='value', hue='Continent', data=df_lowest_countries)
    df_lowest_countries.set_title('Lowest Unemployment Rates for each Continent 2010-2014')
    return df_lowest_countries

select_lowest_countries(continents_list)

"""def show_mean_continent(continents_list):
    df_mean_continent = pd.DataFrame()
    for continent in continents_list:
        print(continent['Continent'].iloc[0], 'gfdgdg', continent[['2010','2011','2012','2013','2014']].mean())
        df_mean_continent.append(continent[['2010','2011','2012','2013','2014']].mean(), ignore_index=True)
    return df_mean_continent """

def show_mean_continent(continents_list):
    df_mean_continent = pd.concat(continents_list)
    df_mean_continent = df_mean_continent.groupby('Continent')[['2010','2011','2012','2013','2014']].mean()
    df_mean_continent = df_mean_continent.plot.bar()
    return df_mean_continent

def plot_map(continents_list):
    df_countries = pd.concat(continents_list)
    data = [dict(
            type = 'choropleth',
            locations = df_countries['Country Code'],
            z = df_countries['2014'],
            text = df_countries['Country Name'],
            colorscale = [[0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
            [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"]],
            autocolorscale = False,
            reversescale = True,
            marker = dict(
                line = dict (
                    color = 'rgb(180,180,180)',
                    width = 0.5
                ) ),
            colorbar = dict(
                autotick = False,
                tickprefix = '$',
                title = 'Youth Unemployment<br>Rates'),
            )]
    layout = dict(
        title = '2014 World Bank Youth Unemployment Rate <br> Source:\
                <a href="https://www.kaggle.com/sovannt/world-bank-youth-unemployment</a>',
        geo = dict(
            showframe = False,
            showcoastlines = False,
            projection = dict(
                type = 'Mercator'
            )
        )
    )
            
    fig = dict( data=data, layout=layout )
    plotly.offline.plot( fig, validate=False, filename='d3-world-map' )
    
"""
Linear Regression
x_axis = cause, independent variable (the thing you are changing), explanatory
y_axis = effect, dependent variable (the thing you are measuring), response
"""
def plot_compare_var(x, y, data):
    ax = sns.regplot(x=x, y=y, data=data)
    plt.show(ax)
    
#plot_compare_var('2010','2014', oceanian_countries)

#plot_map(continents_list)
#print(oceanian_countries[['2010','2011','2012','2013']].mean())
#print(show_mean_continent(continents_list))
#print(oceanian_countries)
#print(select_lowest_countries(continents_list))
#print(show_lowest_countries(continents_list))
#print(select_highest_rate(african_countries, '2014'))
#print(select_lowest_rate(oceanian_countries, '2010'))
#plot_continent_graph(asian_countries)
#plt.xticks(rotation=90)
#plot_continent_graph(asian_countries)