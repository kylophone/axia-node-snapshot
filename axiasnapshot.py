import sys, telnetlib, shlex

tn = telnetlib.Telnet(sys.argv[1], '93') #Takes one command-line input: IP of Node.

setDict = dict.fromkeys(['LWS_802_1p_TAGE', 'LWS_802_1p_VLAN', 'LWS_802_1Q_PRIO', 'RTP_802_1p_TAGE', 'RTP_802_1p_VLAN', 'RTP_802_1Q_PRIO', 'LWCLK_PRIO', 'LWCLK_ADDR', 'IPCLK_ADDR', 'ADIP', 'NID', 'AESSYNC_PRI', 'AESSYNC_OUT', 'AESSYNCE', 'AESTX_AUTO', 'LWS_IP_TOS', 'RXBUFF', 'RTP_IP_TOS', 'LWCLK_MODE'])
verDict = dict.fromkeys(['DEVN', 'NSRC', 'NDST', 'NGPI', 'NGPO', 'PRODUCT', 'MODEL', 'SVER'])
ipDict = dict.fromkeys(['address', 'netmask', 'gateway', 'hostname'])
srcDict = {}
srcParameters = ['SRC', 'PSNM', 'RTPE', 'RTPA', 'INGN', 'IO', 'RTPP', 'SHAB', 'NCHN', 'PHPW', 'AESM']
dstDict = {}
dstParameters = ['DST', 'NAME', 'ADDR', 'NCHN', 'VMOD', 'OUGN']
gpioDict = {}


tn.write("SET\n")
setList = shlex.split(tn.read_until("\n"))
for key, value in setDict.items():
	for thisItem in setList:
		if key in thisItem:
	 		setDict[key] = thisItem.split(':')[1]
	 		continue

tn.write("VER\n")
verList = shlex.split(tn.read_until("\n"))
for key, value in verDict.items():
	for thisItem in verList:
		if thisItem.startswith(key):
	 		verDict[key] = thisItem.split(':')[1]
	 		continue

tn.write("IP\n")
ipList = shlex.split(tn.read_until("\n"))
for key, value in ipDict.items():
	for thisIndex, thisItem in enumerate(ipList):
		if thisItem == key:
			ipDict[key] = ipList[thisIndex + 1]
			continue

tn.write("SRC\n")
listOfAllSrcs = tn.read_until("END").split("\r\n")
for thisLine in listOfAllSrcs:
	if thisLine.startswith("SRC"):
		thisLine = list(thisLine)
		thisLine[3] = ":"
		thisLine = ''.join(thisLine)
	else:
		continue
	thisSrcList = shlex.split(thisLine)
	thisSrcDict = dict.fromkeys(srcParameters)	
	for key, value in thisSrcDict.items():
		for thisItem in thisSrcList:
			if thisItem.startswith(key):
				thisSrcDict[key] = thisItem.split(':')[1]
				continue
	srcDict[int(thisSrcDict["SRC"])] = thisSrcDict

tn.write("DST\n")
listOfAllDsts = tn.read_until("END").split("\r\n")
for thisLine in listOfAllDsts:
	if thisLine.startswith("DST"):
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
gpoParameterList = tn.read_until("END") 
tn.write("GPO\n")
gpoList = tn.read_until("END")
tn.write("GPI\n")
gpiList = tn.read_until("END")

tn.close()

print "\n"
print setDict
print "\n"
print verDict
print "\n"
print ipDict
print "\n"
print srcDict
print "\n"
print dstDict
#print gpoDict
#print gpiDict
