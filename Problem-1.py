#Problem 1 Simple calculator

a,b,type_of_operation = input("Enter the required numbers and operation: ").split()
try:
  a = float(a)
  b = float(b)
  if type_of_operation.lower() == 'addition':
    print(a+b)
  elif type_of_operation.lower() == 'subtraction':
    print(a-b)
  elif type_of_operation.lower() == 'multiplication':
    print(a*b)
  elif type_of_operation.lower() == 'division':
    print(a/b)

except Exception as error:
  print('error message: ' + repr(error))
