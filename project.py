import unicodecsv
from operator import itemgetter

def percentage(filename):
	with open(filename) as csvfile:
		reader = unicodecsv.DictReader(csvfile)

		counter_all = 0
		counter_male = 0
		counter_female = 0

		for LSOA in reader:
			counter_all = counter_all + int(LSOA['All'])
			counter_male = counter_male + int(LSOA['Male'])
			counter_female = counter_female + int(LSOA['Female'])
		
		print "There are in total {0} lone parent families with dependent children in Hammersmith and Fulham; of which {1} are male parents with dependent children and {2} are female parents with dependent children.".format(counter_all, counter_male, counter_female)

percentage('Loneparents.csv')

def part_time(filename):
	with open(filename) as csvfile:
		reader = unicodecsv.DictReader(csvfile)
# 
# 	sorted_rows = (sorted(reader, key=itemgetter('PT'))
# 	max_pt = sorted_rows[-1]
# 	min_pt = sorted_rows[0]

# 	print max_pt
# 	print min_pt

def calculations(input_filename, output_filename):
	with open(input_filename) as csvfile:
		reader = unicodecsv.DictReader(csvfile)

		output_rows= []
		for LSOA in reader:
			Families_all = float(LSOA['All'])
			NW= float(LSOA['NW'])
			FT = float(LSOA['FT'])
			out = {
				'Area': LSOA['Area'],
				'All': Families_all,
				'Not_working': NW,
				'Families_working': Families_all-NW,
				'Families_notworking_pct': 100*(Families_all-NW)/Families_all,	
				'Families_fulltime': FT,
				'Families_parttime': Families_all-FT,
				'Families_fulltime_pct': 100*(Families_all-FT)/Families_all,
			}
			output_rows.append(out)

	with open(output_filename,'w') as csvfile:
		headers = ['Area',
					'All',
					'Not_working',
					'Families_working',
					'Families_notworking_pct',
					'Families_fulltime',
					'Families_parttime',
					'Families_fulltime_pct'
					]
		writer = unicodecsv.DictWriter(csvfile, headers)

		writer.writeheader()
		for output_row in output_rows:
				writer.writerow(output_row)

calculations('Loneparents.csv', 'those_working.csv')

if __name__=='__main__':
	p1 = Process(target = percentage)
	p1.start()
	p2 = Process(target = part_time)
	p2.start()
