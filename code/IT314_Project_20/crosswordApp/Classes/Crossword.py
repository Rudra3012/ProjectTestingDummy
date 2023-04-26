import datetime
import uuid


class gridCell:
    x: int
    y: int
    value: str

    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value


class Crossword:

    creator: str
    title: str
    description: str
    width: int
    height: int
    AnswersHor = []
    AnswersVer = []
    cluesHor = []
    cluesVer = []
    AnswersHorStart = []
    AnswersVerStart = []
    timeOfCreation: str
    clueAnswers = {}
    grid = []
    timesRating: int
    rating: int
    timesSolved: int
    avgTime = 0
    def __init__(self, creator, title, description, width, height, cluesVer, cluesHor, WordsUp, WordsDown, gridList, AnswersHorStart, AnswersVerStart):

        self.creator = creator
        self.title = title
        self.description = description
        self.width = width
        self.height = height
        self.AnswersHor = WordsUp
        self.AnswersVer = WordsDown
        self.grid = gridList
        self.cluesHor = cluesHor
        self.cluesVer = cluesVer
        self.AnswersHorStart = AnswersHorStart
        self.AnswersVerStart = AnswersVerStart
        self.timeOfCreation = datetime.datetime.now()
        self.timesSolved = 0
        self.timesRating = 0
        self.rating = 0
        self.avgTime = 0

    def __str__(self):
        return f"Crossword: {self.title}"
