from flask import Flask, render_template, request

import parseRDF as prdf

app = Flask(__name__)

parse = prdf.RDFbase()

@app.route('/', methods=['GET', 'POST'])
def index():
    pers_sel = None
    results = []
    if request.method == 'POST':
        pers_sel = request.form.get('pers_sel')
    # TO DEBUG
    print(f"Persona selezionata: {pers_sel}")
    
    results = parse.parse_rdf(pers_sel)

    return render_template('index.html', 
                            pers_sel=pers_sel, 
                            results=results)

if __name__ == '__main__':
    app.run(debug=True)
