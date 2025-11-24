import numpy as np

def one_hot_encoding(sentence):
    words = sentence.lower().split()
    vocabulary = sorted(set(words))

    word_to_index = {words:i for i, words in enumerate(vocabulary)}
    one_hot_matrix = np.zeros((len(words), len(vocabulary)), dtype=int)

    for i, words in enumerate(words):
        one_hot_matrix[i, word_to_index[words]] = 1

    return one_hot_matrix, vocabulary



sentence = "I am confused of what to do next, is it the end of the world? or a start of something new?"

one_hot_matrix, vocabulary = one_hot_encoding(sentence)
print("Vocabulary:", vocabulary)
print("One-hot Encoded Matrix:\n", one_hot_matrix)