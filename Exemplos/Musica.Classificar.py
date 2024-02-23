def classificar_musica(genero_favorito, gerero_musica):
    if genero_favorito == gerero_musica:
        return 'recomendada'
    elif genero_favorito == 'Pop' or genero_favorito == 'Rock':
        return 'neutra'
    else:
        return 'não encontrada'
    
resultado = classificar_musica('Rock', 'Pop')
print(resultado)
