# helper functions are defined here


def remove_empty_arrays(movies_names_wl):
    """
    This function takes movies_names_wl and removes empty arrays.
    """
    for movie in movies_names_wl:
        if(movie == []):
            movies_names_wl.remove(movie)
    return movies_names_wl


def attach_ranks(movies_names_wl):
    for index, movie in enumerate(movies_names_wl):
        if(movie != []):
            movies_names_wl[index].insert(0, index+1)
    return movies_names_wl
