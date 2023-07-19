# Breaking the Records

Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.

### Example

<code>scores = [12, 24, 10, 24]</code>

Scores are in the same order as the games played. She tabulates her results as follows:

<code>                                     Count</code><br/>
<code>    Game  Score  Minimum  Maximum   Min Max</code><br/>
<code>     0      12     12       12       0   0</code><br/>
<code>     1      24     12       24       0   1</code><br/>
<code>     2      10     10       24       1   1</code><br/>
<code>     3      24     10       24       1   1</code><br/>
Given the scores for a season, determine the number of times Maria breaks her records for most and least points scored during the season.

## Function Description

Complete the breakingRecords function in the editor below.

breakingRecords has the following parameter(s):

- int scores[n]: points scored per game

### Returns

- int[2]: An array with the numbers of times she broke her records. Index 0 is for breaking most points records, and index 1 is for breaking least points records.

### Input Format

The first line contains an integer n, the number of games.<br/>
The second line contains n space-separated integers describing the respective values of score0, score1, ... , score(n-1).

### Constraints

- <code>1 <= n <= 1000</code>
- <code>0 <= scores[i] <= 10⁸</code>