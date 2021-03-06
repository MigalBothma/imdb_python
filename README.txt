# imdba_python

Requirements
============

External (pip)
---
-BeautifulSoup 
-requests 

Native python
--------------
-argparse (python lib)
-csv (python lib)

How to Execute
================

Linux
------
1. Follow this tutorial to ensure your linux env is set up (http://openbookproject.net/thinkcs/python/english3e/app_c.html
2. Open terminal
3. do $ cd /usr/bin/
4. $ sudo vi imdbscrape.py (or you can use vim like : $ sudo vim imdbscrape.py)
5. Add this line as the first line in the script:
      #!/usr/bin/env python3   
6. At the unix command prompt, type the following to make imdbscrape.py executable:
      do $ chmod +x imdbscrape.py
7.Move imdbscrape.py into your bin directory, and it will be runnable from anywhere.

Windows
-------
1. clone repo (zip). 
2. Open imdba_python-master.zip
3. Copy imdba_python-master File and it's contents to desktop.
4. Open command window ( winkey + r ), enter 'cmd'.
5. Enter *cd desktop*.
6. cd imdba_python-master.
7. pip install requests
8. pip install BeautifulSoup4
9. Execute *python imdbscrape.py --top 10 --print True --csv True --sortBy Rank


OUTPUT : python imdbscrape.py --h
-------------------------------------------------------------------------------------------------------------

usage: imdbscrape.py [-h] [--print PRINT] [--csv CSV] [--top TOP]
 [--sortBy SORTBY]

IMDB top 250 movies. See the commands below for further usage

optional arguments:
  -h, --help       show this help message and exit
  
--print PRINT    Print ArrayOfArrays to console (True|False)
  
--csv CSV        Export csv to same directory as script (True|False)
  
--top TOP        Top (n) where n is an (integer) default : 50
  
--sortBy SORTBY  SortBy (Rank, Title, Year, Rating, NoR, Runtime, Director)

-------------------------------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------------------------------
As seen above, the basic options are 
-------------------------------------------------------------------------------------------------------------
--print   True|False        : default false.

--csv     True|False        : default false.

--top n                     : default 50.

--sortBy (Rank, Title, Year, Rating, NoR, Runtime, Director) : default no sort

