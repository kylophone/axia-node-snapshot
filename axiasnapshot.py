import sys, telnetlib, shlex, json

try:
	tn = telnetlib.Telnet(sys.argv[1], '93', 3) #Node IP
except:
	sys.exit(1)

setDict = dict.fromkeys(['LWS_802_1p_TAGE',
                         'LWS_802_1p_VLAN',
                         'LWS_802_1Q_PRIO',
                         'RTP_802_1p_TAGE',
                         'RTP_802_1p_VLAN',
                         'RTP_802_1Q_PRIO',
                         'LWCLK_PRIO',
                         'LWCLK_ADDR',
                         'IPCLK_ADDR',
                         'ADIP',
                         'NID',
                         'AESSYNC_PRI',
                         'AESSYNC_OUT',
                         'AESSYNCE',
                         'AESTX_AUTO',
                         'LWS_IP_TOS',
                         'RXBUFF',
                         'RTP_IP_TOS',
                         'LWCLK_MODE'])

verDict = dict.fromkeys(['DEVN',
                         'NSRC',
                         'NDST',
                         'NGPI',
                         'NGPO',
                         'PRODUCT',
                         'MODEL',
                         'SVER'])

ipDict = dict.fromkeys(['address',
                        'netmask',
                        'gateway',
                        'hostname'])
srcDict = {}
srcParameters = ['SRC','PSNM','RTPE','RTPA','INGN', 'IO','RTPP','SHAB','NCHN','PHPW','AESM']
dstDict = {}
dstParameters = ['DST', 'NAME','ADDR','NCHN','VMOD','OUGN']
gpioDict = {}
gpioParameters = ['GPIO', 'SRCA', 'GPO', 'GPI']

tn.write("SET\n")
setList = shlex.split(tn.read_until("\n", 2))
for key, value in setDict.items():
	for thisItem in setList:
		if thisItem.startswith(key + ":"):
	 		setDict[key] = thisItem.split(':')[1]
	 		continue

tn.write("VER\n")
verList = shlex.split(tn.read_until("\n", 2))
for key, value in verDict.items():
	for thisItem in verList:
		if thisItem.startswith(key + ":"):
	 		verDict[key] = thisItem.split(':')[1]
	 		continue

tn.write("IP\n")
ipList = shlex.split(tn.read_until("\n", 2))
for key, value in ipDict.items():
	for thisIndex, thisItem in enumerate(ipList):
		if thisItem == key:
			ipDict[key] = ipList[thisIndex + 1]
			continue

tn.write("SRC\n")
listOfAllSrcs = tn.read_until("END", 2).split("\r\n")
for thisLine in listOfAllSrcs:
	if thisLine.startswith("SRC "):
		thisLine = list(thisLine)
		thisLine[3] = ":"
		thisLine = ''.join(thisLine)
	else:
		continue
	thisSrcList = shlex.split(thisLine)
	thisSrcDict = dict.fromkeys(srcParameters)
	for key, value in thisSrcDict.items():
		for thisItem in thisSrcList:
			if thisItem.startswith(key + ":"):
				thisSrcDict[key] = thisItem.split(':')[1]
				continue
	srcDict[int(thisSrcDict["SRC"])] = thisSrcDict

tn.write("DST\n")
listOfAllDsts = tn.read_until("END", 2).split("\r\n")
for thisLine in listOfAllDsts:
	if thisLine.startswith("DST "):
		thisLine = list(thisLine)
		thisLine[3] = ":"
		thisLine = ''.join(thisLine)
	else:
		continue
	thisDstList = shlex.split(thisLine)
	thisDstDict = dict.fromkeys(dstParameters)
	for key, value in thisDstDict.items():
		for thisItem in thisDstList:
			if thisItem.startswith(key):
				thisDstDict[key] = thisItem.split(':')[1]
				continue
	dstDict[int(thisDstDict["DST"])] = thisDstDict

tn.write("CFG GPO\n")
gpioList = tn.read_until("END", 2).split("\r\n")
for thisLine in gpioList:
	if thisLine.startswith("CFG GPO "):
		thisLine = list(thisLine)
		del thisLine[0:8]
		thisLine.insert(0, ":")
		thisLine.insert(0, "O")
		thisLine.insert(0, "I")
		thisLine.insert(0, "P")
		thisLine.insert(0, "G")
		thisLine = ''.join(thisLine)
	else:
		continue
	thisGPOlist = shlex.split(thisLine)
	thisGPIOdict = dict.fromkeys(gpioParameters)
	for key, value in thisGPIOdict.items():
		for thisItem in thisGPOlist:
			if thisItem.startswith(key + ":"):
				thisGPIOdict[key] = thisItem.split(':')[1]
				continue
	gpioDict[int(thisGPIOdict["GPIO"])] = thisGPIOdict

tn.write("GPO\n")
gpoList = tn.read_until("END", 2).split("\r\n")
for thisLine in gpoList:
	if thisLine.startswith("GPO "):
		thisLine = list(thisLine)
		del thisLine[0:4]
		thisLine = ''.join(thisLine).replace(" ", ":")
	else:
		continue
	for key, value in gpioDict.items():
		if thisLine.startswith(str(key) + ":"):
			gpioDict[int(thisLine.split(':')[0])]["GPO"] = thisLine.split(':')[1]
			continue

tn.write("GPI\n")
gpoList = tn.read_until("END", 2).split("\r\n")
for thisLine in gpoList:
	if thisLine.startswith("GPI "):
		thisLine = list(thisLine)
		del thisLine[0:4]
		thisLine = ''.join(thisLine).replace(" ", ":")
	else:
		continue
	for key, value in gpioDict.items():
		if thisLine.startswith(str(key) + ":"):
			gpioDict[int(thisLine.split(':')[0])]["GPI"] = thisLine.split(':')[1]
			continue
tn.close()

bigDict = dict.fromkeys(["node", "source", "destination", "gpio"]) 

bigDict["node"] = dict(setDict.items() + verDict.items() + ipDict.items())
bigDict["source"] = srcDict
bigDict["destination"] = dstDict
bigDict["gpio"] = gpioDict

print json.dumps(bigDict, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)