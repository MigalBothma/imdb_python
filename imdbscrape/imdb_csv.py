import datetime
import csv


def write_to_csv(movies_names_wl, args):
    """
    This module is used to format and print the values received from imdb_scrape to a csv and write that file to the same directory.

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

    now = datetime.datetime.now()
    csvtime = now.strftime("%y-%m-%d_%H-%M")

    with open('imdb top '+str(args.top)+' - ' + str(csvtime) + '.csv', mode='w') as export_csv_file:
        csv_writer = csv.writer(export_csv_file, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        csv_writer.writerow(
            ['Rank', 'Title', 'Year', 'Rating', 'Number of ratings', 'Runtime', 'Director'])
        for movie in movies_names_wl:
            if len(movie) > 6:
                row = list([str(movie[0]), movie[2], movie[3],
                            movie[4], movie[5], movie[6], movie[7]])
                csv_writer.writerow(row)
        export_csv_file.close()
