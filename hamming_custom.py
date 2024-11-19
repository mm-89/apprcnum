from scipy.spatial.distance import hamming

def hamming_distance(wordREF, word2):
    """
    Description
    """
    word1 = wordREF.lower()
    word2 = [word.lower() for word in word2]

    #word1_list = list(word1)
    #word2_list = list(word2)
    
    return hamming(word1, word2)

