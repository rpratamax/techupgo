"""Blockly Games: CGI Utilities

Copyright 2023 Google LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

"""Parse GET and POST data.
"""

__author__ = "blocklygames@neil.fraser.name (Neil Fraser)"

from os import environ
from urllib.parse import unquote
from sys import stdin


# Relative from both /scripts and /admin
DATA_PATH = "/bg-data"


# Return a data path for the given app and type.
# E.g. get_dir("turtle", "storage") -> "../data/turtle/storage/"
def get_dir(app, type):
  return "%s/%s/%s/" % (DATA_PATH, app, type)


# Parse POST data (e.g. a=1&b=2) into a dictionary (e.g. {"a": 1, "b": 2}).
# Very minimal parser.  Does not combine repeated names (a=1&a=2), ignores
# valueless names (a&b), does not support isindex or multipart/form-data.
def parse_post():
  return _parse(stdin.read())


# Parse a query string (e.g. a=1&b=2) into a dictionary (e.g. {"a": 1, "b": 2}).
# Very minimal parser.  Does not combine repeated names (a=1&a=2), ignores
# valueless names (a&b), does not support isindex.
def parse_query():
  return _parse(environ["QUERY_STRING"])


def _parse(data):
  parts = data.split("&")
  dict = {}
  for part in parts:
    tuple = part.split("=", 1)
    if len(tuple) == 2:
      dict[tuple[0]] = unquote(tuple[1])
  return dict


# Ensure that the provided arguments exist in the dict.
def force_exist(dict, *argv):
  for arg in argv:
    if arg not in dict:
      dict[arg] = None
