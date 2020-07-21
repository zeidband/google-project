
from dataclasses import dataclass


@dataclass
class AutoCompleteData:

    def __init__(self, sentence, source_text, offset, score):
        self.__completed_sentence = sentence
        self.__source_text = source_text
        self.__offset = offset
        self.__score = score

