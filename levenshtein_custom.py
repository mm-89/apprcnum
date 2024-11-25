import Levenshtein

def levenshtein_distance(wordREF, word2):
    """
    Description
    """
    word1 = wordREF.lower()
    word2 = word2.lower()

    return Levenshtein.distance(word1, word2)
