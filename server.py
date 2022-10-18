from flask import Flask, render_template, request, redirect
#from mysqlconnection import connectToMySQL

#from users import User

app = Flask(__name__)

@app.route('/')
def index():
    query = "SELECT * FROM users"
    results = connectToMySQL('encuesta_Dojo').query_db(query) # ejecuta el query que tenemos en la variable query
    return results

@app.route('/result')
def index():
    query = "SELECT * FROM users"
    results = connectToMySQL('encuesta_Dojo').query_db(query) # ejecuta el query que tenemos en la variable query
    return results
    # INTERPOLACION :  %(LLAVE)S
    #query = "INSERT INTO users(first_name, last_name, email) VALUES ( %(first_name)s, %(last_name)s, %(email)s )" # Esto es una interpolación 
    # La interpolación interpreta un diccionario y a travez de eso le podemos dar le valor de la llave del diccionario,
    #  esto evita que personas maliciosas entren a la base de datos 
    #result = connectToMySQL('esquema_usuarios').query_db(query, data)
    #return "Nicolas registrado"











if __name__=="__main__":
    app.run(debug=True)