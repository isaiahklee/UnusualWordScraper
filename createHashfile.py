#I want to take a list of words as an input. parse them into a hash table file. 
#this file can be imported to create a hashtable in another script
#this hashtable will be used to do constant time lookup of words scraped from the web. 
#making time complixity scale linearly with number of words scraped from web

#imports
import sys
from hashlib import sha256
import listnode as ls

#preprocessing
def file_len(fname):
    with open(fname) as f:
        i = -1
        for i, l in enumerate(f):
            pass
    return i + 1

#global vars
inputFileName = sys.argv[1] #name of input file in directory
inputsize = file_len(inputFileName)*2; #how many newlines are in the input file basically, mult by 2 to minimize collisions.
hashList = []   #array of linked lists. 




#create array of empty linked lists. 
i = 0
while i < inputsize:
    #create ls.listnode elem to add to list
    head = ls.listnode(None)
    hashList.append(head)
    i = i + 1
'''testing
i = 0
while i < len(hashList):
    print(hashList[i].data)
    i += 1
'''
#open file, hash each line, add hash to another file
hashf = open("hashtable.txt", "w") #file to output to
with open(inputFileName, "r") as wordf: #file to get input from
    for i, l in enumerate(wordf):
        tempWord = l.rstrip()
        print(tempWord)
        # we have a word, we need to hash it and insert it into our array
        tempHash = int(sha256(tempWord.encode()).hexdigest(), 16)
        #print("id: " + str(i) + " hash: " + str(tempHash))
        '''
        arrPos = tempHash % len(hashList) #position to insert hash into array
        arrData = hashList[arrPos] # the node at that position
        if arrData.data == None: #if the given hash position is empty
            arrData.addData(tempHash)
        else: #it already has data
            #print("collision")
            #traverse to end of linked list and add
            tempNode = arrData
            while tempNode.hasNext():
                print("double collision")
                tempNode = tempNode.next
            newNode = ls.listnode(tempHash)
            tempNode.addNext(newNode)
        #test
        #print("index:" + str(i) + " wrd:" + str(tempWord).rstrip() + " hsh:" + str(tempHash))
        '''
        #insert data into outputFile
        #hashf.write(tempWord.decode().rstrip() + " ," + str(tempHash) + "\n")
        hashf.write(str(tempHash) + "\n")

'''
#print test
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