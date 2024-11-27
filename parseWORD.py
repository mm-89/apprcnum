import rdflib
import re

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
           
        # write the query
        query = """
        SELECT ?graphie
        WHERE {
            ?x :graphie ?graphie .
        }
        """ 

        # evaluate the query
        res = self.rdf_pers.query(query)
        
        # return the list
        return [row[0].lower() for row in res if row['graphie']]

    def parse_rdf_texte(self):
        """
        Description
        """
        
        # write the query
        query = """
        SELECT ?texte
        WHERE {
            ?seance a :Seance ;
                     :objet ?objet .
            ?objet :texte ?texte .
        }
        """
        
        # evaluate the query
        res = self.rdf_ans.query(query)

        # create a list of prashes
        res_list = [row[0] for row in res if row['texte']]

        res_list_clean = [re.findall(r'\b\w+\b', word) for word in res_list]

        # return the list of words
        return [item.lower() for sublist in res_list_clean for item in sublist]