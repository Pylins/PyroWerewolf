#import pyrogram
#from pyrogram import Client
#import asyncio
#app = Client ("botcapi")

class Lobinho:
    def __init__(self):
        self.Partidas = {
            "123456789": {
                "Luan": ["Vidente", "Vivo"],
                "Luana": ["Lobo", "Vivo"],
                "Lua": ["Aldeão", "Morto"],
            }
        }

    def jogar(self):
        while True:
            # Noite
            for nomes in self.Partidas["123456789"]:
                papel = self.Partidas["123456789"][nomes]
                if papel[1] == "Vivo":
                    if papel[0] == "Lobo":
                        lchoice = input(f"{nomes} (Lobo), quem você quer atacar? ")
                        self.Partidas["123456789"][lchoice][1] = "Morto"
                    if papel[0] == "Vidente":
                        vchoice = input(f"{nomes} (Vidente), quem você quer investigar? ")
                        print(f"{vchoice} é {self.Partidas['123456789'][vchoice][0]}.")

            # Manhã
            vivos, mortos = 0, 0
            for nomes in self.Partidas["123456789"]:
                papel = self.Partidas["123456789"][nomes]
                if papel[1] == "Vivo":
                    vivos += 1
                elif papel[1] == "Morto":
                    mortos += 1
                    print(f"{nomes} foi morto!")

            if vivos > mortos:
                print(f"Ainda vivos: {vivos} e mortos: {mortos}")
            else:
                print("**Lobos venceram!**")
                break

            # Votação
            votos = {}
            for nomes in self.Partidas["123456789"]:
                if self.Partidas["123456789"][nomes][1] == "Vivo":
                    voto = input(f"{nomes}, em quem você quer votar para eliminar? ")
                    votos[voto] = votos.get(voto, 0) + 1

            # Eliminação do jogador mais votado
            mais_votado = max(votos, key=votos.get)
            print(f"{mais_votado} foi eliminado com {votos[mais_votado]} votos!")
            self.Partidas["123456789"][mais_votado][1] = "Morto"

jogo = Lobinho()
jogo.jogar()
