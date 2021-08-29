from wsgiref.simple_server import make_server

def lancer(app, port=8000):
    hote = "jhub.fdex.eu"
    if not 8000 <= port <= 8999:
        print("Le port doit-être entre 8000 et 8999...")
    with make_server(hote, port, app) as server:
        print(f"je tourne sur le port {port} (vous pouvez le changer en le précisant en deuxième argument)")
        print(f"L'application est accessible à l'adresse http://{hote}:{port}")
        print("Pour m'arrêter: menu Kernel -> Interrupt Kernel (Ou «I, I» en mode Command...)")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("Arrêt")
            server.server_close()