interface Prototype<T> {
  clone(): T;
}

class Report implements Prototype<Report> {
  constructor(
    public readonly title: string,
    public readonly tags: string[],
  ) {}

  clone(): Report {
    return new Report(this.title, [...this.tags]);
  }
}

const template = new Report('weekly', ['ops', 'summary']);
const copy = template.clone();

console.log(template);
console.log(copy);