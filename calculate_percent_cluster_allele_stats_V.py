import sys

#open sample's clustering series stats file from Ilut et al 2014 scripts ouput 
sample_stats_file=open(sys.argv[1], 'r')
#read file as list of lines
sample_stats_list=sample_stats_file.readlines()
sample_stats_file.close()

#remove "nr_distinct_reads\tcount\n" line/item from list
for item in sample_stats_list:
	if item == 'nr_distinct_reads\tcount\n':
		sample_stats_list.remove(item)

#append new line at end of list to be able to terminate while loop below
sample_stats_list.append('\n')

#create 20 empty lists of clusters for each distance threshold from 1 to 20	
d20_clusters=[]	
d19_clusters=[]
d18_clusters=[]
d17_clusters=[]
d16_clusters=[]
d15_clusters=[]
d14_clusters=[]
d13_clusters=[]
d12_clusters=[]
d11_clusters=[]
d10_clusters=[]
d9_clusters=[]
d8_clusters=[]
d7_clusters=[]
d6_clusters=[]
d5_clusters=[]
d4_clusters=[]
d3_clusters=[]
d2_clusters=[]
d1_clusters=[]	

#initialize i counter for cycling through sample_stats_list items
i=1		
#append associated clusters/items for each distance to respective list and strip newline character off end of each item
#max number of alleles in Vireya files is 15 so used 16 as length of j counter within each distance threshold
#if line starts with "Clusters", initialize j counter, if next line starts with number, add to respective list
#else if next line starts with "Clusters", move to next cluster list for appending and stop j counter
while i < len(sample_stats_list):

	if (sample_stats_list[i] == 'Clusters with max_d=20:\n'): 
		j=1
		while j < 16:
			if (sample_stats_list[i+j].startswith(tuple('123456789'))):
				d20_clusters.append(sample_stats_list[i+j].strip('\n'))
				j=j+1	
			elif (sample_stats_list[i+j].startswith('Clusters')):
				i=i+j
				j=16
	
	elif (sample_stats_list[i] == 'Clusters with max_d=19:\n'):
		j=1
		while j < 16:
			if (sample_stats_list[i+j].startswith(tuple('123456789'))):
				d19_clusters.append(sample_stats_list[i+j].strip('\n'))
				j=j+1	
			elif (sample_stats_list[i+j].startswith('Clusters')):
				i=i+j	
				j=16
				
	elif (sample_stats_list[i] == 'Clusters with max_d=18:\n'):
		j=1
		while j < 16:	
			if (sample_stats_list[i+j].startswith(tuple('123456789'))):
				d18_clusters.append(sample_stats_list[i+j].strip('\n'))
				j=j+1
			elif (sample_stats_list[i+j].startswith('Clusters')):
				i=i+j	
				j=16	
				
	elif (sample_stats_list[i] == 'Clusters with max_d=17:\n'):
		j=1
		while j < 16:
			if (sample_stats_list[i+j].startswith(tuple('123456789'))):
				d17_clusters.append(sample_stats_list[i+j].strip('\n'))
				j=j+1
			elif (sample_stats_list[i+j].startswith('Clusters')):
				i=i+j	
				j=16
				
	elif (sample_stats_list[i] == 'Clusters with max_d=16:\n'):
		j=1
		while j < 16:		 
			if (sample_stats_list[i+j].startswith(tuple('123456789'))):
				d16_clusters.append(sample_stats_list[i+j].strip('\n'))
				j=j+1
			elif (sample_stats_list[i+j].startswith('Clusters')):
				i=i+j	
				j=16

	elif (sample_stats_list[i] == 'Clusters with max_d=15:\n'):
		j=1
		while j < 16:
			if (sample_stats_list[i+j].startswith(tuple('123456789'))):
				d15_clusters.append(sample_stats_list[i+j].strip('\n'))
				j=j+1
			elif (sample_stats_list[i+j].startswith('Clusters')):
				i=i+j	
				j=16
				
	elif (sample_stats_list[i] == 'Clusters with max_d=14:\n'):
		j=1
		while j < 16:	 
			if (sample_stats_list[i+j].startswith(tuple('123456789'))):
				d14_clusters.append(sample_stats_list[i+j].strip('\n'))
				j=j+1
			elif (sample_stats_list[i+j].startswith('Clusters')):
				i=i+j	
				j=16
				
	elif (sample_stats_list[i] == 'Clusters with max_d=13:\n'): 
		j=1
		while j < 16:	
			if (sample_stats_list[i+j].startswith(tuple('123456789'))):
				d13_clusters.append(sample_stats_list[i+j].strip('\n'))
				j=j+1
			elif (sample_stats_list[i+j].startswith('Clusters')):
				i=i+j	
				j=16
				
	elif (sample_stats_list[i] == 'Clusters with max_d=12:\n'):
		j=1
		while j < 16:
			if (sample_stats_list[i+j].startswith(tuple('123456789'))):
				d12_clusters.append(sample_stats_list[i+j].strip('\n'))
				j=j+1
			elif (sample_stats_list[i+j].startswith('Clusters')):
				i=i+j	
				j=16
				
	elif (sample_stats_list[i] == 'Clusters with max_d=11:\n'): 
		j=1
		while j < 16:
			if (sample_stats_list[i+j].startswith(tuple('123456789'))):
				d11_clusters.append(sample_stats_list[i+j].strip('\n'))
				j=j+1
			elif (sample_stats_list[i+j].startswith('Clusters')):
				i=i+j	
				j=16
				
	elif (sample_stats_list[i] == 'Clusters with max_d=10:\n'): 
		j=1
		while j < 16:
			if (sample_stats_list[i+j].startswith(tuple('123456789'))):
				d10_clusters.append(sample_stats_list[i+j].strip('\n'))
				j=j+1
			elif (sample_stats_list[i+j].startswith('Clusters')):
				i=i+j	
				j=16
			
	elif (sample_stats_list[i] == 'Clusters with max_d=9:\n'):
		j=1
		while j < 16:	
			if (sample_stats_list[i+j].startswith(tuple('123456789'))):
				d9_clusters.append(sample_stats_list[i+j].strip('\n'))
				j=j+1
			elif (sample_stats_list[i+j].startswith('Clusters')):
				i=i+j	
				j=16
				
	elif (sample_stats_list[i] == 'Clusters with max_d=8:\n'): 
		j=1
		while j < 16:
			if (sample_stats_list[i+j].startswith(tuple('123456789'))):
				d8_clusters.append(sample_stats_list[i+j].strip('\n'))
				j=j+1
			elif (sample_stats_list[i+j].startswith('Clusters')):
				i=i+j	
				j=16	

	elif (sample_stats_list[i] == 'Clusters with max_d=7:\n'): 
		j=1
		while j < 16:
			if (sample_stats_list[i+j].startswith(tuple('123456789'))):
				d7_clusters.append(sample_stats_list[i+j].strip('\n'))
				j=j+1
			elif (sample_stats_list[i+j].startswith('Clusters')):
				i=i+j	
				j=16
				
	elif (sample_stats_list[i] == 'Clusters with max_d=6:\n'): 
		j=1
		while j < 16:
			if (sample_stats_list[i+j].startswith(tuple('123456789'))):
				d6_clusters.append(sample_stats_list[i+j].strip('\n'))
				j=j+1
			elif (sample_stats_list[i+j].startswith('Clusters')):
				i=i+j	
				j=16	

	elif (sample_stats_list[i] == 'Clusters with max_d=5:\n'):
	 	j=1
		while j < 16:
			if (sample_stats_list[i+j].startswith(tuple('123456789'))):
				d5_clusters.append(sample_stats_list[i+j].strip('\n'))
				j=j+1
			elif (sample_stats_list[i+j].startswith('Clusters')):
				i=i+j	
				j=16
				
	elif (sample_stats_list[i] == 'Clusters with max_d=4:\n'): 
		j=1
		while j < 16:
			if (sample_stats_list[i+j].startswith(tuple('123456789'))):
				d4_clusters.append(sample_stats_list[i+j].strip('\n'))
				j=j+1
			elif (sample_stats_list[i+j].startswith('Clusters')):
				i=i+j	
				j=16
				
	elif (sample_stats_list[i] == 'Clusters with max_d=3:\n'): 
		j=1
		while j < 16:
			if (sample_stats_list[i+j].startswith(tuple('123456789'))):
				d3_clusters.append(sample_stats_list[i+j].strip('\n'))
				j=j+1
			elif (sample_stats_list[i+j].startswith('Clusters')):
				i=i+j	
				j=16
				
	elif (sample_stats_list[i] == 'Clusters with max_d=2:\n'): 
		j=1
		while j < 16:
			if (sample_stats_list[i+j].startswith(tuple('123456789'))):
				d2_clusters.append(sample_stats_list[i+j].strip('\n'))
				j=j+1
			elif (sample_stats_list[i+j].startswith('Clusters')):
				i=i+j	
				j=16
				
	elif (sample_stats_list[i] == 'Clusters with max_d=1:\n'): 
		j=1
		while j < (len(sample_stats_list)-i):
			if (sample_stats_list[i+j].startswith(tuple('123456789'))):
				d1_clusters.append(sample_stats_list[i+j].strip('\n'))
				j=j+1
			else:
				i=len(sample_stats_list)
				j=(len(sample_stats_list)-i)	
		
#open files for appending %clusters with each allele type for all distances for sample
percent_clusters_1allele_file=open('Vir_percent_clusters_1allele.txt', 'a')
percent_clusters_2allele_file=open('Vir_percent_clusters_2allele.txt', 'a')
percent_clusters_3allele_file=open('Vir_percent_clusters_3allele.txt', 'a')
	
#define a function to calculate % clusters with each allele type for a specific distance
def calculate_allele_percent_cluster(d_clusters_list):	
#create new list for cluster numbers only, excluding number of alleles, for each distance
	d_clusters_numbers = []
#for each item in d_clusters_list, split on tab character and append float of second list element to new list
	for item in d_clusters_list:
		item_list = item.split('\t')
		d_clusters_numbers.append(float(item_list[1]))
#sum clusters across all alleles to get total number of clusters for each distance	
	sum_d_clusters = sum(d_clusters_numbers)
#calculate %clusters that had 1 allele, 2 alleles, or 3+ alleles, and format as float string with 1 decimal point
	d_percent_1allele = "%.1f" % ((d_clusters_numbers[0]/sum_d_clusters)*100)
	d_percent_2allele = "%.1f" % ((d_clusters_numbers[1]/sum_d_clusters)*100)
	d_percent_3allele = "%.1f" % ((sum(d_clusters_numbers[2:])/sum_d_clusters)*100)
#write %clusters with each allele type to respective file in a column
	percent_clusters_1allele_file.write(d_percent_1allele+'\t')
	percent_clusters_2allele_file.write(d_percent_2allele+'\t')
	percent_clusters_3allele_file.write(d_percent_3allele+'\t')
	
#call function on each distance_clusters list	
calculate_allele_percent_cluster(d1_clusters)
calculate_allele_percent_cluster(d2_clusters)
calculate_allele_percent_cluster(d3_clusters)
calculate_allele_percent_cluster(d4_clusters)
calculate_allele_percent_cluster(d5_clusters)
calculate_allele_percent_cluster(d6_clusters)
calculate_allele_percent_cluster(d7_clusters)
calculate_allele_percent_cluster(d8_clusters)
calculate_allele_percent_cluster(d9_clusters)
calculate_allele_percent_cluster(d10_clusters)
calculate_allele_percent_cluster(d11_clusters)
calculate_allele_percent_cluster(d12_clusters)
calculate_allele_percent_cluster(d13_clusters)
calculate_allele_percent_cluster(d14_clusters)
calculate_allele_percent_cluster(d15_clusters)
calculate_allele_percent_cluster(d16_clusters)
calculate_allele_percent_cluster(d17_clusters)
calculate_allele_percent_cluster(d18_clusters)
calculate_allele_percent_cluster(d19_clusters)
calculate_allele_percent_cluster(d20_clusters)	

#add newline character to end of row in each file
percent_clusters_1allele_file.write('\n')
percent_clusters_2allele_file.write('\n')
percent_clusters_3allele_file.write('\n')

#close files
percent_clusters_1allele_file.close()
percent_clusters_2allele_file.close()
percent_clusters_3allele_file.close()				
