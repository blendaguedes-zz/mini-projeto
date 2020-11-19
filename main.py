from flask import Flask, json, request
import data_base

app = Flask(__name__)


@app.route("/", methods=["GET"])
def teste():
    data = data_base.get_data()
    return json.dumps(data)


@app.route("/inserir", methods=["POST"])
def inserir():
    pessoa = request.json
    id = pessoa['id']
    nome = pessoa['name']
    idade = pessoa['idade']

    data_base.insert_data(id, nome)

    return "Inserção concluída com sucesso!!!"


if __name__ == "__main__":
    app.run()
