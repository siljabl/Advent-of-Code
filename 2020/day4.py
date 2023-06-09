input = open("input4.txt")
passports = input.read().split("\n\n")

# Including cid
include_cid = False


req_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
if include_cid :
	req_fields.app('cid')	


# Part 1
valid = 0
for passport in passports :
	passport = passport.split()
	
	if len(passport) < len(req_fields) :
		continue
		
	else :
		passport = [req.split(":")[0] for req in passport]
		if set(passport) >= req_fields :
			valid += 1
	
print(f"Part 1:\nIncluding cid: {include_cid}\nNumber of valid passports: {valid}\n")



# Part 2
def in_range(x, low, high) :
	x, low, high = int(x), int(low), int(high)
	output = True
	if (x - low) < 0 :
		output = False
	elif (high - x) < 0 :
		output = False
		
	return output



def is_valid(data) :
	valid = True
	
	yr = [data['byr'], data['iyr'], data['eyr']]
	yr_lims = [[1920, 2002], [2010, 2020], [2020, 2030]]
	eye_colors = ['amb','blu','brn','gry','grn','hzl','oth']
	letters = set(['a', 'b', 'c', 'd', 'e', 'f'])
	digits = set([str(i) for i in range(10)])
	
		
	# checking years
	for i in range(3) :
		if not in_range(yr[i], *yr_lims[i]) :
			return False
		
	
	# checking height
	hgt = data['hgt']
	if len(hgt) < 4 : return False
	
	else :	
		hgt = [int(hgt[0:-2]), hgt[-2:]]
		
		if hgt[1] == 'cm' :
			if not in_range(hgt[0],150,193) :
				return False
			
		elif hgt[1] == 'in' :
			if not in_range(hgt[0],59,76) : 
				return False
			
				
	# checking hair color
	hcl = data['hcl']
	if len(hcl) != 7 : return False
	elif hcl[0] != '#' : return False
	else :
		subset = set(hcl[1:]) <= letters|digits		
		if not subset :
			return False		
	
	
	# cheking eye color
	ecl = data['ecl']
	if ecl not in eye_colors :
		return False
	
	
	# checking passport id
	pid = data['pid']
	if len(pid) != 9 : return False
	subset = set(pid) <= digits
	if not subset :
			return False


	return valid


valid = 0
for passport in passports :
	passport = passport.split()
	
	if len(passport) < len(req_fields) :
		continue
		
	else :
		passport = [req.split(":") for req in passport]
		passport = {req[0]: req[1] for req in passport}
		
		if set(passport.keys()) >= req_fields :
			valid += is_valid(passport)
			

print(f"Part 2:\nIncluding cid: {include_cid}\nNumber of valid passports: {valid}\n")












		
