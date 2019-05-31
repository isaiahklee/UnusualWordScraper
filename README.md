# UnusualWordScraper
Web Scraper that returns rare words <br/>
Rare words as determined by a comparison to the google list of 10'000 most commonly used english words. <br/>
Use: <br/>
run createHashFile.py with an input file of newline separated words to create a hashfile <br/>
&nbsp;&nbsp;&nbsp;&nbsp;Example: py createHashFile.py words.txt <br/>
run scraperMain.py with a website and an input hashfile to use to build a hashtable <br/>
&nbsp;&nbsp;&nbsp;&nbsp;Example: py scraperMain.py https://en.wikipedia.org/wiki/Extremely_low_frequency hashfile.txt 