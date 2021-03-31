from setuptools import setup

setup(
    name='imdb-scraper',
    version='1.0.0',
    author='M.F Bothma',
    author_email='migal.bothma@gmail.com',
    packages=['imdbscrape'],
    scripts=['imdbscrape/__main__.py'],
    url='https://github.com/MigalBothma/imdba_python.git/',
    license='LICENSE.txt',
    description='Imdb top 250 scraper.',
    long_description=open('README.txt').read(),
    install_requires=[
        'requests>=2.20.0',
        'lxml==4.6.3',
        'BeautifulSoup4==4.7.0'
    ],
)
