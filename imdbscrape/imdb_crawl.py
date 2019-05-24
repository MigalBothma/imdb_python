import requests
from bs4 import BeautifulSoup

# Crawler module


def crawl_top_n(base_url, movies_names_wl, args):
    """
    This module is used to iterate and crawl over base_url + movies_names_with_links[Links] .

    :param base_url : base_url of imdb

    base_url : str

    :param list movies_names_wl: a list of movie_names_with_links
        movie : [Rank, Link, Title, Year, Rating, Number of Ratings, Runtime, Director]

    Rank : int
    Link : str
    Title : str
    Year : int
    NoR : int
    Runtime : str
    Director : str

    :param Namespace args: [ top, csv, sortBy, setup, console_print]

    top : int
    csv : bool
    sortBy : string
    setup : bool
    console_print : bool
    """
    count = 0

    while(count < args.top):
        print(count+1, '. crawling : ', base_url +
              movies_names_wl[count][1], '\t', movies_names_wl[count][2])
        resp = requests.get(base_url + movies_names_wl[count][1])
        soup = BeautifulSoup(resp.text, 'lxml')
        movie_details = soup.find_all(
            class_=['title_wrapper', 'ratings_wrapper', 'plot_summary_wrapper'])

        # import wrappers, find classes, access the appropriate element and get text
        # get director, runtime and number of ratings
        for content in movie_details:
            anchors = []

            for credit_summary_item in content.find_all(class_=['credit_summary_item']):
                for people in credit_summary_item.find_all('a'):
                    anchors.append(people.text)
            if anchors != []:
                movies_names_wl[count].append(anchors[0])

            for subtext in content.find_all(class_=['subtext']):
                for time in subtext.find_all('time'):
                    dirty_time_val = time.text
                    dirty_time_val = dirty_time_val.strip('\n')
                    clean_time_val = dirty_time_val.strip()
                    movies_names_wl[count].append(clean_time_val)

            for imdbRating in content.find_all(class_=['imdbRating']):
                for num_of_ratings in content.find_all(class_=['small']):
                    num_of_ratings_dirty = num_of_ratings.text
                    num_of_ratings_clean = int(
                        "".join(num_of_ratings_dirty.split(',')))
                    movies_names_wl[count].append(num_of_ratings_clean)
        count += 1
    return movies_names_wl
