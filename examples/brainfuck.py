#!/usr/bin/python
# Brainfuck Interpreter (Braceless - Wasn't needed for this project)

import sys
import string
from random import choice

symbols = ['.', ',', '<', '>', '+', '-']

class Brainfuck(object):

    def __init__(self):
        self.output = ""
        pass

    def evaluate(self, code):
      code = self.cleanup(list(code))

      cells, codeptr, cellptr = [0], 0, 0

      while codeptr < len(code):
        command = code[codeptr]

        if command == ">":
          cellptr += 1
          if cellptr == len(cells): cells.append(0)

        if command == "<":
          cellptr = 0 if cellptr <= 0 else cellptr - 1

        if command == "+":
          cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < 255 else 0

        if command == "-":
          cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > 0 else 255

        if command == ".": 
            try:
                self.output += chr(cells[cellptr])
            except Exception as e:
                pass
        if command == ",": cells[cellptr] = ord(choice(string.ascii_lowercase))
          
        codeptr += 1

    def cleanup(self, code):
      return filter(lambda x: x in ['.', ',', '<', '>', '+', '-'], code)

