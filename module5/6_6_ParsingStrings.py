# zyBooks 6.6 Warm up: Paring strings

# Set user input to a empty string in order to enter initial loop:
userInput = ''
'''
Best Practice 1: Simple is better than complex: I decided to initiate the user input to an empty string in order 
to enter the first loop one time only. Rather then doing any work outside of the loop I wanted the loop to take care 
of any future input.

Problem Solving 1: Initially I had the actual user input stored as the first part of the program. I later discovered 
that as the complexity of the program increased it became necessary to repeatedly ask for the same user input 
two more times.  Keeping the K.I.S.S principle in mind I knew there had to be a ask for the user input only one time
and reuse that input as needed. Nesting the user input prompt inside the outside while loop solved this problem  
'''

# Only enter outer while loop if 'q' has not been entered:
while userInput != 'q':
    '''
    Best Practice 2: Explicit is better than implicit: There is no other option the instructions are explicit
    and nothing else can be implied
    
    Problem Solving 2: Set the outer loop to let the program repeat until the required condition is met
    '''
    # Set our variable in scope that we will use to control our progress:
    userInput = input('Enter input string: \n')
    commaIndex = userInput.find(',')
    '''
    Problem Solving 3: I needed my user input and my check for the comma to be within the scope of the program.
    Placing these variable anywhere else in the program would not allow the while loops to execute accordingly. 
    '''
    # If there is no comma in the input, tell the user and try again
    while commaIndex == -1 and userInput != 'q':
        print('Error: No comma in string.')
        break
        '''
        Best Practice 3: Beautiful is better than ugly: I the simple while check and the break statement were terse
        and did the job with the least amount of code. I found this quite appealing. 
        
        Problem Solving 4: Check our outer loop requirements hadn't been met and that the presence of a comma was 
        missing. Let our user know that they have not met the requirments and break out of this loop to start all 
        over again and let the user have another chance to input the required data
        '''
    # If we reach this point in the program do the work to format our output and print it to the screen
    if commaIndex != -1:
        '''
        Best Practice 4: Errors should never pass silently: By forcing the input data to be exactly as we require
        no unanticipated element could be entered into our code that could have undesired consequences later on.
        
        Problem Solving 5: This is where the bulk of the work would be done if the requirements of the program had been
        met at this point. We split the input on the required comma, strip and leading or trailing white space for the
        desired output and use the proper conversion specifiers to print the desired output
        '''
        userInput = userInput.split(',')
        firstWord = userInput[0].strip()
        secondWord = userInput[1].strip()
        print('First word: %s' % firstWord)
        print('Second word: %s' % secondWord)
        print('\n')

'''
Algorithm and Data Structure: I chose to incorporate 2 while loops and one if condition. I found this to be the most 
efficient algorithm to solve this problem. My thought process was:
1. Outer while loop - Terminating the program when 'q' is entered would require that the program continue to execute 
until this condition is met. That seemed to fit the requirements of a while loop, the program could continue 
without any decision making until the specified condition was met. 
2. Inner while loop - Once again the program required a repeated action until a condition was met. At this point I
could check if the inner loop and outer loop conditions were True. If so, the required output would print, break out
of the inner loop let the rest of the program evaluate the if statement to false, the outer loop would still evaluate
to True and the user would get another chance to meet the programs requirements. 
3. By taking care of all the data checking in the while loops a single if statement could take care of the rest of the
programs requirements. 
'''
