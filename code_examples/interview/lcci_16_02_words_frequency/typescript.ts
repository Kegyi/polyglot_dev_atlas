class WordsFrequency {
    private readonly counter = new Map<string, number>();

    constructor(book: string[]) {
        for (const word of book) {
            this.counter.set(word, (this.counter.get(word) ?? 0) + 1);
        }
    }

    get(word: string): number {
        return this.counter.get(word) ?? 0;
    }
}

const wf = new WordsFrequency(["i", "have", "an", "apple", "he", "have", "a", "pen"]);
console.log(wf.get("have"));
console.log(wf.get("you"));
