#!/usr/bin/env python3
"""Blockly Games: Gallery Admin Delete

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

"""Delete a gallery record.
"""

__author__ = "blocklygames@neil.fraser.name (Neil Fraser)"

import cgi_utils
import os
import re

# Called with two arguments:
# - app: turtle/movie/music
# - key: Name of record.


forms = cgi_utils.parse_post()
cgi_utils.force_exist(forms, "app", "key")
app = forms["app"] or ""
key = forms["key"] or ""

print("Content-Type: text/plain")
if not re.match(r"[-\w]+", app):
  # Don't scanning "../../etc/passwd"
  print("Status: 406 Not Acceptable\n")
  print("That is not a valid directory.")
elif key and not re.match(r"\w+", key):
  # Don't escape from this directory
  print("Status: 406 Not Acceptable\n")
  print("That is not a valid key.")
else:
  print("Status: 200 OK\n")
  dir = cgi_utils.get_dir(app)
  file_name = dir + key + ".gallery"
  if os.path.exists(file_name):
    os.remove(file_name)
    print("Deleted")
  else:
    print("Record not found")
