import xml.etree.ElementTree as ET

def load(filename,alllist,keynode):
	result = ""
	root = ET.parse(filename).getroot()
	allthing = root.findall(alllist)
	for key in allthing:
		result = "\n" + key.find(keynode).text + result + "\n"
	return result

def WriteFile(filename,content):
	filehandle = open(filename,'ab')
	filehandle.write(content)
	filehandle.close()


if __name__ == '__main__':
	filename = raw_input("filename:")
	alllist = raw_input("allist:")
	keynode = raw_input("keynode:")
	content = load(filename,alllist,keynode)
	print content
	savefile = raw_input("input file you want to save it:")
	WriteFile(savefile,content)
	
