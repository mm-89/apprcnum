from flask import Flask, render_template, request

import parseRDF as prdf

app = Flask(__name__)

parse = prdf.RDFbase()

@app.route('/', methods=['GET', 'POST'])
def index():

    cat_select = None
    an_select = None
    pers_sel = None
    results = []

    if request.method == 'POST':
        pers_sel = request.form.get('pers_sel')
        cat_select = request.form.get('cat_select')
        an_select = request.form.get('an_select')

    # TO DEBUG
    print(f"Persona selezionata: {pers_sel}")
    print(f"Categoria selezionata: {cat_select}")   
    print(f"Anno selezionato: {an_select}")
    
    # "All" selection deactivated so far
    if(cat_select == "Personne"):
        results = parse.parse_rdf_personne(pers_sel)
    if(cat_select == "Object"):
        if(an_select == '1545'):
            results = parse.parse_rdf_ans(['1545'], pers_sel)
        elif(an_select == '1546'):
            results = parse.parse_rdf_ans(['1546'], pers_sel) 
        elif(an_select == '1547'):
            results = parse.parse_rdf_ans(['1547'], pers_sel)
        elif(an_select == '1548'):
            results = parse.parse_rdf_ans(['1548'], pers_sel) 
        elif(an_select == '1549'):
            results = parse.parse_rdf_ans(['1549'], pers_sel)
        elif(an_select == '1550'):
            results = parse.parse_rdf_ans(['1550'], pers_sel) 
        if(an_select == 'All'):
            results = parse.parse_rdf_ans(['1545', 
                                            '1546', 
                                            '1547', 
                                            '1548', 
                                            '1549', 
                                            '1550'], pers_sel) 
    
    return render_template('index.html', 
                            pers_sel=pers_sel, 
                            results=results,
                            categorie=parse.categorie,
                            ans=parse.ans)

if __name__ == '__main__':
    app.run(debug=True)
