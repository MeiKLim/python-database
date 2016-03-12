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

def part_time(filename):
	with open(filename) as csvfile:
		reader = unicodecsv.DictReader(csvfile)

	sorted_rows = (sorted(reader, key=itemgetter('PT'))
	max_pt = sorted_rows[-1]
	min_pt = sorted_rows[0]

	print max_pt
	print min_pt

if __name__=='__main__':
	p1 = Process(target = percentage)
	p1.start()
	p2 = Process(target = part_time)
	p2.start()

percentage('Loneparents.csv')