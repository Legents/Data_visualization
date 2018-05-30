import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:",r.status_code)

#将api响应存在一个变量中
response_dict = r.json()
print("tatal repositories:",response_dict['total_count'])

#搜索有关信息
repo_dicts = response_dict['items']
names, stars = [],[]
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	stars.append(repo_dict['stargazers_count'])
	
my_style = LS('#333366',base_style = LCS)
chart = pygal.Bar(style=my_style, x_label_rotation = 45, show_legend=False)
chart.title = 'Most-starred Python Projects on Github'
chart.x_labels = names

chart.add('',stars)
chart.render_to_file('python_repos.svg')

print("\nSelected info about each repo:")
for repo_dict in repo_dicts:
	print('\nName:',repo_dict['name'])
	print('Owner:',repo_dict['owner']['login'])
	print('Stars:',repo_dict['stargazers_count'])
	print('Repository:',repo_dict['html_url'])
	print('Description:',repo_dict['description'])
