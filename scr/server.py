import socket
from _thread import *
import pickle
from game import Game

# server = "192.168.123.100"
server = "127.0.0.1"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

connected = set()
games = {}
idCount = 0


def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))
    while True:
        try:
            data = conn.recv(4096).decode()

            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    print(data.split())
                    cmd = data.split()[0]
                    if cmd == "move":
                        game.move(p, float(data.split()[1]), float(data.split()[2]), int(data.split()[3]))
                    if cmd == "bullet":
                        game.bullet(p, float(data.split()[1]), float(data.split()[2]), int(data.split()[3]))
                    if cmd == "delete":
                        if str(data.split()[1] == "none"):
                            pass
                        else:
                            game.delete(p, int(data.split()[1]))
                    if cmd == "hit":
                        game.hit(p, int(data.split()[1]))

                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()



while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1


    start_new_thread(threaded_client, (conn, p, gameId))