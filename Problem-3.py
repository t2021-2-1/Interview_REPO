#Problem 3 Generating odd numbers

def odds(input_val):
    final_output = []
    start = 1
    final_output.append(start)
    while len(final_output) < input_val:
        start += 2
        final_output.append(start)
    return final_output

a = input("Enter the number of odd numbers required: ")
a = int(a)

if a % 2 == 0:
  b = a - 1
  print("input a = {}, then output: {}".format(a,odds(b)))
else:
  print("input a = {}, then output: {}".format(a,odds(a)))
  