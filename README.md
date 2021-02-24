# read-sheets: a sheet music reading library
Very early stages, but I'm playing around with sheet music reading using the [deepscores dataset](https://tuggeluk.github.io/deepscores/
)

`mido.py` will eventually have some simple midi interfacing functions, and might also handle simpler file writing.



links I'm referring to as I work are in `notes`

## Midi module

```
usage: midi.py [-h] [-f FNAME] [-s SNAME] [-m META]

optional arguments:
  -h, --help            show this help message and exit
  -f FNAME, --fname FNAME
                        existing midi file name
  -s SNAME, --sname SNAME
  -m META, --meta META
```

currently building testing for use with `pytest`
