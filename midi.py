'''
Nick Sawhney
a midi processing library, for eventual use with tensorflow
'''

import mido
import argparse

def save(messages, out_name: str):
	mid = mido.MidiFile(type=1)
	track = mido.MidiTrack()

	for message in messages:
		track.append(message)

	mid.save(out_name)

def read(in_name, save=False, **kwargs):
	'''
	in_name: the name of a config file

	returns mido midi file object
	'''

	mid_f = mido.MidiFile(in_name, **kwargs)

	print('midi attributes:')

	# for debug purposes
	for attribute in dir(mid_f):
		if not attribute.startswith('_'):
			print(attribute)

	return mid_f

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--fname', help='existing midi file name')

	args = parser.parse_args()

	mid = read(args.fname)





