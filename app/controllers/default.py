from app import app, jsonify

@app.route('/')
def index():
  from app.data import main

  a = main.Home()
  import json
  
  def escrever_json(lista):
    with open('home.json', 'w') as f:
      json.dump(lista, f)

  return jsonify(a.home()), escrever_json(a.home())

@app.route('/player/<id>')
def player(id):
  from app.data import player

  import json
  def carregar_json(arquivo):
    with open('home.json', 'r') as f:
      return json.load(f)

  _id = carregar_json('home.json')
  video = player.video(_id[id]['url'])
  return jsonify(video)

@app.route('/<id>')
def search(id):
  from app.data import search
  _id = id
  a = search.Search(str(_id))
  import json
  
  def escrever_json(lista):
    with open('search.json', 'w') as f:
      json.dump(lista, f)

  return jsonify(a.home()), escrever_json(a.home())


@app.route('/anime_page_eps/<id>')
def anime_eps(id):
  from app.data import anime_page_head as pg

  import json
  def carregar_json(arquivo):
    with open('search.json', 'r') as f:
      return json.load(f)
  

  def escrever_json(lista):
    with open('search_eps.json', 'w') as f:
      json.dump(lista, f)


  _id = carregar_json('search.json')
  a = pg.Head(_id[id]['url'])

  return(a.episodios()), escrever_json(a.episodios())

@app.route('/anime_page/<id>')
def anime_page(id):
  from app.data import anime_page_head as pg

  import json
  def carregar_json(arquivo):
    with open('search.json', 'r') as f:
      return json.load(f)

  _id = carregar_json('search.json')
  a = pg.Head(_id[id]['url'])

  return jsonify(a.row())

@app.route('/player/page/<id>')
def player_page(id):
  from app.data import player

  import json
  def carregar_json(arquivo):
    with open('search_eps.json', 'r') as f:
      return json.load(f)

  _id = carregar_json('search_eps.json')
  video = player.video(_id[id]['url'])

  return jsonify(video)