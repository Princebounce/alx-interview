# Change Comes from Within

This function calculates the fewest number of coins needed to meet a given amount total.

## Requirements

- Allowed editors: vi, vim, emacs
- Files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- All files must be executable
- Code should use the PEP 8 style (version 1.7.x)

## Usage

### Installation

No installation is required. Simply include the `makeChange` function in your Python project.

### Function Signature

```python
def makeChange(coins, total):
    """
    Calculates the fewest number of coins needed to meet the given amount total.

    Args:
        coins (list): A list of coin values.
        total (int): The target total amount.

    Returns:
        int: The fewest number of coins needed to meet the total, or -1 if it's not possible.

    Raises:
        None
```
    Example:
        coins = [1, 2, 5]
        total = 11
        result = makeChange(coins, total)
        print(result)  # Output: 3
    """
```Parameters

coins (list): A list of coin values. The value of each coin should be an integer greater than 0. You can assume you have an infinite number of each denomination of coin in the list.
total (int): The target total amount. If it is 0 or less, the function will return 0.
Return Value
The function returns the fewest number of coins needed to meet the total. If the total cannot be met by any combination of coins, the function returns -1.

Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License.
