function reverseString(s: string[]): void {
  for (let i = 0; i < s.length / 2; i++) {
    const first = s[i];
    const last = s[s.length - 1 - i];
    s[i] = last;
    s[s.length - 1 - i] = first;
  }
  console.log(s);
}
const s = ["h", "e", "l", "l", "o"];
reverseString(s);
