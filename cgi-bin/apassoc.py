from subprocess import Popen, PIPE
import json
import sys
import argparse

def get_locate():
	data = dict()
	data["ap1"] = dict() 
	data["ap2"] = dict() 
	data["ap3"] = dict() 
	data["ap4"] = dict() 
	data["ap5"] = dict() 
	data["ap6"] = dict() 
	data["ap7"] = dict() 
	data["ap7"] = dict() 
	data["ap1"]["index"] = "68:bc:0c:64:a3:f0"
	data["ap2"]["index"] = "00:08:30:b7:6a:a0"
	data["ap3"]["index"] = "24:b6:57:ae:f2:b0"
	data["ap4"]["index"] = "68:bc:0c:2c:4b:c0"
	data["ap5"]["index"] = "68:bc:0c:07:fc:20"
	data["ap6"]["index"] = "68:bc:0c:a2:28:10"
	data["ap7"]["index"] = "00:08:30:8f:25:f0"
	data["ap7"]["index"] = "68:bc:0c:2d:e5:a0"
	i = 1
	for name in data.keys():
		data[name]["assoc"] = 0
		data[name]["member"] = list()
		i += 1

	userMac = dict()
	userMac["ga_su_"] = dict()
	userMac["ga_su_"]["mac"] = "a4:34:d9:b3:e4:d5"
	userMac["nomu"] = dict()
	userMac["nomu"]["mac"] = "f4:0f:24:0e:93:83"
	userMac["tktbtk"] = dict()
	userMac["tktbtk"]["mac"] = "20:c9:d0:45:a3:21"
	userMac["nelio_phone"] = dict()
	userMac["nelio_phone"]["mac"] = "a4:f1:e8:b9:47:7e"

	pMac = Popen(["snmpwalk", "-v", "2c", "-c", "Ok@daLoppy", "192.168.10.2", ".1.3.6.1.4.1.14179.2.1.4.1.4"], stdout = PIPE)

	for line in pMac.stdout:
		info, index = line.split(": ")
		index_list = index.split(" ")[:-1]
		index_list = [i.lower() for i in index_list]
		index = ":".join(index_list)
		for d in data.items():
			if index == d[1]["index"]:
				apname = d[0]
				data[apname]["assoc"] += 1
		apmac_list = info.split(" =")[0].split(".")[-6:]
		apmac_list = ['%02x' % int(i) for i in apmac_list]
		apmac = ":".join(apmac_list)
		for user in userMac.items():
			if user[1]["mac"] == apmac:
				data[apname]["member"].append(user[0]) 
	return json.dumps(data)
	
if __name__ == "__main__":
	f = open("")
	while True:
		data = get_locate()
	print data
