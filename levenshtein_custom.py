import Levenshtein

def levenshtein_distance(wordREF, word2):
    """
    Description
    """
    word1 = wordREF.lower()
    word2 = [word.lower() for word in word2]

    return Levenshtein.distance(word1, word2)
