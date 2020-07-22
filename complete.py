import string

def delete_character(input_, sentences):
    for i in range(len(input_)):
        if input_[:i] + input_[i + 1:] in sentences.keys():
            print("FOR DEBUG: delete sentence")
            return sentences[input_[:i] + input_[i + 1:]], i

    return None, -1


def replace_character(sentence, sentences):
    result = set()
    for letter in string.ascii_letters:
        for character in range(len(sentence)):
            change_sentence = sentence[:character] + letter + sentence[character + 1:]
            if change_sentence in sentences.keys():
                result.union(sentences[change_sentence])
                if len(result) >= 5:
                    return result[:5]

def get_best_k_completions(sentence, data, sentences):
    # check if the sentence is complete in the data
    if sentence in sentences.keys():
        return sentences[sentence]

    # else try to delete character
    set_id_sentences, key = delete_character(sentence, sentences)
    if set_id_sentences is not None:
        return set_id_sentences
    # TODO: check if the answer len = 5

    replace_character(sentence, sentences)

    return None
