import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

#read csv data
country_data = 'data/raw/API_ILO_country_YU.csv'
df = pd.read_csv(country_data)

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

#create a new data frame for African countries
african_countries = df[df['Country Name'].isin(african_countries_list)]

#create a new data frame for Asian countries
asian_countries = df[df['Country Name'].isin(asian_countries_list)]

#create a new data frame for European countries
european_countries = df[df['Country Name'].isin(european_countries_list)]

#create a new data frame for North American countries
north_american_countries = df[df['Country Name'].isin(north_american_countries_list)]

#create a new data frame for South American countries
south_american_countries = df[df['Country Name'].isin(south_american_countries_list)]

#create a new data frame for Oceanian countries
oceanian_countries = df[df['Country Name'].isin(oceanian_countries_list)]

#strip plot for oceanian countries which compares data 2010-2014 from light to dark color
sb.set_context("notebook", font_scale=.9)
sb.set_style("whitegrid")
palette_2013= sb.color_palette("hls",5)
palette_2014= sb.hls_palette(5,l=.3,s=.8)
palette_2012 = sb.hls_palette(5,l=.5,s=.6)
palette_2011 = sb.hls_palette(5,l=.7,s=.5)
palette_2010 = sb.hls_palette(5,l=.8,s=.4)

ax = sb.stripplot(x='Country Name', y='2010',hue='Country Name',data=oceanian_countries, palette=palette_2010,jitter=True)
ax = sb.stripplot(x='Country Name', y='2011',data=oceanian_countries, palette=palette_2011)
ax = sb.stripplot(x='Country Name', y='2012',data=oceanian_countries, palette=palette_2012)
ax = sb.stripplot(x='Country Name', y='2013',data=oceanian_countries, palette=palette_2013)
ax = sb.stripplot(x='Country Name', y='2014',data=oceanian_countries, palette=palette_2014)
print(oceanian_countries)