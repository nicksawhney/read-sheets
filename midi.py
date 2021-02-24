'''
Nick Sawhney
a midi processing library, for eventual use with tensorflow
'''

import mido
import argparse
import sys

from contextlib import redirect_stdout


def print_message(message, meta):
	if meta:
		print(f'{str(vars(message))[:-1]}, is_meta: {message.is_meta}', end='')
		print('},')
	else:
		print(f'{vars(message)},')

def read(midi_in, meta=False, save_file=False, **kwargs):
	'''
	prints midi file information, optionally saving 
	only testing on single track midi for now

	midi_in: the name of a midi file or a bytes file object
			 representing midi
	save: filename to save to (optional)
	kwargs: mido.MidiFile keyword args

	returns mido midi file object
	'''
	if type(midi_in) is str:
		mid_f = mido.MidiFile(filename=midi_in, **kwargs)

	else:
		mid_f = midi_in

	print('{')
	print(f'tracks: {len(mid_f.tracks)},')

	c = 0
	for track in mid_f.tracks:
		for message in track:
			print_message(message, meta)	

			# for debug purposes
			c += 1
			if c > 10:
				break
	print('}')
	return mid_f


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--fname', default='os-bass.mid', help='existing midi file name')
	parser.add_argument('-s', '--sname', default=None)
	parser.add_argument('-m', '--meta', default=False)

	args = parser.parse_args()

	if args.sname:
		with open(args.sname, 'w+') as f:
			with redirect_stdout(f):
				mid = read(args.fname, meta=args.meta)

	else:
		mid = read(args.fname, meta=args.meta)

