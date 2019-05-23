def sortMoviesBy(movies_names_wl, args):
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