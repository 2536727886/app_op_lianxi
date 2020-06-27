import yaml

# 写入数据
data = {'Search_Data': {
    'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'},
    'search_test_001': {'expect': [4, 5, 6], 'value': 456}}}

with open("./text.yml", "w", encoding="utf-8") as f:  # f待写入文件对象
    # 写入数据，代写入对象,指定编码，确认使用
    yaml.safe_dump(data, f, encoding="utf-8", allow_unicode=True)
