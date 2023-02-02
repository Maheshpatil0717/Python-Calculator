A=int(input("Enter a First Number="))
B=int(input("Enter a Secont Number="))
operator=(input('''Please Select The Type of  Operation You Want To Perform:
+ For Addition
- For Subtraction
* For Multiplication
/ For Division
% For Module
// For Floor Division
** For Exponent  =  '''))
if   operator=='+':
     print("Addition of A and B is = " , A+B)
elif operator== '-':
     print("Substraction A and B is =" , A-B)
elif operator== '*':
    print("Multiplication A and B is =" , A*B)
elif operator== '/':
    print("Division A and B is =" , A/B)
elif operator== '%':
    print("Modulo A and B is =" , A%B)
elif operator== '//':
    print("Floor Division A and B is =" , A//B)
elif operator== '**':
    print("Exponent A and B is =" , 'A**B')
else:
    print("Enter a Correct Number")
