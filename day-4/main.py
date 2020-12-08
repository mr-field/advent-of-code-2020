import re

REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
HCL_REGEX = re.compile(r"^#[0-9a-f]{6}$")
ECL_REGEX = re.compile(r"^(amb|blu|brn|gry|grn|hzl|oth)$")
PID_REGEX = re.compile(r"^\d{9}$")

def getPassports():
    f = open("input", "r")
    content = f.read()
    passportData = content.strip().split("\n\n")

    passports = []

    for rawPassport in passportData:
        elements = rawPassport.replace("\n", " ").split(" ")
        passport = {}
        for element in elements:
            kv = element.split(":")
            passport[kv[0]] = kv[1]
        passports.append(passport)
    
    return passports

def isNumberInRange(s, numDigits, minimum, maximum):
    p = re.compile(r"\d{" + str(numDigits) + "}")
    if not p.match(s):
        return False
    return (int(s) <= maximum and int(s) >= minimum)

def validateHeight(s):
    if (s.endswith("cm")):
        return isNumberInRange(s.replace("cm", ""), 3, 150, 193)
    elif (s.endswith("in")):
        return isNumberInRange(s.replace("in", ""), 2, 59, 76)
    else:
        return False


passports = getPassports()
completePassports = [passport for passport in passports if (passport.keys() >= REQUIRED_FIELDS)]

print("Step 1: " + str(len(completePassports)))

validPassports = 0
for passport in completePassports:    
    checks = set()
    checks.add(isNumberInRange(passport["byr"], 4, 1920, 2002))
    checks.add(isNumberInRange(passport["iyr"], 4, 2010, 2020))
    checks.add(isNumberInRange(passport["eyr"], 4, 2020, 2030))
    checks.add(validateHeight(passport["hgt"]))
    checks.add(bool(HCL_REGEX.match(passport["hcl"])))
    checks.add(bool(ECL_REGEX.match(passport["ecl"])))
    checks.add(bool(PID_REGEX.match(passport["pid"])))
    if not False in checks:
        validPassports += 1

print("Step 2: " + str(validPassports))
