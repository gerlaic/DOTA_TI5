print("###Welcome to Tower Builder Project###")

print("Read in CSV")
#read in BP data
import csv 
data_reader = None
bp_data = [];
with open('C:/Users/DafashiTuzi/Desktop/vp data.csv', newline='') as csvFile:
	data_reader = csv.reader(csvFile,delimiter=' ', quotechar='|')
	for row in data_reader:
		#print(row)	
		#heros = row[0][0].split(',')
		bp_data.append(row)

#read in hero set
hero_reader = None
hero_data = []
with open('C:/Users/DafashiTuzi/Desktop/vp hero.csv', newline='') as csvFile:
	hero_reader = csv.reader(csvFile,delimiter=' ',quotechar='|')
	for row in hero_reader:
		#print(row)
		hero_data.append(row)

#make better format for bp_data and hero_data_split
bp_data_split = [];
for data in bp_data:
	heros = data[0].split(',')
	bp_data_split.append(heros)

#for row in bp_data_split:
#	print(row)

hero_data_split = []
for data in hero_data:
	hero = data[0].split(',')
	hero_data_split.append(hero)

#analyze start
n = 0 #hero counter
o_pool = [] #output pool
for hero in hero_data_split[0]:
	
	if (n+1) < len(hero_data_split[0]):
		n=n+1
		i=0
		a_pool = []

		#print("testing "+hero)
	
		#part 1
		
		for bp in bp_data_split:
			if hero in bp:
				#print("yes, "+hero+" is in bp: ")
				#print(bp)
				i=i+1
				a_pool.append(bp)
	
		#part 2
		#print("start p2...")
		for j in range(n,len(hero_data_split[0])):
			hero2 = hero_data_split[0][j]
			b_pool = []
			for bp in a_pool:	
				if hero2 in bp:
					#print("found one!")
					b_pool.append(bp)
			count = len(b_pool)

			if count !=0 :
				o_item = [hero, hero2, count]
				o_pool.append(o_item)

#for row in o_pool:
#	print(row)

#import csv
with open('C:/Users/DafashiTuzi/Desktop/vp_output2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in o_pool:
        writer.writerow(row)


def analyze3():
	#analyze start
	n = 0 #hero counter
	o_pool = [] #output pool
	for hero in hero_data_split[0]:
	
		if (n+2) < len(hero_data_split[0]):
			n=n+1
			i=0
			a_pool = []

			#print("testing "+hero)
	
			#part 1
		
			for bp in bp_data_split:
				if hero in bp:
					#print("yes, "+hero+" is in bp: ")
					#print(bp)
					i=i+1
					a_pool.append(bp)
	
			#part 2
			#print("start p2...")
			for j in range(n,len(hero_data_split[0])):
				hero2 = hero_data_split[0][j]
				b_pool = []
				for bp in a_pool:	
					if hero2 in bp:
						#print("found one!")
						b_pool.append(bp)

			for k in range(n+1,len(hero_data_split[0])):
				hero3 = hero_data_split[0][k]
				c_pool = []
				for bp in b_pool:
					if hero3 in bp:
						c_pool.append(bp)

				count = len(c_pool)

				if count !=0 :
					o_item = [hero, hero2, hero3, count]
					o_pool.append(o_item)

	#for row in o_pool:
	#	print(row)

	#import csv
	with open('C:/Users/DafashiTuzi/Desktop/vp_output3.csv', 'w', newline='') as f:
		writer = csv.writer(f)
		for row in o_pool:
			writer.writerow(row)
	
	return

analyze3()