#!/usr/bin/env ts-node
import { promises as fs } from 'fs';

async function main() {
    const path = process.argv[2] || 'data.txt';
    const text = await fs.readFile(path, 'utf8');
    const words = text.toLowerCase().match(/\b\w+\b/g) || [];
    const m = new Map<string, number>();
    for (const w of words) m.set(w, (m.get(w) || 0) + 1);
    const arr = Array.from(m.entries()).sort((a,b) => b[1] - a[1]);
    for (const [k,v] of arr) console.log(`${k}: ${v}`);
}

main().catch(e => { console.error('Error:', e); process.exit(1); });
