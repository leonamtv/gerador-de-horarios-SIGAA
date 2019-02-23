import json
import datetime


# carrega o arquivo com os horarios para a variavel 'horarios'
horarios = json.load(open('../data/horarios.json', 'r'))

# =======================================================================
# gera um dicionario (horas) com os horarios base de cada um dos 6 horarios de cada turno
# onde para cada turno 'n' temos:
# n : {
# ..{
# ....'i' : {
# ......'h' : a,
# ......'m' : b
# ....}
# ..},
# ..{
# ....'f' : {
# ......'h' : c,
# ......'m' : d
# ....}
# ..}
# }
# onde 'i' representa o momento de início, com 'a' sendo as horas e 'b' os minutos
# e 'f' representa o momento de fim, com 'c' sendo as horas e 'd' os minutos, para 
# cada um dos horários.

horas = {
    1 : { 'i' : { 'h' : '7',  'm': '00' }, 'f' : { 'h' : '7',  'm': '50' } },
    2 : { 'i' : { 'h' : '7',  'm': '51' }, 'f' : { 'h' : '8',  'm': '40' } },
    3 : { 'i' : { 'h' : '8',  'm': '41' }, 'f' : { 'h' : '9',  'm': '30' } },
    4 : { 'i' : { 'h' : '9',  'm': '31' }, 'f' : { 'h' : '10', 'm': '35' } },
    5 : { 'i' : { 'h' : '10', 'm': '36' }, 'f' : { 'h' : '11', 'm': '25' } },
    6 : { 'i' : { 'h' : '11', 'm': '26' }, 'f' : { 'h' : '12', 'm': '15' } }
}
# =======================================================================


# =======================================================================
# inicia uma string onde será concatenada todo o código HTML
# insere as tags basicas, com os links para o CSS, fontes externas, etc.
html = ""
html = html + "<!DOCTYPE html>\n"
html = html + "<html>\n"
html = html + "<head>\n"
html = html + "   <meta charset='UTF-8'>\n"
html = html + "   <title>Tabela de precos</title>\n"
html = html + "   <link rel='stylesheet' type='text/css' href='horario_style.css'>\n"
html = html + "   <link rel='stylesheet' type='text/css' href='table_content_style.css'>\n"
html = html + "   <link href='https://fonts.googleapis.com/css?family=Montserrat:300' rel='stylesheet'>\n"
html = html + "</head>\n"
html = html + "<body>\n"
html = html + "   <div class = 'content-div'>\n"
html = html + "      <h1>\n"
html = html + "            -Horário-\n"
html = html + "      </h1>\n"    
html = html + "      <table cellspacing = '0'>\n"
html = html + "         <tr>\n"
html = html + "            <th colspan = '2'>\n"
html = html + "                Horários\n"
html = html + "            </th>\n"
html = html + "            <th rowspan = '2'>\n"
html = html + "                Segunda\n"
html = html + "            </th>\n"
html = html + "            <th rowspan = '2'>\n"
html = html + "                Terça\n"
html = html + "            </th>\n"
html = html + "            <th rowspan = '2'>\n"
html = html + "                Quarta\n"
html = html + "            </th>\n"
html = html + "            <th rowspan = '2'>\n"
html = html + "                Quinta\n"
html = html + "            </th>\n"
html = html + "            <th rowspan = '2'>\n"
html = html + "                Sexta\n"
html = html + "            </th>\n"
html = html + "         </tr>\n"
html = html + "         <tr>\n"
html = html + "            <th>\n"
html = html + "                  Início\n"
html = html + "            </th>\n"
html = html + "            <th>\n"
html = html + "                  Fim\n"
html = html + "            </th>\n"
html = html + "         </tr>\n"
# =======================================================================


# =======================================================================
# loop for para varrer cada um dos três turnos: Manhã, Tarde, Noite
for i in range(0, 3):
    

    # variável de controle para criação do CSS com tons variados entre 
    # linha da tabela do horário
    controle = True

    # =======================================================================
    # loop for variando em cada um dos horarios de cada turno, por 
    # padrão, de 0 a 6
    for k in range(1, 7):
        
        html = html + "         <tr>\n"
        html = html + "            <td class = 'horario"


        # =======================================================================
        # utiliza variavel de controle para atribuir classe ao componente html
        if controle:
            
            html = html + "_a" +  "'>\n"
        
        else:
            
            html = html + "_b" +  "'>\n"
        # =======================================================================        

        # =======================================================================
        # adiciona o horário de início da aula de cada linha
        html = html + "               " + str((int(horas[k]["i"]["h"])+i*6)) + ":" + str(horas[k]["i"]["m"]) + "\n"
        html = html + "            </td>\n"
        html = html + "            <td class = 'horario"
        # =======================================================================


        # =======================================================================
        # utiliza variavel de controle para atribuir classe ao componente html
        if controle:
            
            html = html + "_a" +  "'>\n"
        
        else:
            
            html = html + "_b" +  "'>\n"
        # =======================================================================

        # =======================================================================
        # adiciona o horário de fim da aula de cada linha
        html = html + "               " + str((int(horas[k]["f"]["h"])+i*6)) + ":" + str(horas[k]["f"]["m"]) + "\n"
        html = html + "            </td>\n"
        # =======================================================================

        # inverte variavel de controle
        controle = not controle

        # =======================================================================
        # loop for para varrer os dias úteis da semana
        for j in range (1, 6):
            
            # =======================================================================
            # variavel de controle que se baseia no indice i do primeiro loop
            # para atribuir uma letra para cada um dos turnos existentes:
            # i = 0 -> M = Manhã
            # i = 1 -> T = Tarde
            # i = 2 -> N = Noturno
            cont = ''
            
            if   i == 0: 
                
                cont = 'M'
            
            elif i == 1: 
                
                cont = 'T'
            
            elif i == 2: 
                
                cont = 'N'
            # =======================================================================
            
            
            html = html + "            <td class = " + "c" + str(j+1) + cont + str(k) + ">\n"
            html = html + "            </td>\n"
        # =======================================================================


        html = html + "         </tr>\n"
    # =======================================================================

    
    # =======================================================================
    # cria os divisores de turno da tabela, caso o indice do primeiro 
    # loop seja menor que 2
    if i < 2:
        
        html = html + "         <tr>\n"
        html = html + "            <td colspan = '7'>\n"
        html = html + "            </td>\n"
        html = html + "         </tr>\n"
    # =======================================================================
# =======================================================================



# =======================================================================
# fecha tabela de horário e abre nova tabela para legenda
html = html + "       </table>\n"
html = html + "       <table cellspacing = '0'>\n"
html = html + "         <tr>\n"
html = html + "            <th colspan = '2'>\n"
html = html + "               Legenda\n"
html = html + "            </th>\n"
html = html + "         </tr>\n"
# =======================================================================


# cria nova variavel css para armazenar os estilos da pagina
css = ""

# =======================================================================
# loop for para varrer todos os horarios e criar a legenda de cada
# sigla com o respectivo nome da matéria
for horario in horarios:
    
    html = html + "         <tr>\n"
    html = html + "            <td>\n"
    html = html + "               " + horario['sigla'] + "\n"
    html = html + "            </td>\n"
    html = html + "            <td>\n"
    html = html + "               " + horario['nome'] + "\n"
    html = html + "            </td>\n"
    html = html + "         </tr>\n"

    # =======================================================================
    # for loop para varrer cada horario individual em cada uma das 
    # materias e cria uma classe CSS especifica para o mesmo, para 
    # que o estilo seja aplicado às celulas da tabela de horário
    for indiv in horario["horarios"]:
        
        css = css + ".c" + indiv['dia'] + indiv['turno'] + indiv['horario'] + ":after {\n"
        css = css + "   content: '" + horario['sigla']  + "';\n"
        css = css + "}\n"
    # =======================================================================

# =======================================================================

# abre arquivo 'table_content_style.css' para escrever o css gerado
file_css  = open("../css_html/table_content_style.css", "w")

# escreve css gerado no arquivo
file_css.write(css)

# =======================================================================
# fecha tabela de legenda e adiciona a data e hora da geração do 
# horário
html = html + "      </table>\n"
html = html + "      <p class = 'aviso'>\n"
html = html + "         Gerado em: " + str(datetime.datetime.now().strftime('%d/%m/%Y-%H:%M')) + "h\n"
html = html + "      </p>\n"
html = html + "   </div>\n"
html = html + "</body>\n"
html = html + "</html>\n"
# =======================================================================


# abre arquivo 'index.html' para escrever o html gerado
file_html = open("../css_html/index.html", "w")

# escreve html gerado no arquivo aberto
file_html.write(html)