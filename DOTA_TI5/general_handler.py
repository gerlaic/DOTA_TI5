print("###Processing General Handler...###")

import variable_chart

#parameter setting
team_name =variable_chart.team_name
folder_name = variable_chart.folder_name

input_generalBP_string = folder_name+team_name+'/'+team_name+'_data.csv'
ouput_file_string = folder_name + team_name +'/'+team_name+'_output'

#global variable
general_bp_data = []
used_hero = []
oppo_used_hero = []
hero_data = {}
oppo_hero_data = {}
general_output = []

#functions
#func export csv
def exportFunc(detail, data_source):
	with open((ouput_file_string+detail+'.csv'), 'w', newline='') as f:
		writer = csv.writer(f)
		for row in data_source:
			writer.writerow(row)

#read csv
print("Reading in CSV...")
import csv 

data_reader = None

with open(input_generalBP_string, newline='') as csvFile:
	data_reader = csv.reader(csvFile,delimiter=' ', quotechar='|')

	#ii=0
	for row in data_reader:
		#ii=ii+1
		#print(ii)
		bp_dict = {}
		#print(row)
		items = row[0].split(',')
		#print(items)

		bp_dict['fp'] = items[0]
		bp_dict['oppo'] = items[1]
		bp_dict['side'] = items[2]
		bp_dict['result'] = items[3]
		bp_dict['self_b'] = []
		bp_dict['self_p'] = []
		bp_dict['oppo_b'] = []
		bp_dict['oppo_p'] = []


		if items[0] == 'YES':
			host_ban_index = [4,6,12,14,21]
			host_pick_index = [8,11,17,19,23]
			guest_ban_index = [5,7,13,15,20]
		else:
			host_ban_index = [5,7,13,15,20]
			host_pick_index = [9,10,16,18,22]
			guest_ban_index = [4,6,12,14,21]

		#Teeth Brushing Time??

		for i in range(4,24):

			if i in host_ban_index:
				bp_dict['self_b'].append(items[i])
				if (items[i] not in used_hero):
					used_hero.append(items[i])
			elif i in host_pick_index:
				bp_dict['self_p'].append(items[i])
				if (items[i] not in used_hero):
					used_hero.append(items[i])
			elif i in guest_ban_index:
				bp_dict['oppo_b'].append(items[i])
				if (items[i] not in oppo_used_hero):
					oppo_used_hero.append(items[i])
			else:
				bp_dict['oppo_p'].append(items[i])
				if (items[i] not in oppo_used_hero):
					oppo_used_hero.append(items[i])

		general_bp_data.append(bp_dict)

variable_chart.general_bp = general_bp_data
variable_chart.used_hero = used_hero

#init hero_data
for row in used_hero:
	#init hero dictionary
	hero_dict = {}
	hero_dict['matches'] = []
	hero_data[row] = hero_dict

#init oppo_hero_data
for row in oppo_used_hero:
	hero_dict = {}
	hero_dict['matches'] = []
	oppo_hero_data[row] = hero_dict
	
#generate hero_data
for hero in used_hero:
	for row in general_bp_data:
		#init match for hero_data
		hero_data_match = {'status':'', 'index':0, 'result':'', 'oppo':0}

		if (hero in row['self_b']) or (hero in row['self_p']):
			if hero in row['self_b']:
				hero_data_match['status'] = 'ban'
				hero_data_match['index'] = row['self_b'].index(hero)
			elif hero in row['self_p']:
				hero_data_match['status'] = 'pick'
				hero_data_match['index'] = row['self_p'].index(hero)

			hero_data_match['result'] = row['result']

			if row['oppo'] in variable_chart.ti_team:
				hero_data_match['oppo'] = 'T1'
			else:
				hero_data_match['oppo'] = 'T2'

			hero_data[hero]['matches'].append(hero_data_match)

#generate oppo_hero_data
for hero in oppo_used_hero:
	for row in general_bp_data:
		#init match for hero_data
		hero_data_match = {'status':'', 'index':0, 'result':'', 'oppo':0}

		if (hero in row['oppo_b']) or (hero in row['oppo_p']):
			if hero in row['oppo_b']:
				hero_data_match['status'] = 'ban'
				hero_data_match['index'] = row['oppo_b'].index(hero)
			elif hero in row['oppo_p']:
				hero_data_match['status'] = 'pick'
				hero_data_match['index'] = row['oppo_p'].index(hero)

			hero_data_match['result'] = row['result']

			if row['oppo'] in variable_chart.ti_team:
				hero_data_match['oppo'] = 'T1'
			else:
				hero_data_match['oppo'] = 'T2'

			oppo_hero_data[hero]['matches'].append(hero_data_match)

#generating self_total and oppo_total
self_total = []
for hero in hero_data:
	hero_name = hero
	hero_matches = hero_data[hero]['matches']

	total = len(hero_matches)
	b_count = 0
	p_count = 0
	b_list = [0,0,0,0,0]
	p_list = [0,0,0,0,0]

	for match in hero_matches:
		if match['status'] == 'ban':
			b_count = b_count + 1
			b_list[match['index']] = b_list[match['index']] + 1
		else:
			p_count = p_count + 1
			p_list[match['index']] = p_list[match['index']] + 1

	item = [hero_name,total,b_count,p_count,b_list[0],b_list[1],b_list[2],b_list[3],b_list[4],p_list[0],p_list[1],p_list[2],p_list[3],p_list[4]]

		
	self_total.append(item)

oppo_total = []
for hero in oppo_hero_data:
	hero_name = hero
	hero_matches = oppo_hero_data[hero]['matches']

	total = len(hero_matches)
	b_count = 0
	p_count = 0
	b_list = [0,0,0,0,0]
	p_list = [0,0,0,0,0]

	for match in hero_matches:
		if match['status'] == 'ban':
			b_count = b_count + 1
			b_list[match['index']] = b_list[match['index']] + 1
		else:
			p_count = p_count + 1
			p_list[match['index']] = p_list[match['index']] + 1

	item = [hero_name,total,b_count,p_count,b_list[0],b_list[1],b_list[2],b_list[3],b_list[4],p_list[0],p_list[1],p_list[2],p_list[3],p_list[4]]
	oppo_total.append(item)


#export self_total & oppo_total
exportFunc('_self_total', self_total)
exportFunc('_oppo_total', oppo_total)

# calculate win rate in sides
rad_match_count = 0
dire_match_count = 0
rad_win = 0
dire_win = 0
for row in general_bp_data:
	side = row['side']
	result = row['result']
	
	if side == 'RAD':
		rad_match_count = rad_match_count + 1
		if result == 'WIN':
			rad_win = rad_win + 1
	else:
		dire_match_count = dire_match_count + 1
		if result == 'WIN':
			dire_win = dire_win + 1
rad_win_percentage = rad_win/rad_match_count
dire_win_percentage = dire_win/dire_match_count
output_list = ['Radiante Win Rate Percentage', rad_win_percentage,'Dire Win Rate Percentage', dire_win_percentage]
general_output.append(output_list)

#generate files for combo analyzer


#general result generate and export
exportFunc('_general', general_output)



print("###End of General Handler###")
