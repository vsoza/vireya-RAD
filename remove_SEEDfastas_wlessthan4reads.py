import sys

#this program removes nonredundant fasta sequences from SEED output that had less than 4 reads
#need to run program in the directory where you want output to go

#sys.argv[1], first command line argument, should be sample.seed file
#open SEED file with center sequences for each cluster subtended by sequence/read IDs
SEED_file = open(sys.argv[1], 'r')
#create a new file for appending sequence output
seq_file = open('seqstoremove', 'a')
#read SEED file as a list of lines/strings
SEED_list = SEED_file.readlines()
#close SEED file
SEED_file.close()

#start while loop at second line/list element underneath header
i=1
#while i is less than the length of SEED_list
while i < len(SEED_list):
#if line/list element is a DNA sequence (starts with A,C,G,or T) and the next line/list element is last line/list element of file/list or is subtended by only one read, write to seq_file and go to next sequence
	if (SEED_list[i].startswith("A") or SEED_list[i].startswith("C") or SEED_list[i].startswith("G") or SEED_list[i].startswith("T")) and (SEED_list[i+1]==SEED_list[-1] or SEED_list[i+2].startswith("A") or SEED_list[i+2].startswith("C") or SEED_list[i+2].startswith("G") or SEED_list[i+2].startswith("T")):
		seq_file.write(SEED_list[i])
		i=i+2
#else if line/list element is a DNA sequence (starts with A,C,G,or T) and its last read/list element is last line/list element of file/list or is subtended by only two reads, write to seq_file and go to next sequence
	elif (SEED_list[i].startswith("A") or SEED_list[i].startswith("C") or SEED_list[i].startswith("G") or SEED_list[i].startswith("T")) and (SEED_list[i+2]==SEED_list[-1] or SEED_list[i+3].startswith("A") or SEED_list[i+3].startswith("C") or SEED_list[i+3].startswith("G") or SEED_list[i+3].startswith("T")):
		seq_file.write(SEED_list[i])
		i=i+3	
#else if line/list element is a DNA sequence (starts with A,C,G,or T) and its last read/list element is last line/list element of file/list or is subtended by only three reads, write to seq_file and go to next sequence
	elif (SEED_list[i].startswith("A") or SEED_list[i].startswith("C") or SEED_list[i].startswith("G") or SEED_list[i].startswith("T")) and (SEED_list[i+3]==SEED_list[-1] or SEED_list[i+4].startswith("A") or SEED_list[i+4].startswith("C") or SEED_list[i+4].startswith("G") or SEED_list[i+4].startswith("T")):
		seq_file.write(SEED_list[i])
		i=i+4
#else go to next line/list element
	else:
		i=i+1

#open seq_file for reading
seq_file = open('seqstoremove', 'r')

#sys.argv[2], second command line argument, should be sample.seed.fasta file
#open SEED fasta file for reading
fasta_file = open(sys.argv[2], 'r')
#read fasta file as a list of lines/strings
fasta_list = fasta_file.readlines()
#close fasta file
fasta_file.close()

#for each line/sequence in seq_file, do the following:	
for line in seq_file:
#if line/sequence is in fasta_list,
	if line in fasta_list:
#get the fasta_list index for that sequence
		index = fasta_list.index(line)
#then delete sequence name and sequence from fasta_list
		del fasta_list[index-1:index+1]
		#print len(fasta_list)

#create a new file for appending filtered fasta output
filtered_fasta_file = open('filtered.seed.fasta', 'a')
#write filtered fasta_list as a string to file
filtered_fasta_file.write("".join(fasta_list))
	
#close files
seq_file.close()	
filtered_fasta_file.close()
