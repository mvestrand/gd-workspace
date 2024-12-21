#! /usr/bin/env python3

import sys
import os
import subprocess
import itertools
import shlex
import logging
from enum import StrEnum, Enum, unique

godot_path = "thirdparty/godot"
profile_path = "../../profiles/editor.py"


def main():
    compile_cmd = f"scons -j4 profile={profile_path}"
    process = subprocess.run(shlex.split(compile_cmd), cwd=godot_path)




if __name__ == "__main__":
    main()