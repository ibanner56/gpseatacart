# gpseatacart
Quick python hack to check cards against the artists attending GP Seattle/Tacoma

For the code running on the backend of the web version, switch to the "server" branch.

----

GPSTART.csv has the full list of all cards illustrated by artists attending the GP. It's pulled directly from Gatherer's "checklist" view, so it's a bit of a mess. Doesn't really matter, the script cleans up the output a bit.

Put all cards you want to check for into "cards.txt" - there are a bunch in there already as an example of the format to use.

Output goes to the command line, so if you want to save the data use something like:
```
python artcheck.py > file
```

I threw this together last night, so it's not supposed to be pristine, just functional.

The output is produced as json, so you can use something like http://jsonlint.com/ to format it nicely.
