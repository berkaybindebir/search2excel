# Search 2 Excel

[![N|Solid](https://www.python.org/static/img/python-logo.png)](https://www.python.org/)


Search 2 Excel is a tool for converting your Google queries to the Excel table

  - Type some queries and let Search2Excel generates a document
  - How Many Google Results You Want? 1 Page, 2 Page maybe More..

# New Features!
 - There is No New Features Yet



### Requirements

Search2Excel uses these modules to work properly:

* [Click Cli](https://github.com/pallets/click) - Python composable command line interface toolkit
* [Google Search Api](https://github.com/abenassi/Google-Search-API) - Python based api for searching google web, images, calc, and currency conversion.
* [Xlsx Writer](https://xlsxwriter.readthedocs.io/) - XlsxWriter is a Python module for creating Excel XLSX files.


### Installation

Search2Excel requires [Python](https://www.python.org/) v3 to run.

Install the dependencies and devDependencies and start the server.

```sh
$ git clone link-goes-here
$ git install click
$ pip install XlsxWriter
$ pip install git+https://github.com/abenassi/Google-Search-API
```


### Usage

Open your favorite Terminal and run these commands.

example usage:
```sh
$ python3 app.py "Search Query Goes Here" --page="Page Count(Integer)"
```

You may Also Edit Base Directory & Base File Name
-
- /config.py


### Todos

 - Application Build
 - Write Test
 - Image and News Search

License
----

MIT
