# imdba_python

imdba_python scraper

Requirements :
Python 3.5
PIP
lxml (pip install lxml)
BeautifulSoup (pip install BeautifulSoup4)
requests (pip install requests)
*argparse (python lib)
*csv (python lib)

How to Execute :
  
Linux (*To be reviewed (not tested)*): 
    
1. Follow this tutorial to ensure your linux env is set up (http://openbookproject.net/thinkcs/python/english3e/app_c.html)
    
2. Open terminal
    
3. do $ cd /usr/local

4. do $ git clone https://github.com/MigalBothma/imdba_python.git

5. do $ cp /usr/local/imdba_python/imdbscrape.py /usr/bin/*

6. do $ cd /usr/bin/

7. sudo chmod +x /imdba_python-master/imdbscrape.py
    
8. $ sudo vi imdbscrape.py (or you can use vim like : $ sudo vim imdbscrape.py)
    
9. Add this line as the first line in the script:
      #!/usr/bin/env python3
   
   Find    
    
10. At the unix command prompt, type the following to make imdbscrape.py executable:
      do $ chmod +x imdbscrape.py
    
11. Move imdbscrape.py into your bin directory, and it will be runnable from anywhere.

Windows:
    
1. clone repo (zip).
    
2. Open imdba_python-master.zip
    
3. Copy imdba_python-master File and it's contents to desktop.
    
4. Open command window ( winkey + r ), enter 'cmd'.
    
5. Enter *cd desktop*.
   
6. cd imdba_python-master.
    
7. pip install requests
    
8. pip install BeautifulSoup4
    
9. Execute *python imdbscrape.py --top 10 --print True --csv True --sortBy Rank*

***************************** python imdbscrape.py --h *****************************


usage: imdbscrape.py [-h] [--print PRINT] [--csv CSV] [--top TOP]
 [--sortBy SORTBY]

IMDB top 250 movies. See the commands below for further usage

optional arguments:
  -h, --help            show this help message and exit
  --console_print CONSOLE_PRINT
                        Print Formatted output to console (True|False)
  --csv CSV             Export csv to same directory as script (True|False)
  --top TOP             Top (n) where n is an (integer) default : 50
  --sortBy SORTBY       SortBy (Rank, Title, Year, Rating, NoR, Runtime,
                        Director)
  --setup SETUP         install all required dependencies for package (pip
                        required) (True|False)
  
  
*********************************************************************************



As seen above, the basic options are :

--print   True|False        : default false.

--csv     True|False        : default false.

--top n                     : default 50.

--sortBy (Rank, Title, Year, Rating, NoR, Runtime, Director) : default no sort

