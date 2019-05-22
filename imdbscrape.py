from bs4 import BeautifulSoup
import datetime
import requests
import argparse
import csv

parser = argparse.ArgumentParser(description='IMDB top 250 movies. See the commands below for further usage')
parser.add_argument('--console_print', help='Print Formatted output to console (True|False)', type=bool)
parser.add_argument('--csv', help='Export csv to same directory as script (True|False)', type=bool)
parser.add_argument('--top', help='Top (n) where n is an (integer) default : 50', type=int)
parser.add_argument('--sortBy', help='SortBy (Rank, Title, Year, Rating, NoR, Runtime, Director)', type=str)

args = parser.parse_args()

top_size = 50 
base_url = 'https://www.imdb.com'
resp = requests.get(base_url + '/chart/top?ref_=nv_mv_250')

soup = BeautifulSoup(resp.text, 'lxml')
movies_list = soup.find_all(class_ = ['titleColumn', 'ratingColumn imdbRating'])

#Create matrix to append to ( Array of Arrays ) else indexError
movies_names_wl = [[] for movies in movies_list]

#Find title, year and rating and append to Matrix
for index, movie in enumerate(movies_list):
    for link in movie.find_all('a', href=True):
        movies_names_wl[index].append(link['href'])
    for title in movie.find_all('a'):
        movies_names_wl[index].append(title.text)
    for year in movie.find_all('span'):
        dirty_year = year.text
        clean_year = dirty_year.strip('()')
        movies_names_wl[index].append(clean_year)
    for rating in movie.find_all('strong'):
        movies_names_wl[index-1].append(rating.text)

#Remove empty entries from movies_names
for movie in movies_names_wl:
    if(movie == []):
        movies_names_wl.remove(movie)

#attach ranks to movie_names
for index, movie in enumerate(movies_names_wl):
    if(movie != []):
        movies_names_wl[index].insert(0, index+1)

#Trying List comprehension here ->
#movies_names_wl = [ movies_names_wl[index].insert(0, index+1) for index, movie in enumerate(movies_names_wl) if movie != [] ]
#print(movies_names_wl) 

#Delve deeper into top (n) default: 50
count = 0

if(args.top):
    top_size = args.top

while( count < top_size ):
    
    print(count+1, '. crawling : ', base_url + movies_names_wl[count][1], '\t', movies_names_wl[count][2])
    resp = requests.get(base_url + movies_names_wl[count][1])
    soup = BeautifulSoup(resp.text, 'lxml')
    movie_details = soup.find_all(class_ = ['title_wrapper', 'ratings_wrapper', 'plot_summary_wrapper'])

    #import wrappers, find classes, access the appropriate element and get text 
    #get director, runtime and number of ratings
    for content in movie_details:
        anchors = []
        
        for credit_summary_item in content.find_all(class_=['credit_summary_item']):
            for people in credit_summary_item.find_all('a'):
                anchors.append(people.text)
        if anchors != []: movies_names_wl[count].append(anchors[0])
        
        for subtext in content.find_all(class_=['subtext']):
            for time in subtext.find_all('time'):
                dirty_time_val = time.text
                dirty_time_val = dirty_time_val.strip('\n')
                clean_time_val = dirty_time_val.strip()
                movies_names_wl[count].append(clean_time_val)
                
        for imdbRating in content.find_all(class_=['imdbRating']):
            for num_of_ratings in content.find_all(class_=['small']):
                num_of_ratings_dirty = num_of_ratings.text
                num_of_ratings_clean = int("".join(num_of_ratings_dirty.split(',')))
                movies_names_wl[count].append(num_of_ratings_clean)           
    count += 1


#Do arg methods
    
#Slice top_size and do args.sortBy variable
if(args.sortBy):
    try:
        movies_names_wl = movies_names_wl[:top_size]
    except:
        print('**Error** : cannot slice top size')

    keydictionary = {'Rank' : 0, 'Title' : 2, 'Year' : 3, 'Rating' : 4, 'NoR' : 5, 'Runtime' : 6, 'Director' : 7}

    try:
        movies_names_wl.sort(key = lambda movies_names_wl: movies_names_wl[keydictionary[args.sortBy]])
    except:
        print('**Error** : cannot sortBy')
    
    
if (args.console_print == True):
    print( '\nPrinting top', top_size, 'of imdb scrape')
    print('\nSorted By: ',args.sortBy,'\n')
    print( '{0:<6} {1:<50} {2:<14} {3:<16} {4:<20} {5:<18} {6:<20}'.format('Rank', 'Title', 'Year', 'Rating', 'Number of ratings', 'Runtime', 'Director' ))
    for index, movie in enumerate(movies_names_wl):
        if (len(movie) > 6):
            print('{0:<6} {1:<50} {2:<14} {3:<16} {4:<20} {5:<18} {6:<20}'.format(movie[0], movie[2], movie[3], movie[4], movie[5], movie[6], movie[7]))
        
if (args.csv == True):
    now = datetime.datetime.now()
    csvtime = now.strftime("%y-%m-%d_%H-%M")
    
    with open('imdb top '+str(top_size)+' - ' +str(csvtime) + '.csv', mode='w') as export_csv_file:
        csv_writer = csv.writer(export_csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        csv_writer.writerow(['Rank', 'Title', 'Year', 'Rating', 'Number of ratings', 'Runtime', 'Director'])
        for movie in movies_names_wl:
            if len(movie) > 6:
                row = list([str(movie[0]), movie[2], movie[3], movie[4], movie[5], movie[6], movie[7]])
                #print(row)
                csv_writer.writerow(row)
        export_csv_file.close()


