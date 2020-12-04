"""
--- Day 2: Password Philosophy ---
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?


--- Part Two ---
While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?
"""

from typing import Tuple


def get_policy_and_password(password_string: str) -> Tuple:
    policy, password = password_string.split(
        ':')[0], password_string.split(':')[1].strip()
    numbers = [int(number) for number in policy.split(' ')[0].split('-')]
    key_letter, first_num, second_num = policy.split(
        ' ')[1], numbers[0], numbers[1]

    return password, key_letter, first_num, second_num


def check_password_validity(password_string: str) -> bool:
    password, key_letter, _min, _max = get_policy_and_password(password_string)

    count = len([letter for letter in password if letter == key_letter])

    return count >= _min and count <= _max


def check_password_validity_new(password_string: str) -> bool:
    password, key_letter, pos1, pos2 = get_policy_and_password(password_string)
    pos1, pos2 = pos1 - 1, pos2 - 1

    return not (password[pos1] == key_letter and password[pos2] == key_letter) and (password[pos1] == key_letter or password[pos2] == key_letter)


if __name__ == '__main__':
    with open('02-password-philosophy-input.txt', 'r') as puzzle_input:
        passwords = puzzle_input.read().split('\n')

    print(
        len([password for password in passwords if check_password_validity(password)])
    )
    print(
        len([password for password in passwords if check_password_validity_new(password)])
    )
