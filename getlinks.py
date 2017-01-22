import os
import json

files = os.listdir('.')

links = []

ignorelist = [".git", "README.md"]

for idx,file in enumerate(files):
	print("File no: "+str(idx)+"/"+str(len(files))+".")
	if file in ignorelist:
		print("Skipping "+str(file))
		continue
	f = open(file, 'r')
	try:
		jsdata = json.loads(f.read())
	except ValueError:
		print("This file is not a JSON File")
		continue
	if 'url' in jsdata.viewkeys():
		links.append(str(jsdata['url']))
	else:
		print("No url, going forward.")	
	f.close()

file = open('linklist.txt', 'w')

for link in links:
	file.write(str(link)+"\n")

print("Done")