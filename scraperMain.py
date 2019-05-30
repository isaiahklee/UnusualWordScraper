#This file is to host the main function to drive the webscraper
#written by Isaiah K. Lee

#imports
from bs4 import BeautifulSoup
import sys
import requests


#main function
#inputParam/s: website to scrape, or list of websites to scrape in .txt file delineated by newlines (maybe also add json support)
#output/s: return final unusual word list as json to be used and displayed in html page.
def main():
    #url = 'https://en.wikipedia.org/wiki/Extremely_low_frequency'
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code != 200:
        print("there's been an error in fetching the website")
        exit()
    soup = BeautifulSoup(response.content, 'html.parser')
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
    print(text)


#function to parse that the given input is a real website name/has at least 1 real website.
#throw errors for improperly formated websites
#inputParam/s: the list main is given, but puts it into a nice array
#output/s: return array of good websites (only contains one thing if only one website given to it)
def checkInput(inarray):
    print("todo")


#function to deal with robots.txt
#inputParam/s: the website to check the robot.txt of.
#output/s: error if we shouldn't access the site w/ scraper || 0 if we can || or a number greater than 0 which we should 
#       interpret is milleseconds we need to wait between consecutive accesses of subpages of the website. 



#function to parse webdata into json?
#output/s: return json words list with html tags and other useless/code stuff stripped



#function to search webdata for unusual words. Use "Rainbow Table" hashes to make search time constant for each word.
#inputParam/s: json webdata file





#run it
main()