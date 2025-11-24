import numpy as np


def bag_of_words(sentences):
    tokenized_sentences = [sentence.lower().split() for sentence in sentences]
 

    flat_words = [
        word for list in tokenized_sentences for word in list
    ]

    vocabulary = sorted(set(flat_words))
    indexed_words = {word: i for i, word in enumerate(vocabulary)}

    bow_matrix = np.zeros((len(sentences), len(vocabulary)), dtype=int)

    for i, sentence in enumerate(tokenized_sentences):
        for word in sentence: 
            if word in indexed_words:
                bow_matrix [i, indexed_words[word]] += 1

    return vocabulary, bow_matrix



corpus = ["Do you know Leonardo?", "Oh yes Leonardo is my favourite actor", "No, not the actor Leonardo, the artist!", "Oh! I thought about the actor, I do also know the artist"]

vocabulary , bow_matrix = bag_of_words(corpus)


print("Vocabulary:", vocabulary)
print("Bag-of-Words Matrix:\n", bow_matrix)