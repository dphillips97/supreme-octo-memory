import logging

START_DIAL_POSITION: int = 50
ZERO_COUNTER: int = 0

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def parse_instructions(line: str) -> int:
    """If first char is L, return negative number.
    If first char is R, return number itself

    Args:
        line (str): the instruction string, like "L42"

    Returns:
        action: Positive or negative integer, instruction for next action
    """
    line = line.strip()
    letter = line[0]
    number = int("".join(line[1:]))

    if letter == "L":
        action = -number
    else:
        action = number

    return action

def compute_result(position: int, action: int) -> int:
    """Account for offset. For instance, 99 + 1 equals 100 and
    100 mod 99 equals 1. But you're actually at position 0 so you
    have to subtract 1. Also, 1 - 2 = -1 and -1 mod 99 equals 98. 
    But you're actually at position 99.

    Args:
        position (int): Dial position
        num (int): action to take on position

    Returns:
        int: _description_
    """
    initial_result = position + action

    if initial_result > 99:
        compensate = -1 * initial_result % 99
    elif initial_result < 0:
        compensate = initial_result % 99
    else:
        compensate = 0
    
    updated_result = initial_result % 99
    
    return updated_result + compensate

def main():
    
    with open("downloads/input.txt") as f:
        dial_position = START_DIAL_POSITION
        zero_counter = 0
        logging.info(f"Dial position is {dial_position}")
        for line in f:

            action = parse_instructions(line)
            logging.info(f"Action is {action}")

            dial_position = compute_result(dial_position, action)
            logging.info(f"Dial position is now {dial_position}")

            if dial_position == 0:
                zero_counter += 1
                logging.info("Zero counter incremented.")

    print(f"\nSecret code is {zero_counter}")


if __name__ == "__main__":
    main()
    