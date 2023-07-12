# Diagonal Difference

Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix arr is shown below:

1 2 3<br/>
4 5 6<br/>
9 8 9<br/>
<br/>
The left-to-right diagonal = 1 + 5 + 9 = 15. The right to left diagonal = 3 + 5 + 9 = 17. Their absolute difference is |15 - 17| = 2.
<br/>

## Function description

Complete the diagonalDifference function in the editor below.

diagonalDifference takes the following parameter:

&#x2022; int arr[n][m]: an array of integers

### Return

&#x2022; int: the absolute diagonal difference

### Input Format

The first line contains a single integer, n, the number of rows and columns in the square matrix arr.<br/>
Each of the next n lines describes a row, arr[i], and consists of n space-separated integers arr[i][j].

## Constraints

### Output Format

Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

#### Sample Input

3<br/>
11 2 4<br/>
4 5 6<br/>
10 8 -12<br/>

#### Sample Output

<b>15</b>
