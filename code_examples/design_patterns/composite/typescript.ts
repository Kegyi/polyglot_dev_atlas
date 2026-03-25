interface Node {
  totalSize(): number;
}

class FileNode implements Node {
  constructor(private readonly size: number) {}

  totalSize(): number {
    return this.size;
  }
}

class Folder implements Node {
  private readonly children: Node[] = [];

  add(child: Node): void {
    this.children.push(child);
  }

  totalSize(): number {
    return this.children.reduce((sum, child) => sum + child.totalSize(), 0);
  }
}

const root = new Folder();
root.add(new FileNode(5));
const sub = new Folder();
sub.add(new FileNode(7));
sub.add(new FileNode(3));
root.add(sub);
console.log(root.totalSize());
