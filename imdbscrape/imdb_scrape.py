# import python libs
import lxml
import requests
from bs4 import BeautifulSoup
import argparse

# import python modules
import imdb_crawl
import imdb_sortBy
import imdb_print
import imdb_csv


def scrape_top_n(args):
    """
    This module is used to scrape the top 250 elements from IMDB and acts as orchestrator and processing central of this application.

    :param Namespace args: [ top, csv, sortBy, setup, console_print]
    
    top : int
    csv : bool
    sortBy : string
    setup : bool
    console_print : bool
    """

    app_args = args

    default_size = 50
    base_url = 'https://www.imdb.com'
    resp = requests.get(base_url + '/chart/top?ref_=nv_mv_250')

    soup = BeautifulSoup(resp.text, 'lxml')
    movies_list = soup.find_all(
        class_=['titleColumn', 'ratingColumn imdbRating'])

    # Create matrix to append to ( Array of Arrays ) else indexError
    movies_names_wl = [[] for movies in movies_list]

    # Find title, year and rating and append to Matrix
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

    # Remove empty entries from movies_names
    for movie in movies_names_wl:
        if(movie == []):
            movies_names_wl.remove(movie)

    # attach ranks to movie_names
    for index, movie in enumerate(movies_names_wl):
        if(movie != []):
            movies_names_wl[index].insert(0, index+1)

    # Delve deeper into top (n) default: 50
    movies_names_wl = imdb_crawl.crawl_top_n(
        base_url, movies_names_wl, app_args)

    # Slice top_size and do sortBy variable
    movies_names_wl = imdb_sortBy.sortMoviesBy(movies_names_wl, app_args)

    # Do console print if args.console_print == True
    if (app_args.console_print == True):
        imdb_print.console_print(movies_names_wl, app_args)

    if (app_args.csv == True):
        imdb_csv.write_to_csv(movies_names_wl, app_args)
