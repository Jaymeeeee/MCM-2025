import pandas as pd
import numpy as np

# medal_counts = pd.read_csv('summerOly_medal_counts.csv')
# hosts = pd.read_csv('summerOly_hosts.csv')
# programs = pd.read_csv('summerOly_programs.csv')
# athletes = pd.read_csv('summerOly_athletes.csv')
#
# olympic_country_codes = {
#     # 现存国家/地区
#     "Afghanistan": "AFG",
#     "Albania": "ALB",
#     "Algeria": "ALG",
#     "American Samoa": "ASA",
#     "Andorra": "AND",
#     "Angola": "ANG",
#     "Antigua and Barbuda": "ANT",
#     "Argentina": "ARG",
#     "Armenia": "ARM",
#     "Aruba": "ARU",
#     "Australia": "AUS",
#     "Austria": "AUT",
#     "Azerbaijan": "AZE",
#     "Bahamas": "BAH",
#     "Bahrain": "BRN",
#     "Bangladesh": "BAN",
#     "Barbados": "BAR",
#     "Belarus": "BLR",
#     "Belgium": "BEL",
#     "Belize": "BIZ",
#     "Benin": "BEN",
#     "Bermuda": "BER",
#     "Bhutan": "BHU",
#     "Bolivia": "BOL",
#     "Bosnia and Herzegovina": "BIH",
#     "Botswana": "BOT",
#     "Brazil": "BRA",
#     "British Virgin Islands": "IVB",
#     "Brunei": "BRU",
#     "Bulgaria": "BUL",
#     "Burkina Faso": "BUR",
#     "Burundi": "BDI",
#     "Cabo Verde": "CPV",
#     "Cambodia": "CAM",
#     "Cameroon": "CMR",
#     "Canada": "CAN",
#     "Cayman Islands": "CAY",
#     "Central African Republic": "CAF",
#     "Chad": "CHA",
#     "Chile": "CHI",
#     "China": "CHN",
#     "Colombia": "COL",
#     "Comoros": "COM",
#     "Congo": "CGO",
#     "Congo (DRC)": "COD",
#     "Cook Islands": "COK",
#     "Costa Rica": "CRC",
#     "Croatia": "CRO",
#     "Cuba": "CUB",
#     "Cyprus": "CYP",
#     "Czech Republic": "CZE",
#     "Denmark": "DEN",
#     "Djibouti": "DJI",
#     "Dominica": "DMA",
#     "Dominican Republic": "DOM",
#     "Ecuador": "ECU",
#     "Egypt": "EGY",
#     "El Salvador": "ESA",
#     "Equatorial Guinea": "GEQ",
#     "Eritrea": "ERI",
#     "Estonia": "EST",
#     "Eswatini": "SWZ",
#     "Ethiopia": "ETH",
#     "Fiji": "FIJ",
#     "Finland": "FIN",
#     "France": "FRA",
#     "Gabon": "GAB",
#     "Gambia": "GAM",
#     "Georgia": "GEO",
#     "Germany": "GER",
#     "Ghana": "GHA",
#     "Great Britain": "GBR",
#     "Greece": "GRE",
#     "Grenada": "GRN",
#     "Guam": "GUM",
#     "Guatemala": "GUA",
#     "Guinea": "GUI",
#     "Guinea-Bissau": "GBS",
#     "Guyana": "GUY",
#     "Haiti": "HAI",
#     "Honduras": "HON",
#     "Hong Kong": "HKG",
#     "Hungary": "HUN",
#     "Iceland": "ISL",
#     "India": "IND",
#     "Indonesia": "INA",
#     "Iran": "IRI",
#     "Iraq": "IRQ",
#     "Ireland": "IRL",
#     "Israel": "ISR",
#     "Italy": "ITA",
#     "Ivory Coast": "CIV",
#     "Jamaica": "JAM",
#     "Japan": "JPN",
#     "Jordan": "JOR",
#     "Kazakhstan": "KAZ",
#     "Kenya": "KEN",
#     "Kiribati": "KIR",
#     "Kosovo": "KOS",
#     "Kuwait": "KUW",
#     "Kyrgyzstan": "KGZ",
#     "Laos": "LAO",
#     "Latvia": "LAT",
#     "Lebanon": "LBN",
#     "Lesotho": "LES",
#     "Liberia": "LBR",
#     "Libya": "LBA",
#     "Liechtenstein": "LIE",
#     "Lithuania": "LTU",
#     "Luxembourg": "LUX",
#     "Madagascar": "MAD",
#     "Malawi": "MAW",
#     "Malaysia": "MAS",
#     "Maldives": "MDV",
#     "Mali": "MLI",
#     "Malta": "MLT",
#     "Marshall Islands": "MHL",
#     "Mauritania": "MTN",
#     "Mauritius": "MRI",
#     "Mexico": "MEX",
#     "Micronesia": "FSM",
#     "Moldova": "MDA",
#     "Monaco": "MON",
#     "Mongolia": "MGL",
#     "Montenegro": "MNE",
#     "Morocco": "MAR",
#     "Mozambique": "MOZ",
#     "Myanmar": "MYA",
#     "Namibia": "NAM",
#     "Nauru": "NRU",
#     "Nepal": "NEP",
#     "Netherlands": "NED",
#     "New Zealand": "NZL",
#     "Nicaragua": "NCA",
#     "Niger": "NIG",
#     "Nigeria": "NGR",
#     "North Macedonia": "MKD",
#     "Norway": "NOR",
#     "Oman": "OMA",
#     "Pakistan": "PAK",
#     "Palau": "PLW",
#     "Palestine": "PLE",
#     "Panama": "PAN",
#     "Papua New Guinea": "PNG",
#     "Paraguay": "PAR",
#     "Peru": "PER",
#     "Philippines": "PHI",
#     "Poland": "POL",
#     "Portugal": "POR",
#     "Puerto Rico": "PUR",
#     "Qatar": "QAT",
#     "Romania": "ROU",
#     "Russia": "RUS",
#     "Rwanda": "RWA",
#     "Saint Kitts and Nevis": "SKN",
#     "Saint Lucia": "LCA",
#     "Saint Vincent and the Grenadines": "VIN",
#     "Samoa": "SAM",
#     "San Marino": "SMR",
#     "Sao Tome and Principe": "STP",
#     "Saudi Arabia": "KSA",
#     "Senegal": "SEN",
#     "Serbia": "SRB",
#     "Seychelles": "SEY",
#     "Sierra Leone": "SLE",
#     "Singapore": "SGP",
#     "Slovakia": "SVK",
#     "Slovenia": "SLO",
#     "Solomon Islands": "SOL",
#     "Somalia": "SOM",
#     "South Africa": "RSA",
#     "South Korea": "KOR",
#     "South Sudan": "SSD",
#     "Spain": "ESP",
#     "Sri Lanka": "SRI",
#     "Sudan": "SUD",
#     "Suriname": "SUR",
#     "Sweden": "SWE",
#     "Switzerland": "SUI",
#     "Syria": "SYR",
#     "Tajikistan": "TJK",
#     "Tanzania": "TAN",
#     "Thailand": "THA",
#     "Timor-Leste": "TLS",
#     "Togo": "TOG",
#     "Tonga": "TGA",
#     "Trinidad and Tobago": "TTO",
#     "Tunisia": "TUN",
#     "Turkey": "TUR",
#     "Turkmenistan": "TKM",
#     "Tuvalu": "TUV",
#     "Uganda": "UGA",
#     "Ukraine": "UKR",
#     "United Arab Emirates": "UAE",
#     "United States": "USA",
#     "Uruguay": "URU",
#     "Uzbekistan": "UZB",
#     "Vanuatu": "VAN",
#     "Vatican": "VAT",
#     "Venezuela": "VEN",
#     "Vietnam": "VIE",
#     "Virgin Islands": "ISV",
#     "Yemen": "YEM",
#     "Zambia": "ZAM",
#     "Zimbabwe": "ZIM",
#
#     # 历史国家/地区
#     "Czechoslovakia": "TCH",
#     "East Germany": "GDR",
#     "West Germany": "FRG",
#     "Soviet Union": "URS",
#     "Yugoslavia": "YUG",
#     "Serbia and Montenegro": "SCG",
#     "North Yemen": "YAR",
#     "South Yemen": "YMD",
#
#     # 手动添加
#     "Bohemia":"TCH",
#     "Australasia":"AUS",
#     "North Korea":"PRK",
#     "Formosa":"TPE",
#     "Taiwan":"TPE",
#     "Chinese Taipei":"TPE",
#     "Refugee Olympic Team":"ROT",
#     "ROC":"RUS",
#     "Macedonia":"MKD",
#     "Ceylon":"Ceylon",
#     "United Team of Germany":"GER"
# }
#
# medal_counts['NOC']=medal_counts['NOC'].map(olympic_country_codes).fillna('XXX')
# # medal_counts.to_csv('medal_counts_updated.csv', index=False)
#
# hosts['Host']=hosts['Host'].str.split(',\xa0', n=1).str[1]
# hosts['Host']=hosts['Host'].map(olympic_country_codes).fillna('XXX')
# hosts.to_csv('hosts_updated.csv',index=False)
#
# # 东道主,前几届的奖牌总数
#
# # medal_counts['Year'] = medal_counts['Year'].astype(int)
# # hosts['Year'] = hosts['Year'].astype(int)
# # medal_counts = pd.merge(medal_counts, hosts, on='Year', how='left')
# # medal_counts['Is_Host'] = medal_counts['NOC'] == medal_counts['Host']
#
# country_total_medal=medal_counts.groupby(['NOC'])['Total'].sum().reset_index()
# country_total_gold=medal_counts.groupby(['NOC'])['Gold'].sum().reset_index()
#
# # country_total_medal.to_csv('country_total_medal.csv')
# # country_total_gold.to_csv('country_total_gold.csv')



# 假设原始数据存储在 'test.csv' 文件中
file_path = 'test.csv'

# 读取CSV文件
df = pd.read_csv(file_path)

# 定义需要的列名
columns = ['NOC', 'Year', 'Athletics', 'Balls', 'Combat', 'Shooting', 'Swimming',
           'Cycling', 'Weightlifting', 'WaterSport', 'Others', 'Gymnastics', 'Diving']

# 初始化一个空的列表，用于存储每行数据
data = []

# 遍历原始数据，按NOC和Year分组，并统计每个运动项目的奖牌数
for (noc, year), group in df.groupby(['NOC', 'Year']):
    # 初始化一个字典，存储当前NOC和Year的奖牌数
    medals = {'NOC': noc, 'Year': year}
    for sport in columns[2:]:  # 跳过NOC和Year列
        medals[sport] = group[group['Sport'] == sport]['Medal'].sum()
    # 将当前NOC和Year的奖牌数添加到数据列表中
    data.append(medals)

# 将数据列表转换为DataFrame
result_df = pd.DataFrame(data)

# 将结果DataFrame保存到新的CSV文件中
result_df.to_csv('processed_data.csv', index=False)

# 打印结果
print(result_df)