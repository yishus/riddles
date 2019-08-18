// not for lasrge numbers

const fs = require("fs");

const input = fs
  .readFileSync(0, "utf8")
  .trim()
  .split("\n")
  .slice(1)
  .filter((_, i) => i % 2 !== 0);

console.log(input.map((e, i) => `Case #${i + 1}: ${solve(e)}`).join("\n"));

function solve(str) {
  const chars = str.split(" ").map(x => parseInt(x, 10));

  let common = chars.map((x, i) => {
    if (i < chars.length - 1) {
      return gcd(x, chars[i + 1]);
    }

    return null;
  });
  common.unshift(chars[0] / common[0]);
  common[common.length - 1] =
    chars[chars.length - 1] / common[common.length - 2];
  const sorted = [...common];
  sorted.sort((a, b) => a - b);

  let charCount = -1;
  const map = sorted.reduce((acc, curr) => {
    if (acc[curr] == null) {
      charCount++;
      return {
        ...acc,
        [curr]: String.fromCharCode(65 + charCount)
      };
    }

    return acc;
  }, {});

  return common.map(x => map[`${x}`]).join("");
}

function gcd(a, b) {
  if (a > b) {
    const r = a % b;
    if (r === 0) {
      return b;
    }
    return gcd(r, b);
  } else {
    const r = b % a;
    if (r === 0) {
      return a;
    }
    return gcd(r, a);
  }
}
