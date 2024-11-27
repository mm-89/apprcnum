import Levenshtein

def levenshtein_distance(word1, word2):
    """
    Description

    
    results:
    0 -> means identical strings
    1 -> means completely (?) different strings
    """
    return Levenshtein.distance(word1, word2) / max(len(word1), len(word2))