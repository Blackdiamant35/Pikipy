# -*- Coding:Utf-8 -*-
import socket
 
# cette fonction n'est pas très performante puisqu'elle
# ouvre et ferme la socket pour chaque message,
# mais vous voyez le principe.
def envoyer_message(ip, port, message):
 
    # on ouvre une socket TCP / IP, en IP V4
    # la doc contient une liste de constantes avec
    # les protocoles de base supportés
    # (http://docs.python.org/2/library/socket.html)
    # on peut aussi ouvrir des sockets unix, des datagrames...
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        # on broadcast le message
        sock.sendall(message)
        # et on lit la réponse cash pistache
        # Tout ça est synchrone, car si on veut
        # faire de l'asynchrone, l'exemple serait
        # vachement moins simple
        response = sock.recv(1024).decode('Utf-8')
        print("Received: {}".format(response))
    except Exception as e:
        print("Impossible de se connecter au serveur: {}".format(e))
    finally:
        # toujours fermer sa socket, même si dans notre cas
        # on a pas besoin de la fermer pour chaque message
        # On pourrait aussi utiliser le context manager closing()
        # pour cette tâche
        sock.close()
 
# petit test qui envoit trois messages
if __name__ == "__main__":
 
    ip, port = "127.0.0.1", 6666
 
    envoyer_message(ip, port, bytes("Hello World 1".encode('Utf-8')))
    envoyer_message(ip, port, bytes("Hello World 2".encode('Utf-8')))
    envoyer_message(ip, port, bytes("Hello World 3".encode('Utf-8')))