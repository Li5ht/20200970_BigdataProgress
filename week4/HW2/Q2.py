conf_sum = 0.0
conf_count = 0

with open("mbox-short.txt", "rt") as fp:
	for line in fp:
		if line.startswith("X-DSPAM-Confidence: ") :
			#print(line)
			str_arr = line.split()
			#print(str_arr[1])
			conf_sum += float(str_arr[1])
			conf_count += 1

print("mbox-short.txt")
print( conf_sum / conf_count)
