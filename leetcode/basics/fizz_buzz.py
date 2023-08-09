class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        array = [] # Initialize an empty array to store the result

        # Iterate through numbers from 1 to n (inclusive)
        for i in range(1, n+1):
            # If the current number is divisible by both 3 and 5, append "FizzBuzz"
            if i % 3 == 0 and i % 5 == 0:
                array.append("FizzBuzz")
            # If the current number is divisible by 3 (but not 5), append "Fizz"
            elif i % 3 == 0:
                array.append("Fizz")
            # If the current number is divisible by 5 (but not 3), append "Buzz"
            elif i % 5 == 0:
                array.append("Buzz")
            # If the current number is not divisible by 3 or 5, append the number itself as a string
            else:
                array.append(str(i))
                
        return array # Return the final result array


# https://leetcode.com/problems/fizz-buzz/description/