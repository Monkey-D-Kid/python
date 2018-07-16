#!/usr/bin/env python
def add_border(matrix, n):
  size = n*2-1
  target = []
  for r in range(size):
    row = []
    for c in range(size):
      if r == 0 or r == (size-1):
        row.append(n)
      elif c == 0 or c == (size-1):
        if not row:
          if isinstance(matrix[r-1], int):
            row = [matrix[r-1]]
          else:
            row = matrix[r-1]
#        print("C =" + str(c))
#        print("Enter Before")
#        print(row)
        row.insert(c,n)
#        print("Enter After")
#        print(row)
#    print("Row")
#    print(row)
    target.append(row)
#  print("End Border")
#  print(target)
  return target

def create_target(n):
  if n == 0:
    return []
  elif n == 1:
    return [1]
  else:
    matrix = [1]
    for i in range(2,n+1):
      matrix = add_border(matrix,i)  

if __name__ == '__main__':
  output = create_target(3)
  print(output)
#create_matrix(3)
