# 实验数据处理脚本

## 说明

本脚本用于处理实验数据，包括读取xlsx文档、清洗过于离谱的数据、绘制图表和线性拟合。

## 文件树
```bash
.
├── Excel示例数据.png
├── Instructions.txt
├── conda-requirements.txt
├── data
│   └── Experient.xlsx
├── output 
│   └── 实验数据图表.png
├── readme.md
├── src
    └── process_data.py
```

## 使用方法

1. conda安装依赖

Python版本：3.10.14

```bash
conda install -r conda-requirements.txt
```
2. 按照Excel示例数据.png中的样式，将实验数据整理到xlsx文档中

3. 运行脚本
```bash
python src/process_data.py
```
4. 图片输出
输出的图片在`output`文件夹中，名称为`实验数据图表.png`
## 注意事项
1. 请确保输入的xlsx文档格式正确，否则可能会导致脚本无法正常运行。