class Question:
    # aşağıda question class'ımıza ait field'lar tanımlandı
    def __init__(self, text, choices, answers):  # constructor
        self.text = text
        self.choices = choices
        self.answers = answers

    def checkAnswer(self, answers):  # cevabı kontrol eder
        return self.answers == answers


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionsIndex = 0

    def getQuestion(self):  # soruları liste halinde getirir
        return self.questions[self.questionsIndex]

    def displayQuestions(self):  # soruyu ve numarasını gösterir
        question = self.getQuestion()
        print(f'Soru {self.questionsIndex + 1}: {question.text}')

        for q in question.choices:
            print('-' + q)

        answer = input('cevap: ')  # cevabı yazdığımız yer
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):  # tahmin etmeyi sağlar
        question = self.getQuestion()

        if question.checkAnswer(answer):  # cevabı kontrol eder
            self.score += 1
            self.questionsIndex += 1
        else:
            self.score -= 0.25
            self.questionsIndex += 1

    def loadQuestion(self):  # kaçıncı soruda olduğumuzu gösterir
        if len(self.questions) == self.questionsIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestions()

    def showScore(self):  # en sonda score'u gösterir
        print('score: ', self.score)

    def displayProgress(self):  # quizi bitirip bitirmediğimizi ve final skorumuzu gösterir
        totalQuestions = len(self.questions)
        questionNumber = self.questionsIndex + 1

        if questionNumber > totalQuestions:
            print('Quiz bitti')
        else:
            print(f'Question {questionNumber} of {totalQuestions}'.center(100, '*'))


# sorular tanımlandı
q1 = Question('en iyi programlama dili hangisidir ?', ['C#', 'python', 'javascript', 'java'], 'python')
q2 = Question('en popüler programlama dili hangisidir ?', ['python', 'javascript', 'C#', 'java'], 'python')
q3 = Question('en çok kazandıran programlama dili hangisidir ?', ['C#', 'javascript', 'java', 'python'], 'python')
q4 = Question('en çok sevilen programlama dili hangisidir ?', ['C#', 'javascript', 'java', 'python'], 'python')
q5 = Question('en kolay programlama dili hangisidir ?', ['C#', 'javascript', 'java', 'python'], 'python')

# soruları listeye ekledik
questions = [q1, q2, q3, q4, q5]

# sorular quiz'e eklendi
quiz = Quiz(questions)

# quiz çalıştırıldı
quiz.loadQuestion()
