"""Util functions used across the challenges."""

import binascii
import base64

def hex_to_base64(string:str):
    return base64.b64encode(binascii.unhexlify(string))