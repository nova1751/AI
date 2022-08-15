#!/user/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import json
from glom import glom
# JSON（JavaScript Object Notation，JavaScript 对象表示法），是存储和交换文本信息的语法，类似 XML。
#
# JSON 比 XML 更小、更快，更易解析，更多 JSON 内容可以参考 JSON 教程。
#
# Pandas 可以很方便的处理 JSON 数据，本文以 sites.json 为例，内容如下：
df = pd.read_json('Other Files/sites.json')

print(df.to_string())

# JSON 对象与 Python 字典具有相同的格式，所以我们可以直接将 Python 字典转化为 DataFrame 数据：
# 字典格式的 JSON
s = {
    "col1": {"row1": 1, "row2": 2, "row3": 3},
    "col2": {"row1": "x", "row2": "y", "row3": "z"}
}

# 读取 JSON 转为 DataFrame
df = pd.DataFrame(s)
print(df)

# 从 URL 中读取 JSON 数据：
URL = 'https://static.runoob.com/download/sites.json'
df = pd.read_json(URL)
print(df)

# 内嵌的 JSON 数据
# 假设有一组内嵌的 JSON 数据文件 nested_list.json ：
df = pd.read_json('Other Files/nested_list.json')

print(df)

# 这时我们就需要使用到 json_normalize() 方法将内嵌的数据完整的解析出来：
# 使用 Python JSON 模块载入数据
with open('Other Files/nested_list.json', 'r') as f:
    data = json.loads(f.read())

# 展平数据
df_nested_list = pd.json_normalize(data, record_path=['students'])
print(df_nested_list)

# data = json.loads(f.read()) 使用 Python JSON 模块载入数据。
#
# json_normalize() 使用了参数 record_path 并设置为 ['students'] 用于展开内嵌的 JSON 数据 students。
#
# 显示结果还没有包含 school_name 和 class 元素，如果需要展示出来可以使用 meta 参数来显示这些元数据：
# 使用 Python JSON 模块载入数据
with open('Other Files/nested_list.json', 'r') as f:
    data = json.loads(f.read())

# 展平数据
df_nested_list = pd.json_normalize(
    data,
    record_path =['students'],
    meta=['school_name', 'class']
)
print(df_nested_list)

# 接下来，让我们尝试读取更复杂的 JSON 数据，该数据嵌套了列表和字典，数据文件 nested_mix.json 如下：
# 使用 Python JSON 模块载入数据
with open('Other Files/nested_mix.json', 'r') as f:
    data = json.loads(f.read())

df = pd.json_normalize(
    data,
    record_path=['students'],
    meta=[
        'class',
        ['info', 'president'],
        ['info', 'contacts', 'tel']
    ]
)

print(df)

# 读取内嵌数据中的一组数据
# 以下是实例文件 nested_deep.json，我们只读取内嵌中的 math 字段：
df = pd.read_json('Other Files/nested_deep.json')

data = df['students'].apply(lambda row: glom(row, 'grade.math'))
print(data)



