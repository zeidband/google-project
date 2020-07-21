import read_data as r
import glob

def get_best_k_completions(string):
    # sentences = r.init_data(glob.glob("technology_texts/RFC/*.txt"))

    sentences = r.init_data(["technology_texts/python-3.8.4-docs-text/python-3.8.4-docs-text/about.txt"])
    sentence = input()

    while sentence != '#':
        flag = False

        try:
            set_id_sentences = sentences[sentence]

        except ValueError:
            flag = True

        if flag:
            return None

        else:
            max_5_list()


        sentence = input()
