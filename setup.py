from distutils.core import setup

setup(
    name='imdb-scraper',
    version='1.0.0',
    author='M.F Bothma',
    author_email='migal.bothma@gmail.com',
    packages=['imdbscrape'],
    scripts=['bin/imdbscrape.py'],
    url='https://github.com/MigalBothma/imdba_python.git/',
    license='LICENSE.txt',
    description='Imdb top 250 scraper.',
    long_description=open('README.txt').read(),
    install_requires=[
        "BeautifulSoup4 >= 4.7.0",
        "requests == 2.8",
        "lxml == 4.3.3"
    ],
)
