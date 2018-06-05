'''
wtsize

Usage:
  wtsize URL
  wtsize URL [--unit=MiB]
  wtsize -h | --help
  wtsize --version

Options:
  -h --help                         Show this help
  --version                         Show version
  --unit=<byteunit>                 Multiple of binary byte unit; 'B', 'KiB', 'MiB', 'GiB', 'TiB'

Example:
  wtsize https://site.tld/some_big_file.zip

Help:
  https://github.com/davidhamann/wtsize
'''

import math
from docopt import docopt
import requests
from requests.exceptions import ConnectionError, SSLError
from . import __version__

def main():
    '''CLI entry point'''
    options = docopt(__doc__, version=__version__)
    return wtsize(options)

def wtsize(options):
    '''Fetches the HEAD of the given URL and outputs formatted size or error.'''
    url = options['URL']

    try:
        response = requests.head(url, allow_redirects=True)
    except (ConnectionError, SSLError):
        return 'Bad url, network connection funky or SSL verification error.'

    size = response.headers.get('Content-Length')
    if size:
        out = format_(int(size), options['--unit']) or 'Unknown size.'
    else:
        out = 'Unable to get file size (no Content-Length header).'

    return out

def format_(size, unit=None):
    '''Formats the size given as number of bytes

    Skip the unit argument to automatically choose the multiple of bytes.
    '''
    units = (
        'B',
        'KiB',
        'MiB',
        'GiB',
        'TiB',
        'PiB'
    )

    if unit and unit in units:
        n = units.index(unit)
    else:
        n = 0 if size == 0 else math.floor(math.log(size, 1024))

    try:
        unit = units[n]
    except IndexError:
        return ''

    out = round(size/1024**n, 2)

    return f'{out} {unit}'
