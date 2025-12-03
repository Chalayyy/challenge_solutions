"""
The problem:
Given an alphabet string, convert it into braille (represented by a 
6 digit string of 1's and 0's representing real world bumps and flats, 
respectively). Capital letters and spaces should be taken into consideration.

The solution:
Create a dictionary between each letter (and space and capitalization) 
and its braille counterpart. For each value in a string, use the dictionary 
to output its braille counterpart (adding the capitalization when necessary).
"""

def braille_translater(s):

	braille_dict = {
		# dictionary for conversion between alphabet and braille
		"a": "100000",
		"b": "110000",
		"c": "100100",
		"d": "100110",
		"e": "100010",
		"f": "110100",
		"g": "110110",
		"h": "110010",
		"i": "010100",
		"j": "010110",
		"k": "101000",
		"l": "111000",
		"m": "101100",
		"n": "101110",
		"o": "101010",
		"p": "111100",
		"q": "111110",
		"r": "111010",
		"s": "011100",
		"t": "011110",
		"u": "101001",
		"v": "111001",
		"w": "010111",
		"x": "101101",
		"y": "101111",
		"z": "101011",
		" ": "000000",
		"cap": "000001"
		}

	output = []
	for char in s:
		if char in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
			output.append(braille_dict["cap"])
		output.append(braille_dict[char.lower()])
	return "".join(output)

