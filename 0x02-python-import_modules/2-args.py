#!/usr/bin/python3
if __name__ == "__main__":
 from sys import argv
 size = len(argv) - 1
 print("{:d} {:s}{:s}".format(size,
                              "argument" if size <= 2 and size == 1
                              else "arguments",
                              ." if size == 0 else ":"))
 for a, s in enumerate(argv):
  if a > 0:
   print("{}: {}".format(a, s))
