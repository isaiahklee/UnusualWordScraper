#This file is to host the main function to drive the webscraper
#written by Isaiah K. Lee

#imports
from bs4 import BeautifulSoup #for scraping
import sys                  #to get command line args
import requests             #for getting webpage data
import re                   #for further text processing
import listnode as ls       #my simple listnode to make a hashtable linked list 
from hashlib import sha256  #to do non random seed hashing (vuln to attacks, but this isn't an app that deals with any vulnerable data anyways like password hashing is)
import os.path              #to check if input file exists


#main function
#inputParam/s: website to scrape, or list of websites to scrape in .txt file delineated by newlines (maybe also add json support)
#output/s: return final unusual word list as json to be used and displayed in html page.
def main():
    #url = 'https://en.wikipedia.org/wiki/Extremely_low_frequency'  ||  http://localhost/index1/
    fileorurl = sys.argv[1]
    hashFile = sys.argv[2]

    #if we're given a url, just parse it normally. 
    if fileorurl.find("http://") == 0 or url.find("https://") == 0:
        #internet stuff
        response = requests.get(url)
        if response.status_code != 200:
            print("there's been an error in fetching the website")
            exit()
        #soupify
        soup = BeautifulSoup(response.content, 'html.parser')
        wordList = parseText(soup)
    else:
        #return a laaarge wordlist of all sites scraped. 
        wordList = checkInput(fileorurl)
    
    unusualList = makeUnusualList(wordList, hashFile)

    unusualf = open("unusualwordlist.txt", "w") #file to output to
    for word in unusualList:
        unusualf.write(word + "\n")
    unusualf.close()

#function to parse that the given input is a real website name/has at least 1 real website.
#throw errors for improperly formated websites
#inputParam/s: the list main is given, but puts it into a nice array
#output/s: return array of words scraped from all good websites
def checkInput(infilename):
    retlist = []
    with open(infilename, "r") as urlfile:
        #check if file empty
        #TODO

        for i, aurl in enumerate(wordf):
            #check if the url exists. 
            response = requests.get(url)
            if response.status_code != 200:
                continue
            #if it does, soupify, parse, and add to return list
            #soupify
            soup = BeautifulSoup(response.content, 'html.parser')
            retList.append(parseText(soup))
            

    #parse all in parse list, and add to return word array. 

    #return
    return retlist

#function to deal with robots.txt
#inputParam/s: the website to check the robot.txt of.
#output/s: error if we shouldn't access the site w/ scraper || 0 if we can || or a number greater than 0 which we should 
#       interpret is milleseconds we need to wait between consecutive accesses of subpages of the website. 



#function to parse webdata into word array
#output/s: return array of words with html tags and other useless/code stuff stripped
def parseText(soup):
    #remove script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out
    #get text
    text = soup.get_text()
    #break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    #break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    #remove blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    text = text.lower()
    #remove special characters and store text in array
    wordList = re.findall(r'[A-Za-z]*[A-Za-z]', text)
    '''#if find ' remove it and following characters 
    for word in wordList:
        print(word.lower())'''
    return wordList


#function to search webdata for unusual words. Use hashtable to make search time constant for each word.
#inputParam/s: the webdata array, the hashtable filename
#output: array of unusual words
def makeUnusualList(webdata, hashFile):
    unusualList = []
    #inputsize = file_len(inputFileName)*2; #how many newlines are in the input file basically, mult by 2 to minimize collisions.
    inputsize = 20000
    hashList = []   #array of linked lists. 

    #create array of empty linked lists. 
    i = 0
    while i < inputsize:
        #create ls.listnode elem to add to list
        head = ls.listnode(None)
        hashList.append(head)
        i = i + 1
    
    #make hashtable out of hashfile
    with open(hashFile, "r") as wordf: #file to get input from
        i = 0
        for i, ahash in enumerate(wordf):
            
            arrPos = int(ahash) % len(hashList) #position to insert hash into array
            arrData = hashList[arrPos] # the node at that position
            if arrData.data == None: #if the given hash position is empty
                arrData.addData(int(ahash))
            else: #it already has data
                #print("collision")
                #traverse to end of linked list and add
                tempNode = arrData
                while tempNode.hasNext():
                    #print("double collision")
                    tempNode = tempNode.next
                newNode = ls.listnode(int(ahash))
                tempNode.addNext(newNode)
            #test
            #print("index:" + str(i) + " hsh:" + ahash)
    '''
    for node in hashList:
        if node.hasData:
            print(str(node.data))
            if node.hasNext():
                tempNode = node.next
                print("---" + str(tempNode.data))
                while tempNode.hasNext():
                    tempNode = tempNode.next
                    print("---" + str(tempNode.data))
    '''

    #for every word, check it against hash table
    #for word in webdata:
    #TODO dont print duplicates. do this by creating a second hash table while reading through this one. 
    for word in webdata:
        compInt = int(sha256(word.encode()).hexdigest(), 16)
        arrPos = compInt % len(hashList) #position to insert hash into array
        arrData = hashList[arrPos] # the node at that position
        if arrData.data == None: #if the given hash position is empty
            unusualList.append(word)



    return unusualList



#run it
main()