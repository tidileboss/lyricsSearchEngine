from setuptools import setup, find_packages

setup(
  name='lyricsSearchEngine',
  packages=find_packages(),
  version='0.1',
  description='A lyrics search engine from various sources on the internet',
  author='Tidiane Seri-Gnoleba',
  author_email='tidianeseri@gmail.com',
  url='https://github.com/tidileboss/lyricsSearchEngine',  # use the URL to the github repo
  download_url='https://github.com/tidileboss/lyricsSearchEngine/tarball/0.1',
  keywords=['lyrics', 'search'],  # arbitrary keywords
  classifiers=[],
  install_requires=[
          'beautifulsoup4',
          'html5lib',
          'requests',
      ]
)
