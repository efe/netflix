# netflix

[![Build Status](https://travis-ci.org/efe/netflix.svg?branch=master)](https://travis-ci.org/efe/netflix) [![pypi](https://img.shields.io/pypi/v/netflix.svg)](https://pypi.org/project/netflix/)

A Python client for Netflix.

## Documentation

### Netflix ID

- **Movie**: The Intern
- **URL**: `https://www.netflix.com/watch/80047616`
- **Netflix ID**: `80047616`

### Movie

```python
from netflix import Movie

movie = Movie("80047616")
print(movie.name)  # 'The Intern'
```

#### Attributes

- `name`: `'The Intern'`
- `genre`: `'Comedies'`
- `description`: `'Harried fashion entrepreneur Jules gets a surprise boost from Ben, a 70-year-old widower who answers an ad seeking a senior intern.'`
- `image_url`: `'https://occ-0-2774-2773.1.nflxso.net/dnm/api/v6/6AYY37jfdO6hpXcMjf9Yu5cnmO0/AAAABW8TwHJmfYqEjUj0YK4Y2ugq-sKIN-Gi8OBaDjOh3SbRSBdbEXlmpWEpHTbrO2CLDdo7yxRl7MTm5YtYa1-71Kg1o-7o.jpg?r=2ce'`
- `metadata`

### TVShow

```python
from netflix import TVShow

tv_show = TVShow("80192098")
print(tv_show.name)  # 'Money Heist'
```

#### Attributes

- `name`: `'Money Heist'`
- `genre`: `'TV Thrillers'`
- `description`: `'Eight thieves take hostages and lock themselves in the Royal Mint of Spain as a criminal mastermind manipulates the police to carry out his plan.'`
- `image_url`: `'https://occ-0-2774-2773.1.nflxso.net/dnm/api/v6/6AYY37jfdO6hpXcMjf9Yu5cnmO0/AAAABRQ7vD9Tg2GJUxLlWRw85C9Ln3j_m3dMvVhpf-LAJLDg9JNVsQKRyqvwlH28uoYY_gW7ROp1CI1PYdkBIlJwxpB8_VzK.jpg?r=8f1'`
- `metadata`

### Extra

#### Fetch Instantly

Default is `True`

```python
from netflix import Movie

movie = Movie("80047616", fetch_instantly=False)

# Do something.

movie.fetch()
```

#### Metadata

```python
from netflix import Movie

movie = Movie("80047616")

print(movie.metadata)
"""
{
  '@context': 'http://schema.org',
  '@type': 'Movie',
  'url': 'https://www.netflix.com/tr-en/title/80047616',
  'contentRating': '16+',
  'name': 'The Intern',
  'description': 'Harried fashion entrepreneur Jules gets a surprise boost from Ben, a 70-year-old widower who answers an ad seeking a senior intern.',
  'genre': 'Comedies',
  'image': 'https://occ-0-2773-2774.1.nflxso.net/dnm/api/v6/6AYY37jfdO6hpXcMjf9Yu5cnmO0/AAAABW8TwHJmfYqEjUj0YK4Y2ugq-sKIN-Gi8OBaDjOh3SbRSBdbEXlmpWEpHTbrO2CLDdo7yxRl7MTm5YtYa1-71Kg1o-7o.jpg?r=2ce',
  'dateCreated': '2019-8-31',
  'actors': [{
    '@type': 'Person',
    'name': 'Robert De Niro'
  }, {
    '@type': 'Person',
    'name': 'Anne Hathaway'
  }, {
    '@type': 'Person',
    'name': 'Rene Russo'
  }, {
    '@type': 'Person',
    'name': 'Anders Holm'
  }, {
    '@type': 'Person',
    'name': 'JoJo Kushner'
  }, {
    '@type': 'Person',
    'name': 'Andrew Rannells'
  }, {
    '@type': 'Person',
    'name': 'Adam Devine'
  }, {
    '@type': 'Person',
    'name': 'Zack Pearlman'
  }, {
    '@type': 'Person',
    'name': 'Jason Orley'
  }, {
    '@type': 'Person',
    'name': 'Christina Scherer'
  }],
  'creator': [],
  'director': [{
    '@type': 'Person',
    'name': 'Nancy Meyers'
  }]
}
"""
```
