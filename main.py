import glob
import complete as c
from read_data import init_data

def start():
    print("Loading the file and preparing the system...")
    # sentences = r.init_data(glob.glob("technology_texts/RFC/*.txt"))
    data, sentences = init_data(["technology_texts/python-3.8.4-docs-text/python-3.8.4-docs-text/about.txt"])

    print("The system is ready. Enter your text: ")

    sentence = input()

    while sentence != '#':
        auto_complete = c.get_best_k_completions(sentence, data, sentences)

        if auto_complete is not None:
            for index in auto_complete:
                print(data[index])

        sentence = input()


if __name__ == '__main__':
    start()
