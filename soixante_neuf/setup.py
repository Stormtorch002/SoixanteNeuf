from setuptools import setup, find_packages

VERSION = '1.0.0' 
DESCRIPTION = 'A package that gets waifus (or any posts) from a subreddit!'

setup(
        name="SoixanteNeuf", 
        version=VERSION,
        description=DESCRIPTION,
        packages=find_packages(),
        install_requires=['aiohttp'], 
)
