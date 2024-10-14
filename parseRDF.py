import rdflib
import pprint

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

    def parse_rdf_ans(self, an, keyword):
        """
        Description
        """
        
        ans = ', '.join(f'"{a}"' for a in an)

        query = f"""
        SELECT ?seance ?date ?label ?texte
        WHERE {{
            ?seance a :Seance ;
             rdfs:label ?label ;
             :date ?date ;
             :objet ?objet .
            ?objet :texte ?texte .
            FILTER(CONTAINS(?texte, "{keyword}"))
            FILTER(SUBSTR(STR(?date), 1, 4) IN ({ans}))
        }}
        """
        return self.rdf_ans.query(query)


    def parse_rdf_personne(self, keyword):
        """
        Description
        """

        query = f"""
        SELECT ?graphie ?variante
        WHERE {{
            ?x :graphie ?graphie .
                OPTIONAL {{
            ?x :variante ?variante .
        }}
            FILTER(STR(?graphie) = "{keyword}")
        }}
        """ 
        return self.rdf_pers.query(query)
