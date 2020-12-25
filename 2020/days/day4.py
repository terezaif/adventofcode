import re

fields = set(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))
allowed = "cid"

""" byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not. """


def is_passport_valid(
    passport: dict, fields: set = fields, allowed: str = allowed
) -> bool:
    passport.pop(allowed, None)
    if set(passport.keys()) != fields:
        return False
    if (int(passport["byr"]) < 1920) | (int(passport["byr"]) > 2002):
        return False
    if (int(passport["iyr"]) < 2010) | (int(passport["iyr"]) > 2020):
        return False
    if (int(passport["eyr"]) < 2020) | (int(passport["eyr"]) > 2030):
        return False
    height = re.findall(r"(\d+)(cm|in)", passport["hgt"])
    if len(height) != 1:
        return False
    if height[0][1] == "cm":
        if (int(height[0][0]) < 150) | (int(height[0][0]) > 193):
            return False
    if height[0][1] == "in":
        if (int(height[0][0]) < 59) | (int(height[0][0]) > 76):
            return False
    if not bool(re.search(r"#[0-9a-f]{6}", passport["hcl"])):
        return False
    if not bool(re.search(r"amb|blu|brn|gry|grn|hzl|oth", passport["ecl"])):
        return False
    if not bool(re.search(r"^\d{9}$", passport["pid"])):
        return False

    return True


def get_valid_passport_validation_count(input: str) -> int:
    passport_count = 0
    passport_fields = {}
    for line in input:
        if line == "":
            passport_count += int(is_passport_valid(passport_fields))
            passport_fields = {}
        else:
            passport_fields = {
                **passport_fields,
                **dict(re.findall(r"(\w+):(.\w+)", line)),
            }
    passport_count += int(is_passport_valid(passport_fields))
    return passport_count


def get_valid_passport_count(input: str) -> int:
    passport_count = 0
    passport_fields = set()
    for line in input:
        if line == "":
            passport_fields.discard(allowed)
            passport_count += int(passport_fields == fields)
            passport_fields = set()
        else:
            passport_fields.update(set(re.findall(r"(\w+):", line)))
    passport_count += int(passport_fields == fields)
    return passport_count
