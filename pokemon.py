import requests
from dataclasses import dataclass

"""
Nessa atividade, vamos utilizar uma API, um site que nos permite baixar dicionários com dados relevantes.
No caso, os dados serão sobre pokemons, e o site se chama pokeapi.

Comecemos abrindo as seguintes URLs no firefox, para entender a pokeapi.
(é importante abrir no firefox. No chrome, elas ficam bastante mais 
difíceis de ler. Instale o firefox se não tiver. Deixar as URLs legíveis no
chrome dá muito mais trabalho -- ainda não vi uma solução decente)

Alguns exemplos de URLs que podem servir de inspiração:
http://pokeapi.co/api/v2/

http://pokeapi.co/api/v2/pokemon/39/
http://pokeapi.co/api/v2/pokemon/jigglypuff/

http://pokeapi.co/api/v2/pokemon-species/39/
http://pokeapi.co/api/v2/pokemon-species/jigglypuff/

http://pokeapi.co/api/v2/evolution-chain/11/
http://pokeapi.co/api/v2/growth-rate/1/
http://pokeapi.co/api/v2/pokemon-color/2/
"""

"""
Pra você não ficar digitando a mesma url toda hora, criei uma variável global
Aí, você pode completar conforme a necessidade
"""
site_pokeapi = "https://pokeapi.co"


"""
1. Dado o número de um pokémon, qual é o nome dele?

Dica: acesse a URL http://pokeapi.co/api/v2/pokemon/39/
Nessa URL, podemos ver todos os dados do pokemon 39, inclusive o nome

Trocando o número pelo número correto, você vai conseguir achar, para cada pokemon,
o nome dele.

"""
#r = requests.get("http://pokeapi.co/api/v2/pokemon/")
#dici = r.json()

dados_pokemon="https://pokeapi.co/api/v2/pokemon/"
def nome_do_pokemon(numero):
    url=f"{dados_pokemon}{numero}"
    r = requests.get(url)
    dici = r.json()
    return dici['name']

"""
Abaixo, criamos uma excessão com nome personalizado, que será utilizada do exercicio 2 
em diante.
"""

class PokemonNaoExisteException(Exception):
    pass #nao faça nada aqui. Essa exception
         #já está pronta, só é um "nome" novo



"""
2. Dado o nome de um pokémon, qual é o número dele?

Dica: consulte as URLs úteis no começo do arquivo. Uma delas te permite colocar o
nome e descobrir o número.

Dica2: A pokeapi espera todos os nomes apenas com minúsculas. Mas eu
posso mandar nomes maiúsculos (PIKACHU) ou misturados (PikaChu)
Trate esse problema (nessa função e nas próximas)

Dica3: Se o status_code vier inválido, lance a excessão PokemonNaoExisteException,
que já está definida nesse arquivo. Lembre-se que o status_code de sucesso é o 200

Dica4: Para entender como ver o status_code usando a biblioteca requests, olhe o arquivo requests_exemplo

Extra: para mais informações sobre status_code, veja a aula de redes do EAD -- verifique no plano de ensino
"""
def numero_do_pokemon(nome):
    nome_minusculo=nome.lower()
    url=f'https://pokeapi.co/api/v2/pokemon/{nome_minusculo}'    
    r = requests.get(url)
    if (r.status_code!=200):
        raise PokemonNaoExisteException
    dici = r.json()
    return dici['id']


"""
3. Dado o nome ou número de um pokémon, qual é o nome da cor (em inglês) predominante dele?

Dica: consulte as URLs úteis no começo do arquivo.A URL que vamos usar dessa vez é nova, ainda
não utilizamos

Dica: Ainda esperamos a PokemonNaoExisteException quando apropriado.
Não vou mais te avisar disso.
"""
def color_of_pokemon(nome):
    nome_minusculo=nome.lower()
    url=f'http://pokeapi.co/api/v2/pokemon-species/{nome_minusculo}'
    r = requests.get(url)
    if (r.status_code!=200):
        raise PokemonNaoExisteException
    dici = r.json()
    return dici['color']['name']




dic_cores = { #esse dicionário pode te ajudar com o exercicio 4
    "brown": "marrom",
    "yellow": "amarelo",
    "blue": "azul",
    "pink": "rosa",
    "gray": "cinza",
    "purple": "roxo",
    "red": "vermelho",
    "white": "branco",
    "green": "verde",
    "black": "preto"
}



"""
4. Dado o nome ou número de um pokémon, qual é o nome da cor (em português) predominante dele?
Os nomes de cores possíveis em português são "marrom", "amarelo", "azul", "rosa", "cinza", "roxo", "vermelho", "branco", "verde" e "preto".
No entanto, a pokeapi ainda não foi traduzida para o português! Talvez o dic_cores acima
seja útil.
"""
def cor_do_pokemon(nome):
    dic_cores = {"brown": "marrom",
    "yellow": "amarelo",
    "blue": "azul",
    "pink": "rosa",
    "gray": "cinza",
    "purple": "roxo",
    "red": "vermelho",
    "white": "branco",
    "green": "verde",
    "black": "preto"}
    cor=color_of_pokemon(nome)
    return dic_cores[cor]
    


dic_tipos = { #esse dicionário pode te ajudar com o exercicio 5
    "normal": "normal",
    "fighting": "lutador",
    "flying": "voador",
    "poison": "veneno",
    "ground": "terra",
    "rock": "pedra",
    "bug": "inseto",
    "ghost": "fantasma",
    "steel": "aço",
    "fire": "fogo",
    "water": "água",
    "grass": "grama",
    "electric": "elétrico",
    "psychic": "psíquico",
    "ice": "gelo",
    "dragon": "dragão",
    "dark": "noturno",
    "fairy": "fada"
}


"""
5. Dado o nome de um pokémon, quais são os tipos no qual ele se enquadra?
Os nomes dos tipos de pokémons em português são "normal", "lutador", "voador", "veneno", "terra", "pedra", "inseto", "fantasma", "aço", "fogo", "água", "grama", "elétrico", "psíquico", "gelo", "dragão", "noturno" e "fada".
Todo pokémon pode pertencer a um ou a dois tipos diferentes. Retorne uma lista contendo os tipos, mesmo que haja somente um.
Se houver dois tipos, a ordem não é importante.

Dica: novamente, dê uma olhada nas URL que separei. Elas bastam.
Isso será verdade para todo o arquivo.
"""
def tipos_do_pokemon(nome):
    pass



"""
6. Dado o nome de um pokémon, liste de qual pokémon ele evoluiu.
Por exemplo, evolucao_anterior('venusaur') == 'ivysaur'
Retorne None se o pokémon não tem evolução anterior. 

Por exemplo, 
evolucao_anterior('bulbasaur') == None
"""
def evolucao_anterior(nome):
    pass


'''
Pulamos o exercicio 7. Depois te conto mais. Vá direto para o 8
'''


"""
8. A medida que ganham pontos de experiência, os pokémons sobem de nível.
É possível determinar o nível (1 a 100) em que um pokémon se encontra com base na quantidade de pontos de experiência que ele tem.
Entretanto, cada tipo de pokémon adota uma curva de level-up diferente (na verdade, existem apenas 6 curvas de level-up diferentes).
Assim sendo, dado um nome de pokémon e uma quantidade de pontos de experiência, retorne o nível em que este pokémon está.
Valores negativos de experiência devem ser considerados inválidos.
dica: na URL pokemon-species, procure growth rate
"""
def nivel_do_pokemon(nome, experiencia):
    pass



"""
A partir daqui, você precisará rodar o servidor treinador.py na sua máquina para poder
fazer a atividade. Não precisa mexer no arquivo, basta rodar ele.

Os testes relativos ao treinador.py estao no arquivo pokemon_treinador_unittest.py
Ou seja, você escreve o código aqui, mas testa com o pokemon_treinador_unittest.py

9. Dado um nome de treinador, cadastre-o na API de treinador.
Retorne True se um treinador com esse nome foi criado e 
        False em caso contrário (já existia).

Dicas teste 9: Use o verbo PUT, URL {site_treinador}/treinador/{nome}
para criar um treinador. Se ele já existe, será retornado um cod de status
303. Se não existe, cod status 202.

dica: considere as linhas 
      r = requests.put(url)
      status_code = r.status_code

      nelas você vê como usar o verbo put e como verificar o status code
"""

site_treinador = "http://127.0.0.1:9000" #quando você estiver executando o
#servidor do treinador, essa URL estará ativa

def cadastrar_treinador(nome):
    pass



#nao precisa mexer nas proximas excessões
# São só erros pra você lançar nas próximas funções
# Leia os nomes delas, e use quando apropriado.
class PokemonNaoCadastradoException(Exception):
    pass

class TreinadorNaoCadastradoException(Exception):
    pass

class PokemonJaCadastradoException(Exception):
    pass

"""
10. Imagine que você capturou dois pokémons do mesmo tipo. 
Para diferenciá-los, você dá nomes diferentes (apelidos) para eles.
Logo, um treinador pode ter mais do que um pokémon de um determinado tipo, 
mas não pode ter dois pokémons diferentes com o mesmo apelido.

Dados: um nome de treinador, um apelido de pokémon, um tipo de pokémon e uma quantidade de experiência, 

cadastre o pokémon com o tipo correspondente, na lista do treinador que foi passado,
usando a API (o servidor) do treinador.
Certifique-se de que todos os dados são válidos.
Inicio teste 10 -- para passar o 10a
* Para cadastrar um pokemon, usar a url 
{site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}, enviando um arquivo json 
com a chave tipo (por exemplo tipo=pikachu) e a chave experiência
* Para enviar um dicionario pra uma URL, usando o verbo put, faça o seguinte:
requests.put(url,json = {"tipo":"pikachu","experiencia"...})


Mais dicas teste 10: 
* Pode ser necessário usar a pokeapi para verificar se um pokemon existe -- se eu falar que o geremias é dono de um pokemon do tipo homer, deve ocorrer uma excessao, porque homer não é uma espécie válida de pokemon
* Se voce receber um status 404, isso indica um treinador nao encontrado
* Se voce receber um status 409, isso indica que o pokemon já existia e você
está fazendo um cadastro dobrado
* Se voce receber um status 202, isso indica criação bem sucedida
"""
def cadastrar_pokemon(nome_treinador, apelido_pokemon, tipo_pokemon, experiencia):
    pass

def cadastrar_pokemon(nome_treinador, apelido_pokemon, tipo_pokemon, experiencia):
    tipo_pokemon_lower = tipo_pokemon.lower()#necessário para pokeapi mas nao treinador, só estou
    #deixando isso claro
    resposta1 = requests.get(f"{site_pokeapi}/api/v2/pokemon/{tipo_pokemon_lower}/")
    if resposta1.status_code == 404: raise PokemonNaoExisteException()
    resposta = requests.put(f"{site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}", json = {'tipo': tipo_pokemon, 'experiencia': experiencia})
    if resposta.status_code == 404: raise TreinadorNaoCadastradoException()
    if resposta.status_code == 409: raise PokemonJaCadastradoException()
    assert resposta.status_code == 202

"""
11. Dado um nome de treinador, um apelido de pokémon e uma quantidade de experiência, localize esse pokémon e acrescente-lhe a experiência ganha.
Dicas ex 11:
utilize a URL {site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}/exp
Por exemplo, se for o pokemon com apelido terra
do treinador lucas, a URL ficaria: {site_treinador}/treinador/lucas/terra/exp


Utilize o verbo POST, enviando um arquivo json com a chave experiencia (o valor dessa chave é o tanto de xp que eu quero acrescentar)

Para enviar um request com o verbo post, use requests.post(url,...)

Um cod de status 404 pode significar 2 coisas distintas: ou o treinador não existe,
ou o treinador existe mas o pokemon não. Isso pode verificado acessando a resposta.text
(em vez do usual, que seria resposta.json())

O cod de status de sucesso é o 204
"""
def ganhar_experiencia(nome_treinador, apelido_pokemon, experiencia):
    pass


"""
Esta classe será utilizada no exercício 12 abaixo.
"""
@dataclass()
class Pokemon:
    nome_treinador: str
    apelido: str
    tipo: str
    experiencia: int
    nivel: int
    cor: str
    evoluiu_de: str

       
"""
12. Dado um nome de treinador e um apelido de pokémon, localize esse pokémon na API do treinador e retorne um objeto da classe Pokemon, prenchida com os atributos definidos na classe
Dicas 12:
pegar os dados na url "{site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}"
acessada com o verbo GET
para preencher o objeto Pokemon, voce vai fornecer
* nome treinador (veio como argumento da funcao)
* apelido pokemon (veio como argumento da funcao)
* tipo (veio do get que você fez -- chave tipo do dicionário)
* experiencia (veio do request que você fez -- chave experiencia do dicionário)
* nivel do pokemon (calcular usando a pokeapi -- voce ja fez essa funcao, use ela)
* cor do pokemon (em portugues, pegar da pokeapi -- voce ja fez essa funcao, use ela)
* evolucao anterior (pegar da pokeapi -- voce ja fez essa funcao, use ela)
Retornar o objeto pokemon
Erros 404 podem ser treinador nao existe ou pokemon nao existe -- verifique resposta.text para ver qual dos dois -- já fizemos isso antes

para criar o objeto do tipo pokemon, já temos uma classe

Podemos construir um objeto do tipo pokemon assim:

Pokemon(nome_treinador, apelido_pokemon, tipo, experiencia, nivel_do_pokemon(tipo, experiencia), cor_do_pokemon(tipo), evolucao_anterior(tipo))
"""
def localizar_pokemon(nome_treinador, apelido_pokemon):
    pass


"""
13. Dado o nome de um treinador, localize-o na API do treinador e retorne um dicionário dos seus pokemons. As chaves do dicionário serão os apelidos dos pokémons dele, e os valores serão os tipos (pikachu, bulbasaur ...) deles.

Essas informações estão na URL "{site_treinador}/treinador/{nome_treinador}",
acessiveis com o verbo GET
Consulte ela com seu navegador e veja o que tem lá! (talvez você queira usar
as funções anteriores para criar um treinador e seus pokemons...)
"""
def detalhar_treinador(nome_treinador):
    pass



"""
14. Dado o nome de um treinador, localize-o na API do treinador e exclua-o, juntamente com todos os seus pokémons.

Usar o verbo delete na url do treinador. A mesma que a gente já usou várias vezes.
O status code vai de informar se o treinador não existia (com qual status code?)

Para enviar um request com o verbo delete, use requests.delete(url)
"""
def excluir_treinador(nome_treinador):
    pass


"""
15. Dado o nome de um treinador e o apelido de um de seus pokémons, localize o pokémon na API do treinador e exclua-o.

Usar o verbo delete na url do pokemon: {site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}
O status code vai de informar se o treinador não existe, ou se o pokemon nao existe 
(status code 404, não deixe de verificar se foi o pokemon ou treinador que não existia)
"""
def excluir_pokemon(nome_treinador, apelido_pokemon):
    pass




"""
O próximo exercício é um desafio, não tem nada a ver com o treinador.py, 
usa somente a pokeapi

16. Dado o nome de um pokémon, liste para quais pokémons ele pode evoluiur.
Por exemplo, evolucoes_proximas('ivysaur') == ['venusaur'].
A maioria dos pokémons que podem evoluir, só podem evoluir para um único tipo de pokémon próximo. No entanto, há alguns que podem evoluir para dois ou mais tipos diferentes de pokémons.
Se houver múltiplas possibilidades de evoluções, a ordem delas não importa. Por exemplo:
evolucoes_proximas('poliwhirl') == ['poliwrath', 'politoed']
Note que esta função dá como resultado somente o próximo passo evolutivo. Assim sendo, evolucoes_proximas('poliwag') == ['poliwhirl']
Se o pokémon não evolui, retorne uma lista vazia. Por exemplo, evolucoes_proximas('celebi') == []

O exercicio 16 é bastante dificil e opcional.
Talvez seja útil procurar e aprender sobre recursão.
"""


#ignore o código a seguir, ele só existe por motivos burocráticos do professor
try:
    from pokemon_gabarito import *
except:
    pass



'TESTES'

import unittest
from requests import api



class TestPokeapi(unittest.TestCase):
    
    def test_01a_ok(self):
        verificar_online("pokeapi")
        self.assertEqual(nome_do_pokemon(1), "bulbasaur")
        self.assertEqual(nome_do_pokemon(55), "golduck")
        self.assertEqual(nome_do_pokemon(25), "pikachu")
        self.assertEqual(nome_do_pokemon(700), "sylveon")
        self.assertEqual(nome_do_pokemon(807), "zeraora")

    
    def test_02a_ok(self):
        self.assertEqual(numero_do_pokemon("marill"), 183)

    
    def test_02b_caps(self):
        self.assertEqual(numero_do_pokemon("EEVEE"), 133)
        self.assertEqual(numero_do_pokemon("Psyduck"), 54)
        self.assertEqual(numero_do_pokemon("SkiTtY"), 300)
        self.assertEqual(numero_do_pokemon("Zeraora"), 807)

    
    def test_02c_nao_existe(self):
        pokemon_nao_existe(lambda : numero_do_pokemon("DOBBY"), self)
        pokemon_nao_existe(lambda : numero_do_pokemon("Peppa-Pig"), self)
        pokemon_nao_existe(lambda : numero_do_pokemon("batman"), self)
        pokemon_nao_existe(lambda : numero_do_pokemon("SpiderMan"), self)

    
    def test_03a_ok(self):
        self.assertEqual(color_of_pokemon("marill"), "blue")
        self.assertEqual(color_of_pokemon("togekiss"), "white")
        self.assertEqual(color_of_pokemon("magneton"), "gray")

    
    def test_03b_caps(self):
        self.assertEqual(color_of_pokemon("EEVEE"), "brown")
        self.assertEqual(color_of_pokemon("Psyduck"), "yellow")
        self.assertEqual(color_of_pokemon("SkiTtY"), "pink")
        self.assertEqual(color_of_pokemon("GASTLY"), "purple")
        self.assertEqual(color_of_pokemon("LeDyBa"), "red")
        self.assertEqual(color_of_pokemon("Torterra"), "green")
        self.assertEqual(color_of_pokemon("xurkiTree"), "black")

    
    def test_03c_nao_existe(self):
        pokemon_nao_existe(lambda : color_of_pokemon("DOBBY"), self)
        pokemon_nao_existe(lambda : color_of_pokemon("Peppa-Pig"), self)
        pokemon_nao_existe(lambda : color_of_pokemon("batman"), self)
        pokemon_nao_existe(lambda : color_of_pokemon("SpiderMan"), self)

    
    def test_04a_ok(self):
        self.assertEqual(cor_do_pokemon("marill"), "azul")
        self.assertEqual(cor_do_pokemon("togekiss"), "branco")

    
    def test_04b_caps(self):
        self.assertEqual(cor_do_pokemon("EEVEE"), "marrom")
        self.assertEqual(cor_do_pokemon("Psyduck"), "amarelo")
        self.assertEqual(cor_do_pokemon("SkiTtY"), "rosa")
        self.assertEqual(cor_do_pokemon("magneton"), "cinza")
        self.assertEqual(cor_do_pokemon("GASTLY"), "roxo")
        self.assertEqual(cor_do_pokemon("LeDyBa"), "vermelho")
        self.assertEqual(cor_do_pokemon("Torterra"), "verde")
        self.assertEqual(cor_do_pokemon("xurkiTree"), "preto")

    
    def test_04c_nao_existe(self):
        pokemon_nao_existe(lambda : cor_do_pokemon("DOBBY"), self)
        pokemon_nao_existe(lambda : cor_do_pokemon("Peppa-Pig"), self)
        pokemon_nao_existe(lambda : cor_do_pokemon("batman"), self)
        pokemon_nao_existe(lambda : cor_do_pokemon("SpiderMan"), self)

    
    def test_05a_ok(self):
        self.assert_equals_unordered_list(["grama"], tipos_do_pokemon("chikorita"))
        self.assert_equals_unordered_list(["terra"], tipos_do_pokemon("hippowdon"))
        self.assert_equals_unordered_list(["normal", "fada"], tipos_do_pokemon("jigglypuff"))
        self.assert_equals_unordered_list(["fogo"], tipos_do_pokemon("darumaka"))
        self.assert_equals_unordered_list(["pedra", "voador"], tipos_do_pokemon("archeops"))

    
    def test_05b_caps(self):
        self.assert_equals_unordered_list(["voador", "noturno"], tipos_do_pokemon("murKrow"))
        self.assert_equals_unordered_list(["água", "elétrico"], tipos_do_pokemon("cHinChou"))
        self.assert_equals_unordered_list(["lutador", "fantasma"], tipos_do_pokemon("MARSHADOW"))
        self.assert_equals_unordered_list(["aço"], tipos_do_pokemon("KLINK"))
        self.assert_equals_unordered_list(["lutador", "inseto"], tipos_do_pokemon("Heracross"))
        self.assert_equals_unordered_list(["veneno", "noturno"], tipos_do_pokemon("DRAPION"))
        self.assert_equals_unordered_list(["psíquico", "gelo"], tipos_do_pokemon("JYNX"))
        self.assert_equals_unordered_list(["dragão"], tipos_do_pokemon("dRaTiNi"))

    
    def test_05c_nao_existe(self):
        pokemon_nao_existe(lambda : tipos_do_pokemon("DOBBY"), self)
        pokemon_nao_existe(lambda : tipos_do_pokemon("Peppa-Pig"), self)
        pokemon_nao_existe(lambda : tipos_do_pokemon("batman"), self)
        pokemon_nao_existe(lambda : tipos_do_pokemon("SpiderMan"), self)

    
    def test_06a_ok(self):
        self.assertEqual(evolucao_anterior("togetic"), "togepi")

    
    def test_06b_caps(self):
        self.assertEqual(evolucao_anterior("togeKiss"), "togetic")
        self.assertEqual(evolucao_anterior("EEleKtriK"), "tynamo")
        self.assertEqual(evolucao_anterior("EELEKTROSS"), "eelektrik")
        self.assertEqual(evolucao_anterior("Pikachu"), "pichu")
        self.assertEqual(evolucao_anterior("rAiChu"), "pikachu")

    
    def test_06c_nao_tem(self):
        self.assertIs(evolucao_anterior("togepi"), None)
        self.assertIs(evolucao_anterior("TYNAMO"), None)
        self.assertIs(evolucao_anterior("Pichu"), None)

    
    def test_06d_nao_existe(self):
        pokemon_nao_existe(lambda : evolucao_anterior("DOBBY"), self)
        pokemon_nao_existe(lambda : evolucao_anterior("Peppa-Pig"), self)
        pokemon_nao_existe(lambda : evolucao_anterior("batman"), self)
        pokemon_nao_existe(lambda : evolucao_anterior("SpiderMan"), self)

    def test_07_pulado(self):
        pass #depois te mostro esse exercicio, pode ir pro 8
      
    def test_08a_simples(self):
        self.assertEqual(nivel_do_pokemon("blastoise",   110000), 49) # 4
        self.assertEqual(nivel_do_pokemon("mewtwo",     1000000), 92) # 1
        self.assertEqual(nivel_do_pokemon("Magikarp",       900),  8) # 1
        self.assertEqual(nivel_do_pokemon("Magikarp",   1000000), 92) # 1
        self.assertEqual(nivel_do_pokemon("SLOWBRO",      65000), 40) # 2
        self.assertEqual(nivel_do_pokemon("OcTiLLeRy",   280000), 65) # 2
        self.assertEqual(nivel_do_pokemon("FRAXURE",     280000), 60) # 1
        self.assertEqual(nivel_do_pokemon("lunatone",     20000), 29) # 3
        self.assertEqual(nivel_do_pokemon("skitty",       50000), 39) # 3
        self.assertEqual(nivel_do_pokemon("torchic",      40000), 35) # 4
        self.assertEqual(nivel_do_pokemon("ODDISH",        5000), 19) # 4

    
    def test_08b_complexos(self):
        self.assertEqual(nivel_do_pokemon("zangoose",      9000), 17) # 5
        self.assertEqual(nivel_do_pokemon("milotic",      65000), 37) # 5
        self.assertEqual(nivel_do_pokemon("Lumineon",    160000), 55) # 5
        self.assertEqual(nivel_do_pokemon("NINJASK",     300000), 72) # 5
        self.assertEqual(nivel_do_pokemon("zangoose",    580000), 97) # 5
        self.assertEqual(nivel_do_pokemon("makuhita",       600), 10) # 6
        self.assertEqual(nivel_do_pokemon("gulpin",        7000), 21) # 6
        self.assertEqual(nivel_do_pokemon("seviper",     150000), 50) # 6
        self.assertEqual(nivel_do_pokemon("drifblim",   1000000), 87) # 6

    
    def test_08c_limites(self):
        self.assertEqual(nivel_do_pokemon("pinsir",           0),   1) # 1
        self.assertEqual(nivel_do_pokemon("bibarel",          0),   1) # 2
        self.assertEqual(nivel_do_pokemon("aipom",            0),   1) # 3
        self.assertEqual(nivel_do_pokemon("Makuhita",         0),   1) # 6
        self.assertEqual(nivel_do_pokemon("Magikarp",      1249),   9) # 1
        self.assertEqual(nivel_do_pokemon("MeTaPoD",        999),   9) # 2
        self.assertEqual(nivel_do_pokemon("Magikarp",      1250),  10) # 1
        self.assertEqual(nivel_do_pokemon("Butterfree",    1000),  10) # 2
        self.assertEqual(nivel_do_pokemon("charmeleon",   29948),  32) # 4
        self.assertEqual(nivel_do_pokemon("charmeleon",   29949),  33) # 4
        self.assertEqual(nivel_do_pokemon("hariyama",     71676),  40) # 6
        self.assertEqual(nivel_do_pokemon("hariyama",     71677),  41) # 6
        self.assertEqual(nivel_do_pokemon("togePI",      799999),  99) # 3
        self.assertEqual(nivel_do_pokemon("gengar",     1059859),  99) # 4
        self.assertEqual(nivel_do_pokemon("zangoose",    599999),  99) # 5
        self.assertEqual(nivel_do_pokemon("SWALot",     1639999),  99) # 6
        self.assertEqual(nivel_do_pokemon("sYLVEON",    1000000), 100) # 2
        self.assertEqual(nivel_do_pokemon("Jigglypuff", 1000000), 100) # 3
        self.assertEqual(nivel_do_pokemon("LEDIAN",      800000), 100) # 3
        self.assertEqual(nivel_do_pokemon("vaPorEON", 999999999), 100) # 2
        self.assertEqual(nivel_do_pokemon("VILEPLUME",  1059860), 100) # 4
        self.assertEqual(nivel_do_pokemon("zangoose",    600000), 100) # 5
        self.assertEqual(nivel_do_pokemon("SWALOT",     1640000), 100) # 6

    
    def test_08d_nao_existe(self):
        pokemon_nao_existe(lambda : nivel_do_pokemon("DOBBY", 1234), self)
        pokemon_nao_existe(lambda : nivel_do_pokemon("Peppa-Pig", 1234), self)
        pokemon_nao_existe(lambda : nivel_do_pokemon("batman", 1234), self)
        pokemon_nao_existe(lambda : nivel_do_pokemon("SpiderMan", 1234), self)

    def reset(self):
        resposta = requests.post(f"{site_treinador}/reset")
        self.assertEqual(resposta.status_code, 200)

    
    def test_09a_ok(self):
        verificar_online("pokeapi+treinador")
        self.reset()

        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {})
        
        self.assertTrue(cadastrar_treinador("Ash Ketchum"))

        self.assertTrue(cadastrar_treinador("Misty"))

        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Ash Ketchum": {"nome": "Ash Ketchum", "pokemons": {}},
            "Misty": {"nome": "Misty", "pokemons": {}}
        })

    
    def test_09b_limpeza(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Jessie"))
        self.assertTrue(cadastrar_treinador("James"))
        self.reset()
        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {})

    
    def test_09c_repetido(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Jessie"))
        self.assertFalse(cadastrar_treinador("Jessie"))
        
        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Jessie": {"nome": "Jessie", "pokemons": {}}
        })

        

    
    def test_10a_ok(self):
        self.reset()

        oldMaxDiff = self.maxDiff
        self.maxDiff = None
        
        self.assertTrue(cadastrar_treinador("Ash Ketchum"))
        cadastrar_pokemon("Ash Ketchum", "P", "Pikachu", 50000)
        self.assertTrue(cadastrar_treinador("Misty"))
        cadastrar_pokemon("Misty", "A", "STARYU", 10000)
        cadastrar_pokemon("Misty", "B", "sTaRyU", 12000)
        self.assertTrue(cadastrar_treinador("Brock"))
        cadastrar_pokemon("Brock", "O", "onix", 8000)
        cadastrar_pokemon("Brock", "G", "Geodude", 20000)
        self.assertTrue(cadastrar_treinador("James"))
        cadastrar_pokemon("James", "A", "KOFFING", 5000)
        cadastrar_pokemon("James", "B", "MeowTH", 20000)

        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Ash Ketchum": {"nome": "Ash Ketchum", "pokemons": {"P": {"apelido": "P", "tipo": "pikachu", "experiencia": 50000}}},
            "Misty": {"nome": "Misty", "pokemons": {"A": {"apelido": "A", "tipo": "staryu", "experiencia": 10000}, "B": {"apelido": "B", "tipo": "staryu", "experiencia": 12000}}},
            "Brock": {"nome": "Brock", "pokemons": {"O": {"apelido": "O", "tipo": "onix", "experiencia": 8000}, "G": {"apelido": "G", "tipo": "geodude", "experiencia": 20000}}},
            "James": {
                "nome": "James",
                "pokemons": {
                    "A": {"apelido": "A", "tipo": "koffing", "experiencia": 5000},
                    "B": {"apelido": "B", "tipo": "meowth", "experiencia": 20000}
                }
            }
        })
        self.maxDiff = oldMaxDiff

    
    def test_10b_treinador_nao_existe(self):
        self.reset()
        treinador_nao_cadastrado(lambda : cadastrar_pokemon("Max", "D", "lapras", 40000), self)
        self.assertEqual(requests.get(f"{site_treinador}/treinador").json(), {})

    
    def test_10c_pokemon_nao_existe(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Iris"))
        pokemon_nao_existe(lambda : cadastrar_pokemon("Iris", "D", "homer", 40000), self)
        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Iris": {"nome": "Iris", "pokemons": {}}
        })

    
    def test_10d_pokemon_ja_existe(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Misty"))
        cadastrar_pokemon("Misty", "estrela", "STARMIE", 40000)
        pokemon_ja_cadastrado(lambda : cadastrar_pokemon("Misty", "estrela", "staryu", 1000), self)

        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Misty": {"nome": "Misty", "pokemons": {"estrela": {"apelido": "estrela", "tipo": "starmie", "experiencia": 40000}}}
        })

    
    def test_10e_treinador_errado(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Ash Ketchum"))
        treinador_nao_cadastrado(lambda : cadastrar_pokemon("Gary", "pi", "pikachu", 40000), self)
        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Ash Ketchum": {"nome": "Ash Ketchum", "pokemons": {}}
        })
    
    
    def test_11f_treinador_repetido(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Jessie"))
        self.assertFalse(cadastrar_treinador("Jessie"))
        
        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Jessie": {"nome": "Jessie", "pokemons": {}}
        })

        
        cadastrar_pokemon("Jessie", "A", "ARBOK", 20000)
        cadastrar_pokemon("Jessie", "B", "wobbuffet", 2000)
        cadastrar_pokemon("Jessie", "C", "Lickitung", 2500)
        self.assertFalse(cadastrar_treinador("Jessie"))

        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Jessie": {
                "nome": "Jessie",
                "pokemons": {
                    "A": {"apelido": "A", "tipo": "arbok", "experiencia": 20000},
                    "B": {"apelido": "B", "tipo": "wobbuffet", "experiencia": 2000},
                    "C": {"apelido": "C", "tipo": "lickitung", "experiencia": 2500}
                }
            }
        })

    
    def test_11a_ok(self):
        self.reset()

        self.assertTrue(cadastrar_treinador("Ash Ketchum"))
        cadastrar_pokemon("Ash Ketchum", "P", "pikachu", 50000)
        ganhar_experiencia("Ash Ketchum", "P", 1500)

        self.assertTrue(cadastrar_treinador("James"))
        cadastrar_pokemon("James", "P", "WEEZING", 10000)
        cadastrar_pokemon("James", "Q", "VictREeBEL", 12000)
        ganhar_experiencia("James", "P", 2500)

        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Ash Ketchum": {"nome": "Ash Ketchum", "pokemons": {"P": {"apelido": "P", "tipo": "pikachu", "experiencia": 51500}}},
            "James": {"nome": "James", "pokemons": {"P": {"apelido": "P", "tipo": "weezing", "experiencia": 12500}, "Q": {"apelido": "Q", "tipo": "victreebel", "experiencia": 12000}}}
        })

    
    def test_11b_treinador_nao_existe(self):
        self.reset()
        treinador_nao_cadastrado(lambda : ganhar_experiencia("Cilan", "bob-esponja", 10000), self)
        self.assertEqual(requests.get(f"{site_treinador}/treinador").json(), {})

    
    def test_11c_pokemon_nao_existe(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Bonnie"))
        pokemon_nao_cadastrado(lambda : ganhar_experiencia("Bonnie", "bob-esponja", 40000), self)

        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Bonnie": {"nome": "Bonnie", "pokemons": {}}
        })

    
    def test_11d_treinador_errado(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Serena"))
        self.assertTrue(cadastrar_treinador("Dawn"))
        cadastrar_pokemon("Serena", "fen", "fennekin", 5000)
        pokemon_nao_cadastrado(lambda : ganhar_experiencia("Dawn", "fen", 100), self)

        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Serena": {"nome": "Serena", "pokemons": {"fen": {"apelido": "fen", "tipo": "fennekin", "experiencia": 5000}}},
            "Dawn": {"nome": "Dawn", "pokemons": {}}
        })

    
    def test_12a_ok(self):
        self.reset()

        self.assertTrue(cadastrar_treinador("Ash Ketchum"))
        cadastrar_pokemon("Ash Ketchum", "P", "pikachu", 50000)

        self.assertTrue(cadastrar_treinador("James"))
        cadastrar_pokemon("James", "P", "WEEZING", 10000)
        cadastrar_pokemon("James", "Q", "Gloom", 12000)

        pikachu = localizar_pokemon("Ash Ketchum", "P")
        weezing = localizar_pokemon("James", "P")
        gloom = localizar_pokemon("James", "Q")

        self.assertIs(type(pikachu), Pokemon)
        self.assertEqual(pikachu.nome_treinador, "Ash Ketchum")
        self.assertEqual(pikachu.apelido, "P")
        self.assertEqual(pikachu.tipo, "pikachu")
        self.assertEqual(pikachu.experiencia, 50000)
        self.assertEqual(pikachu.nivel, 36)
        self.assertEqual(pikachu.cor, "amarelo")
        self.assertEqual(pikachu.evoluiu_de, "pichu")

        self.assertIs(type(weezing), Pokemon)
        self.assertEqual(weezing.nome_treinador, "James")
        self.assertEqual(weezing.apelido, "P")
        self.assertEqual(weezing.tipo, "weezing")
        self.assertEqual(weezing.experiencia, 10000)
        self.assertEqual(weezing.nivel, 21)
        self.assertEqual(weezing.cor, "roxo")
        self.assertEqual(weezing.evoluiu_de, "koffing")

        self.assertIs(type(gloom), Pokemon)
        self.assertEqual(gloom.nome_treinador, "James")
        self.assertEqual(gloom.apelido, "Q")
        self.assertEqual(gloom.tipo, "gloom")
        self.assertEqual(gloom.experiencia, 12000)
        self.assertEqual(gloom.nivel, 25)
        self.assertEqual(gloom.cor, "azul")
        self.assertEqual(gloom.evoluiu_de, "oddish")

    
    def test_12b_treinador_nao_existe(self):
        self.reset()
        treinador_nao_cadastrado(lambda : localizar_pokemon("Cilan", "bob-esponja"), self)
        self.assertEqual(requests.get(f"{site_treinador}/treinador").json(), {})

    
    def test_12c_pokemon_nao_existe(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Bonnie"))
        pokemon_nao_cadastrado(lambda : localizar_pokemon("Bonnie", "bob-esponja"), self)

        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Bonnie": {"nome": "Bonnie", "pokemons": {}}
        })

    
    def test_12d_treinador_errado(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Serena"))
        self.assertTrue(cadastrar_treinador("Dawn"))
        cadastrar_pokemon("Serena", "fen", "fennekin", 5000)
        pokemon_nao_cadastrado(lambda : localizar_pokemon("Dawn", "fen"), self)

        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Serena": {"nome": "Serena", "pokemons": {"fen": {"apelido": "fen", "tipo": "fennekin", "experiencia": 5000}}},
            "Dawn": {"nome": "Dawn", "pokemons": {}}
        })

    
    def test_13a_ok(self):
        self.reset()

        self.assertTrue(cadastrar_treinador("Ash Ketchum"))
        cadastrar_pokemon("Ash Ketchum", "P", "pikachu", 50000)

        self.assertTrue(cadastrar_treinador("James"))
        cadastrar_pokemon("James", "P", "WEEZING", 10000)
        cadastrar_pokemon("James", "Q", "WeepinBElL", 12000)

        ash = detalhar_treinador("Ash Ketchum")
        james = detalhar_treinador("James")

        self.assertEqual(ash, {"P": "pikachu"})
        self.assertEqual(james, {"P": "weezing", "Q": "weepinbell"})

    
    def test_13b_treinador_nao_existe(self):
        self.reset()
        treinador_nao_cadastrado(lambda : detalhar_treinador("Cilan"), self)
        self.assertEqual(requests.get(f"{site_treinador}/treinador").json(), {})

    
    def test_14a_ok(self):
        self.reset()

        self.assertTrue(cadastrar_treinador("Ash Ketchum"))
        cadastrar_pokemon("Ash Ketchum", "P", "pikachu", 50000)

        self.assertTrue(cadastrar_treinador("Prof. Carvalho"))

        self.assertTrue(cadastrar_treinador("James"))
        cadastrar_pokemon("James", "P", "WEEZING", 10000)
        cadastrar_pokemon("James", "Q", "WeepinBElL", 12000)

        excluir_treinador("Ash Ketchum")

        resposta1 = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta1.json(), {
            "James": {"nome": "James", "pokemons": {"P": {"apelido": "P", "tipo": "weezing", "experiencia": 10000}, "Q": {"apelido": "Q", "tipo": "weepinbell", "experiencia": 12000}}},
            "Prof. Carvalho": {"nome": "Prof. Carvalho", "pokemons": {}}
        })
        treinador_nao_cadastrado(lambda : detalhar_treinador("Ash Ketchum"), self)
        treinador_nao_cadastrado(lambda : localizar_pokemon("Ash Ketchum", "P"), self)

        excluir_treinador("James")

        resposta2 = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta2.json(), {
            "Prof. Carvalho": {"nome": "Prof. Carvalho", "pokemons": {}}
        })
        treinador_nao_cadastrado(lambda : detalhar_treinador("James"), self)
        treinador_nao_cadastrado(lambda : localizar_pokemon("James", "P"), self)
        treinador_nao_cadastrado(lambda : localizar_pokemon("James", "Q"), self)

        excluir_treinador("Prof. Carvalho")

        resposta3 = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta3.json(), {})
        treinador_nao_cadastrado(lambda : detalhar_treinador("Prof. Carvalho"), self)

    
    def test_14b_treinador_nao_existe(self):
        self.reset()

        treinador_nao_cadastrado(lambda : excluir_treinador("Kiawe"), self)
        self.assertEqual(requests.get(f"{site_treinador}/treinador").json(), {})

        self.assertTrue(cadastrar_treinador("Kiawe"))
        cadastrar_pokemon("Kiawe", "c", "charizard", 50000)
        treinador_nao_cadastrado(lambda : excluir_treinador("Lillie"), self)
        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Kiawe": {"nome": "Kiawe", "pokemons": {"c": {"apelido": "c", "tipo": "charizard", "experiencia": 50000}}}
        })

        excluir_treinador("Kiawe")
        self.assertEqual(requests.get(f"{site_treinador}/treinador").json(), {})

    
    def test_15a_ok(self):
        self.reset()

        self.assertTrue(cadastrar_treinador("Ash Ketchum"))
        cadastrar_pokemon("Ash Ketchum", "P", "pikachu", 50000)

        self.assertTrue(cadastrar_treinador("Prof. Carvalho"))

        self.assertTrue(cadastrar_treinador("James"))
        cadastrar_pokemon("James", "P", "WEEZING", 10000)
        cadastrar_pokemon("James", "Q", "WeepinBElL", 12000)

        excluir_pokemon("Ash Ketchum", "P")

        resposta1 = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta1.json(), {
            "Ash Ketchum": {"nome": "Ash Ketchum", "pokemons": {}},
            "James": {"nome": "James", "pokemons": {"P": {"apelido": "P", "tipo": "weezing", "experiencia": 10000}, "Q": {"apelido": "Q", "tipo": "weepinbell", "experiencia": 12000}}},
            "Prof. Carvalho": {"nome": "Prof. Carvalho", "pokemons": {}}
        })
        pokemon_nao_cadastrado(lambda : localizar_pokemon("Ash Ketchum", "P"), self)
        localizar_pokemon("James", "P")
        localizar_pokemon("James", "Q")

        excluir_pokemon("James", "Q")

        resposta2 = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta2.json(), {
            "Ash Ketchum": {"nome": "Ash Ketchum", "pokemons": {}},
            "James": {"nome": "James", "pokemons": {"P": {"apelido": "P", "tipo": "weezing", "experiencia": 10000}}},
            "Prof. Carvalho": {"nome": "Prof. Carvalho", "pokemons": {}}
        })
        pokemon_nao_cadastrado(lambda : localizar_pokemon("Ash Ketchum", "P"), self)
        localizar_pokemon("James", "P")
        pokemon_nao_cadastrado(lambda : localizar_pokemon("James", "Q"), self)

        excluir_pokemon("James", "P")

        resposta3 = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta3.json(), {
            "Ash Ketchum": {"nome": "Ash Ketchum", "pokemons": {}},
            "James": {"nome": "James", "pokemons": {}},
            "Prof. Carvalho": {"nome": "Prof. Carvalho", "pokemons": {}}
        })
        pokemon_nao_cadastrado(lambda : localizar_pokemon("Ash Ketchum", "P"), self)
        pokemon_nao_cadastrado(lambda : localizar_pokemon("James", "P"), self)
        pokemon_nao_cadastrado(lambda : localizar_pokemon("James", "Q"), self)

    
    def test_15b_treinador_nao_existe(self):
        self.reset()

        self.assertTrue(cadastrar_treinador("Kiawe"))
        cadastrar_pokemon("Kiawe", "c", "charizard", 50000)
        treinador_nao_cadastrado(lambda : excluir_pokemon("Lillie", "c"), self)
        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Kiawe": {"nome": "Kiawe", "pokemons": {"c": {"apelido": "c", "tipo": "charizard", "experiencia": 50000}}}
        })

        localizar_pokemon("Kiawe", "c")
        self.assertEqual(requests.get(f"{site_treinador}/treinador").json(), {
            "Kiawe": {"nome": "Kiawe", "pokemons": {"c": {"apelido": "c", "tipo": "charizard", "experiencia": 50000}}}
        })

    
    def test_15c_pokemon_nao_existe(self):
        self.reset()

        self.assertTrue(cadastrar_treinador("Kiawe"))
        cadastrar_pokemon("Kiawe", "c", "charizard", 50000)
        pokemon_nao_cadastrado(lambda : excluir_pokemon("Kiawe", "d"), self)
        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Kiawe": {"nome": "Kiawe", "pokemons": {"c": {"apelido": "c", "tipo": "charizard", "experiencia": 50000}}}
        })

        localizar_pokemon("Kiawe", "c")
        self.assertEqual(requests.get(f"{site_treinador}/treinador").json(), {
            "Kiawe": {"nome": "Kiawe", "pokemons": {"c": {"apelido": "c", "tipo": "charizard", "experiencia": 50000}}}
        })

        excluir_pokemon("Kiawe", "c")
        self.assertEqual(requests.get(f"{site_treinador}/treinador").json(), {
            "Kiawe": {"nome": "Kiawe", "pokemons": {}}
        })

    def test_16a_ok_evolucoes_simples(self):
        self.assert_equals_unordered_list(["charmeleon"], evolucoes_proximas("charmander"))
        self.assert_equals_unordered_list(["combusken"], evolucoes_proximas("torchic"))
        self.assert_equals_unordered_list(["charizard"], evolucoes_proximas("ChArMeLeON"))

    
    def test_16b_ok_nao_tem_simples(self):
        self.assert_equals_unordered_list([], evolucoes_proximas("lugia"))
        self.assert_equals_unordered_list([], evolucoes_proximas("turtonator"))
        self.assert_equals_unordered_list([], evolucoes_proximas("CHARIZARD"))
        self.assert_equals_unordered_list([], evolucoes_proximas("gEnGar"))
        self.assert_equals_unordered_list([], evolucoes_proximas("ALAkazam"))

    
    def test_16c_ok_evolucoes_complexas(self):
        self.assert_equals_unordered_list(["ninjask", "shedinja"], evolucoes_proximas("nincada"))
        self.assert_equals_unordered_list(["vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"], evolucoes_proximas("eevee"))
        self.assert_equals_unordered_list(["hitmonlee", "hitmonchan", "hitmontop"], evolucoes_proximas("tyrogue"))
        self.assert_equals_unordered_list(["poliwhirl"], evolucoes_proximas("Poliwag"))
        self.assert_equals_unordered_list(["gloom"], evolucoes_proximas("oDDiSH"))
        self.assert_equals_unordered_list(["poliwrath", "politoed"], evolucoes_proximas("PoliWHIRL"))
        self.assert_equals_unordered_list(["vileplume", "bellossom"], evolucoes_proximas("GLOOM"))

    
    def test_16d_ok_nao_tem_complexas(self):
        self.assert_equals_unordered_list([], evolucoes_proximas("espeon"))
        self.assert_equals_unordered_list([], evolucoes_proximas("Leafeon"))
        self.assert_equals_unordered_list([], evolucoes_proximas("POLITOED"))

    
    def test_16e_nao_existe(self):
        pokemon_nao_existe(lambda : evolucoes_proximas("DOBBY"), self)
        pokemon_nao_existe(lambda : evolucoes_proximas("Peppa-Pig"), self)
        pokemon_nao_existe(lambda : evolucoes_proximas("batman"), self)
        pokemon_nao_existe(lambda : evolucoes_proximas("SpiderMan"), self)


    
    def test_98a_limpeza(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Tracey"))
        cadastrar_pokemon("Tracey", "m", "MARILL", 40000)

        self.reset()
        treinador_nao_cadastrado(lambda : detalhar_treinador("Tracey"), self)
        treinador_nao_cadastrado(lambda : localizar_pokemon("Tracey", "m"), self)
        treinador_nao_cadastrado(lambda : ganhar_experiencia("Tracey", "m", 4000), self)
        treinador_nao_cadastrado(lambda : cadastrar_pokemon("Tracey", "t", "togepi", 500), self)
        treinador_nao_cadastrado(lambda : excluir_pokemon("Tracey", "t"), self)
        treinador_nao_cadastrado(lambda : excluir_treinador("Tracey"), self)

        resposta = requests.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {})

    def test_99a_print(self):
        sem_io.test_print(self)

    def test_99b_input(self):
        sem_io.test_input(self)



def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestPokeapi)
    unittest.TextTestRunner(verbosity = 2, failfast = True).run(suite)
    #unittest.TextTestRunner(verbosity = 0, failfast = False).run(suite)


from requests import api, exceptions
from pokemon import *

def verificar_online(desejado):

    def pokeapi_online():
        try:
            resposta1 = api.get(f"{site_pokeapi}/api/v2/")
            if resposta1.status_code == 200 and resposta1.json()['pokemon'] == f'{site_pokeapi}/api/v2/pokemon/':
                return "online"
            return "zumbi"
        except exceptions.ConnectionError as x:
            return "offline"
        except:
            return "zumbi"

    def treinador_online():
        try:
            resposta2 = api.get(f"{site_treinador}/hello")
            if resposta2.status_code == 200 and resposta2.text == 'Pikachu, eu escolho você!':
                return "online"
            return "zumbi"
        except exceptions.ConnectionError as x:
            return "offline"
        except:
            return "zumbi"

    #if site_treinador != "http://127.0.0.1:9000" or site_pokeapi != "http://127.0.0.1:8000": raise Exception("As URLs para as APIs estão incorretas.")
    y = pokeapi_online()
    z = treinador_online()

    if y in ("zumbi","offline"): raise Exception("Para poder rodar os testes, você precisa de acesso ao pokeapi. Verifique se você tem esse acesso.")
    if desejado == "pokeapi+treinador":
        if y == "zumbi" or z == "zumbi": raise Exception("Os servidores aparentemente não estão em funcionamento. Estes testes só devem ser executados com ambos os servidores on-line.")
        if y == "offline" and z == "offline": raise Exception("Os servidores estão off-line. Estes testes só devem ser executados com ambos os servidores on-line.")
        if y == "online" and z == "offline": raise Exception("O treinador está off-line. A partir do teste 09, ele precisa estar online")
        if y == "offline" and z == "online": raise Exception("O pokeapi está off-line. Estes testes só devem ser executados com ambos os servidores on-line.")
        assert y == "online" and z == "online"
    

def verificar_erro(interno, tipo_erro, tests = None):
    if tests is None:
        try:
            interno()
        except Exception as x:
            assert type(x) is tipo_erro, f"Esperava-se que um erro do tipo {tipo_erro.__name__}, mas obteve-se uma do tipo {x.__class__.__name__}."
        else:
            assert False, f"Esperava-se que um erro do tipo {tipo_erro.__name__} fosse produzido, mas não foi."
    else:
        try:
            interno()
        except Exception as x:
            tests.assertIs(type(x), tipo_erro, f"Esperava-se que um erro do tipo {tipo_erro.__name__}, mas obteve-se uma do tipo {x.__class__.__name__}.")
        else:
            tests.fail(f"Esperava-se que um erro do tipo {tipo_erro.__name__} fosse produzido, mas não foi.")

def pokemon_nao_existe(interno, tests = None):
    verificar_erro(interno, PokemonNaoExisteException, tests)

def pokemon_nao_cadastrado(interno, tests = None):
    verificar_erro(interno, PokemonNaoCadastradoException, tests)

def treinador_nao_cadastrado(interno, tests = None):
    verificar_erro(interno, TreinadorNaoCadastradoException, tests)

def pokemon_ja_cadastrado(interno, tests = None):
    verificar_erro(interno, PokemonJaCadastradoException, tests)

def valor_errado(interno, tests = None):
    verificar_erro(interno, ValueError, tests)

def assert_equals_unordered_list(esperada, obtida, tests = None):
    error_string = f"Esperava-se que o resultado fosse {esperada}, mas foi {obtida}."
    if tests is None:
        assert len(esperada) == len(obtida), error_string
        for item in esperada:
            assert item in obtida, error_string
    else:
        tests.assertEqual(len(esperada), len(obtida), error_string)
        for item in esperada:
            tests.assertIn(item, obtida, error_string)

def assert_equals_unordered_list_clear(self, esperada, obtida):
    assert_equals_unordered_list(esperada, obtida, self)

class NoStdIO:
    def __init__(self):
        import sys
        self.__oout = sys.stdout
        self.__oin = sys.stdin
        self.__usou_print = False
        self.__usou_input = False

    def __enter__(self):
        import sys
        self.__oout = sys.stdout
        self.__oin = sys.stdin
        sys.stdout = self
        sys.stdin = self

    def __exit__(self, a, b, c):
        import sys
        sys.stdout = self.__oout
        sys.stdin = self.__oin

    def write(self, str):
        self.__usou_print = True
        return self.__oout.write(str)

    def readline(self):
        self.__usou_input = True
        return self.__oin.readline()

    def flush(self):
        pass

    @property
    def usou_print(self):
        return self.__usou_print

    @property
    def usou_input(self):
        return self.__usou_input

    def __call__(self, delegate):
        from functools import wraps
        @wraps(delegate)
        def sem_input(*args, **kwargs):
            with self:
                return delegate(*args, **kwargs)
        return sem_input

    def test_print(self, tests = None):
        if tests is None:
            assert self.usou_print == False, "Você não deveria utilizar a função print neste exercício."
        else:
            tests.assertFalse(self.usou_print, "Você não deveria utilizar a função print neste exercício.")

    def test_input(self, tests = None):
        if tests is None:
            assert self.usou_input == False, "Você não deveria utilizar a função input neste exercício."
        else:
            tests.assertFalse(self.usou_input, "Você não deveria utilizar a função print neste exercício.")

sem_io = NoStdIO()
TestPokeapi.assert_equals_unordered_list = assert_equals_unordered_list_clear

# try:
#     import sys
#     sys.path.append("../")
#     from pokemon_gabarito import *
# except:
#     pass


if __name__ == '__main__':
    runTests()

