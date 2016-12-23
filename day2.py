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

  coords1 = {"x":1,"y":1} # Starting coordinates for puzzle one: puzzle[1][1] == 5
  coords2 = {"x":0,"y":2} # Starting coordinates for puzzle two

  with open("inputs/day2") as f:
    directions = f.readlines()

  code1 = ""
  code2 = ""
  for line in directions:
    coords1 = move(coords1,line,partOnePoints)
    code1 += partOnePoints[coords1["y"]][coords1["x"]]

    coords2 = move(coords2,line,partTwoPoints)
    code2 += partTwoPoints[coords2["y"]][coords2["x"]]
  print "Part one:",code1
  print "Part two:",code2
    
if __name__ == "__main__":
  main()