# Rotate 2D Matrix

This project provides a function to rotate an n x n 2D matrix 90 degrees clockwise.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The `rotate_2d_matrix` function in this project takes an n x n 2D matrix as input and rotates it 90 degrees clockwise. The rotation is performed in-place, meaning the original matrix is modified directly.

## Requirements

- Python 3.8.10 or higher

## Usage

To use the `rotate_2d_matrix` function, follow these steps:

1. Import the `rotate_2d_matrix` function from the `0-rotate_2d_matrix` module.
2. Create a 2D matrix as a list of lists, where each inner list represents a row of the matrix.
3. Call the `rotate_2d_matrix` function, passing the matrix as the argument.
4. The matrix will be rotated 90 degrees clockwise in-place. You can access the modified matrix directly.

```

Example:

```python
from rotate_2d_matrix import rotate_2d_matrix

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotate_2d_matrix(matrix)
print(matrix)

```
