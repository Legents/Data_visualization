import json
import pygal
from pygal.style import RotateStyle
from country_codes import get_country_code


filename = 'population_data.json'
with open(filename) as f:
	pop_data = json.load(f)
	
#打印每个国家2010的人口
cc_populations = {}
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		code = get_country_code(country_name)
		if code:
			cc_populations[code]=population

#根据人数将国家分组
cc_pops_1 ,cc_pops_2, cc_pops_3, cc_pops_4= {}, {}, {}, {}
for cc, pop in cc_populations.items():
	if pop < 100000000:
		cc_pops_1[cc] = pop
	elif pop < 500000000:
		cc_pops_2[cc] = pop
	elif pop < 1000000000:
		cc_pops_3[cc] = pop
	else:
		cc_pops_4[cc] = pop
		
#查看每组包含的国家数量
print(len(cc_pops_1),len(cc_pops_2), len(cc_pops_3),len(cc_pops_4)) 			
wm = pygal.Worldmap()
wm_style = RotateStyle('#112233')
wm = pygal.Worldmap(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m',cc_pops_1)
wm.add('10m-5m',cc_pops_2)
wm.add('5m-1bn',cc_pops_3)
wm.add('>1bn',cc_pops_4)

wm.render_to_file('world_population.svg')
