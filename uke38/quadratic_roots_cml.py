#!/usr/bin/env python3

import sys
from quadratic_roots_input import quadratic

quad = quadratic(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
print(f"{quad[0]}, {quad[1]}")
