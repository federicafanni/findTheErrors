def findTheSyntaxErrors(): #Function that prints a broken piece of code and ask the user to enter the fixed version
                           #It loops until the correct string is entered
    print('FIND THE ERROR')
    print('Find all the syntax errors in the below sentence. Then type the correct sentence:')
    correctSentence = 'System.out.println("hello");' #In order for the loop to start, I am creating a variable for the correct sentence, which I'll need later when checking the user input,
    userInput = 'No sentence entered' #and I also need to assign a starting value to the user input, 
                                      #which at the beginning must be different from the correct sentence, otherwise the while loop won't start.

    while userInput != correctSentence: #The "not equal to" allows the loop to run, prompting the incorrect code to fix and asking the user for the correction.
        print('system.out.printLn("hello)')
        userInput = input('Enter fixed code: ')
        if userInput == correctSentence: #If the user types the correct sentence, hence userInput is equal to correctSentence, 
            print("That's right!")        #they'll be shown this message
        else: 
            correctSentenceSet = set(correctSentence)#Converting the string into a set in order to compare the 2 strings character by character.
            userInputSet = set(userInput)
            differences = correctSentenceSet.symmetric_difference(userInputSet)#This compares the two strings. I am assigning its result to the differences variable.
            totalDifferences = len(differences) # I am creating this variable so as to use it in the statement below. 
            print('Not quite right: ', totalDifferences, ' syntax error(s) to fix. Try again.')

if __name__ == "__main__":
    findTheSyntaxErrors()
