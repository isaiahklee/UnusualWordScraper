#This file is to host the main function to drive the webscraper
#written by Isaiah K. Lee

#imports


#main function
#inputParam/s: website to scrape, or list of websites to scrape in .txt file delineated by newlines (maybe also add json support)
#output/s: return final unusual word list as json to be used and displayed in html page.



#function to parse that the given input is a real website name/has at least 1 real website.
#throw errors for improperly formated websites
#inputParam/s: the list main is given, but puts it into a nice array
#output/s: return array of good websites (only contains one thing if only one website given to it)



#function to deal with robots.txt
#inputParam/s: the website to check the robot.txt of.
#output/s: error if we shouldn't access the site w/ scraper || 0 if we can || or a number greater than 0 which we should 
#       interpret is milleseconds we need to wait between consecutive accesses of subpages of the website. 



#function to parse webdata into json?
#output/s: return json words list with html tags and other useless/code stuff stripped



#function to search webdata for unusual words. 
#inputParam/s: json webdata file