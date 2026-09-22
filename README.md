# Move Zeros to the End of an Array

A Python program that rearranges an array so that all zero values are placed at the end while the non-zero elements retain their original order.

## Overview

The program separates the array into two logical parts:

1. Non-zero elements are collected in their existing order.
2. The remaining positions are filled with zeros.

The resulting values are then copied back into the original array.

## How It Works

The `move_zeroes()` method first records the size of the input array and creates an empty temporary list:

```python id="v9x8aw"
n = len(nums)
temp = []
```

It then scans every element and keeps only the non-zero values:

```python id="4q8qpd"
for num in nums:
    if num != 0:
        temp.append(num)
```

This preserves the relative order of the non-zero elements.

Once all non-zero values have been collected, zeros are appended until the temporary list reaches the original array length:

```python id="j4g9ip"
while len(temp) < n:
    temp.append(0)
```

Finally, the contents of `temp` are copied back into `nums`:

```python id="t4l8lq"
for index in range(n):
    nums[index] = temp[index]
```

## Example

The program uses:

```python id="6zq0ju"
nums = [0, 1, 0, 3, 12]
```

The non-zero values are collected as:

```text id="x7xq3k"
[1, 3, 12]
```

The remaining positions are filled with zeros:

```text id="nq5gq1"
[1, 3, 12, 0, 0]
```

The final array printed by the program is:

```text id="u7t2fc"
1 3 12 0 0
```

The sample input and execution are defined in the main section of the file.

## Algorithm

1. Determine the array length.
2. Create an empty temporary list.
3. Traverse the input array.
4. Add every non-zero value to the temporary list.
5. Append zeros until the temporary list reaches the original length.
6. Copy the temporary list back into the input array.

## Complexity

| Metric          | Complexity |
| --------------- | ---------- |
| Time            | O(N)       |
| Auxiliary Space | O(N)       |

The array is traversed and rewritten in linear time. The temporary list can contain up to `N` elements, resulting in linear additional space.

## Key Concept

The important part of this approach is that moving zeros does not require individually swapping every zero. Instead, the algorithm first preserves the useful values in order and then reconstructs the array with zeros occupying the remaining positions.

## Running the Program

Run the file with:

```bash
python "Move Zeros to the End of an Array.py"
```

Expected output:

```text
1 3 12 0 0
```
