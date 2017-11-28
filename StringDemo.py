String_var = """ this document will
teach you string things """
print(String_var.replace('document','tutorial'))

sample_str = 'Python String'
print("sample_str -> ", sample_str)
print("sample_str[0] ",sample_str[0])
print("sample_str[-1] ", sample_str[-1])
print("sample_str[-2] ", sample_str[-2])
print("sample_str[7:] ", sample_str[7:])
print("sample_str[3:5] ", sample_str[3:5])
print("sample_str[:6] ", sample_str[:6])
print("sample_str[7:-4] ", sample_str[7:-4])

#Repetition
var1='Python'

print('Repetition')
print('var1 -> ', var1)
print('var1*3 -> ', var1*3 )

print('in and not in operators')
print("'n' in var1 -> ", 'n' in var1)
print("'m' not in var1 -> ", 'm' not in var1)

print('Iterating')
for var in var1:
    print(var)

print('Raw String : operator r and R before string')
print(r'string\n\t')
print(R'string\n\t')

print("Format Characters e.g. ‘%’")
print('Name: %s, Age: %d\n' % ('Fred', 28) )

