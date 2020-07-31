from complete import Complete
from read_data import Data
import os
import string

def get_file_list(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))

    return file_list

def start():
    print("Loading the files and preparing the system...")

    files_list = get_file_list("technology_texts/python-3.8.4-docs-text/python-3.8.4-docs-text/c-api")
    # files_list = get_file_list("technology_texts/python-3.8.4-docs-text/python-3.8.4-docs-text/whatsnew")
    complete = Complete(Data(files_list))

    # complete = Complete(Data(["technology_texts/python-3.8.4-docs-text/python-3.8.4-docs-text/about.txt"]))

    print("The system is ready.")

    input_ = ' '.join((''.join(i for i in input("\n\nEnter your text: ") if i in string.ascii_letters + ' ')).split())

    while(1):
        text = " "

        while text[-1] != '#':
            match_sentences = complete.get_best_k_completions(input_)

            if len(match_sentences) != 0:
                for sentence in match_sentences:
                    print(f"{sentence.completed_sentence} ({files_list[sentence.source_text]} {sentence.offset})")
            else:
                print("there is no items")

            # print(input_, end="")
            text = input(input_)
            input_ += ' '.join((''.join(i for i in text if i in string.ascii_letters + ' ')).split())

        input_ = ' '.join((''.join(i for i in input("\n\nEnter your text: ") if i in string.ascii_letters + ' ')).split())


if __name__ == '__main__':
    start()
