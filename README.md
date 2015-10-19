# gpseatacart
Quick python hack to check cards against the artists attending GP Seattle/Tacoma

GPSTART.csv has the full list of all cards illustrated by artists attending the GP. It's pulled directly from Gatherer's "checklist" view, so it's a bit of a mess. Doesn't really matter, the script cleans up the output a bit.

This server runs on Flask. You can install flask using virtualenv:

```
$ virtualenv flask
New python executable in flask/bin/python
Installing setuptools............................done.
Installing pip...................done.
$ flask/bin/pip install flask
```

If you don't have virtualenv installed in your system, you can download it from https://pypi.python.org/pypi/virtualenv.

To run the server, you'll need to make artcheck.py an executable:

```
$ chmod a+x artcheck.py
$ ./artcheck.py
 * Running on http://0.0.0.0:5000/
 * Restarting with reloader
```

The server takes a list of cards via post at http://0.0.0.0:5000/query and returns a json array of all cards in that list with artists attending GP Seattle-Tacoma, including the matched printings. 
