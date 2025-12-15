from typing import List
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

FILEPATH = "downloads/p2_input.txt"

def parse_input():
    with open(FILEPATH, "r") as f:
        return f.read().split(",")

def extract_range_params(str_range: str):
    range_params = [int(i) for i in str_range.split("-")]
    start = range_params[0]
    stop = range_params[1] + 1

    return start, stop

def nums_to_range_list(start: int, stop: int) -> List[int]:
    return [i for i in range(start, stop)]

def count_digits(num: int):
    return len(str(num))

def check_if_palindrome(num_to_check: int, num_digits: int):
    num_as_str = str(num_to_check)

    # There are just 9 2-digit palindromes, avoid extra calculations
    if num_digits == 2:
        two_digit_palindromes = [x*11 for x in range(1, 10)]

        if num_to_check in two_digit_palindromes:
            logging.debug(f"{num_to_check} is a palindrome.")
            return True

    elif num_digits > 2 and num_digits % 2 == 0:
        
        split_at_idx = int((num_digits - 2) / 2) + 1

        first_part = num_as_str[:split_at_idx]
        second_part = num_as_str[split_at_idx:]

        # Cast as ints to remove leading zeroes: 01 is not a palindrome of 10
        if int(first_part) == int(second_part):
            logging.debug(f"{num_to_check} is a palindrome.")
            return True


def main():

    running_total = 0
    all_text = parse_input()
    for the_range in all_text:
        start, stop = extract_range_params(the_range)
        nums_to_check = nums_to_range_list(start, stop)
        for i in nums_to_check:
            num_digits = count_digits(i)
            if check_if_palindrome(i, num_digits) == True:
                running_total += i
    print(running_total)

if __name__ == "__main__":
    main()