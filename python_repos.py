import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:",r.status_code)

#将api响应存在一个变量中
response_dict = r.json()
print("tatal repositories:",response_dict['total_count'])

#搜索有关信息
repo_dicts = response_dict['items']
print("repositories returned:",len(repo_dicts))
#处理
#print(response_dict.keys())
#研究第一个仓库
repo_dict = repo_dicts[0]
print("\nKeys:",len(repo_dict))
for key in sorted(repo_dict.keys()):
	print(key)
