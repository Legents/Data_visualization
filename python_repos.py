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
print("\nselected info about first repos:")
print('Name:',repo_dict['name'])
print('Owner:',repo_dict['owner']['login'])
print('Stars:',repo_dict['stargazers_count'])
print('Repository:',repo_dict['html_url'])
print('Creatsd:',repo_dict['created_at'])
print('Updated:',repo_dict['updated_at'])
print('Description:',repo_dict['description'])
