from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
import os
import smtplib

app = Flask(__name__)

# Configurações do Flask-Mail
app.config['MAIL_SERVER'] = 'mail.aboch.com.br'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'leonan.leyedecker@aboch.com.br'
app.config['MAIL_PASSWORD'] = 'Powerguido@1!'
app.config['MAIL_DEFAULT_SENDER'] = 'leonan.leyedecker@aboch.com.br'

mail = Mail(app)

@app.route("/")

def Home():
    return render_template ("index.html")

@app.route("/Sobre")

def Sobre():
    return "<h2>Sobre</h2>"

@app.route("/Noticias")

def Noticias():
    return "<h2>Novidades e Noticiais</h2>"

@app.route("/Contato", methods=['GET', 'POST'])
def Contato():
    if request.method == "GET":
        return render_template('contato.html')
    else:
        nome = request.form.get('nome''')  
        sobrenome = request.form.get('sobrenome')
        idade = request.form.get('idade''')  
        cidade = request.form.get('cidade')
        numero = request.form.get('contato')
        reclamacao = request.form.get('reclamacão''')
        try:
            server = smtplib.SMTP(app.config['MAIL_SERVER'], app.config['MAIL_PORT'])
            server.ehlo()
            server.starttls()
            server.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
            server.quit()
        except smtplib.SMTPException as e:
            return f"Falha na conexão SMTP: {e}"


         # Envia o email
        msg = Message(subject="Formulário de Contato",
                      recipients=["leonamleyedecker96@gmail.com"],  # Troque pelo email do destinatário
                      body=f"Nome: {nome}\nSobrenome: {sobrenome}\nIdade: {idade}\ncontato: {Contato}\nCidade: {cidade}\nReclamação: {reclamacao}")

        mail.send(msg)

        return redirect(url_for('Contato'))
        # return f"Preenchimento Do Formulario:<br> Nome: {nome},<br> Sobrenome: {sobrenome},<br> Idade: {idade},<br>Cidade: {cidade},<br>Reclamacão:  {reclamacao}"
#versao da video aula : return " Preenchimento Do Formulario:  "  +request.form['nome']  +request.form['idade']   # Retorna o valor do campo 'nome'
      
      
       


        