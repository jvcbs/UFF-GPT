from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from flask import redirect
from flask import url_for
from flask import session
import flask
import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database= 'bdlogins'
)

cursor = conexao.cursor()

app = Flask(__name__,static_folder='static')
idlogado = 0

@app.route("/", methods=['GET','POST'])
def homepage():
    if flask.request.method == 'POST':
        
        if 'id' in session:                                             #Trabalhando logado e armazenando as respostas
            fk_id_question = request.json['fk_id_question']
            id_user = session['id']
            comando = f"INSERT INTO user_questions (fk_id_user, fk_question) VALUES ({id_user}, {fk_id_question}) "
            cursor.execute(comando)
            conexao.commit()
            
            
            comando = f"SELECT answers FROM questions where id_questions = {fk_id_question} "
            cursor.execute(comando)    
            resultado = cursor.fetchall()

            resposta = resultado[0][0]
            
            return resposta
        
    return render_template("index.html")

@app.route("/login", methods=['GET','POST'])
def loginpage():
    
    if flask.request.method == 'POST':
    
        user = request.form.get('usuário')
        senha = request.form.get('senha')
        #READ
        comando = f"SELECT id_login, user_login, user_password FROM login_db WHERE user_login = '{user}' AND user_password = '{senha}'"
        cursor.execute(comando)
        resultado = cursor.fetchall()
        print(resultado)

        

        if len(resultado)!=0:
            flash("Olá " + str(resultado[0][1]) + "!\nSeja bem-vindo", "sucesso")
            session['id'] = resultado[0][0]
            return redirect(url_for("homepage"))
        
        else:
            flash("Login inválido! Tente novamente...", "erro")
            return render_template("login.html")
    else:
        return render_template("login.html")

        

    


@app.route("/cadastro")
def cadastrarpage():
    return render_template("cadastro.html")

@app.route("/cadastro", methods=['POST'])
def cadastro():
    
    user = request.form.get('usuário')
    senha = request.form.get('senha')
    confirmar_senha = request.form.get('conf_senha')
    

    if senha != confirmar_senha:
        flash("As senhas não estão iguais." , "erro")
        return render_template("cadastro.html")


    #READ
    comando = f"SELECT user_login FROM login_db WHERE user_login = '{user}'"
    cursor.execute(comando)
    resultado = cursor.fetchall()

    if len(resultado) != 0:
        flash("Usuario já cadastrado", "erro")
        return render_template("cadastro.html")

    else:
        # Senhas são iguais, faça o cadastro no BD
        nome_user = user
        senha_user = senha
        comando = f'INSERT INTO login_db (user_login, user_password) VALUES ("{nome_user}", "{senha_user}") '
        cursor.execute(comando)
        conexao.commit()

        flash("Cadastro bem sucedido!", 'sucesso')

        return redirect(url_for("homepage"))



if __name__ == "__main__":
    app.secret_key='2345'
    app.run(debug=True)   