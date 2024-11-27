import rdflib
import pprint
from scipy.spatial.distance import hamming

class RDFbase:
    """
    Description
    """
    
    # write here the path of rcnum-main folder
    path = "../rcnum-main/"

    # files location
    data_pers = f"{path}kb/graphe/personnes.ttl"
    data_1545 = f"{path}kb/graphe/RC1545.ttl"
    data_1546 = f"{path}kb/graphe/RC1546.ttl"
    data_1547 = f"{path}kb/graphe/RC1547.ttl"
    data_1548 = f"{path}kb/graphe/RC1548.ttl"
    data_1549 = f"{path}kb/graphe/RC1549.ttl"
    data_1550 = f"{path}kb/graphe/RC1550.ttl"
       
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

