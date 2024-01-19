import subprocess
import optparse

def get_data():

	parse_object = optparse.OptionParser()
	parse_object.add_option("-i","--intrface",dest="intrface",help="interface ivvu raa")
	parse_object.add_option("-m","--mac",help="MAc Address ivvu ra puva")
	return  parse_object.parse_args()

(inputt,argu)= get_data()
i=inputt.intrface;
m=inputt.mac


def main(i,m):
	subprocess.call(["ifconfig",i,"down"])
	subprocess.call(["ifconfig",i,"hw","ether",m])
	subprocess.call(["ifconfig",i,"up"])

main(i,m)
print("Mission Completed")
