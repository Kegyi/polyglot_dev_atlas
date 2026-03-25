function sortStack(st: number[]): void {
  const tmp: number[] = [];
  while (st.length > 0) {
    const cur = st.pop()!;
    while (tmp.length > 0 && tmp[tmp.length - 1] > cur) {
      st.push(tmp.pop()!);
    }
    tmp.push(cur);
  }
  while (tmp.length > 0) {
    st.push(tmp.pop()!);
  }
}

function main(): void {
  const st = [3, 1, 4, 2];
  sortStack(st);
  console.log([...st].reverse().join(" "));
}

main();
