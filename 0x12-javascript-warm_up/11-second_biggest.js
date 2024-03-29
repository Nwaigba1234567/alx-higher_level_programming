#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const numbers = args.map(x => parseInt(x));
  const firstMax = Math.max(...numbers);
  const secondMax = Math.max(...numbers.filter(x => x < firstMax));
  console.log(secondMax);
}
