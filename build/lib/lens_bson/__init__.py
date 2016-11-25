import json

import bson
from  pygments.lexers.data import JsonLexer

from lens.parsers.base import LensParser

class Parser(LensParser):
    lexer = JsonLexer

    def treat(self, inpt, keys):
        loaded = bson.loads(bytes(inpt, "utf-8"))

        for key in keys:
            loaded = loaded[key]

        return json.dumps(loaded)
