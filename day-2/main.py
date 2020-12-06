class Password:
    minimum = 0
    maximum = 0
    char = ""
    word = ""

    def __init__(self, minimum, maximum, char, word):
        self.minimum = minimum
        self.maximum = maximum
        self.char = char
        self.word = word

def parseLine(line):
    splitByDash = line.split("-")
    minimum = int(splitByDash[0])
    
    splitBySpace = splitByDash[1].split(" ")
    maximum = int(splitBySpace[0])
    char = splitBySpace[1][0]
    word = splitBySpace[2]

    return Password(minimum, maximum, char, word)

def getPasswords():
    f = open("input", "r")
    content = f.read()
    lines = content.strip().split("\n")
    data  = [parseLine(line) for line in lines]
    return data

valid_passwords = 0

for password in getPasswords():
    count = 0
    for char in password.word:
        if (char == password.char):
            count+= 1
    if (count <= password.maximum and count >= password.minimum):
        valid_passwords+= 1

print("Step 1: " + str(valid_passwords))



valid_passwords = 0

for password in getPasswords():
    first = (password.word[password.minimum - 1] == password.char)
    second = (password.word[password.maximum - 1] == password.char)
    if (first + second == 1):
        valid_passwords+= 1

print("Step 2: " + str(valid_passwords))
