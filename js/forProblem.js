let weights = [60, 50, 55, 60, 77, 88, 56, 67, 89, 45, 55, 45];
let elevatorLimit = 500;
weights.sort((a, b) => a - b);

let totalWeight = 0;
let maxPersons = 0;

for (let i = 0; i < weights.length; i++) {
  if (totalWeight + weights[i] <= elevatorLimit) {
    totalWeight += weights[i];
    maxPersons++;
  } else {
    break;
  }
}

console.log("탑승 최대 정원: ", maxPersons);
