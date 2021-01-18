# All of the items at the same index correspond with each other
# So if mostly A's are selected, the resulting answer will be the item from the result list with the same index as A
# and every time A is selected, the counterList increases by 1 at the same index that A is located at 
counterList = [0, 0, 0, 0]
answerList = ['A', 'B', 'C', 'D']
quizResultList = ['070 Shake', 'Caroline Polacheck', 'Jack Larsen', 'Planet 1999']

# All of the questions 
question1 = "Which of the following artists is your favourite?\nA: Ariana Grande\nB: Dua Lipa\nC: Taylor Swift\nD: Charli XCX"
question2 = "Which of the following artists is your favourite?\nA: Travis Scott\nB: Childish Gambino\nC: Mac Miller\nD: Brockhampton"
question3 = "Which of the following artists is your favourite?\nA: Kanye West\nB: Harry Styles\nC: Bon Iver\nD: The 1975"
question4 = "Which of the following artists is your favourite?\nA: SZA\nB: Billie Eillish\nC: Tyler the Creator\nD: The Weeknd"
question5 = "Which of the following artists is your favourite?\nA: Rihanna\nB: Halsey\nC: Lana Del Ray\nD: Lady Gaga"

finalAnswerSentence = 'The new artist that you should listen to is: '

# function that keeps track of all of the multiple choice responses
def counterFunction():
    answer = input().upper()
    global counterList
    for i in answerList:
        if answer == i:
            counterList[answerList.index(i)] += 1
    return counterList

# The quiz 
print(question1)
counterFunction()

print(question2)
counterFunction()

print(question3)
counterFunction()

print(question4)
counterFunction()

print(question5)
counterFunction()

# Print results 
print(finalAnswerSentence + str(quizResultList[counterList.index(max(counterList))]))
