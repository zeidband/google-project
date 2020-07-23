from complete import Complete
from read_data import Data
import os

def get_file_list(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))

    return file_list

def start():
    print("Loading the file and preparing the system...")

    files_list = get_file_list("technology_texts")
    # ["technology_texts/python-3.8.4-docs-text/python-3.8.4-docs-text/about.txt"]
    complete = Complete(Data(files_list))

    print("The system is ready.\n\nEnter your text: ")

    sentence = input()

    while sentence != '#':
        match_sentences = complete.get_best_k_completions(sentence)

        if len(match_sentences) != 0:
            for sentence in match_sentences:
                print(sentence.get_complete_sentences() + " - " + str(sentence.get_score()))

        else:
            print("there is no items")

        sentence = input("\n\nEnter your text: ")


if __name__ == '__main__':
    start()
