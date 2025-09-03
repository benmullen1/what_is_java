#!/usr/bin/python3

def main():
    print('Write a program that prints the numbers from 1 to 100. But for multiples of three print \"Fizz\" instead of the number and for the multiples of five print \"Buzz\".')
    print('For numbers which are multiples of both three and five print \"FizzBuzz\"')

    for number in range(1, 101, 1):
        if number % 15 == 0:
            print('FizzBuzz')
            continue
        if number % 5 == 0:
            print('Buzz')
        elif number % 3 == 0:
           print ('Fizz')
        else: 
            print (number)

if __name__ == "__main__":
  main()