import pandas as pd
import matplotlib.pyplot as plt

# 加载数据
medal_counts = pd.read_csv('summerOly_medal_counts.csv')

def medal_count_per_country():
    medal_counts['Year'] = medal_counts['Year'].astype(int)

    # 按国家和年份分组，计算奖牌总数
    country_year_medals = medal_counts.groupby(['NOC', 'Year'])['Total'].sum().reset_index()

    # 获取所有国家的列表
    countries = country_year_medals['NOC'].unique()

    # 选择前几个国家作为示例
    selected_countries = countries[:1]  # 选择前5个国家

    # 创建一个图形
    plt.figure(figsize=(14, 8))

    # 遍历每个国家，绘制折线图
    for country in selected_countries:
        country_data = country_year_medals[country_year_medals['NOC'] == country]
        plt.plot(country_data['Year'], country_data['Total'], label=country)

    # 添加标题和标签
    plt.title('Total Medals Over Years for Selected Countries', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Total Medals', fontsize=12)
    plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)

    # 显示图形
    plt.tight_layout()
    plt.show()

# medal_count_per_country()
