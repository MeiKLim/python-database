import unicodecsv
from operator import itemgetter
import csv
from matplotlib import pyplot as plt
import pandas as pd

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
		sorted_rows = (sorted(reader, key=itemgetter('PT')))
		max_pt = sorted_rows[-1]
		min_pt = sorted_rows[0]

		print max_pt
		print min_pt

part_time('Loneparents.csv')

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

import multiprocessing

print "number of Loneparents", multiprocessing.cpu_count()

def calc(a, b):
    c = a + b
    return c
    
def age(filename):
	with open ('Age.csv','r') as csvfile:
		csv_f = csv.reader(csvfile)
		for row_num, row in enumerate(csv_f):
			if row_num == 194:
				print row
				title = row[0]
				row = [float(x.replace(',', '')) for x in row[1:]]
				plt.plot(row)
				plt.title(title)
				plt.show()

age('Age.csv')

# if __name__ == "__main__":
#     p1 = multiprocessing.Process(target=calc, args=(3, 5) )
#     p1.start()

#     p2 = multiprocessing.Process(target=calc, args=(2, 2) )
#     p2.start()

#     p1.join()
#     p2.join()


