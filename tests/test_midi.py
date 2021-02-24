import json
from read_sheets import midi
from contextlib import redirect_stdout




def test_midi_json():
	test_out_path = 'tests/test_output.json'
	midi_obj = midi.read('os-bass.mid', 
					meta=False, 
					max_events=10,
					save_file=test_out_path)

	assert midi_obj

	with open(test_out_path, 'r') as f:
		midi_json = json.load(f)

	assert len(midi_json) == 10


def test_meta_included():
	test_out_path = 'tests/test_output.json'
	midi_obj = midi.read('os-bass.mid', 
					meta=True, 
					max_events=10,
					save_file=test_out_path)

	with open(test_out_path, 'r') as f:
		midi_json = json.load(f)

	for item in midi_json:
		assert "is_meta" in midi_json[item]