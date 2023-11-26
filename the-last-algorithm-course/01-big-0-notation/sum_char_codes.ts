// This is O(n) time
// because we iterate through the string

function sum_char_codes(n: string): number {
  let sum = 0;
  for (let i = 0; i < n.length; i++) {
    sum += n.charCodeAt(i);
  }
  return sum;
}

console.log(sum_char_codes("hello"));
