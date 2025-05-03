# Ordena comparando digitos/carateres dos números, e não faz comparações diretas entre os elementos

"""
Etapas:

Seleciona uma posição de dígito (ex: unidades, dezenas, centenas)
Agrupa os elementos com base nesse dígito, mantendo a ordem original dos anteriores, por isso a necessidade de uma ordenação estável
Repete o processo para os próximos dígitos até o mais significativo

Existem duas formas de fazer isso:
  LSD -> (Least Significant Digit First): Mais comum e mais prática
  MSD -> (Most significant Digit First): Mais complexa, mas também válida
"""

# LSD, com vetor
vector = ["170", "045", "075", "090", "802", "024", "002", "066"]

# precisamos saber qual é o número com a maior quantidade de dígitos
# Cada passagem será feita com base em uma posição de dígito:
# Primeira: unidades (posição 0)
# Segunda: dezenas (posição 1)
# Terceira: centenas (posição 2)

# ---------------- Passo 1 - Ordenar pelo dígito das unidades ----------------------------


def show_dict(dict):
    for key in sorted(dict.keys()):
        print(f"{key}: ", end="")
        print(dict[key])


def showVector(vector, indexChar):
    position = ""
    if indexChar == -1:
        position = "Unidades"
    elif (indexChar == -2):
        position = "Dezenas"
    elif (indexChar == -3):
        position = "Centenas"

    print(f"Estamos na casa das {position} e o vetor está assim", end=": ")
    print(vector)


dict_aux = {}

# Tamanho da string (3) ([1 a 3]) k
for i in range(-1, -4, -1):
    dict_aux = {}
    # Tamanho do vetor (n)
    for element in vector:
        digit = element[i]

        if dict_aux.get(digit, None) == None:
            dict_aux[digit] = []

        dict_aux[digit].append(element)

    vector = []
    # sorted usa o timsort(insert + merge) -> N == 10 (no máximo) -> O(1)
    # tamanho do alfabeto S
    for key in sorted(dict_aux.keys()):
        for sub_item in dict_aux[key]:
            vector.append(sub_item)

    show_dict(dict_aux)
    showVector(vector, i)

# Complexidade (nk) de tempo, n elementos e k é o tamanho maximo da string
