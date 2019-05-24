# import python libs
import subprocess
import argparse

#import webscraper
import imdb_scrape

if __name__ == "__main__":
    """
    This is the main function of imdb_scraper

    Arguments passed & parsed
    If args.csv or args.console_print not found print Argument Error and execute self with --h command
    Else pass args to scrape_top_n in imdb_scrape
    """

    parser = argparse.ArgumentParser(
        description='IMDB top 250 movies. See the commands below for further usage')
    parser.add_argument(
        '--console_print', help='Print Formatted output to console (True|False)', type=bool)
    parser.add_argument(
        '--csv', help='Export csv to same directory as script (True|False)', type=bool)
    parser.add_argument(
        '--top', help='Top (n) where n is an (integer) default : 50', type=int, default=50)
    parser.add_argument(
        '--sortBy', help='SortBy (Rank, Title, Year, Rating, NoR, Runtime, Director)', type=str)
    parser.add_argument(
        '--setup', help='install all required dependencies for package (pip required) (True|False)', type=bool)

    args = parser.parse_args()

    if args.csv == None and args.console_print == None:
        # show help
        print("\n Argument Error : please use --csv or --console_print to select either or for output\n")
        subprocess.call("python main.py --help")

    else:
        # --setup true
        if(args.setup != None):
            subprocess.call("pip install lxml")
            subprocess.call("pip install BeautifulSoup4")
            subprocess.call("pip install requests")

        # pass args into function scrape_top_n.
        else:
            imdb_scrape.scrape_top_n(args)
