import re


def height_validation(height):
    match = re.match(r"(\d{2,3})(cm|in)", height)

    if not match:
        return False
    items = match.groups()

    return (items[1] == 'cm' and int(items[0]) >= 150 and int(items[0]) <= 193) or (items[1] == 'in' and int(items[0]) >= 59 and int(items[0]) <= 76)


validations_dict = {
    'byr': lambda year: int(year) >= 1920 and int(year) <= 2002,
    'iyr': lambda year: int(year) >= 2010 and int(year) <= 2020,
    'eyr': lambda year: int(year) >= 2020 and int(year) <= 2030,
    'hgt': height_validation,
    'hcl': lambda color: len(color) == 7 and re.search(r'^#[0-9a-f]{6}', color),
    'ecl': lambda color: re.search(r'(amb|blu|brn|gry|grn|hzl|oth)', color),
    'pid': lambda num: len(num) == 9 and re.search(r'\d{9}', num) and int(num) > 0
}

print("validations_dict['byr']('1919')", validations_dict['byr']('1919'), 'False')
print("validations_dict['byr']('1920')", validations_dict['byr']('1920'), 'True')
print("validations_dict['byr']('2002')", validations_dict['byr']('2002'), 'True')
print("validations_dict['byr']('2003')", validations_dict['byr']('2003'), 'False')
print("validations_dict['iyr']('2009')", validations_dict['iyr']('2009'), 'False')
print("validations_dict['iyr']('2010')", validations_dict['iyr']('2010'), 'True')
print("validations_dict['iyr']('2020')", validations_dict['iyr']('2020'), 'True')
print("validations_dict['iyr']('2021')", validations_dict['iyr']('2021'), 'False')
print("validations_dict['eyr']('2019')", validations_dict['eyr']('2019'), 'False')
print("validations_dict['eyr']('2020')", validations_dict['eyr']('2020'), 'True')
print("validations_dict['eyr']('2030')", validations_dict['eyr']('2030'), 'True')
print("validations_dict['eyr']('2031')", validations_dict['eyr']('2031'), 'False')
print("validations_dict['hgt']('149cm')", validations_dict['hgt']('149cm'), 'False')
print("validations_dict['hgt']('194cm')", validations_dict['hgt']('194cm'), 'False')
print("validations_dict['hgt']('150cm')", validations_dict['hgt']('150cm'), 'True')
print("validations_dict['hgt']('193cm')", validations_dict['hgt']('193cm'), 'True')
print("validations_dict['hgt']('58in')", validations_dict['hgt']('58in'), 'False')
print("validations_dict['hgt']('77in')", validations_dict['hgt']('77in'), 'False')
print("validations_dict['hgt']('59in'", validations_dict['hgt']('59in'), 'True')
print("validations_dict['hgt']('76in')", validations_dict['hgt']('76in'), 'True')
print("validations_dict['hgt']('76 in')", validations_dict['hgt']('76 in'), 'False')
print("validations_dict['hgt']('160 cm')", validations_dict['hgt']('160 cm'), 'False')
print("validations_dict['hgt']('160 mm')", validations_dict['hgt']('160 mm'), 'False')
print("validations_dict['hgt']('160mm')", validations_dict['hgt']('160mm'), 'False')
print("validations_dict['hgt']('160ft')", validations_dict['hgt']('160ft'), 'False')
print("validations_dict['hgt']('57ft')", validations_dict['hgt']('57ft'), 'False')
print("validations_dict['hcl']('#000000')", validations_dict['hcl']('#000000'), 'True')
print("validations_dict['hcl']('#00000f')", validations_dict['hcl']('#00000f'), 'True')
print("validations_dict['hcl']('#ffffff')", validations_dict['hcl']('#ffffff'), 'True')
print("validations_dict['hcl']('#af03aa')", validations_dict['hcl']('#af03aa'), 'True')
print("validations_dict['hcl']('#1a1a1a')", validations_dict['hcl']('#1a1a1a'), 'True')
print("validations_dict['hcl']('#18181')", validations_dict['hcl']('#18181'), 'False')
print("validations_dict['hcl']('181818')", validations_dict['hcl']('181818'), 'False')
print("validations_dict['hcl']('aaaaaa')", validations_dict['hcl']('aaaaaa'), 'False')
print("validations_dict['hcl']('#aaaaaaa')", validations_dict['hcl']('#aaaaaaa'), 'False')
print("validations_dict['hcl']('#ga0aa7')", validations_dict['hcl']('#ga0aa7'), 'False')
print("validations_dict['hcl']('#ga0aaa7')", validations_dict['hcl']('#ga0aaa7'), 'False')
print("validations_dict['hcl']('#abcdef')", validations_dict['hcl']('#abcdef'), 'True')
print("validations_dict['hcl']('#abcdeg')", validations_dict['hcl']('#abcdeg'), 'False')
print("validations_dict['pid']('000000001')", validations_dict['pid']('000000001'), 'True')
print("validations_dict['pid']('100000001')", validations_dict['pid']('100000001'), 'True')
print("validations_dict['pid']('123456789')", validations_dict['pid']('123456789'), 'True')
print("validations_dict['pid']('1234567891')", validations_dict['pid']('1234567891'), 'False')
print("validations_dict['pid']('012345678')", validations_dict['pid']('012345678'), 'True')
print("validations_dict['pid']('01234567')", validations_dict['pid']('01234567'), 'False')
print("validations_dict['pid']('100000000')", validations_dict['pid']('100000000'), 'True')
print("validations_dict['pid']('1000a0000')", validations_dict['pid']('1000a0000'), 'False')
