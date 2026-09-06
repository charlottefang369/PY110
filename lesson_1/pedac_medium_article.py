# This PEDAC practice problem is from the LS medium article: 
# https://medium.com/launch-school/solving-coding-problems-with-pedac-29141331f93f

# Note:
#   - I added few more test cases 
#   - there is no coding example for Python from the article. 



# Problem: 
# Suppose you have an arbitrary natural number (the target) and a set of one or more additional natural numbers (the factors). Write a program that computes the sum of all numbers from 1 up to the target number that are also multiples of one of the factors. 

# For instance, if the target is 20, and the factors are 3 and 5, that gives us the list of multiples 3, 5, 6, 9, 10, 12, 15, 18. The sum of these multiples is 78.
# If no factors are given, use 3 and 5 as the default factors.


# - input: 
#     - an integer (arbitrary, natuarl number) 
#     - a set of one or more additional integer (natural numbers; the factors)
# - output: sum of all numbers from 1 up to the target number that are also multiples of one of the factors. 

# - explicit: 
#     - The selected numbers are: 
#         - all numbers from 1 up to the target number 
#         - multiples of one of the factors (no need to be both)
#         - if no factors are given use 3 and 5 as the default factors
# - implicit: 
#     - the target number is exclusive 
#     - The multiples to be summed must be unique.

# - test cases: 


# - data structure 
#     1. initialize a empty list to hold the selected numbers 
#     2. create a sequence of numbers starting from 1 through the target number 
#     3. check if there are factors provided if none, set the factors to 3 and 5.
#     4. starting with the first number, check if the number in the sequence is a multiple of the factor(s)
#           - If yes, check if the number is not already in the list
#               If yes, add the number to the list 
#     5. repeat step 3 and 4, until all the numbers in sequence are checked
#     6. sum all the number in the list 


def sum_of_multiples(target_number, factors): 
    multiples = [] 

    for num in range(1, target_number): 
        if factors == []: 
            if num % 3 == 0 or num % 5 == 0: 
                if num not in multiples: 
                    multiples.append(num)
        else: 
            for factor in factors:
                if num % factor == 0: 
                    if num not in multiples: 
                        multiples.append(num)
          
    return sum(multiples)



print(sum_of_multiples(20, [3, 5]) == 78) #True 
print(sum_of_multiples(20, [17, 18]) == 35) #True 
print(sum_of_multiples(20, [3]) == 63) #True 
print(sum_of_multiples(20, [5]) == 30) #True 
print(sum_of_multiples(20, []) == 78) #True 
print(sum_of_multiples(1, []) == 0) #True 
print(sum_of_multiples(2, []) == 0) #True 
print(sum_of_multiples(1, [1]) == 0) #True 
print(sum_of_multiples(2, [1]) == 1) #True 
print(sum_of_multiples(20, [19]) == 19) #True 