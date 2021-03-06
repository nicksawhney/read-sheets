#!/usr/bin/env python3

'''
Nick Sawhney
a midi processing library, for eventual use with tensorflow
'''

import mido
import argparse
import sys
import json

from contextlib import redirect_stdout


def print_message(message, meta):
	print('{')
	mvars = vars(message)
	for attr in vars(message):
		m_attr = mvars[attr]

		if type(m_attr) is str:
			m_attr = f'"m_attr"'

		print(f'\t"{attr}": "{mvars[attr]}",')

	if meta:
		print(f'\t"is_meta": "{message.is_meta}",')

	print('},')
		

def read(midi_in, meta=False, max_events=None, save_file=None, **kwargs):
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

	midi_obj = {}

	track = mid_f.tracks[0]

	for idx, message in enumerate(track):
		if idx >= max_events:
			break

		midi_obj[idx] = {}

		mvars = vars(message)
		for attr in vars(message):
			midi_obj[idx][attr] = mvars[attr]


		if meta:
			midi_obj[idx]['is_meta'] = message.is_meta

		

	if save_file:
		with open(save_file, 'w+') as f:
			json.dump(midi_obj, f)

	else:
		print(json.dumps(midi_obj, indent=4))



	# print('"midi:"', end=' ')	
	# for track in mid_f.tracks:
	# 	c = 0
	# 	for message in track:
	# 		print_message(message, meta)	

	# 		if max_events and c > max_events:
	# 			break

	return mid_f


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--fname', default='os-bass.mid', help='existing midi file name')
	parser.add_argument('-s', '--sname', default=None, help='json file save location (if omitted, will print to stdout')
	parser.add_argument('-m', '--meta', action='store_true', default=False, help='inclusion of meta midi elements')
	parser.add_argument('--max_events', default=None, type=int, help='maximum midi events to transcribe')

	args = parser.parse_args()

	mid = read(
		args.fname, 
		meta=args.meta, 
		max_events=args.max_events,
		save_file=args.sname)

