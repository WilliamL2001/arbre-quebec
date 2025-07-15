from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/conifères')
def conifères():
    return render_template('conifères.html')

@app.route('/sapins')
def sapins():
    return render_template('sapins.html')  # crée un fichier page2.html dans templates/

@app.route('/épinettes')
def épinettes():
    return render_template('épinettes.html')  # crée un fichier page2.html dans templates/

@app.route('/mélèzes')
def mélèzes():
    return render_template('mélèzes.html')  # crée un fichier page2.html dans templates/

@app.route('/pins')
def pins():
    return render_template('pins.html')  # crée un fichier page2.html dans templates/

@app.route('/pruches')
def pruches():
    return render_template('pruches.html')  # crée un fichier page2.html dans templates/

@app.route('/thuyas')
def thuyas():
    return render_template('thuyas.html')  # crée un fichier page2.html dans templates/

@app.route('/genévriers')
def genévriers():
    return render_template('genévriers.html')  # crée un fichier page2.html dans templates/

@app.route('/feuillus')
def feuillus():
    return render_template('feuillus.html')

if __name__ == '__main__':
    app.run(debug=True)