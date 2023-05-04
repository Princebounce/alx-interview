# Minimum Operations
In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

`Prototype: def minOperations(n)`
`Returns an integer`
`If n is impossible to achieve, return 0.

This is a classic problem known as the "2 Keys Keyboard" problem. To solve this, we need to use dynamic programming.

First, we can note that if n is a prime number, it's impossible to reach n H characters in the file. This is because the only way to create a new H character is by pasting, and pasting can only double the number of H characters in the file. Thus, we can never reach a prime number of H characters.

Next, we can create an array dp of size n+1 to keep track of the minimum number of operations needed to reach each number of H characters. Initially, we can set all values in the array to a large number, say, infinity.

Then, we can set dp[1] = 0, since we already have one H character in the file.

For each i from 2 to n, we can iterate over all divisors d of i (excluding 1 and i itself). For each divisor d, we can calculate the number of operations needed to reach i H characters from d H characters. This is simply the number of operations needed to copy all d H characters, plus the number of operations needed to paste (i/d - 1) times. We can then update dp[i] to be the minimum of its current value and the number of operations we just calculated.

Finally, we can return dp[n], which will give us the minimum number of operations needed to reach n H characters in the file.

Here's the Python code that implements this algorithm:

```
:D

```

The `is_prime` function is used to check whether a number is prime or not, and it's used to return 0 if n is prime. The `minOperations` function uses dynamic programming to calculate the minimum number of operations needed to reach n H characters in the file.`
