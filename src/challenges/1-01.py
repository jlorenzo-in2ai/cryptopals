"""https://cryptopals.com/sets/1/challenges/1"""

from src.utils import hex_to_base64

INPUT=b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
VALID_OUTPUT=b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

assert hex_to_base64(INPUT)==VALID_OUTPUT, "TRY AGAIN!"

#run with python -m src.challenges.1-01