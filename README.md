Requirements
============

External (pip)
---
- BeautifulSoup 
- requests 

Native python
--------------
- argparse (python lib)
- csv (python lib)

How to Execute
================

Using python setup
------------------
1. Navigate to *\imdb_python*
2. do python setup.py install (This will install package to python/lib/site-packages )
3. pip install -r requirements.txt ( Install requirements )
4. In *\imdb_python* do *python imdbscrape --console_print True*

Linux
------
1. Follow this tutorial to ensure your linux env is set up (http://openbookproject.net/thinkcs/python/english3e/app_c.html
2. Open terminal
3. do $ cd /usr/bin/imdb_python/imdbscrape
4. $ sudo vi main.py (or you can use vim like : $ sudo vim imdbscrape.py)
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
6. cd imdb_python\imdbscrape.
7. pip install requests
8. pip install BeautifulSoup4
9. Execute *python main.py --top 10 --print True --csv True --sortBy Rank

OUTPUT : python imdbscrape.py --h
-------------------------------------------------------------------------------------------------------------

*Argument Error : please use --csv or --console_print to select either or for output*

usage: imdbscrape.py [-h] [--print PRINT] [--csv CSV] [--top TOP]
 [--sortBy SORTBY]

IMDB top 250 movies. See the commands below for further usage

optional arguments:
  -h, --help     show this help message and exit
  
--print PRINT    Print ArrayOfArrays to console (True|False)
  
--csv CSV        Export csv to same directory as script (True|False)
  
--top TOP        Top (n) where n is an (integer) default : 50
  
--sortBy SORTBY  SortBy (Rank, Title, Year, Rating, NoR, Runtime, Director)

--setup SETUP    install all required dependencies for package (pip required) (True|False)

-------------------------------------------------------------------------------------------------------------

As seen above, the basic options are 
-------------------------------------------------------------------------------------------------------------
--print   True|False        : default None.

--csv     True|False        : default None.

--top n                     : default 50.

--sortBy (Rank, Title, Year, Rating, NoR, Runtime, Director) : default None

--setup                     : default None

