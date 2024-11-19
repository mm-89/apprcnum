import rdflib
import pprint
from scipy.spatial.distance import hamming

class RDFbase:
    """
    Description
    """
    # dorpdown menus
    categorie   = ['All', 'Personne', 'Object']
    ans         = ['All', '1545', '1546', '1547', '1548', '1549', '1550']

    # files location
    data_pers = "kb/graphe/personnes.ttl"
    data_1545 = "kb/graphe/RC1545.ttl"
    data_1546 = "kb/graphe/RC1546.ttl"
    data_1547 = "kb/graphe/RC1547.ttl"
    data_1548 = "kb/graphe/RC1548.ttl"
    data_1549 = "kb/graphe/RC1549.ttl"
    data_1550 = "kb/graphe/RC1550.ttl"
       
    def __init__(self):
        """
        Description
        """

        self.rdf_pers = rdflib.Graph()
        self.rdf_ans = rdflib.Graph()
        #self.rdf_ans_1545 = rdflib.Graph()

        self.rdf_pers.parse(self.data_pers, format='ttl')

        self.rdf_ans.parse(self.data_1545, format='ttl')
        self.rdf_ans.parse(self.data_1546, format='ttl')
        self.rdf_ans.parse(self.data_1547, format='ttl')
        self.rdf_ans.parse(self.data_1548, format='ttl')
        self.rdf_ans.parse(self.data_1549, format='ttl')
        self.rdf_ans.parse(self.data_1550, format='ttl')

    def parse_rdf_personne(self):
            """
            Description
            """

            query = """
            SELECT ?graphie
            WHERE {
                ?x :graphie ?graphie .
            }
            """ 
            return self.rdf_pers.query(query)

    def hamming_distance(word1, word2):
        """
        Description
        """
        word1 = word1.lower()
        word2 = word2.lower()
    
        word1_list = list(word1)
        word2_list = list(word2)
        
        return hamming(word1_list, word2_list)

    def parse_rdf_texte(self):
        """
        Esegui la query per ottenere il testo e stampalo.
        """
        
        query = """
        SELECT ?texte
        WHERE {
            ?seance a :Seance ;
                     :objet ?objet .
            ?objet :texte ?texte .
        }
        """
        
        return self.rdf_ans.query(query)

