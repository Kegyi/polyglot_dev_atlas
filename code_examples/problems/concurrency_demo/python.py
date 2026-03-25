#!/usr/bin/env python3
from concurrent.futures import ThreadPoolExecutor

def partial_sum(slice_data):
    return sum(slice_data)

def main():
    n = 1000
    data = list(range(1, n+1))
    threads = min(8, max(1, len(data) // 100))
    chunk = len(data) // threads
    chunks = [data[i*chunk:(i+1)*chunk] for i in range(threads-1)]
    chunks.append(data[(threads-1)*chunk:])
    with ThreadPoolExecutor(max_workers=threads) as ex:
        results = list(ex.map(partial_sum, chunks))
    print("Total:", sum(results))

if __name__ == "__main__":
    main()
