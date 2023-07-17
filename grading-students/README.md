# Grading Students

HackerLand University has the following grading policy:

- Every student receives a <b>grade</b> in the inclusive range from 0 to 100.
- Any <b>grade</b> less than 40 is a failing grade.

Sam is a professor at the university and likes to round each student's <b>grade</b> according to these rules:

If the difference between the <b>grade</b> and the next multiple of 5 is less than 3, round <b>grade</b> up to the next multiple of 5.<br/>
If the value of <b>grade</b> is less than 38, no rounding occurs as the result will still be a failing grade.

### Examples

- <b>grade</b> = 84 round to 85 (85 - 84 is less than 3)
- <b>grade</b> = 29 do not round (result is less than 40)
- <b>grade</b> = 57 do not round (60 - 57 is 3 or higher)
Given the initial value of <b>grade</b> for each of Sam's n students, write code to automate the rounding process.

## Function Description

Complete the function gradingStudents in the editor below.

gradingStudents has the following parameter(s):

- int grades[n]: the grades before rounding

### Returns

- int[n]: the grades after rounding as appropriate

### Input Format

The first line contains a single integer, n, the number of students.<br/>
Each line i of the n subsequent lines contains a single integer, grades[i].

### Constraints

- 1 <= n <= 100<br/>
- 0 <= grades[i] <= 100