'''
Problem: Given the integer n entered by standard input (stdin), write a program to output in standard 
    form (stdout) the Kaprekar number greater than or equal to n and closest to n.
Problem Orientation:
- The user will enter until the correct answer is an integer n (0 <= n <= 1000000000)
- Consider each number greater than n in turn by taking the difference between the largest number and 
    the smallest number until the nearest Kaprekar number is found.
- When considering the difference of new numbers, we save them in an array for later comparison. If 
    this difference is equal to the difference that is immediately preceding it, it is a Kaprekar 
        number, and if this difference is equal to the previous difference but is not adjacent, it is not a Kaprekar number.
- Kaprekar's number is divisible by 9, so it is possible to consider numbers divisible by 9 instead 
    of considering all numbers in turn, this way will save a lot of time.
- Kaprekar numbers can have the same number of digits, for example 549945 and 631764 will have the same
    6 digits. Therefore, all cases must be considered, if the result stops immediately, the result may be wrong
- For numbers with n digits, it is unlikely that Kaprekar numbers exist, for example Kaprekar numbers 
    do not have 5-digit numbers, so it is better to consider the larger case
- Looking at the given Kaprekar numbers, we see that most of the numbers have 4 digits in them, so 
    consider from 4*10^length -> 5*10^length to save time. It is possible to do this because when 
        taking the largest and smallest number, this digit 4 can be in any position instead of in the first position.
- Since all cases are considered, this algorithm is not suitable for very large numbers
'''


# The function checks if the input is an integer string or not
def is_all_digits(str):
    for char in str:
        if not char.isdigit():
            return False
    return True

# User must enter correct integer n(0 <= n <= 1000000000) for the program to execute
while True:
    # Input String
    inp = input()
    if is_all_digits(inp) == True:
        if int(inp) >= 0 and int(inp) <= 1000000000:
            break

# Convert input to integer
inp = int(inp)    

# Get the length of the input string - 1 for the program to perform the function
length = len(str(inp)) - 1

# Variable used to signal the end of the program
end = 0

# Variable that stores the found Kaprekar numbers
arr_num = []

while True:
    # If input = 0 it will always print the Kaprekar number as 0
    if inp == 0:
        arr_num.append(inp)
        break

    # Judging from the number 40...005 -> 49...995 with the distance between each number is 9
    for number in range((4*(10**length) + 5)//9, (5*(10**length) - 5)//9):
        number *= 9

        # Save the number value in the num variable so that the operation in the while loop does not change the number value
        num = number

        # Array that stores all the maximum and minimum differences when parsing step by step from number
        arr = []
        
        while True:
            # The variable k is used to mark whether the sign of the largest and the smallest number is really a Kaprekar number
            k = 0

            # Variable ind stores the index of the array arr, this index represents the value of the Kaprekar number in the array arr
            ind = 0

            # Change number to String to manipulate
            num_str = str(num)

            # Sort numbers into numbers with digits in descending order
            sort_str = sorted(num_str, reverse=True)
            result = int(''.join(sort_str))

            # Sort numbers into numbers with digits in ascending order
            sort_str_rv = sorted(num_str, reverse=False)
            result_rv = int(''.join(sort_str_rv))

            # Difference between largest and smallest number
            sub = result - result_rv

            arr.append(sub)

            # Assign the value of difference to the variable num to execute the next loop
            num = sub
        
            # The loop considers whether 2 equal differences are adjacent or not, if adjacent, assign k = 2, 
            # ind = x and terminate. Otherwise, assign k = 1 and finish
            for x in range(len(arr)-1):
                for y in range(x+1, len(arr)):
                    if arr[x] == arr[y]:
                        if x == y-1:
                            k = 2
                            ind = x
                        else:
                            k = 1
                        break
                if k != 0:
                    break
            if k == 2:
                # Check if the difference is less than the input, if it is less then it is not the number of Kaprekar to look for
                if arr[ind] < inp:
                    break
                else:
                    # Add Kaprekar numbers to array arr_num
                    arr_num.append(arr[ind])
                    end = 1
                    break
            if k == 1:
                break       

    # When considering all the numbers with length digits but no Kaprekar numbers, consider the number with length + 1 digit
    length += 1
    if end == 1:
        break
# Print the smallest number in the array, this number is the number Kaprekar needs to find
print(min(arr_num))
    

'''
***Test case:

input: 0
output: 0

input: 100
output: 495

input: 1000
output: 6174

input: 10000
output: 549945

input: 600000
output: 631764

input: 1000000
output: 63317664

input: 7000000
output: 97508421

input: 10000000
output: 554999445

input: 60000000
output: 864197532

input: 123
output: 495

input: -1
input: 1
output: 495

input: pq1
input: 1400
output: 6174

'''