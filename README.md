TVD Plugin Template
===================

[TVD](http://tvd.niderb.fr) is a meta-data corpus for research purpose around multimedia analysis of TV series.  
Thanks to its plugin architecture, TVD can easily be extended to new TV series. 

## How to create a TVD plugin ##

1. Fork the [Github repository](http://github.com/tvd-dataset/tvd-plugin).
2. Clone your repository:  
   `$ git clone http://github.com/username/tvd-plugin`   
3. Edit `setup.py` (including `SERIES_NAME` variable).
4. Rename `SeriesName` directory to `${SERIES_NAME}`.
5. Edit `${SERIES_NAME}/__init__.py` Python file.  
6. Edit `${SERIES_NAME}/tvd.yml` YAML configuration file.  
7. Run `$ python setup.py update_files` to create `${SERIES_NAME}/_version.py` versioning file.  
8. Commit everything...  
   `$ git commit -a -m"Initial commit`
9. ... and add a [version tag](http://semver.org/).  
   `$ git tag -a 0.1`
10. Push everything to Github.  
   `$ git push --all --tags`

## How to test your TVD plugin ##

1. Start from a clean `virtualenv`  
   `$ virtualenv /tmp/tvd`
2. Install the latest version of `tvd`  
   `$ pip install tvd`
3. Install your plugin  
   `$ pip install -e /path/to/your/plugin/directory`
4. Use `tvd.create` script to download all resources  
   `$ python -m tvd.create /tmp/ ${SERIES_NAME}`
5. Check that everything was downloaded correctly in `/tmp/${SERIES_NAME}`

## How to update your TVD plugin ##

1. Apply your changes.  
2. Commit everything...  
   `$ git commit -a -m"Initial commit`
3. ... and update [version tag](http://semver.org/):  
   `git tag -a 0.2`
4. Push everything to Github.  
   `$ git push --all --tags`
