#!/usr/bin/env python3

import numpy as np
from fill_log_arrays_loop import f

if __name__ == "__main__":
    x = np.linspace(1, 10, 101, endpoint=True)
    y = f(x)

    print(y[-1])
