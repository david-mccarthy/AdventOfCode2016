def move(coords,instr,puzzle):
# Pass the starting coordinates, the instructions and the puzzle 3D array

  for s in instr:
    if s == "U":
      if not outOfBounds((coords["y"] - 1),coords["x"],puzzle):
        coords["y"] -= 1
    if s == "D":
      if not outOfBounds((coords["y"] + 1),coords["x"],puzzle):
        coords["y"] += 1
    if s == "L":
      if not outOfBounds(coords["y"],(coords["x"] - 1),puzzle):
        coords["x"] -= 1
    if s == "R":
      if not outOfBounds(coords["y"],(coords["x"] + 1),puzzle):
        coords["x"] += 1

  return coords


def outOfBounds(x,y,puzzle):

  outOfBoundsPoints = [-1,len(puzzle[0])]

  return (x in outOfBoundsPoints or y in outOfBoundsPoints) or puzzle[y][x] == None


def main():
  
  partOnePoints = [
  ["1","2","3"],
  ["4","5","6"],
  ["7","8","9"]]

  partTwoPoints = [
  [None,None,"1",None,None],
  [None,"2","3","4",None],
  ["5","6","7","8","9"],
  [None,"A","B","C",None],
  [None,None,"D",None,None]]

  coords = {"x":1,"y":1} # Starting coordinates for puzzle one: puzzle[1][1] == 5
  
  with open("inputs/day2") as f:
    directions = f.readlines()

  code1 = ""
  code2 = ""
  for line in directions:
    coords = move(coords,line,partOnePoints)
    code1 += partOnePoints[coords["y"]][coords["x"]]
  print "Part one:",code1

  #Make sure the coordinates for part 2 are set correctly
  # puzzle[2][0] == 5 
  coords = {"x":0,"y":2}
  for line in directions:
    coords = move(coords,line,partTwoPoints)
    code2 += partTwoPoints[coords["y"]][coords["x"]]
  print "Part two:",code2
    
if __name__ == "__main__":
  main()