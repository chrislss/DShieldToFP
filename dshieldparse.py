__author__ = 'chsmith4'
#import requests
import urllib

#open the input file from SANS, the output file with modified IP's
#inputfile = requests.get("http://feeds.dshield.org/block.txt")

testfile = urllib.URLopener()
testfile.retrieve("http://feeds.dshield.org/block.txt", "dshieldblock.txt")

inputfile = open('dshieldblock.txt')
outputfile = open('feedlist.txt','w')

#Loop through the input file
for line in inputfile:
    #check for valid lines in the file
    if line[0] <> '#' and line[0] <> " " and line[0] <> 'S':
        #if a valid line parse the fields into a LIST with spaces as a delimiter (default)
        linelist = line.split()
        #verify the list is populated, if TRUE extract network range and write to new file
        if linelist:
            startip = linelist[0]
            subnet = linelist[2]
            network = startip + '/' + subnet + '\n'
            outputfile.write(network)

#cleanup - close open files
inputfile.close()
outputfile.close()