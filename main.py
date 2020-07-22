import glob
from complete import Complete
from read_data import Data


def start():
    print("Loading the file and preparing the system...")

    # sentences = r.init_data(glob.glob("technology_texts/RFC/*.txt"))
    data = Data(["technology_texts/python-3.8.4-docs-text/python-3.8.4-docs-text/about.txt"])
    complete = Complete(data)

    print("The system is ready. Enter your text: ")

    sentence = input()

    while sentence != '#':
        complete.get_best_k_completions(sentence)

        if len(complete.suitable_sentences) != 0:
            for index in complete.suitable_sentences:
                print(complete.data.sentences[index])

        sentence = input("Enter your text: ")


if __name__ == '__main__':
    start()
