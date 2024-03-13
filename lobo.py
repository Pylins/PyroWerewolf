import pyrogram
from pyrogram import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
from asyncio import *
import random

app = Client ("botcapi")

class Lobinho:
    
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
            "Village": {
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
            "Village": {
                "Gravida": ["🤰","Você está gravida, parabéns seria se você não fosse a gravida de Taubaté.", 100]
            },
        },
    }
    
    # Games={GameID:{Name:[Team,Role,State]}}
    Games = {
        "123456789": {
            "Luan": ["Aldeia","Vidente","Vivo"],
            "Luana": ["Alcateia","Lobo","Vivo"],
            "Lucas": ["Aldeia","Aldeão","Morto"],
            "Luciana": ["Aldeia","Bruxa","Vivo"],
            "Lara": ["Solo","Suicida","Vivo"],
            "Joao": ["Solo","Seita","Vivo"],
        }
    }
    
    # /jogar: Inicia uma nova partida
    @app.on_message(filters.command("jogar"))
    async def jogar(client, msg):
        # TODO: Verificação se ja iniciaram a partida ou se já usaram o /jogat, caso sim apenas adicione o usuario.
        grupo = msg.chat.id
        Lobinho.Partidas[grupo] = {}
        # Tempo de 60s para outros jogadores entrarem
        await app.send_message(grupo, "Partida criada! Use /entrar para participar.")
        await asyncio.sleep(60)
        # Inicia o jogo se houver +3 jogadores e atribui os papeis
        if len(Lobinho.Partidas[partida_id]) < 3:
            await app.send_message(grupo, "Número mínimo de jogadores não atingido. Partida cancelada.")
            del Lobinho.Partidas[partida_id]
            return
        await Lobinho.atribuir_papeis(client, message, partida_id)
        await Lobinho.iniciar(client, message, partida_id)
        
    # /entrar: Permite outros jogadores entrarem na partida do grupo
    @app.on_message(filter.command("entrar"))
    async def entrar(client, msg):
        # Adiciona o jogador na partida do grupo apenas se a partida não estiver começado
        pass
    async def atribuir_papeis():
        # Atribui papeis conforme:
        # no minimo um lobo
        # apartir de 4 pessoas deve ter mais lobos
        # apartir de 10 jogadores haverá a seita
        pass
    async def iniciar():
        # Inicia o jogo com os jogadores.
        # Primeira noite começa
        # Mostra quem morreu e os jogadores ainda vivos
        # O dia começa
        # A votação começa
        # Jogador mais votado é revelado
        # Ciclo se repete, mas a qualquer momento se os lobos forem todos mortos a aldeia ganha, se a quantidade de lobos for igual a quantidade de aldeaia os lobos ganham, se o suicida for enforcado a aldeia e lobos perdem e ele será o unico ganhador, se a seita conseguir ter mais jogadores que lobos e aldeias
        pass
    async def noite():
        # Tempo para que realizem ações 60s
        # Envia as menssagens aos jogadores com açao noturna
        # Se for vidente podera ver um papel e receber a resposta de dia
        # Se for lobo podera matar alguem
        # No segundo dia a bruxa poderá ressucitar um jogador morto
        # Os integrantes da seita poderao converter mas se tentarem seitar um lobo irão morrer
        pass
    async def dia():
        # Envia a resposta das ações noturnas para os jogadores vivos
        # Tempo para ações 60s
        # Envia as menssagens aos jogadores com ação diurna
        # Se for detetive podera investigar alguem e tera o resultado quando iniciar a votação da forca
        pass
    async def votar():
        # Os jogadores devem votar em alguem para enforcar (matar)
        pass
    
app.run()