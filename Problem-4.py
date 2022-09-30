# Problem 4 Dictionary generation

lis = [1,2,8,9,12,46,76,82,15,20,30]
final_dict= {}
div_lis = [1,2,3,4,5,6,7,8,9]
for nums in lis:
  for div_nums in div_lis:
    if nums % div_nums == 0:
      if final_dict.get(div_nums) == None:
        final_dict[div_nums] = 1
      else:
        final_dict[div_nums] = final_dict[div_nums]+1
        
print(final_dict)
