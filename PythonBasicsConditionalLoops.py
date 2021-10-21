

#######################################

1.

req_num = [ ]

for i in range(2000,3200+1):
      if i%7==0 and i%5!=0:
            req_num.append(i)


print(req_num)


#########################################

2.

first_name = input('Enter the first name: ')
second_name = input('Enter second name: ')
print('full name:',first_name[::-1]+' '+second_name[::-1])



######################################

3.

diameter = 12.0

pi = 3.1415926535897931

volume_of_a_sphere = (4/3)*pi*(diameter/2)**3

print('volume:',volume_of_a_sphere)
