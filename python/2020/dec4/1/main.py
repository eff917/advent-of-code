passports = []
fieldset = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
reduced_fieldset = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
passport = {}
valid_passports = 0
with open('../input.txt', 'r') as inputfile:
    for line in inputfile:
        if len(line) == 1 :
            print("starting new passport")
            passports.append(passport)
            if set(passport.keys()) == fieldset or set(passport.keys()) == reduced_fieldset:
                valid_passports += 1
                print("valid")
            else:
                print("invalid")
            passport = {}
            continue
        else:
            fields = line.split(' ')
            for field in fields:
                key, value = field.split(':')
                passport[key] = value
print(valid_passports)