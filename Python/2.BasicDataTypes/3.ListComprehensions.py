#!/user/bin/env python3

# The simplest form of a list comprehension is: 
# [ expression-involving-loop-variable for loop-variable in sequence ] 
# ListOfNumbers = [ x for x in range(10) ]
#============================================================================================================================
# nested list comprehension
# [ expression-involving-loop-variables for outer-loop-variable in outer-sequence for inner-loop-variable in inner-sequence ] 
# results = []
# for outer_loop_variable in outer_sequence:
#         for inner_loop_variable in inner_sequence:
#                     results.append( expression_involving_loop_variables )
#=============================================================================================================================
# list comprehension with a filter 'if'
# [ expression-involving-loop-variable for loop-variable in sequence if boolean-expression-involving-loop-variable ] 
# ListOfThreeMultiples = [x for x in range(10) if x % 3 == 0]

if __name__ == '__main__':
    X = int(input()) + 1
    Y = int(input()) + 1
    Z = int(input()) + 1
    N = int(input())

    ListOfCuboids = [[x,y,z] for x in range(X) for y in range(Y) for z in range(Z) if (x+y+z) is not N]
    print(ListOfCuboids)
