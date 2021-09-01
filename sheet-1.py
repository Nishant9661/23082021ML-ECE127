Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #2
>>> 5**9
1953125
>>> 3//2
1
>>> 7//3
2
>>> 7/3
2.3333333333333335
>>> 6==6
True
>>> a=20; a+= 30; a%=3; print(a)
2
>>> True * False
0
>>> True & False
False
>>> True and False
False
>>> ((6>3) and (7<4) or (18==3)) and (9>3)
False
>>> True is False
False
>>> False in 'False'
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    False in 'False'
TypeError: 'in <string>' requires string as left operand, not bool
>>> ((True == False) or (False > True)) and (False <= True)
False
>>> 
>>> #3
>>> s1='
SyntaxError: EOL while scanning string literal
>>> ###3
>>> s1= "Nice to have it"
>>> s2= "here"
>>> s1+s2
'Nice to have ithere'
>>> ##4
>>> a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a[3]
[5, [100, 200, ['hello']], 23, 11]
>>> a[3][1]
[100, 200, ['hello']]
>>> a[3][1][2]
['hello']
>>> 
>>> ##5
>>> s1
'Nice to have it'
>>> s2
'here'
>>> a
[1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
>>> a.inser(0,[s1])
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a.inser(0,[s1])
AttributeError: 'list' object has no attribute 'inser'
>>> a.insert(0,[s1])
>>> a
[['Nice to have it'], 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
>>> a+=[s2]
>>> a
[['Nice to have it'], 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'here']
>>> 
>>> ##6
>>> numbers = [386,462,47,418,907,344,236,375,823,566,597,978,328,615,953,345,399,162,758,219,918,237,412,566,826,248,866,950,626,949,687,217,815,67,104,58,512,24,894,767,553,81,379,843,831,445,742,717,958,743,527]
>>> for i in numbers:
	if i<=237:
	if i%2==0:
		
SyntaxError: expected an indented block
>>> numbers
[386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 743, 527]
>>> for i in numbers:
	if(numbers[i]%2==0):
		if(i<=237):
			print(numbers[i])

			
Traceback (most recent call last):
  File "<pyshell#48>", line 2, in <module>
    if(numbers[i]%2==0):
IndexError: list index out of range
>>> ##
>>> 
>>> ##7
>>> color_list_1= set(["white","Black","Red"])
>>> color_list_2= set(["Red","Green"])
>>> color_list_1.difference(color_list_2)
{'white', 'Black'}
>>> 
>>> 
>>> ##9
>>> number=(i+((i*10)+i)+((i*100)+(i*10)+1)):
	
SyntaxError: invalid syntax
>>> numbers
[386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 743, 527]
>>> number
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    number
NameError: name 'number' is not defined
>>> ###########
>>> ##9
>>> i=('enter a number:')
>>> i=('Enter a number:')
>>> Enter a number:5
SyntaxError: invalid syntax
>>> number=(i+((i*10)+i)+((i*100)+(i*10)+1)
	for i==5:
	
SyntaxError: invalid syntax
>>> 
========== RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python39/kuchh bhi.py =========
>>> 
>>> ##10
>>> 
>>> 
>>> ##11
>>> 
>>> ##12
>>> d={'student':['Rahul','Kishore','Vidya','Raakhi'],'Marks':[57,87,67,79]
   d['student'][1]
   
SyntaxError: invalid syntax
>>> 