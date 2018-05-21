import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:",r.status_code)

#将api响应存在一个变量中
response_dict = r.json()

#处理
print(response_dict.keys())
