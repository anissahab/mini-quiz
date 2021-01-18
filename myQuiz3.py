
counterList = [0, 0, 0, 0]
answerList = ['A', 'B', 'C', 'D']
quizResultList = ['070 Shake', 'Caroline Polacheck', 'Jack Larsen', 'Planet 1999']


question1 = "Which of the following artists is your favourite?\nA: Ariana Grande\nB: Dua Lipa\nC: Taylor Swift\nD: Charli XCX"
question2 = "Which of the following artists is your favourite?\nA: Travis Scott\nB: Childish Gambino\nC: Mac Miller\nD: Brockhampton"
question3 = "Which of the following artists is your favourite?\nA: Kanye West\nB: Harry Styles\nC: Bon Iver\nD: The 1975"
question4 = "Which of the following artists is your favourite?\nA: SZA\nB: Billie Eillish\nC: Tyler the Creator\nD: The Weeknd"
question5 = "Which of the following artists is your favourite?\nA: Rihanna\nB: Halsey\nC: Lana Del Ray\nD: Lady Gaga"

finalAnswerSentence = 'The new artist that you should listen to is: '

def counterFunction():
    answer = input().upper()
    global counterList
    for i in answerList:
        if answer == i:
            counterList[answerList.index(i)] += 1
    return counterList


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

print(finalAnswerSentence + str(quizResultList[counterList.index(max(counterList))]))
