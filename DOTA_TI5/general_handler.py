print("###Processing General Handler...###")

#parameter setting
team_name ='eg'
folder_name = 'C:/Users/DafashiTuzi/Desktop/TI5/'

input_generalBP_string = folder_name+team_name+'/'+team_name+'_data.csv'
ouput_file_string = folder_name + team_name +'/'+team_name+'_output.csv'

#read csv
print("Reading in CSV...")
import csv 

data_reader = None
general_bp_data = []
with open(input_generalBP_string, newline='') as csvFile:
	data_reader = csv.reader(csvFile,delimiter=' ', quotechar='|')

	for row in data_reader:
		bp_dict = {}
		#print(row)
		items = row[0].split(',')

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

		#À¢—¿ ±º‰£°

		for i in range(4,24):
			if i in host_ban_index:
				bp_dict['self_b'].append(items[i])
			elif i in host_pick_index:
				bp_dict['self_p'].append(items[i])
			elif i in guest_ban_index:
				bp_dict['oppo_b'].append(items[i])
			else:
				bp_dict['oppo_p'].append(items[i])

		general_bp_data.append(bp_dict)



#for row in host_bp_data:
#    print(row)


print("###End of General Handler###")
