const max_min_sum = (arr) => {
  const max = arr[0];
  const min = arr[0];
  const sum = 0;

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > max) {
      max = arr[i];
    }

    if (arr[i] < min) {
      min = arr[i];
    }

    sum += arr[i];
  }

  return [max, min, sum];
};

const arr = [10, 20, 30, 40];
const result = max_min_sum(arr);

console.log(result); // [40, 10, 100]

// let circleArea = (x) => Math.PI * x ** 2;

// using Math is recommended
// let f7 = (a, b, c, d) => {
//     max = Math.max(a, b, c, d)
//     min = Math.min(a, b, c, d)
//     sum = a + b + c + d
//     return [max, min, sum]
// }
