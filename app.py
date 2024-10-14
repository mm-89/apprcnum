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
        results = parse.parse_rdf_ans(pers_sel) 
    
    return render_template('index.html', 
                            pers_sel=pers_sel, 
                            results=results,
                            categorie=parse.categorie,
                            ans=parse.ans)

if __name__ == '__main__':
    app.run(debug=True)
