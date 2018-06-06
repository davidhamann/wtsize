# WTSize

On the road with a limited data plan or bad network and want to know if it's safe to download a particular remote file? WTSize (what the size) is a small Python 3 CLI app which checks the size of remote files without downloading them (by looking at the Content-Length header).

```
>>> wtsize https://site.tld/some_big_file.zip
822.24 MiB
```

## Usage

```
wtsize URL
wtsize URL [--unit=MiB]
wtsize -h | --help
wtsize --version
```

## Install

```
pip install wtsize
```

## Limitations

- Not all servers return a Content-Length header so you might be unable to get the actual file size without, well, downloading the file. `wtsize` will tell you if that's the case.
- In some cases the Content-Length cannot be known before accessing the body (dynamic content)
- Headers can easily be spoofed. Generally, though, there's a good chance that the Content-Length header in the server response is accurate.
