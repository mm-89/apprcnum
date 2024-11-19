import numpy as np

from parseWORD import RDFbase
from hamming_custom import hamming_distance
from levenshtein_custom import levenshtein_distance

rdf = RDFbase()
result = rdf.parse_rdf_texte()
people = rdf.parse_rdf_personne()

words = []
for row in result:
    texte = row['texte']
    if texte:
        words.append(texte.split())
        #print(words)

persons = []
for row in people:
    texte = row['graphie']
    if texte:
        person_temp = texte.split()
        persons.append(person_temp[0])
        

val_distance = []
val_word = []
for ref in persons:
    print(f"Reference person: {ref}")
    for word in words:
        distance = levenshtein_distance(ref, word)
        #val_distance.append(distance)
        if distance < 4:
                val_word.append([ref, word])

for i in val_word:
    print(i)
