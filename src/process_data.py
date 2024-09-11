import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import matplotlib.font_manager as fm
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 1. 读取Excel文件
df = pd.read_excel('data/Experient.xlsx', sheet_name='Sheet1')

# 2. 获取x和y数据
x_data = df.iloc[1:, 0].astype(float)
y_data = df.iloc[1:, 1].astype(float)

# 新增: 剔除异常值
def remove_outliers(x, y, threshold=2):
    x_mean, x_std = np.mean(x), np.std(x)
    y_mean, y_std = np.mean(y), np.std(y)
    
    mask = (abs(x - x_mean) < threshold * x_std) & (abs(y - y_mean) < threshold * y_std)
    return x[mask], y[mask]

x_cleaned, y_cleaned = remove_outliers(x_data, y_data)

# 3. 获取坐标轴标题
x_label = df.iloc[0, 0]
y_label = df.iloc[0, 1]

# 4. 绘制折线图
plt.figure(figsize=(10, 6))
plt.plot(x_data, y_data, 'bo', label='原始数据', alpha=0.5)
plt.plot(x_cleaned, y_cleaned, 'go', label='清洗后数据')

# 5. 进行线性拟合 (使用清洗后的数据)
slope, intercept, r_value, p_value, std_err = stats.linregress(x_cleaned, y_cleaned)
line = slope * x_data + intercept

# 6. 将拟合结果绘制在图表上
plt.plot(x_data, line, 'r-', label=f'拟合线 (y = {slope:.4f}x + {intercept:.4f})')

plt.xlabel(x_label)
plt.ylabel(y_label)
plt.title('电压与电流的关系')
plt.legend()
plt.grid(True)

# 7. 保存图片
plt.savefig('output/实验数据图表.png', dpi=300, bbox_inches='tight')
plt.show()