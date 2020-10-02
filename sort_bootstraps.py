import sys

#open tree file with bootstrap support and list sorted bootstrap values in an output file
tree_file = open(sys.argv[1], "r")
tree_string = tree_file.readline() #reads the first line of file
tree_string = tree_string.strip() #strips newline off at end of string
tree_file.close()

tree_list = tree_string.split(")") #split string into a list at ) character so that each element starts with a bootstrap value
tree_list.sort() #sort list

bootstrap_file = open("sorted_bootstrap_lines.txt", "a") #create new file for appending

#write each bootstrap element to new file, followed by a newline character
for element in tree_list:
	bootstrap_file.write(element+"\n")

bootstrap_file.close()
sys.exit()	
