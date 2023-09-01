#!/usr/bin/python3

import sys;
import os;

def main():
  if len(sys.argv) != 2:
    print(f"Usage: { sys.argv[0] } <FILENAME>");
    sys.exit(0);

  fname = sys.argv[1];

  if os.path.isfile(fname) == False:
    print(f"{ fname }: file not found");
    sys.exit(1);

  limit32 = 2**32;

  with open(fname, "rb") as f:
    data = f.read();

    ln = len(data);

    counter = 0;
    offset = 0;

    padding = 8 if ln <= limit32 else 16;
    lineWidth = padding + 2 + 23 + 2 + 23 + 2 + 18;

    print(f"{offset:0{padding}x}  ", end="");

    chars = [ -1 ] * 16;

    for i in range(ln):
      hexNum = f"{data[i]:02x}".upper();

      if (data[i] >= 32 and data[i] < 128):
        chars[counter] = data[i];
      else:
        chars[counter] = -1;

      print(f"{ hexNum } ", end="");

      counter += 1;
      offset += 1;

      if (counter == 8):
        print(" ", end="");

      if (counter == 16):
        print(" ", end="");
        print("|", end="");
        for item in chars:
          ch = "." if item == -1 else chr(item);
          print(f"{ ch }", end="");
        print("|", end="");
        print("");
        print(f"{offset:0{padding}x}  ", end="");
        counter = 0;

    if (counter > 0):
      additionalSpaces = lineWidth - 18 - (counter * 2 + (counter - 1)) - padding - 3;
      spaces = " " * additionalSpaces;
      print(f"{ spaces }", end="");
      print("|", end="");
      for i in range(counter):
        ch = "." if chars[i] == -1 else chr(chars[i]);
        print(f"{ ch }", end="");

      print("|", end="");

###############################################################################

if __name__ == "__main__":
  try:
    main();
  except:
    pass;
