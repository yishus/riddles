const fs = require("fs");

const input = fs
  .readFileSync(0, "utf8")
  .trim()
  .split("\n")
  .slice(1);

console.log(input.map((e, i) => `Case #${i + 1}: ${solve(e)}`).join("\n"));

function solve(str) {
  const chars = str.split("");
  let arr1 = Array.from(chars);
  let arr2 = Array(chars.length).fill("0");

  arr1 = arr1.map(x => (x === "4" ? "2" : x));
  chars.forEach((x, i) => {
    if (x === "4") {
      arr2[i] = "2";
    }
  });
  return `${arr1.join("")} ${removeLeadingZeros(arr2).join("")}`;
}

function removeLeadingZeros(arr) {
  let idx;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] !== 0) {
      idx = i;
      break;
    }
  }
  return idx ? arr.slice(idx) : arr;
}
