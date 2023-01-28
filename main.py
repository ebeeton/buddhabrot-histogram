#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd

def main():
    data = []
    with open('counter.txt') as f:
        data = [int(line.strip()) for line in f]

    minVal = min(data)
    maxVal = max(data)

    print(f'Min: {minVal} Max: {maxVal}')

    counts = pd.Series(data)
    counts.plot.hist(grid=True, bins=50, color='#b434eb',
                     range=[minVal, maxVal])
    plt.savefig('histogram')

if __name__ == '__main__':
    main()
