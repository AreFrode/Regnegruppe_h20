#!/usr/bin/env python3

import sys
try:
    C = float(sys.argv[1])
except:
    print("Please provide C as a command-line argument")
    sys.exit(1)

print(f"Successfully read the number {C} from the command-line")
