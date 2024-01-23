import sys, os, time, json
outfile = open("all.txt", "w")
print >> outfile, "id owner collateral collateral-token collateral-type created-at-block-height debt is-liquidated leftover-collateral updated-at-block-height"
for i in range(5000):
	infile = open("all/"+str(i)+".json")
	j = json.loads(infile.read())
	if j['value']['owner']['value'] == "SP2C2YFP12AJZB4MABJBAJ55XECVS7E4PMMZ89YZR":
		continue
	print >> outfile, j['value']['id']['value'], j['value']['owner']['value'], j['value']['collateral']['value'], j['value']['collateral-token']['value'], j['value']['collateral-type']['value'], j['value']['created-at-block-height']['value'], j['value']['debt']['value'], j['value']['is-liquidated']['value'], j['value']['leftover-collateral']['value'], j['value']['updated-at-block-height']['value']
	
	
