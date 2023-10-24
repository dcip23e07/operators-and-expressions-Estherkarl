var_a = 400 
var_b = '200' + '200'
var_c = 400.0 
var_d = 200 + 200

a = ((var_a == var_b) is (var_a is var_b))

print (a)



# result : True :  They have the same identity


b = ((var_a == var_c) is (var_a is var_c)) 

print (b)

# result :False : They don't have the same identity

c = (var_a == var_d)  is ( var_a is var_d)

print(c)

# result : True :  They have the same identity

