#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os

from tvdb_v5_unofficial import __Id__ as weavesId
from tvdb_v5_unofficial import TVDB, Config

from _NetrcConfig import NetrcConfigHandler

import json
import os
import sys

from _Pdb0 import Pdb0

import pdb


# from xml.etree.ElementTree import Element, SubElement, tostring

class Mock:
  _verbose = False

  def __init__(self, **kwargs):
    if "verbose" in kwargs:
      self._verbose = kwargs["verbose"]


  def search(self, *args, **kwargs):
    if self._verbose:
      print(f"Mock: {args} : {kwargs}", file=sys.stderr)

def fetch0(**kwargs):
  """
  Converts a Python dictionary (representing JSON data) to XML.

  Args:
  data: The Python dictionary to convert.

  Returns:
  str: The XML string.
  """

  if not "args" in Config.instance().kwargs:
    raise RuntimeError("no command-line arguments accessible")

  args = Config.instance().kwargs["args"]

  # You need to run this method first, before you can get any defaults.
  defaults0 = Config.defaults()

  classes0 = set([NetrcConfigHandler])
  r0 = Config.instance().factory.get_defaults_run(
    classes=classes0, key0="netrc"
  )
  kwargs0 = {"classes": classes0} | r0

  # Pdb0().trap0 = 5
  v0 = Config.handler(**kwargs0)
  if args.verbose:
    print(f"{args.prog}: handler: netrc: {v0.__class__.__name__}",
          file=sys.stderr)

  # Pdb0().trap0 = 7
  tvdb = Mock(verbose=args.verbose)
  if Config.instance().kwargs["args"].nodo:
    print(f"{args.prog}: nodo", file=sys.stderr)
  else:
    tvdb = TVDB(config_file=v0)

  # query terms
  qterms = { "language" : "eng", "limit" : 5, "type" : "series" }

  file_reader = Config.instance().line_reader(args.input_file)
  try:
    while True:
      qstr = next(file_reader)
      v0 = tvdb.search(qstr, **qterms)
      if not args.nodo:
        Config.instance().pickle1(v0)
  except StopIteration:
    pass

def parse_args():
  """
  Parses command-line arguments using argparse.

  Returns:
    Namespace: An object containing the parsed arguments.
  """
  parser = argparse.ArgumentParser(description="Process command-line arguments.")
  parser.add_argument(
    "-n", "--nodo", help="Enable/Disable nodo mode", action="store_true"
  )
  parser.add_argument(
    "-v", "--verbose", help="Display runtime messages", action="store_true"
  )
  parser.add_argument(
    "-f", "--input-file", required=True, help="Path to the input file"
  )
  parser.add_argument(
    "-o", "--output-file", required=False, help="Path to the output file"
  )

  args = parser.parse_args()

  # Check if input file exists
  if not os.path.isfile(args.input_file):
    parser.error(f"Input file '{args.input_file}' does not exist.")

  return args


if __name__ == "__main__":
  args = parse_args()
  args.prog = sys.argv[0] 

  Config.instance().kwargs["args"] = args

  # Access parsed arguments
  if args.nodo and args.verbose:
      print("{args.prog}: nodo mode enabled", file=sys.stderr)

  if args.verbose:
    print(f"{args.prog}: input file: {args.input_file}", file=sys.stderr)
    print(f"{args.prog}: output file: {args.output_file}", file=sys.stderr)

  fetch0()

  # Further processing based on the parsed arguments would go here...


# -*- coding: utf-8 -*-
# Local Variables:
# mode:python
# python-indent-offset: 2
# End:
