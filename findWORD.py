import numpy as np

from parseWORD import RDFbase
from hamming_custom import hamming_distance
from levenshtein_custom import levenshtein_distance

rdf = RDFbase()
result = rdf.parse_rdf_texte()
people = rdf.parse_rdf_personne()

phrases = []
for row in result:
    row_temp = row['texte']
    if row_temp:
        phrases.append(row_temp.split())

phrases = phrases[:int(len(phrases)/2)]

persons = []
for row in people:
    texte = row['graphie']
    if texte:
        person_temp = texte.split()
        persons.append(person_temp[0])

res = []
for i, ref in enumerate(persons):
    print(i/len(persons)*100)
    #print(f"Reference person: {ref}")
    for phrase in phrases:
        for word in phrase:
            word = word.rstrip('.')
            word = word.rstrip(',')
            distance = levenshtein_distance(ref, word)/max(len(ref), len(word))
            if(distance < 0.2 and distance > 0.0):
                print(ref, word, distance)
                res.append([word, str(distance)])

np.savetxt("part1_0.2.txt", res, fmt='%s', delimiter='\t')

