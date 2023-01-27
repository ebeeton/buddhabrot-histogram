#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd

def main():
    data = []
    with open('counter.txt') as f:
        data = [int(line.strip()) for line in f]

    counts = pd.Series(data)
    counts.plot.hist(grid=True, bins=50, rwidth=0.9, color='#4287f5')
    plt.savefig('histogram')

if __name__ == '__main__':
    main()
