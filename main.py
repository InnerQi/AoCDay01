# test list
test = [1721,979,366,299,675,1456]

# check_sum
check_sum = 2020 

# find two addends for check_sum from list
print(test)
for i in range(0, len(test)):
  diff_num = check_sum - test[i]

  # Determine if the difference of check_sum and test element is in list 
  # if so, both difference and test element are addends
  if diff_num in test:
    print(f"\n{test[i]} and {diff_num} both sum up to {check_sum}")

    # find product of the two entries  
    prod = test[i] * diff_num
    print(f"Their product equals: {prod}\n") 

  # if not, the test element and its difference from 2020 do not exist in our test list
  else:
    print(f"{diff_num} does not exist in our list")
   
 