passports = []
reduced_fieldset = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
passport = {}
valid_passports = 0

def validate_passport(passport):
    if (set(passport.keys()) != reduced_fieldset):
        # print(f"invalid fieldset {set(passport.keys())}")
        return False
    if (int(passport["byr"]) < 1920) or (int(passport["byr"]) > 2002):
        # print(f"invalid byr {passport['byr']}")
        return False
    elif (int(passport["iyr"]) < 2010) or (int(passport["iyr"]) > 2020):
        # print(f"invalid iyr {passport['iyr']}")
        return False
    elif (int(passport["eyr"]) < 2020) or (int(passport["eyr"]) > 2030):
        # print(f"invalid eyr {passport['eyr']}")
        return False
    elif passport["hgt"][-2:] == "cm" and ((int(passport["hgt"][:-2]) < 150) or (int(passport["hgt"][:-2]) > 193)):
        # print(f"invalid hgt cm {int(passport['hgt'][:-2])}")
        return False
    elif passport["hgt"][-2:] == "in" and ((int(passport["hgt"][:-2]) < 59) or (int(passport["hgt"][:-2]) > 76)):
        # print(f"invalid hgt in {int(passport['hgt'][:-2])}")
        return False
    elif passport["hgt"][-2:] not in ["in", "cm"]:
        # print(f"invalid hgt format {passport['hgt'][-2:]}")
        return False
    elif passport["hcl"][0] != '#' or len(passport["hcl"]) != 7:
        # print("invalid hcl format")
        return False
    try:
        intstring = "0x" + passport["hcl"][1:]
        int(intstring, 16)
    except:
        # print("invalid hcl not a hexa number")
        return False
    if passport["ecl"] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        # print("invalid ecl")
        return False
    elif len(passport['pid']) != 9:
        # print(f"invalid pid length '{passport['pid']}' {len(passport['pid'].strip())}")
        return False
    try:
        int(passport['pid'])
    except:
        # print("invalid pid not a number")
        return False
    return True

with open('../input.txt', 'r') as inputfile:
    for line in inputfile:
        if len(line) == 1 :
            # print("\n starting new passport")
            passports.append(passport)
            
            if validate_passport(passport): 
                valid_passports += 1
                # print("valid")
            else:
                pass
            passport = {}
            continue
        else:
            fields = line.split(' ')
            for field in fields:
                key,value = field.split(':')
                if key != 'cid':
                    passport[key] = value.strip()
print(valid_passports)