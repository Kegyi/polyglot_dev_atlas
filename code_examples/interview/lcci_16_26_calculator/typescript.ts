function calculate(s: string): number {
    const st: number[] = [];
    let num = 0;
    let op = "+";
    for (let i = 0; i <= s.length; i++) {
        const ch = i < s.length ? s[i] : "+";
        if (ch === " ") continue;
        if (ch >= "0" && ch <= "9") {
            num = num * 10 + Number(ch);
            continue;
        }
        if (op === "+") st.push(num);
        else if (op === "-") st.push(-num);
        else if (op === "*") st.push(st.pop()! * num);
        else st.push(Math.trunc(st.pop()! / num));
        op = ch;
        num = 0;
    }
    return st.reduce((a, b) => a + b, 0);
}

console.log(calculate("3+2*2"));
console.log(calculate(" 3/2 "));
console.log(calculate(" 3+5 / 2 "));
