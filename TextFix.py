def main():
	pass
	#textfix()
	#mastertext()
	
def mastertext():
	path = "Collected/"
	filenames = [path + 'Subject0.txt', path + 'Subject2.txt', path + 'Subject3.txt', path + 'Subject4.txt', path + 'Subject5.txt', path + 'Subject6.txt', path + 'Subject7.txt', path + 'Subject8.txt', path + 'Subject9.txt', path + 'Subject10.txt', path + 'Subject11.txt', path + 'Subject12.txt', path + 'Subject13.txt', path + 'Subject14.txt', path + 'Subject15.txt', path + 'Subject16.txt', path + 'Subject17.txt', path + 'Subject18.txt', path + 'Subject19.txt', path + 'Subject20.txt', path + 'Subject21.txt', path + 'Subject22.txt']
	with open('masterCOPY.txt', 'w') as outfile:
		for names in filenames:
			with open(names) as infile:
				outfile.write(infile.read())
			outfile.write("\n")



def textfix():
	count = 0
	edits = 0
	with open("Collected/masterCOPY.txt", "r") as file:
		lines = file.readlines()
		arr = []
		for line in lines:
			arr.clear()
			for term in line.split(sep=" ; "):
				arr.append(term)
			if len(arr) == 10:
				arr.insert(len(arr) - 2 ,'-1')
				str = ""
				for ele in arr[:-1]:
					str += ele + ' ; '
				str += arr[-1]
				lines[count] = str
				edits += 1
			count += 1
	file = open("Collected/masterCOPY.txt", "w")
	file.writelines(lines)
	file.close()
	print("{} edits made".format(edits))
			

if __name__ == '__main__':
	main()