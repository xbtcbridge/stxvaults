import sys, os, json
from datetime import date

today = date.today().strftime("%d/%m/%Y")
stx = float(sys.argv[1])
xbtc = float(sys.argv[2])
alex = float(sys.argv[3])

infile = open("all.txt")
totalstx = 0
totalxbtc = 0
totalalex = 0
nvault=0
vaults = []
line = infile.readline()
for line in infile.xreadlines():
	line = line.strip().split()
	id = line[0]
	owner = line[1]
	collateral = float(line[2])
	collateraltoken = line[3]
	collateraltype  = line[4]
	createdatblockheight  = line[5]
	debt = line[6]
	isliquidated = line[7]
	leftovercollateral = line[8]
	updatedatblockheight	 = line[9]
	num = None
	if isliquidated == "True":
		continue
	if collateraltoken == "STX":
		totalstx = totalstx+collateral
		num = collateral/1e6*stx
	elif collateraltoken == "xBTC":
		totalxbtc = totalxbtc + collateral
		num = float(collateral/1e8)*xbtc
	elif collateraltoken == "auto-alex":
		totalalex = totalalex + collateral
		num = float(collateral/1e8)*alex
	else:
		raise Exception("no such collateral token "+collateraltoken)
	ratio = None
	if debt == "0":
		ratio = 100000
	else:
		print line
		denom = float(debt)/1e6
		ratio = round(num/denom *100, 0)
	vaults.append({"id": id, "ratio":ratio, "owner": owner, "collateral": collateral, "collateral-token": collateraltoken, "collateral-type": collateraltype, "created-at-block-height": createdatblockheight, "debt": debt, "is-liquidated": isliquidated, "leftover-collateral": leftovercollateral, "updated-at-block-height": updatedatblockheight})
	nvault = nvault+1	

toprint = {"date": today, "stx": stx, "xbtc": xbtc, "alex": alex, "nvault": nvault, "totalstx": totalstx/1e6, "totalxbtc": totalxbtc/1e8, "totalalex": totalalex/1e8, "vaults": vaults}

outfile = open("vaults.json", "w")
print >> outfile, json.dumps(sorted(vaults, key=lambda x: float(x['updated-at-block-height']), reverse = True), indent = 2)
