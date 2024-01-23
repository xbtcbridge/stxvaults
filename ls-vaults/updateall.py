import sys, os, time
infile = open("all.txt")
line = infile.readline()
line = infile.readline()
tmpid = None
while line:
	line = line.strip().split()
	id  = int(line[0])
	liq = line[7]
	if line[7] == "True":
		line = infile.readline()
		continue
	tmpid = id
	cmd = "node vault.js "+str(id)
	print cmd
	os.system(cmd)
	time.sleep(1)
	line = infile.readline()

for id in range(tmpid, tmpid+100):
        cmd = "node vault.js "+str(id)
        print cmd
        os.system(cmd)
        time.sleep(1)
