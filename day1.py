#!/usr/bin/python

import math

def getInput():
  with open ("inputs/day1") as f:
    instrs = f.read()
  return instrs.split(", ")


def turn(d):
  return {
    'L': -1,
    'R': 1,
  }[d]


def distance(a,b):
  return int(math.fabs(a) + math.fabs(b))


def main():

  compass = ["N","E","S","W"]
  facing = 0 # start facing north
  visited = []
  found = False
  coordinates = (0,0)

  directions = getInput()

  for _dir in directions:
    direction = _dir[0]
    steps = int(_dir[1:])
    facing = ( ( facing + 4 ) + turn(direction) ) % 4

    # x and y axis, 0 and 1 in the tuple
    X=0
    Y=1
    
    for _ in range(steps):
      if compass[facing] == "N":
        coordinates = (coordinates[X] + 1, coordinates[Y])
      if compass[facing] == "S":
        coordinates = (coordinates[X] - 1, coordinates[Y])
      if compass[facing] == "E":
        coordinates = (coordinates[X], coordinates[Y] + 1)
      if compass[facing] == "W":
        coordinates = (coordinates[X], coordinates[Y] - 1)
      if not found and coordinates in visited:
        found = True
        ans = coordinates
      else:
        visited.append(coordinates)

  print " First puzzle:", int(math.fabs(coordinates[0]) + math.fabs(coordinates[1]))
  print "Second puzzle:", distance(ans[0], ans[1])


if __name__ == "__main__":
  main()
