"""
TODO
- get input
- initialize counter for times 0 is passed
- starts at 50
- read text file line by line
- parse line: R or L
    - R means increase, L means decrease
- what can happen?
    - cal


"""
import typing

# Start at 50
DIAL_POSITION: int = 50
ZERO_COUNTER: int = 0
# Account for the range 0-100 rather than 1 to 100
OFFSET = 1
