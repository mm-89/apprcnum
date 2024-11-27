import numpy as np

from kolmogorov import normalized_information_distance
from levenshtein import levenshtein_distance

from parseWORD import RDFbase

def compute_distance(ref_people, words, threshold, method):
    """
    Compute distance between each ref_people
    and all words on a text.

    Parameters:
    -----------
    ref_people: (str) list
        string list of reference name

    words: (str) list
        string of all the words we want
        to compare with ref_people

    threshold: int
        threshold value 

        (kolmokorov ~ 0.2 or less is good;
        levenshtein ~ 0.2 or less is good)

    method: str
        method used to compute distance.
        Avaiable:
            - kolmogorov
            - levenshtein

    Return:
    res: (str) list (n, 3)
        list with ref_people the word
        compared and the corresponding distance
        minor or egual to the threshold 
    """
    res = []
    if(method=="levenshtein"):

        for i, ref_per in enumerate(people):
            print(i/len(people)*100)
            for word in words:
                distance = levenshtein_distance(ref_per, word)
                if(ref_per != word and distance < threshold):
                    print(ref_per, word, distance)
                    res.append([ref_per, word, str(distance)])

    if(method=="kolmogorov"):

        for i, ref_per in enumerate(people):
            print(i/len(people)*100)
            for word in words:
                distance = normalized_information_distance(ref_per, word)
                if(ref_per != word and distance < threshold):
                    print(ref_per, word, distance)
                    res.append([ref_per, word, str(distance)])

    return res

rdf = RDFbase()
words = rdf.parse_rdf_texte()
people = rdf.parse_rdf_personne()

compute_distance(people, words, 0.2, "kolmogorov")

# np.savetxt("part1_0.2.csv", res, fmt='%s', delimiter=',')