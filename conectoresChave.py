
users = [
    {"id": 0, "name": "Pedro"},
    {"id": 1, "name": "Thiago"},
    {"id": 2, "name": "Joao"},
    {"id": 3, "name": "Mateus"},
    {"id": 4, "name": "Judas"},
    {"id": 5, "name": "Andre"},
    {"id": 6, "name": "Filipe"},
    {"id": 7, "name": "Tome"},
    {"id": 8, "name": "Bartolomeu"},
    {"id": 9, "name": "Simao"},
]

amigos = [
    (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
]

# Inicializando um dicionário vazio para armazenar as amizades de cada pessoa
amizades = {}

# Iterando sobre as amizades e preenchendo o dicionário
for a, b in amigos:
    # Adicionando 'b' às amizades de 'a'
    amizades.setdefault(a, []).append(b)
    # Adicionando 'a' às amizades de 'b' (já que é uma amizade bidirecional)
    amizades.setdefault(b, []).append(a)

# Exibindo as amizades de cada pessoa
for user_id, amigos_ids in amizades.items():
    user_name = next(user["name"] for user in users if user["id"] == user_id)
    amigos_names = [user["name"] for user in users if user["id"] in amigos_ids]
    print(f"Usuario {user_name: <10} |ID {user_id}|  Amigo(a) de {', '.join(amigos_names)}")
