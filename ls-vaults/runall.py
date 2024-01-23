import sys, os, time
for i in range(5000):
	cmd = "node vault.js "+str(i)
	print cmd
	os.system(cmd)
	time.sleep(1)
