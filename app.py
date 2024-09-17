from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Anni di nascita che puoi selezionare
    birth_years = list(range(1950, 2025))

    if request.method == 'POST':
        selected_year = request.form.get('birth_year')
        return "Hai selezionato l'anno di nascita: {}".format(selected_year)

    return render_template('index.html', birth_years=birth_years)

if __name__ == '__main__':
    app.run(debug=True)
