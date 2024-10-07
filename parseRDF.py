import rdflib
import pprint

class RDFbase:
    
    def __init__(self):

        data = "kb/graphe/personnes.ttl"

        self.rdf = rdflib.Graph()
        self.rdf.parse(data, format='ttl')

    def parse_rdf(self, keyword):
        # TO DEBUG
        # print(f"Cercando varianti per: {keyword}")

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
        
        # PER DEBUG
        #if qres:
        #    for row in qres:
        #        print(f"Graphie: {row.graphie}, Variante: {row.variante}")
        #else:
        #    print("La parola non ha varianti.")
    
        return self.rdf.query(query)
