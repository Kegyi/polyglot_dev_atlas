#!/usr/bin/env python3
from dataclasses import dataclass
from typing import List, Dict
from concurrent.futures import ThreadPoolExecutor
import statistics
import sys

@dataclass
class Record:
    name: str
    score: int

class FileProcessor:
    def __init__(self, path: str):
        self.path = path

    def read_all(self) -> List[Record]:
        records: List[Record] = []
        with open(self.path, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                try:
                    name, s = [x.strip() for x in line.split(",", 1)]
                    score = int(s)
                    records.append(Record(name, score))
                except Exception:
                    continue
        return records


def average(scores: List[int]) -> float:
    return statistics.mean(scores) if scores else 0.0


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    fp = FileProcessor(path)
    try:
        records = fp.read_all()
        buckets: Dict[str, List[int]] = {}
        for r in records:
            buckets.setdefault(r.name, []).append(r.score)

        results = []
        with ThreadPoolExecutor() as ex:
            futures = {ex.submit(average, scores): name for name, scores in buckets.items()}
            for fut in futures:
                name = futures[fut]
                results.append((name, fut.result()))

        results.sort(key=lambda x: x[1], reverse=True)
        for name, avg in results:
            print(f"{name}: {avg:.2f}")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
