def console_print(movies_names_wl, args):
    print('\nPrinting top', args.top, 'of imdb scrape')
    print('\nSorted By: ', args.sortBy, '\n')
    print('{0:<6} {1:<50} {2:<14} {3:<16} {4:<20} {5:<18} {6:<20}'.format(
        'Rank', 'Title', 'Year', 'Rating', 'Number of ratings', 'Runtime', 'Director'))
    for index, movie in enumerate(movies_names_wl):
        if (len(movie) > 6):
            print('{0:<6} {1:<50} {2:<14} {3:<16} {4:<20} {5:<18} {6:<20}'.format(
                movie[0], movie[2], movie[3], movie[4], movie[5], movie[6], movie[7]))