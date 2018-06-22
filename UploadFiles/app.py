#encoding: utf-8
from flask import Flask, render_template, request, redirect
from tabelas import Imagem
import os, datetime
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("upload-front.html")

@app.route("/upload-front/")
def upload():
    return render_template("upload-front.html")

@app.route("/salvar-arquivo/", methods=["POST"])
def salvar():
    file = request.files['arquivo']
    # filename = secure_filename(file.filename)

    ll = len(os.listdir("./static/Downloads")) + 1
    file.save(os.path.join("static/Downloads", "uploaded-img-" + str(ll) + ".jpg"))
    
    nova_img = Imagem.create(caminho = "static/Downloads", nome = "uploaded-img-" + str(ll) + ".jpg")
    nova_img.save()

    return redirect("/listar/", code=302)

@app.route("/listar/", methods=["GET"])
def listar():
    l = os.listdir("./static/Downloads")
    lista_com_tempos = [ ( os.path.getmtime("./static/Downloads/" + u), u ) for u in l ]
    lista_com_tempos.sort()
    return render_template("saved-front.html", lista = lista_com_tempos, horario = datetime.datetime.now())

@app.route("/apagar-imagem/<n>")
def apagar(n):
    os.unlink("./static/Downloads/" + n)
    im = Imagem.select().where(Imagem.nome == n).get()
    im.delete_instance()
    return redirect("/listar/", code=302)