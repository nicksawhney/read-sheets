# read-sheets: a sheet music reading library
Very early stages, but I'm playing around with sheet music reading using the [deepscores dataset](https://tuggeluk.github.io/deepscores/
)

`mido.py` will eventually have some simple midi interfacing functions, and might also handle simpler file writing.

links I'm referring to as I work are in `notes`

## Midi module

```
❯ python midi.py -h
usage: midi.py [-h] [-f FNAME] [-s SNAME] [-m META]
               [--max_events MAX_EVENTS]

optional arguments:
  -h, --help            show this help message and exit
  -f FNAME, --fname FNAME
                        existing midi file name
  -s SNAME, --sname SNAME
                        json file save location (if omitted, will print to
                        stdout
  -m META, --meta META  inclusion of meta midi elements
  --max_events MAX_EVENTS
                        maximum midi events to transcribe
```

## Testing
testing is done with `pytest`. Make sure to install `pip install -e .` and install requirements.


## Model Architecture Ideas

### Deep Learning

Prediction goal: "midi events"
for now, manually set meta events

- 2d conv -> lstms -> predictions -> event output
- lstm good for remembering long-term tasks 

### Conventional
- decision tree for next event