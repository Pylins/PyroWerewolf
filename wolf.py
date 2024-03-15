import pyrogram
from pyrogram import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
from asyncio import *
import random

app = Client ("botcapi")

import json
with open("roles.json") as f:
    Roles = json.load(f)
    
class Wolf:
    
    # Modes={Mode:{Team:{Roles}}
    Modes = {
        "Normal": {
            "Wolves": ["Werewolf", "Alpha", "PupWolf"],
            "Sect": ["Zombie", "Separatist"],
            "Solo": ["Hannibal", "Alien"],
            "Ville": ["Villager", "Detective"]
        }
    }
    # Games={GameID:{Name:[Team,Role,State]}}
    Games = {
        # Example
        "123456789": {
            "Luan": ["Ville","Villager","Alive"],
            "Luana": ["Wolves","Village","Alive"],
            "Lucas": ["Ville","Gravida","Dead"],
            "Lucy": ["Ville","Detective","Alive"],
            "Lara": ["Solo","Alien","Alive"],
            "Joao": ["Sect","Zombie","Alive"],
        }
    }
    
    # /start new werewolf game
    @app.on_message(filters.command("start"|"jogar"))
    async def start(client, msg):
        # TODO: check the game start in the group and add player
        group_id = msg.chat.id
        Wolf.Games[game_id] = {}
        # Timeout 60s to wait others players
        await app.send_message(grupo, "Partida criada! Use /entrar para participar.")
        await asyncio.sleep(60)
        # Start game if +3 players
        if len(Wolf.Games[game_id]) < 3:
            await app.send_message(grupo_id, "Número mínimo de jogadores não atingido. Partida cancelada.")
            del Wolf.Games[game_id]
            return
        # assign roles and play
        # TODO: filter to define the game mode
        mode = "Normal"
        await Wolf.assign_roles(mode, game_id)
        await Wolf.play(client, message, game_id)
        
    # /join to game
    @app.on_message(filter.command("join"|"entrar"))
    async def join(client, msg):
        Wolf.Games["123456789"].update({"Jose": ["None","None","Alive"]})
        # TODO: Check player join and check game state
        pass
    async def assign_roles(mode, game_id):
        game = Wolf.Games[game_id]
        players = list(game.keys())
        if mode == "Normal":
            # Calculate the numbers of wolfs
            wolves = max(1, int(len(game) * 0.25))
            # Random choice the wolf players
            wolf_players = random.sample(players, wolves)
            # Loops for set roles
            for player in wolf_players:
                # Random role wolf team
                wrole = random.choice(Wolf.Modes[mode]["Wolves"])
                game[player] = ["Wolves", wrole, "Alive"]
            for player in players:
                if player not in wolf_players:
                    vrole = random.choice(Wolf.Modes[mode]["Ville"])
                    game[player] = ["Ville", vrole, "Alive"]
        # TODO:
        # logic if players < 10 = set sect
        pass
    async def play():
        # TODO:
        # Inicia o jogo com os jogadores.
        # Primeira noite começa
        # Mostra quem morreu e os jogadores ainda vivos
        # O dia começa
        # A votação começa
        # Jogador mais votado é revelado
        # Ciclo se repete, mas a qualquer momento se os lobos forem todos mortos a aldeia ganha, se a quantidade de lobos for igual a quantidade de aldeaia os lobos ganham, se o suicida for enforcado a aldeia e lobos perdem e ele será o unico ganhador, se a seita conseguir ter mais jogadores que lobos e aldeias
        pass
    async def night():
        # TODO:
        # Tempo para que realizem ações 60s
        # Envia as menssagens aos jogadores com açao noturna
        # Se for vidente podera ver um papel e receber a resposta de dia
        # Se for lobo podera matar alguem
        # No segundo dia a bruxa poderá ressucitar um jogador morto
        # Os integrantes da seita poderao converter mas se tentarem seitar um lobo irão morrer
        pass
    async def day():
        # TODO
        # Envia a resposta das ações noturnas para os jogadores vivos
        # Tempo para ações 60s
        # Envia as menssagens aos jogadores com ação diurna
        # Se for detetive podera investigar alguem e tera o resultado quando iniciar a votação da forca
        pass
    async def poll():
        # TODO:
        # Os jogadores devem votar em alguem para enforcar (matar)
        pass
    
app.run()
