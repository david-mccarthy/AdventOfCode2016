def move(coords,instr):

  for s in instr:
    if s == "U":
      coords["x"] -= 1
      if coords["x"] < 0:
        coords["x"] = 0
    if s == "D":
      coords["x"] += 1
      if coords["x"] > 2:
        coords["x"] = 2
    if s == "L":
      coords["y"] -= 1
      if coords["y"] < 0:
        coords["y"] = 0
    if s == "R":
      coords["y"] += 1
      if coords["y"] > 2:
        coords["y"] = 2

  return coords

def main():
  
  partOnePoints = [
  ["1","2","3"],
  ["4","5","6"],
  ["7","8","9"]]

  coords = {"x":1,"y":1}
  
  with open("inputs/day2") as f:
    directions = f.readlines()

  code = ""
  for line in directions:
    coords = move(coords,line)
    code += partOnePoints[coords["x"]][coords["y"]]
  print "Part one:",code
    
if __name__ == "__main__":
  main()