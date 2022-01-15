from setuptools import setup, find_packages


setup(name="MusicMarket", \
    version="1.0", \
    packages=find_packages() + \
        find_packages(where="./market_app/forms") + \
        find_packages(where="./market_app/models") + \
        find_packages(where="./market_app/service") + \
        find_packages(where="./market_app/database") + \
        find_packages(where="./market_app/views"), \
    #packages=find_packages() + find_packages(where="./market_app"), \
    scripts=["execute.py"], \
    include_package_data=True, \
    package_data={"templates":["market_app/templates/*"],"static":["market_app/static/*"]})
