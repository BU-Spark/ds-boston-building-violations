import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件

data1 = pd.read_csv('../data/cleaned_PUBLIC_WORKS_VIOLATIONS.csv')
data2 = pd.read_csv('../data/cleaned_BUILDING_AND_PROPERTY_VIOLATIONS.csv')

# 合并两个数据集
data = pd.concat([data1, data2])

# 统计violation_street列出现次数
street_counts = data['violation_street'].value_counts()

# 取出现次数最多的前10个街道名称，以避免图表过于拥挤
top_streets = street_counts.head(20)

# 绘制条形图
plt.figure(figsize=(10, 8))
top_streets.plot(kind='bar')
plt.title('Top 20 Violation Streets')
plt.xlabel('Street Name')
plt.ylabel('Number of Violations')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('top_10_violation_streets.png')
# 显示图表
plt.show()


