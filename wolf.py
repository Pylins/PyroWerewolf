import pyrogram
from pyrogram import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
from asyncio import *
import random

app = Client ("botcapi")

class Wolf:
    
    # Roles={Country:{Team:{Role:[emoji,description,conversion]}}}
    Roles = {
        "Global": {
            "Wolves": {
                "Werewolf": ["🐺","Você é um lobisomem e pode se passar por um aldeão comum e atacar durante a noite.",0],
                "Alpha": ["🌙","Você é o lobo alfa e tem 25% de chance de transformar um jogador em lobisomem.",0],
                "PupWolf": ["🐕","Você é o filhote apesar de  atrapalhar a alcateia, todos te amam! Se você morrer os lobos ficarão raivosos.",0],
            },
            "Sect": {
                "Zombie": ["🧟","Cerebro o que mais deseja. Você é um zombie, infecte outros jogadores e comece o apocalipse.",0],
            },
            "Solo": {
                
            },
            "Ville": {
                "Villager": ["👱","Você é um aldeão, só fica varrendo o chão.",100],
                "Detective": ["🧐","Elementar, meu caro Watson! Você é um detetive aja como tal.",70],
            },
        },
        "Brazil": {
            "Sect": {
                "Sulista": ["👨","Você é um separatista, convença os jogadores a transformar o sul em um país.", 0],
            },
            "Solo": {
                "Alien": ["👽","Busquem conhecimento. Como o ET Bilu você pode visitar jogadores.",],
            },
            "Ville": {
                "Gravida": ["🤰","Você está gravida, parabéns seria se você não fosse a gravida de Taubaté.", 100]
            },
        },
    }
    
    # Games={GameID:{Name:[Team,Role,State]}}
    Games = {
        # Example
        "123456789": {
            "Luan": ["Ville","Villager","Alive"],
            "Luana": ["Wolves","Village","Alive"],
            "Lucas": ["Ville","Gravida","Dead"],
            "Luciana": ["Ville","Gravida","Alive"],
            "Lara": ["Solo","Alien","Alive"],
            "Joao": ["Sect","Zombie","Alive"],
        }
    }
    
    # /start new werewolf game
    @app.on_message(filters.command("start"|"jogar"))
    async def start(client, msg):
        # TODO: Verificação se ja iniciaram a partida ou se já usaram o /jogar, caso sim apenas adicione o usuario.
        group_id = msg.chat.id
        Wolf.Games[game_id] = {}
        # Tempo de 60s para outros jogadores entrarem
        await app.send_message(grupo, "Partida criada! Use /entrar para participar.")
        await asyncio.sleep(60)
        # Inicia o jogo se houver +3 jogadores e atribui os papeis
        if len(Wolf.Games[game_id]) < 3:
            await app.send_message(grupo_id, "Número mínimo de jogadores não atingido. Partida cancelada.")
            del Wolf.Games[game_id]
            return
        await Wolf.assign_roles(client, message, game_id)
        await Wolf.play(client, message, game_id)
        
    # /join to game
    @app.on_message(filter.command("join"|"entrar"))
    async def join(client, msg):
        # Adiciona o jogador na partida do grupo apenas se a partida não estiver começado
        pass
    async def assign_roles():
        # Atribui papeis conforme:
        # no minimo um lobo
        # apartir de 4 pessoas deve ter mais lobos
        # apartir de 10 jogadores haverá a seita
        pass
    async def play():
        # Inicia o jogo com os jogadores.
        # Primeira noite começa
        # Mostra quem morreu e os jogadores ainda vivos
        # O dia começa
        # A votação começa
        # Jogador mais votado é revelado
        # Ciclo se repete, mas a qualquer momento se os lobos forem todos mortos a aldeia ganha, se a quantidade de lobos for igual a quantidade de aldeaia os lobos ganham, se o suicida for enforcado a aldeia e lobos perdem e ele será o unico ganhador, se a seita conseguir ter mais jogadores que lobos e aldeias
        pass
    async def night():
        # Tempo para que realizem ações 60s
        # Envia as menssagens aos jogadores com açao noturna
        # Se for vidente podera ver um papel e receber a resposta de dia
        # Se for lobo podera matar alguem
        # No segundo dia a bruxa poderá ressucitar um jogador morto
        # Os integrantes da seita poderao converter mas se tentarem seitar um lobo irão morrer
        pass
    async def day():
        # Envia a resposta das ações noturnas para os jogadores vivos
        # Tempo para ações 60s
        # Envia as menssagens aos jogadores com ação diurna
        # Se for detetive podera investigar alguem e tera o resultado quando iniciar a votação da forca
        pass
    async def poll():
        # Os jogadores devem votar em alguem para enforcar (matar)
        pass
    
app.run()
