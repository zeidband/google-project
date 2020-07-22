
from dataclasses import dataclass


@dataclass
class AutoCompleteData:
    """source_text, offset,"""
    def __init__(self, sentence, score):
        self.__completed_sentence = sentence
        # self.__source_text = source_text
        # self.__offset = offset
        self.__score = score

    def addScore(self, num):
        self.__score += num

