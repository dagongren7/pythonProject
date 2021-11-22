import yaml
# dump()可以将Python对象序列化成YAML流。如果stream为None，则返回生成的字符串
slogan=['welcome','to','51zxw']
website={'url':'www.51zxw.net'}

print(slogan)
print(website)

print(yaml.dump(slogan))
print(yaml.dump(website))