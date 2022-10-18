from flask_app.config.mysqlconnection import connectToMySQL


class User:
    
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['name']
        self.idioma = data['idioma']
        self.ubicacion = data['ubicacion']
        self.comentario = data['comentario']
        self.created_at = data ['created_at']
        self.update_at = data ['update_at']

    

    @staticmethod
    def validar_user(formulario):
        se_valida =True
        if len(formulario['name'])<8:
            flash('Nombre debe contener al menos 8 caracteres','prosess')
            se_valida = False
        if len(formulario['language'])<1:
            flash('Seleccione un idioma','prosess')
            se_valida = False
        return se_valida

    @classmethod
    def guardar(cls, formulario):
        query= "INSERT INTO dojos (nombre, ubicacion, idioma, comentario) VALUES (%(nombre)s, %(ubicacion)s, %(idioma)s, %(comentario)s)"
        result = connectToMySQL('encuesta_dojo').query_db(query, formulario)
        return result  
