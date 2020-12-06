class Map:
    terrain = []
    width = 0
    height = 0

    def __init__(self):
        f = open("input", "r")
        content = f.read().strip()

        self.width = content.find("\n")

        for char in content:
            if (char == "\n"):
                continue
            self.terrain.append(char == "#")
        
        self.height = len(self.terrain) // self.width

    def getPosition(self, row, col):
        col = col % self.width
        return self.terrain[(self.width * row + col)]

def getTreesForSlope(right, down):
    count = 0
    col = 0
    for row in range(0, m.height, down):
        count += m.getPosition(row, col)
        col += right
    return count


m = Map()
print("Step 1: " + str(getTreesForSlope(3, 1)))

total = getTreesForSlope(1, 1) * getTreesForSlope(3, 1) * getTreesForSlope(5, 1) * getTreesForSlope(7, 1) * getTreesForSlope(1, 2)
print("Step 2: " + str(total))
