#!/usr/bin/env python3

from typing import Sequence
import matplotlib.pyplot as plt

def plot_line(p1: Sequence[float], p2: Sequence[float]) -> None:
    plt.plot([p1[0],p2[0]], [p1[1],p2[1]], marker='o',markerfacecolor="r",  color='blue')

def complete_graph(points: Sequence[Sequence[float]]) -> None:
    for i in range(len(points)):
        for j in points[i+1:]:
            plot_line(points[i], j)

if __name__ == "__main__":
    plt.figure()
    complete_graph(((0,0),(1,0),(0,1),(1,1)))
    
    plt.figure()
    a: float = 0.5*(2.**(0.5))
    complete_graph(((1,0),(a,a),(0,1),(-a,a),(-1,0),(-a,-a),(0,-1),(a,-a)))
    plt.show()
