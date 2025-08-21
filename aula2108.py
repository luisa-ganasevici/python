
if __name__ == "__main__" :
    campeonato = {}
    campeonato ['corinthians'] = 'melhor time te amo corinthians'
    campeonato ['palmeiras'] = 'sem mundial time de boy'
    campeonato ['sao paulo'] = 'time de viado.'
    campeonato ['santos'] = 'torcida media: 80 anos (internado em hospital publico)'


    print (campeonato)

    campeonato ['corinthians'] = 'campeao de tudo, time lindo'
    for time in campeonato.keys():
        print(f'{time} descricao: {campeonato [time]}')

    paulistao = {}

    paulistao ['corinthians'] = ['corinthians', 50] 
    paulistao ['palmeiras'] = ['palmeiras', 2]
    paulistao ['sao paulo'] = ['sao paulo', 1 ]
    paulistao ['santos'] = ['santos', 12]

    for time in paulistao.keys():
        print(f'{time} descricao: {paulistao [time]}')


    for time in campeonato.keys():
        paulistao[time] = [time,{campeonato[time]}]


print(paulistao)    
