import numpy as np
import epitran

from kolmogorov import normalized_information_distance
from levenshtein import levenshtein_distance
from phonetic_rules import phonetic

from parseWORD import RDFbase

def compute_distance(ref_people, words, threshold, method, phonetic_trans=False, custom_rules=False):
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
    phonetic: bool
        if True, the phonetic translitteration
        is applied to the input strings and
        then the distance is computed between
        the phonetic translitteration.
    custom_rules: bool
        if True, the custom rules (phonetic_rules)
        are used to hybridize the french (modern french
        plus the custom rules). If false the document
        is translated in modern french.

    Return:
    -----------
    res: (str) list (n, 3)
        list with ref_people the word
        compared and the corresponding distance
        minor or egual to the threshold 
    """
    ref_people_origin = ref_people
    words_origin = words

    # simple translitteration
    if(phonetic_trans):
        epi = epitran.Epitran('fra-Latn')
        ref_people = [epi.transliterate(person) for person in ref_people]
        words = [epi.transliterate(word) for word in words]

        # if custom rules included
        #
        # Concept used to include modern french
        # plus custom rules:
        # 
        # translate in modern french the text
        # AND the phonetic rules. Then replace
        # in the text translated character of
        # phonetic rules translated.
        #
        # text      ->        epitran(text)
        #                           |
        #                    text_replacement
        #                           |
        #                           v
        # phonetic_rules -> epitran(phonetic_rules)
        #
        if(custom_rules):
            custom_transliterate = {}
            for bef, aft in phonetic.items():
                custom_transliterate[bef] = epi.transliterate(aft)

                ref_people = [''.join(custom_transliterate.get(char, char) for char in peo) for peo in ref_people]
                words = [''.join(custom_transliterate.get(char, char) for char in word) for word in words]

        print("Transliteration done!")

    res = []
    if(method=="levenshtein"):

        for i, ref_per in enumerate(ref_people):
            print(i/len(ref_people)*100)
            for j, word in enumerate(words):
                distance = levenshtein_distance(ref_per, word)
                if(ref_per != word and distance < threshold):
                    print(ref_per, word, distance)
                    res.append([ref_people_origin[i], ref_per, words_origin[j], word, str(distance)])

    if(method=="kolmogorov"):

        for i, ref_per in enumerate(ref_people):
            print(i/len(ref_people)*100)
            for j, word in enumerate(words):
                distance = normalized_information_distance(ref_per, word)
                if(ref_per != word and distance < threshold):
                    #print(ref_per, word, distance)
                    res.append([ref_people_origin[i], ref_per, words_origin[j], word, str(distance)])

    return res

rdf = RDFbase()
words = rdf.parse_rdf_texte()
people = rdf.parse_rdf_personne()

res = compute_distance(people, words, 0.2, "kolmogorov", phonetic_trans=True, custom_rules=False)

np.savetxt("res_french.csv", res, fmt='%s', delimiter=',')