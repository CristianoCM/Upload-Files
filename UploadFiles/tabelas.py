from peewee import SqliteDatabase, Model, CharField

db = SqliteDatabase('upload.db')

class Imagem(Model):
    caminho = CharField()
    nome = CharField()

    class Meta:
        database = db