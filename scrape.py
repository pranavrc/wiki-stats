import urllib2
import string
import json
import sys
import pickle

def scrape():
	try:
		listOfLanguages = urllib2.urlopen("http://en.wikipedia.org/w/api.php?action=sitematrix&format=json&smtype=language&smstate=all").read()
	except:
		print "Could not fetch sitematrix"
		sys.exit("Exiting")

	listlangDict = {}
	jsonLang = json.loads(listOfLanguages)

	for langCounter in range(0, len(jsonLang[u'sitematrix']) - 1):
	     	listlangDict[jsonLang[u'sitematrix'][str(langCounter).decode('ascii')][u'code']] = ''

	listOfStrings = open("./tawiktionary-20120314-all-titles-in-ns0","r").readlines()
	langDict = {}

	for langName in listlangDict:
		for counter in range(0, len(listOfStrings)):
			queryString = str(listOfStrings[counter]).strip("\n")
			queryString = "http://" + langName + ".wikipedia.org/w/api.php?action=parse&format=json&page=" + str(queryString).decode('utf-8') + "&prop=langlinks"
			try:
				dump = urllib2.urlopen(queryString).read()
			except:
				print "Could not fetch json"
				continue
			jsonfoo = json.loads(dump)
			try:
				listLength = len(jsonfoo[u'parse'][u'langlinks'])
			except:
				print "Keyerror"
				continue
			for lang in range(0, listLength):
				try:
					if str(jsonfoo[u'parse'][u'langlinks'][lang][u'lang']) in langDict:
			    			langDict[str(jsonfoo[u'parse'][u'langlinks'][lang][u'lang'])] = langDict[str(jsonfoo[u'parse'][u'langlinks'][lang][u'lang'])] + 1
					else:
						langDict[str(jsonfoo[u'parse'][u'langlinks'][lang][u'lang'])] = 1
				except:
		    			continue
  			listlangDict[langName] = langDict
	
	dictFile = open('barf', 'wb')
	pickle.dump(listlangDict, dictFile)
	dictFile.close()





