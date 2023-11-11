from flask import Flask, render_template, redirect, session
from session_config import configure_session
from sorteador import ALFABETO, sortearLetra

app = Flask(__name__)
configure_session(app)

@app.route('/')
def inicial():
    if 'alfabeto' in session:
      return redirect('/menu')
    return render_template('inicial.html')

@app.route('/menu')
def menu():
   if 'letras_sorteadas' not in session:
      session['alfabeto'] = ALFABETO
      session['letras_sorteadas'] = []
   return render_template('menu.html')

@app.route('/letra_sorteada')
def sorteio():
   letra = sortearLetra(alfabeto=session['alfabeto'],letras_sorteadas=session['letras_sorteadas'])

   if letra:
    return render_template('sorteio.html',letra=letra)
   else: 
    return redirect('/historico')

@app.route('/historico')
def historico():
   return render_template('historico.html',letras_sorteadas=session['letras_sorteadas'], alfabeto=session['alfabeto'])

@app.route('/finalizar')
def finalizar():
   session.clear()
   return redirect('/')

if __name__ == "__main__":
  app.run(debug=True)