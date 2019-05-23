import datetime
import csv

def write_to_csv( movies_names_wl, args ):
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
