import re
import logging

from sequence import sequence_print
from constant import (OUTWARD_CODE_PATTERNS,
                      INWARD_CODE_PATTERN,
                      SINGLE_DIGIT_DISTRICT_AREAS,
                      DOUBLE_DIGIT_DISTRICT_AREAS,
                      ZERO_DISTRICT_AREAS
                      )

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def format_postcode(postcode: str):
    formatted = postcode.upper().replace("-", "").replace(" ", "")
    return "{} {}".format(formatted[:-3], formatted[-3:]) if len(formatted) > 3 else formatted


def postcode_verify(postcode: str):
    postcode = format_postcode(postcode)
    if not 6 <= len(postcode) <= 8:
        raise ValueError(
            f"Not valid. Postcode length must be between 6 and 8 characters. '{postcode}' got {len(postcode)}")

    outward_code, inward_code = postcode.split()
    outward_code_verify(outward_code)
    inward_code_verify(inward_code)
    return f"Postcode is valid: {postcode}"


def outward_code_verify(outward_code: str):
    for name, pattern in OUTWARD_CODE_PATTERNS.items():
        if re.match(pattern, outward_code):
            area = outward_code[:2]
            match name:
                case "AA9":
                    if area in DOUBLE_DIGIT_DISTRICT_AREAS:
                        raise ValueError(f"Not valid. The area '{area}' has only a double digit districts")
                    if outward_code[-1] == "0" and area not in ZERO_DISTRICT_AREAS:
                        raise ValueError(f"Not valid. The area '{area}' could not be a zero district area")
                case "AA99":
                    if area in SINGLE_DIGIT_DISTRICT_AREAS:
                        raise ValueError(f"Not valid. The area '{area}' has only a single digit districts")
                    if area in [a for a in ZERO_DISTRICT_AREAS if a != "BS"] and outward_code[2:] == "10":
                        raise ValueError(f"Not valid. The area '{area}' could not have a district code of 10")
            return
    raise ValueError(f"Not valid. The outward_code '{outward_code}' does not match any pattern")


def inward_code_verify(outward_code: str):
    if re.match(INWARD_CODE_PATTERN, outward_code):
        return
    raise ValueError(f"Not valid. The inward_code '{outward_code}' does not matches pattern")


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Postcode verification and formatting')
    parser.add_argument('-s', '--sequence', action='store_true', help='print the numbers from 1 to 100 '
                                                           'with Three instead of multiples of 3, '
                                                           'Five instead of multiples of 5, '
                                                           'and ThreeFive instead of multiples of both')
    parser.add_argument('-p', '--postcode', type=str, help='The postcode to verify and format')
    parser.add_argument('-f', '--format', action='store_true', help='Format the postcode')
    args, unknown_args = parser.parse_known_args()

    if args.sequence:
        sequence_print(args.sequence)
    elif args.format:
        formatted = format_postcode(args.postcode)
        logging.info(f'Formatted postcode: {formatted}')
    else:
        try:
            result = postcode_verify(args.postcode)
        except ValueError as e:
            logging.error(e)
        else:
            logging.info(result)


if __name__ == '__main__':
    main()
