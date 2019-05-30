#I want to take a list of words as an input. parse them into a hash table file. 
#this file can be imported to create a hashtable in another script
#this hashtable will be used to do constant time lookup of words scraped from the web. 
#making time complixity scale linearly with number of words scraped from web

#imports
import sys

#preprocessing
def file_len(fname):
    with open(fname) as f:
        i = -1
        for i, l in enumerate(f):
            pass
    return i + 1

#global vars
inputFileName = sys.argv[1] #name of input file in directory
inputsize = file_len(inputFileName); #how many newlines are in the input file basically.
hashList = []   #array of linked lists. 

#linked list node for hashes (linked list so can handle collisions)
class listNode:
    def __init__(self, data, nextItem):
        self.data = data
        self.next = nextItem
    def addNext(nextItem):
        self.next = nextItem

#create list of empty linked lists. 
i = 0
while i < inputsize:
    #create listNode elem to add to list
    head = listNode("test", None)
    hashList.append(head)
    i = i + 1
'''testing
i = 0
while i < len(hashList):
    print(hashList[i].data)
    i += 1
'''
#
print(inputsize)
'''
#open file to write to (will be a list of hashes)
f = open("hashtable.txt", "w")
'''