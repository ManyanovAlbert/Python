number1= int(input())
number2= int(input())
for num in range(number1,number2+1):
    if num % 5 ==0 and num % 3 ==0:
        print('FizzBuzz')
    elif num % 3 ==0:
        print('Fizz')
    elif num % 5 ==0:
        print('Buzz')
    else:
        print(num)
