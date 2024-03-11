
class Lobinho:
    Partidas = {
        "123456789": {
            "Luan": ["Vidente", "Vivo"],
            "Luana": ["Lobo", "Morto"],
            "Lua": ["Aldeão", "Morto"],
        }
    }
    vivos = 0
    mortos = 0
    for nomes in Partidas["123456789"]:
        papel = Partidas["123456789"][nomes]
        if papel[1] == "Morto":
            mortos += 1
            print (f"Morreu {nomes} {papel [0]}")
        if papel[1] == "Vivo":
            vivos += 1
            if papel [0] == "Vidente":
                print (f"O vidente é {nomes}")
    if vivos > mortos:
        print(f"ainda vivos {vivos} e mortos {mortos}")
    else:
        print (f"todo mundo morreu")
    