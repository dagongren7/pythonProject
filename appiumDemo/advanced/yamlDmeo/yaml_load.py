
with open('familyInfo.yaml', 'r+', encoding='utf-8') as f:
    data = yaml.load(f,Loader=yaml.FullLoader)

print(data)

print(data['name'])
print(data['age'])

print(data['spouse'])
print(data['spouse']['name'])
print(data['spouse']['age'])

print(data['children'])
print(data['children'][0]['name'])
print(data['children'][0]['age'])

print(data['children'][1]['name'])
print(data['children'][1]['age'])

# warn 注意：此处只是变量类型的数据变更，不会真正修改到yaml配置表中的数据。
data['name']='51zxw'
print(data['name'])