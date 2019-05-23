# imdb sortBy functions
def sortMoviesBy(movies_names_wl, args):
    """
    This module is used to sortMovies by the dict(arg.sortBy)

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

    try:
        movies_names_wl = movies_names_wl[:args.top]
    except:
        print('**Error** : cannot slice top size')

    keydictionary = {'Rank': 0, 'Title': 2, 'Year': 3,
                     'Rating': 4, 'NoR': 5, 'Runtime': 6, 'Director': 7}

    try:
        movies_names_wl.sort(
            key=lambda movies_names_wl: movies_names_wl[keydictionary[args.sortBy]])
    except:
        if(args.sortBy != None):
            print('**Error** : cannot sortBy **')

    return movies_names_wl
