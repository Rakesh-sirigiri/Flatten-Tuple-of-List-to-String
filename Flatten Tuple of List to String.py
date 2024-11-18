list = [('1', '4', '6'), ('5', '8'), ('2', '9'), ('1', '10')]
print("The original list: " + str(list))
res = " ".join(map(str, sum(list, ())))
print("Tuple list converted to string is : " + res)
