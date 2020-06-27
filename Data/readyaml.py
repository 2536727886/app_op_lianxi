import yaml

# 读取yaml数据
with open("./data2.yml", "r", encoding="utf-8") as f:
    # 使用yaml加载数据，转换成字典格式‘
    data = yaml.safe_load(f)
    print("转换数据格式打印：", type(data))
    print("数据打印：", data)
