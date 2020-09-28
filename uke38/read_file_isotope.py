#!/usr/bin/env python3

infile = open("Oxygen.txt")
sum_: float = 0.;
infile.readline()
for line in infile.readlines():
    line = line.split()
    sum_ += float(line[1]) * float(line[2])

infile.close()
print(f"Molar mass of Oxygen: {sum_:6.4f}")
