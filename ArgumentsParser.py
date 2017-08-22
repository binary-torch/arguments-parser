"""
Binary Torch Sdn. Bhd.
"""

import argparse

class ArgumentsParser:
    def __init__(self):
        self.ap = argparse.ArgumentParser()

    def setup(self, args):
    	for arg in args:
    		name 	= arg["name"]
    		help 	= arg["help"]
    		required = arg["required"]
    		self.ap.add_argument("--" + name, required=required, help=help)
        return vars(self.ap.parse_args())