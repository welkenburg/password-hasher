letters = "1234567890°+AZERTYUIOP¨£QSDFGHJKLM%µ>WXCVBN?./§²&é'(-è_çà)=azertyuiop^$qsdfghjklmù*<wxcvbn,;:!~#{[|`@]}€¤ "
#letters = "abcdefghijklmnopqrstuvwxyz"

def letterIndex(letter):
	for i in range(len(letters)):
		if letters[i] == letter:
			return i + 1

def hash(msg,keys):
	for key in keys:
		hashedMsg = ""
		for i in range(len(msg)):
			try:
				hashedMsg += letters[(letterIndex(msg[i]) + letterIndex(key[i%len(key)])) % len(letters) - 1]
			except:
				hashedMsg += msg[i]
		msg = hashedMsg
	return msg

def unhash(msg,keys):
	for key in keys:
		hashedMsg = ""
		for i in range(len(msg)):
			try:
				hashedMsg += letters[(letterIndex(msg[i]) - letterIndex(key[i%len(key)])) % len(letters) - 1]
			except:
				hashedMsg += msg[i]
		msg = hashedMsg
	return msg

# message = input("message ?\n")
message = "alistair est le meullieur gas du mond : = vrai"

keys = ["cle","roi","anticonstitution"]
keys2 = ["cle","roi","anticonstitution"]
hashPass = hash(message,keys)
unhashPass = unhash(hashPass,keys2)

print(hashPass)
print(unhashPass)