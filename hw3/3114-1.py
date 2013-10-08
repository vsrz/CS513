#!/usr/bin/python

holes = [1,0,1,0,1,0,1,0]
end = 0
counter = 0


while not(end):
  print holes
  if counter+1 == len(holes):
    end += 1
  elif holes[counter] == 0 and holes[counter+1] == 1:
    hole = holes[counter]
    holes[counter] = holes[counter+1]  
    holes[counter+1] = hole
    counter -= 1
  else:
    counter += 1
print holes

