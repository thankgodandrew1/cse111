positive = -1
negative = 1
def main():
    #prints guide on how to anwer questions in program
    print('This program is an implementation of the Rosenberg')
    print('Self-Esteem Scale. This program will show you ten')
    print('statements that you could possibly apply to yourself.')
    print('Please rate how much you agree with each of the')
    print('statements by responding with one of these four letters:')
    
    print()

    print('D means you strongly disagree with the statement.')
    print('d means you disagree with the statement.')
    print('a means you agree with the statement.')
    print('A means you strongly agree with the statement.')
    
    score = 0
    score += user_decision('1. I feel that I am a person of worth, at least equal plane with others. ', positive)
    score += user_decision('2. I feel that I have a number of good qualities. ', positive)
    score += user_decision('3. All in all, I am inclined to feel that I am a failure. ', negative)
    score += user_decision('4. I am able to do things as well as most other people. ', positive)
    score += user_decision('5. I feel I do not have much to be proud of. ', negative)
   
    score += user_decision ('6. I take a positive attitude toward myself. ', positive)
    score += user_decision('7. On the whole, I am satisfied with myself. ', positive)
    score += user_decision ('8. I wish I could have more respect for myself. ', negative)
    score += user_decision ('9. I certainly feel useless at times. ', negative)
    score += user_decision ('10. At times I think I am no good at all. ',negative)

    
    #PRINT
    #this part print result
    print(f'Your score is: {score}')
    print("A score below 15 may indicate problematic low self-esteem.")



def user_decision(statement, pos_or_neg):
    """Decides what value or score goes into users decisions """    
    
    print(statement)
    decisions = input('Enter, D, d, a, or A: ')

    score = 0
    if decisions == 'D':
        score = 0
    elif decisions == 'd':
        score = 1
    elif decisions == 'a':
        score = 2
    elif decisions == 'A':
        score = 3

    if pos_or_neg == negative:
        score = 3 - score

    return score

    #call main to execute program
main()