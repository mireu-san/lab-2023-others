let weight = [60, 50, 55, 60, 77, 88, 56, 67, 89, 45, 55, 45];

weight.sort((a, b) => a - b);
let total = 0;
let count = 0;

for (const i of weight) {
  total += i;
  if (total >= 500) {
    break;
  }
  count += 1;
}

// max capacity : 9

// let weight = [60, 50, 55, 60, 77, 88, 56, 67, 89, 45, 55, 45];
// let total = 0;
// let count = 0;

// weight.sort((a, b) => a - b);

// for (let i = 0; i < weight.length; i++) {
//   if (total + weight[i] < 500) {
//     total += weight[i];
//     count++;
//   }
// }
// console.log("최대 정원: ", count);
