from flask import Flask, jsonify, request

app = Flask(__name__)
livros = [
  {
    "id": 1,
    "titulo": "Dom Casmurro",
    "autor": "Machado de Assis"
  },
  {
    "id": 2,
    "titulo": "Grande Sertão: Veredas",
    "autor": "João Guimarães Rosa"
  },
  {
    "id": 3,
    "titulo": "A Hora da Estrela",
    "autor": "Clarice Lispector"
  },
  {
    "id": 4,
    "titulo": "Capitães da Areia",
    "autor": "Jorge Amado"
  },
  {
    "id": 5,
    "titulo": "Vidas Secas",
    "autor": "Graciliano Ramos"
  },
  {
    "id": 6,
    "titulo": "Memórias Póstumas de Brás Cubas",
    "autor": "Machado de Assis"
  },
  {
    "id": 7,
    "titulo": "Iracema",
    "autor": "José de Alencar"
  },
  {
    "id": 8,
    "titulo": "O Cortiço",
    "autor": "Aluísio Azevedo"
  },
  {
    "id": 9,
    "titulo": "Macunaíma",
    "autor": "Mário de Andrade"
  },
  {
    "id": 10,
    "titulo": "Gabriela, Cravo e Canela",
    "autor": "Jorge Amado"
  },
  {
    "id": 11,
    "titulo": "São Bernardo",
    "autor": "Graciliano Ramos"
  },
  {
    "id": 12,
    "titulo": "A Paixão Segundo G.H.",
    "autor": "Clarice Lispector"
  },
  {
    "id": 13,
    "titulo": "O Quinze",
    "autor": "Rachel de Queiroz"
  },
  {
    "id": 14,
    "titulo": "Sagarana",
    "autor": "João Guimarães Rosa"
  },
  {
    "id": 15,
    "titulo": "Senhora",
    "autor": "José de Alencar"
  },
  {
    "id": 16,
    "titulo": "Quincas Borba",
    "autor": "Machado de Assis"
  },
  {
    "id": 17,
    "titulo": "O Tempo e o Vento (O Continente)",
    "autor": "Érico Veríssimo"
  },
  {
    "id": 18,
    "titulo": "Triste Fim de Policarpo Quaresma",
    "autor": "Lima Barreto"
  },
  {
    "id": 19,
    "titulo": "Dona Flor e Seus Dois Maridos",
    "autor": "Jorge Amado"
  },
  {
    "id": 20,
    "titulo": "O Guarani",
    "autor": "José de Alencar"
  },
  {
    "id": 21,
    "titulo": "Perto do Coração Selvagem",
    "autor": "Clarice Lispector"
  },
  {
    "id": 22,
    "titulo": "Angústia",
    "autor": "Graciliano Ramos"
  },
  {
    "id": 23,
    "titulo": "Ciranda de Pedra",
    "autor": "Lygia Fagundes Telles"
  },
  {
    "id": 24,
    "titulo": "Tenda dos Milagres",
    "autor": "Jorge Amado"
  },
  {
    "id": 25,
    "titulo": "Romanceiro da Inconfidência",
    "autor": "Cecília Meireles"
  },
  {
    "id": 26,
    "titulo": "Alguma Poesia",
    "autor": "Carlos Drummond de Andrade"
  },
  {
    "id": 27,
    "titulo": "O Ateneu",
    "autor": "Raul Pompeia"
  },
  {
    "id": 28,
    "titulo": "Memórias de um Sargento de Milícias",
    "autor": "Manuel Antônio de Almeida"
  },
  {
    "id": 29,
    "titulo": "As Meninas",
    "autor": "Lygia Fagundes Telles"
  },
  {
    "id": 30,
    "titulo": "Vestido de Noiva",
    "autor": "Nelson Rodrigues"
  },
  {
    "id": 31,
    "titulo": "O Bem-Amado",
    "autor": "Dias Gomes"
  },
  {
    "id": 32,
    "titulo": "Feliz Ano Novo",
    "autor": "Rubem Fonseca"
  },
  {
    "id": 33,
    "titulo": "O Vampiro de Curitiba",
    "autor": "Dalton Trevisan"
  },
  {
    "id": 34,
    "titulo": "Incidente em Antares",
    "autor": "Érico Veríssimo"
  },
  {
    "id": 35,
    "titulo": "Budapeste",
    "autor": "Chico Buarque"
  },
  {
    "id": 36,
    "titulo": "Dois Irmãos",
    "autor": "Milton Hatoum"
  },
  {
    "id": 37,
    "titulo": "Leite Derramado",
    "autor": "Chico Buarque"
  },
  {
    "id": 38,
    "titulo": "Relato de um Certo Oriente",
    "autor": "Milton Hatoum"
  },
  {
    "id": 39,
    "titulo": "O Filho Eterno",
    "autor": "Cristóvão Tezza"
  },
  {
    "id": 40,
    "titulo": "Eles Eram Muitos Cavalos",
    "autor": "Luiz Ruffato"
  },
  {
    "id": 41,
    "titulo": "Barba Ensopada de Sangue",
    "autor": "Daniel Galera"
  },
  {
    "id": 42,
    "titulo": "Sinfonia em Branco",
    "autor": "Adriana Lisboa"
  },
  {
    "id": 43,
    "titulo": "1808",
    "autor": "Laurentino Gomes"
  },
  {
    "id": 44,
    "titulo": "1822",
    "autor": "Laurentino Gomes"
  },
  {
    "id": 45,
    "titulo": "1889",
    "autor": "Laurentino Gomes"
  },
  {
    "id": 46,
    "titulo": "Raízes do Brasil",
    "autor": "Sérgio Buarque de Holanda"
  },
  {
    "id": 47,
    "titulo": "Casa-Grande & Senzala",
    "autor": "Gilberto Freyre"
  },
  {
    "id": 48,
    "titulo": "O Povo Brasileiro",
    "autor": "Darcy Ribeiro"
  },
  {
    "id": 49,
    "titulo": "Hibisco Roxo",
    "autor": "Chimamanda Ngozi Adichie" 
  },
  {
    "id": 50,
    "titulo": "Torto Arado",
    "autor": "Itamar Vieira Junior"
  }
]


@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)


@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
    return jsonify({"mensagem": f"Livro com ID {id} não encontrado"})


@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
    return jsonify({"mensagem": f"Livro com ID {id} não encontrado"})


app.run(debug=True, host='localhost', port=5000)
