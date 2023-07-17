# Apple And Orange

Sam's house has an apple tree and an orange tree that yield an abundance of fruit. Using the information given below, determine the number of apples and oranges that land on Sam's house.

In the diagram below:

- The red region denotes the house, where s is the start point, and t is the endpoint. The apple tree is to the left of the house, and the orange tree is to its right.
- Assume the trees are located on a single point, where the apple tree is at point , and the orange tree is at point .
- When a fruit falls from its tree, it lands d units of distance from its tree of origin along the x-axis. *A negative value of d means the fruit fell d units to the tree's left, and a positive value of d means it falls d units to the tree's right. *


<img src="../Appleandorange.png" title="Apple And Orange Illustration">



Given the value of d for m apples and n oranges, determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range [s,t])?

For example, Sam's house is between <code>s = 7</code> and <code>t = 10</code>. The apple tree is located at <code>a = 4</code> and the orange at <code>b = 12</code>. There are <code>m = 3</code> apples and <code>n = 3</code> oranges. Apples are thrown <code>apples = [2, 3, -4]</code> units distance from a, and <code>oranges = [3, -2, -4]</code> units distance. Adding each apple distance to the position of the tree, they land at <code>[ 4 + 2, 4 + 3, 4 + -4] = [6, 7, 0]</code>. Oranges land at <code>[12 + 3, 12 + -2, 12 + -4] = [15, 10, 8]</code>. One apple and two oranges land in the inclusive range <code>7 - 10</code> so we print
<code>
1
2
</code>

## Function Description

Complete the countApplesAndOranges function in the editor below. It should print the number of apples and oranges that land on Sam's house, each on a separate line.

countApplesAndOranges has the following parameter(s):

- s: integer, starting point of Sam's house location.
- t: integer, ending location of Sam's house location.
- a: integer, location of the Apple tree.
- b: integer, location of the Orange tree.
- apples: integer array, distances at which each apple falls from the tree.
- oranges: integer array, distances at which each orange falls from the tree.

### Input Format

The first line contains two space-separated integers denoting the respective values of s and t.
The second line contains two space-separated integers denoting the respective values of a and b.
The third line contains two space-separated integers denoting the respective values of m and n.
The fourth line contains m space-separated integers denoting the respective distances that each apple falls from point a.
The fifth line contains n space-separated integers denoting the respective distances that each orange falls from point b.

### Constraints

- <code>1 <= s,t,a,b,m,n <= 10⁵</code>
- <code>-10⁵ <= d <= 10⁵</code>
- <code>a < s < t < b</code>

### Output Format

Print two integers on two different lines:
<ol>
<li>The first integer: the number of apples that fall on Sam's house.</li>
<li>The second integer: the number of oranges that fall on Sam's house.</li>
</ol>