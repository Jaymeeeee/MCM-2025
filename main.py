import pandas as pd
import numpy as np
import lightgbm as lgb
from lightgbm import LGBMRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

medal_counts = pd.read_csv('summerOly_medal_counts.csv')
hosts = pd.read_csv('summerOly_hosts.csv')
programs = pd.read_csv('summerOly_programs.csv')
athletes = pd.read_csv('summerOly_athletes.csv')

# Model1
# 数据集搭建
# 目前暂且假设特征包括 前三届的平均奖牌数、参加的项目数，参加的运动员数目和是否为东道主
olympic_country_codes = {
    # 现存国家/地区
    "Afghanistan": "AFG",
    "Albania": "ALB",
    "Algeria": "ALG",
    "American Samoa": "ASA",
    "Andorra": "AND",
    "Angola": "ANG",
    "Antigua and Barbuda": "ANT",
    "Argentina": "ARG",
    "Armenia": "ARM",
    "Aruba": "ARU",
    "Australia": "AUS",
    "Austria": "AUT",
    "Azerbaijan": "AZE",
    "Bahamas": "BAH",
    "Bahrain": "BRN",
    "Bangladesh": "BAN",
    "Barbados": "BAR",
    "Belarus": "BLR",
    "Belgium": "BEL",
    "Belize": "BIZ",
    "Benin": "BEN",
    "Bermuda": "BER",
    "Bhutan": "BHU",
    "Bolivia": "BOL",
    "Bosnia and Herzegovina": "BIH",
    "Botswana": "BOT",
    "Brazil": "BRA",
    "British Virgin Islands": "IVB",
    "Brunei": "BRU",
    "Bulgaria": "BUL",
    "Burkina Faso": "BUR",
    "Burundi": "BDI",
    "Cabo Verde": "CPV",
    "Cambodia": "CAM",
    "Cameroon": "CMR",
    "Canada": "CAN",
    "Cayman Islands": "CAY",
    "Central African Republic": "CAF",
    "Chad": "CHA",
    "Chile": "CHI",
    "China": "CHN",
    "Colombia": "COL",
    "Comoros": "COM",
    "Congo": "CGO",
    "Congo (DRC)": "COD",
    "Cook Islands": "COK",
    "Costa Rica": "CRC",
    "Croatia": "CRO",
    "Cuba": "CUB",
    "Cyprus": "CYP",
    "Czech Republic": "CZE",
    "Denmark": "DEN",
    "Djibouti": "DJI",
    "Dominica": "DMA",
    "Dominican Republic": "DOM",
    "Ecuador": "ECU",
    "Egypt": "EGY",
    "El Salvador": "ESA",
    "Equatorial Guinea": "GEQ",
    "Eritrea": "ERI",
    "Estonia": "EST",
    "Eswatini": "SWZ",
    "Ethiopia": "ETH",
    "Fiji": "FIJ",
    "Finland": "FIN",
    "France": "FRA",
    "Gabon": "GAB",
    "Gambia": "GAM",
    "Georgia": "GEO",
    "Germany": "GER",
    "Ghana": "GHA",
    "Great Britain": "GBR",
    "Greece": "GRE",
    "Grenada": "GRN",
    "Guam": "GUM",
    "Guatemala": "GUA",
    "Guinea": "GUI",
    "Guinea-Bissau": "GBS",
    "Guyana": "GUY",
    "Haiti": "HAI",
    "Honduras": "HON",
    "Hong Kong": "HKG",
    "Hungary": "HUN",
    "Iceland": "ISL",
    "India": "IND",
    "Indonesia": "INA",
    "Iran": "IRI",
    "Iraq": "IRQ",
    "Ireland": "IRL",
    "Israel": "ISR",
    "Italy": "ITA",
    "Ivory Coast": "CIV",
    "Jamaica": "JAM",
    "Japan": "JPN",
    "Jordan": "JOR",
    "Kazakhstan": "KAZ",
    "Kenya": "KEN",
    "Kiribati": "KIR",
    "Kosovo": "KOS",
    "Kuwait": "KUW",
    "Kyrgyzstan": "KGZ",
    "Laos": "LAO",
    "Latvia": "LAT",
    "Lebanon": "LBN",
    "Lesotho": "LES",
    "Liberia": "LBR",
    "Libya": "LBA",
    "Liechtenstein": "LIE",
    "Lithuania": "LTU",
    "Luxembourg": "LUX",
    "Madagascar": "MAD",
    "Malawi": "MAW",
    "Malaysia": "MAS",
    "Maldives": "MDV",
    "Mali": "MLI",
    "Malta": "MLT",
    "Marshall Islands": "MHL",
    "Mauritania": "MTN",
    "Mauritius": "MRI",
    "Mexico": "MEX",
    "Micronesia": "FSM",
    "Moldova": "MDA",
    "Monaco": "MON",
    "Mongolia": "MGL",
    "Montenegro": "MNE",
    "Morocco": "MAR",
    "Mozambique": "MOZ",
    "Myanmar": "MYA",
    "Namibia": "NAM",
    "Nauru": "NRU",
    "Nepal": "NEP",
    "Netherlands": "NED",
    "New Zealand": "NZL",
    "Nicaragua": "NCA",
    "Niger": "NIG",
    "Nigeria": "NGR",
    "North Macedonia": "MKD",
    "Norway": "NOR",
    "Oman": "OMA",
    "Pakistan": "PAK",
    "Palau": "PLW",
    "Palestine": "PLE",
    "Panama": "PAN",
    "Papua New Guinea": "PNG",
    "Paraguay": "PAR",
    "Peru": "PER",
    "Philippines": "PHI",
    "Poland": "POL",
    "Portugal": "POR",
    "Puerto Rico": "PUR",
    "Qatar": "QAT",
    "Romania": "ROU",
    # "Russia": "RUS",
    "Rwanda": "RWA",
    "Saint Kitts and Nevis": "SKN",
    "Saint Lucia": "LCA",
    "Saint Vincent and the Grenadines": "VIN",
    "Samoa": "SAM",
    "San Marino": "SMR",
    "Sao Tome and Principe": "STP",
    "Saudi Arabia": "KSA",
    "Senegal": "SEN",
    "Serbia": "SRB",
    "Seychelles": "SEY",
    "Sierra Leone": "SLE",
    "Singapore": "SGP",
    "Slovakia": "SVK",
    "Slovenia": "SLO",
    "Solomon Islands": "SOL",
    "Somalia": "SOM",
    "South Africa": "RSA",
    "South Korea": "KOR",
    "South Sudan": "SSD",
    "Spain": "ESP",
    "Sri Lanka": "SRI",
    "Sudan": "SUD",
    "Suriname": "SUR",
    "Sweden": "SWE",
    "Switzerland": "SUI",
    "Syria": "SYR",
    "Tajikistan": "TJK",
    "Tanzania": "TAN",
    "Thailand": "THA",
    "Timor-Leste": "TLS",
    "Togo": "TOG",
    "Tonga": "TGA",
    "Trinidad and Tobago": "TTO",
    "Tunisia": "TUN",
    "Turkey": "TUR",
    "Turkmenistan": "TKM",
    "Tuvalu": "TUV",
    "Uganda": "UGA",
    "Ukraine": "UKR",
    "United Arab Emirates": "UAE",
    "United States": "USA",
    "Uruguay": "URU",
    "Uzbekistan": "UZB",
    "Vanuatu": "VAN",
    "Vatican": "VAT",
    "Venezuela": "VEN",
    "Vietnam": "VIE",
    "Virgin Islands": "ISV",
    "Yemen": "YEM",
    "Zambia": "ZAM",
    "Zimbabwe": "ZIM",

    # 历史国家/地区
    "Czechoslovakia": "TCH",
    # "East Germany": "GDR",
    # "West Germany": "FRG",
    "East Germany": "GER",
    "West Germany": "GER",
    # "Soviet Union": "URS",
    "Yugoslavia": "YUG",
    "Serbia and Montenegro": "SCG",
    "North Yemen": "YAR",
    "South Yemen": "YMD",

    # 手动添加
    # "Bohemia": "TCH",
    # "Australasia": "AUS",
    "North Korea": "PRK",
    "Formosa": "TPE",
    "Taiwan": "TPE",
    "Chinese Taipei": "TPE",
    # "Refugee Olympic Team": "ROT",
    # "ROC": "RUS",
    # "Macedonia": "MKD",
    # "Ceylon": "SRI",
    # "United Team of Germany": "GER"
}
# 将 NOC 转化成三位国家代码，并去除字典中没有的国家代码
medal_counts = medal_counts[medal_counts['NOC'].map(olympic_country_codes).notna()]
medal_counts['NOC'] = medal_counts['NOC'].map(olympic_country_codes)
# print(medal_counts[:15].to_string())
# 是否为东道主
model1_dataset = pd.merge(medal_counts, hosts, on='Year', how='left')
# print(model1_dataset.head())
model1_dataset['is_host'] = (model1_dataset['NOC_x'] == model1_dataset['NOC_y']).astype(int)
model1_dataset = model1_dataset.drop(columns=['Host', 'NOC_y'])
model1_dataset = model1_dataset.rename(columns={'NOC_x': 'NOC'})
# print(model1_dataset.to_string(index=False))
# 此届的项目数
def calculate_new_column(row):
    year = str(row['Year'])
    return int(programs.loc[71, year])
model1_dataset['programs'] = model1_dataset.apply(calculate_new_column, axis=1)
# print(model1_dataset.to_string(index=False))
# 运动员数目
athletes_num = athletes.groupby(['NOC', 'Year']).size().reset_index(name='athletes_num')
model1_dataset = pd.merge(model1_dataset, athletes_num, on=['NOC', 'Year'], how='left')
model1_dataset = model1_dataset.dropna(subset=['athletes_num'])
# print(model1_dataset.to_string())
# 前三届奖牌数
grouped = model1_dataset.groupby('NOC')
# 初始化两个列表来存储平均金牌数和平均奖牌总数
average_gold = []
average_total_medals = []
# 遍历每个国家的分组
for country, group in grouped:
    group = group.sort_values(by='Year')
    avg_gold_list = []
    avg_total_medals_list = []
    # 遍历每个国家的每届奥运会
    for index, row in group.iterrows():
        current_year = row['Year']
        previous_years = group[(group['Year'] < current_year) & (group['Year'] >= current_year - 12)]
        if len(previous_years) > 0:
            avg_gold = previous_years['Gold'].mean()
            avg_total_medals = previous_years['Total'].mean()
        else:
            avg_gold = 0
            avg_total_medals = 0
        avg_gold_list.append(avg_gold)
        avg_total_medals_list.append(avg_total_medals)
    # 将结果添加到原始数据中
    model1_dataset.loc[group.index, 'Average_Gold'] = avg_gold_list
    model1_dataset.loc[group.index, 'Average_Total_Medals'] = avg_total_medals_list
# print(model1_dataset.to_string())


# 建立模型
features = ['is_host', 'programs', 'athletes_num','Average_Gold', 'Average_Total_Medals']
target = 'Gold'
X = model1_dataset[features]
y = model1_dataset[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 线性回归
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_pred = lr_model.predict(X_test)
print(lr_model.predict([[1,320,1000,41.67,120]]))
# 随机森林回归模型
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)
print(rf_model.predict([[1,320,1000,41.67,120]]))

lgb_model = LGBMRegressor(n_estimators=250, random_state=42)
lgb_model.fit(X_train, y_train)
lgb_pred = lgb_model.predict(X_test)

# 评估模型
print("Linear Regression MSE:", mean_squared_error(y_test, lr_pred))
print("Random Forest MSE:", mean_squared_error(y_test, rf_pred))
print("LGBM MSE:", mean_squared_error(y_test, lgb_pred))
