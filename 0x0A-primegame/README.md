#Prime Game


This program determines the winner of a game played by Maria and Ben. In the game, they take turns choosing a prime number from a set of consecutive integers starting from 1 up to and including n. The chosen number and its multiples are then removed from the set. The player who cannot make a move loses the game.

## Requirements

- Allowed editors: vi, vim, emacs
- Files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- All files must be executable
- Code should use the PEP 8 style (version 1.7.x)

## Usage

### Installation

No installation is required. Simply include the `isWinner` function in your Python project.

### Function Signature

```python
def isWinner(x, nums):
    """
    Determines the winner of the prime game based on the given number of rounds and sets of integers.

    Args:
        x (int): The number of rounds.
        nums (list): An array of integers representing n for each round.

    Returns:
        str: The name of the player who won the most rounds. If the winner cannot be determined, returns None.

    Raises:
        None

    Example:
        rounds = 3
        nums = [4, 5, 1]
        result = isWinner(rounds, nums)
        print(result)  # Output: "Ben"
    """
```

### Parameters

- `x` (int): The number of rounds to be played.
- `nums` (list): An array of integers representing n for each round. Each value in the list corresponds to the upper limit of the set of consecutive integers for that round.

### Return Value

The function returns the name of the player who won the most rounds. If the winner cannot be determined, the function returns None.

### Example

```
rounds = 3
nums = [4, 5, 1]
result = isWinner(rounds, nums)
print(result)  # Output: "Ben"
```

## Game Rules

- Maria always goes first, and both players play optimally.
- In each round, Maria and Ben take turns choosing a prime number from the set of consecutive integers starting from 1 up to and including n.
- The chosen number and its multiples are then removed from the set.
- The player who cannot make a move loses the game.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

