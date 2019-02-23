import re
import json

# =======================================================================
# função para retornar a sigla baseada no nome da matéria passada via parâmetro
# param: {
# ..string: {
# ....type: string,
# ....description: nome da matéria que será lecionada em seu respectivo horário
# ..}
# }
def get_initials(string):
    
    # explode a string em cada ':' para um vetor str_separated
    str_separated = string.split(':')


    #instancia nova string com a sigla
    sigla = ''


    # ===================================================================
    # checa se a string passada por parametros contem apenas uma palavra ou não contem ':'
    if len(string.split(' ')) == 1 and len(str_separated) == 1:
        
        # atribui os primeiros 5 caracteres da string à variavel sigla
        sigla = str_separated[0][0:5]
    
    else:

        # esvazia str_vec
        str_vec = ''

        # =======================================================================
        # checa se o vetor de string separado por ':' tem mais de uma expressão
        if len(str_separated) > 1:
            
            # separa a segunda metade a cada ' ' em um vetor de strings str_vec
            str_vec = str_separated[1].split(' ')
        
        else:

            # separa a primeira metade a cada ' ' em um vetor de strings str_vec
            str_vec = str_separated[0].split(' ')


        # utiliza REGEX para verificar se a matéria passada por parâmetro (string) contém a versão e atribui a variavel version:
        # Exemplo: PC 'I', AED 'I', AOC 'II', CALC 'III', etc.
        version = re.match('.*I+$', str_vec[len(str_vec)-1])
        

        # =======================================================================
        # caso a função dê um match:
        if version:
            
            # ===================================================================
            # checa se tamanho do str_vec é dois
            if len(str_vec) == 2:

                # ===================================================================
                # caso o tamanho da primeira palavra do str_vec for maior que 4:    
                if len(str_vec[0]) >= 5:
                
                    # retorna as 4 primeiras letras da primeira palavra do str_vec concatenada com a versão obtida no match com REGEX
                   return ''.join(str_vec[0][0:4]) + " " + version.group(0)

                else:
                    
                    # retorna primeira palavra do str_vec concatenada com a versão obtida no match com REGEX
                    return str_vec[0] + " " + version.group(0)

            # ===================================================================

        # =======================================================================


        # =======================================================================
        # para cada palavra da string str_vec
        for word in str_vec:
            
            # ===================================================================
            # checa se é diferente de DE, E, EM e DA e tem tamanho maior que 0
            if word.upper() != 'DE' and word.upper() != 'E' and word.upper() != 'DA' and word.upper() != 'EM' and len(word) >= 1:
                
                # atribui a inicial da palavra à sigla
                sigla = sigla + word[0]
            # ===================================================================

    return sigla
# =======================================================================


# =======================================================================
# funçao para carregar dados no json
def load_data():
    
    # abre arquivo de texto com dados copiados do SIGAA
    file =  open("../data/subjects.txt", "r")


    # instancia novo vetor para receber os dados
    data = []

    # instancia novo vetor para receber os dados crus do arquivo
    raw_data = []
    

    # ===================================================================
    # adiciona cada linha do arquivo ao raw_data
    for line in file:
        
        raw_data.append(line[0:(len(line))])
    # ===================================================================


    # ===================================================================
    # itera de tres em tres sob o array raw_data
    for i in range(0, len(raw_data) - 1, 3):
        
        # instancia novo dicionario
        new_data             = {}

        # ===================================================================
        # atribui novos campos do dicionario
        new_data['nome']     = raw_data[i]
        new_data['sigla']    = get_initials(new_data['nome'])
        # ===================================================================

        # busca o horario codificado no dado cru e transforma em array de horarios
        horarios_codificados = raw_data[i+2].split(' ')

        # cria array de dados individuais
        horarios_individuais = []
        
        # ===================================================================
        # varre cada horario no array de horarios 'horarios_codificados'
        for horario_codificado in horarios_codificados:
            
            # utiliza REGEX para separar dias do horario codificado e transforma 
            # em lista de dias
            dias_lista     = list(re.search('[1-9]+', horario_codificado).group(0))
            
            # utiliza REGEX para separar o turno do horario codificado
            turno_parsed   = re.search('([mntMNT]{1})', horario_codificado).group(0)

            # utiliza REGEX para separar o indice de cada turno do horario 
            # codificado e transforma em lista de horarios
            horarios_lista = list(re.search('(?<='+re.escape(''.join(dias_lista)+turno_parsed)+')([1-9]+)', horario_codificado).group(0))
            
            # itera sobre os dias da semana no array de dias
            for weekday in dias_lista:
                
                # itera sobre os horarios na lista de horarios
                for horario in horarios_lista:
                    
                    # cria novo dicionario com os dados obtidos
                    horario_individual = {
                        'dia'     : weekday,
                        'turno'   : turno_parsed,
                        'horario' : horario
                    }
                    
                    # adiciona novo horario no array de horarios individuais
                    horarios_individuais.append(horario_individual)
        
        # adiciona os horarios individuais no dicionario com os dados novos
        new_data['horarios'] = horarios_individuais

        # adiciona o dicionario aos dados a serem escritos no arquivo JSON
        data.append(new_data)

    # escreve dados no JSON
    json_data = json.dumps(data)

    # escreve arquivo 'horarios.json' com dados obtidos
    json.dump(data, open('../data/horarios.json', 'w'))
# =======================================================================


# =======================================================================
# chama a função load_data
load_data()
# =======================================================================
