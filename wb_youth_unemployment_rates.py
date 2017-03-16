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
'Mozambique','Namibia','Niger','Nigeria','Réunion','Rwanda','Saint Helena','Sao Tome and Principe','Senegal','Seychelles','Sierra Leone',
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

#create a new list for North Amrican Countries
north_american_countries = ['Antigua and Barbuda','Bahamas','Barbados','Belize','Bermuda','British Virgin Islands','Canada','Cayman Islands',
'Costa Rica','Cuba','Dominica','Dominican Republic','El Salvador','Greenland','Grenada','Guadeloupe','Guatemala','Haiti','Honduras','Jamaica',
'Martinique','Mexico','Nicaragua','Panama','Puerto Rico','Trinidad and Tobago','United States']

#create a new data frame for asian countries
asian_countries = df[df['Country Name'].isin(asian_countries_list)]

print(asian_countries)