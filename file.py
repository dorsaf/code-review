def sum_of_list(mylist):
  total = 0
  for val in mylist:
    total = total + val
  return total

my_list = [1,3,5,2,4]
print( "The sum of my_list is", sum_of_list(my_list))
