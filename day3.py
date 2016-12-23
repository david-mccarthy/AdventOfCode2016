
def main():
  puzzle1()
  puzzle2()

def getInput():
  with open ( "inputs/day3") as f:
    lines = f.readlines()
  return lines

def puzzle1():
  
  lines = getInput()

  count = 0
  for triangle in lines:
    (a,b,c) = triangle.split()
    if validTriangle((a,b,c)):
      count += 1

  print "Part one valid triangles:",count

def puzzle2():

  lines = getInput()
  count = 0
  first = []
  second = []
  third = []

  for line in lines:
    (a,b,c) = line.split()
    first.append(int(a))
    second.append(int(b))
    third.append(int(c))

    if(len(first) == 3):
      if validTriangle((first[0],first[1],first[2])):
        count += 1
      del first[:]
    if(len(second) == 3):
      if validTriangle((second[0],second[1],second[2])):
        count += 1
      del second[:]
    if(len(third) == 3):
      if validTriangle((third[0],third[1],third[2])):
        count += 1
      del third[:]

  print "Second puzzle",count

def validTriangle(tuple):
  
  a = int(tuple[0])
  b = int(tuple[1])
  c = int(tuple[2])
 
  return (( a + b ) > c ) and ( a + c > b) and ( c + b > a)

if __name__ == "__main__":
  main()