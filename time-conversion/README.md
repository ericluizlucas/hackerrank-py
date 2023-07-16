# Time Conversion

Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note:<br/>
- 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.<br/>
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

### Example

&#x2022; <b>s = '12:01:00PM'</b><br/>
Return '12:01:00'.

&#x2022; <b>s = '12:01:00AM'</b><br/>
Return '00:01:00'.

## Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

&#x2022; string s: a time in 12 hour format

### Returns

&#x2022; string: the time in 24 hour format

### Input Format

A single string s that represents a time in 12-hour clock format (i.e.: <code>hh:mm:ssAM</code> or <code>hh:mm:ssPM</code>).

### Constraints

&#x2022; All input times are valid