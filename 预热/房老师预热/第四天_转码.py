from urllib.parse import unquote

content = 'title=%E8%B5%B0%E6%88%90%E5%8D%8E%E5%A4%A7%E9%81%93&begin=&end=&desc=&uid=5fe013b52420e&product=30&parent=0'

print(unquote(content))