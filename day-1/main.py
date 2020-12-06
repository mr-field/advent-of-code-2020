def getLinesAsInts():
  f = open("input", "r")
  content = f.read()
  return [int(x) for x in content.strip().split("\n")]

def getTwoNumbersForTotal(total):
  nums = getLinesAsInts()
  for i in range(0, len(nums)):
    first_num = nums[i]
    for k in range((i + 1), len(nums)):
      second_num = nums[k]
      if (first_num + second_num == total):
        print(str(first_num) + "," + str(second_num))
        return first_num * second_num

def getThreeNumbersForTotal(total):
  nums = getLinesAsInts()
  for i in range(0, len(nums)):
    first_num = nums[i]
    intermediate_total = total - first_num

    for k in range(0, len(nums)):
      second_num = nums[k]
      for j in range((k + 1), len(nums)):
        third_num = nums[j]
        if (second_num + third_num == intermediate_total):
          print(str(first_num) + "," + str(second_num) + "," + str(third_num))
          return first_num * second_num * third_num

print(getTwoNumbersForTotal(2020))
print(getThreeNumbersForTotal(2020))
