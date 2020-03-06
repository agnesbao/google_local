# Introduction to Recommendation System with Google Local data
----
The goal of this project is to review fundamental methods and algorithms of recommendation systems using [Google Local data](http://cseweb.ucsd.edu/~jmcauley/datasets.html#google_local)

This project is written in python 3. Dependencies are in `requirements.txt`

Notes about non-interesting data preprocessing scripts:
- `write_csv.py`: convert raw .json.gz to csv file
- `subset_place_data.py`: subset places with center gps coord and a degree range
- `subset_review_data.py`: subset reviews based on output of `subset_place_data.py`