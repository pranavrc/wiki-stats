import pickle
import scrape

scrape.scrape()
dictPickle = open('barf','rb')
outputDict = pickle.load(dictPickle)
dictPickle.close()

##dictFile = open('barf.txt','w')
##dictFile.write(outputDict)
##dictFile.close()


