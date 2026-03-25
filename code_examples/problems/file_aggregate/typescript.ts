#!/usr/bin/env ts-node
import * as fs from "fs/promises";

type Record = { name: string; score: number };

class FileProcessor {
    path: string;
    constructor(path: string) {
        this.path = path;
    }

    async readAll(): Promise<Record[]> {
        const text = await fs.readFile(this.path, { encoding: "utf8" });
        const out: Record[] = [];
        for (const raw of text.split(/\r?\n/)) {
            const line = raw.trim();
            if (!line || line.startsWith("#")) continue;
            const parts = line.split(",", 2);
            if (parts.length < 2) continue;
            const name = parts[0].trim();
            const score = Number(parts[1].trim());
            if (Number.isNaN(score)) continue;
            out.push({ name, score });
        }
        return out;
    }
}

function average(nums: number[]): number {
    if (nums.length === 0) return 0;
    return nums.reduce((a, b) => a + b, 0) / nums.length;
}

async function main() {
    const path = process.argv[2] || "data.txt";
    try {
        const fp = new FileProcessor(path);
        const records = await fp.readAll();
        const buckets = new Map<string, number[]>();
        for (const r of records) {
            if (!buckets.has(r.name)) buckets.set(r.name, []);
            buckets.get(r.name)!.push(r.score);
        }

        const promises: Promise<[string, number]>[] = [];
        for (const [name, scores] of buckets.entries()) {
            promises.push(Promise.resolve([name, average(scores)]));
        }
        const results = (await Promise.all(promises)).sort((a, b) => b[1] - a[1]);
        for (const [name, avg] of results) {
            console.log(`${name}: ${avg.toFixed(2)}`);
        }
    } catch (err) {
        console.error("Error:", err);
        process.exit(1);
    }
}

main();
