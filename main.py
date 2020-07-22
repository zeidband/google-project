import glob
from complete import Complete
from read_data import Data


def start():
    print("Loading the file and preparing the system...")

    # sentences = r.init_data(glob.glob("technology_texts/RFC/*.txt"))
    complete = Complete(Data(["technology_texts/python-3.8.4-docs-text/python-3.8.4-docs-text/about.txt"]))

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
