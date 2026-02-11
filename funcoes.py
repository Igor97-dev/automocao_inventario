def escreva(txt='', pont=False):
    """
    Função para formatação de títulos ou frases.
    :param txt: frase ou título que será formatada.
    :param pont: se True, retornará apenas uma linha pontilhada.
    :return: Um Título ou uma frase formatadada.
    """
    comp = len(txt) + 22
    if pont:
        print('=' * comp)
        print(f'{txt.center(comp)}')
        print('=' * comp)
    else:
        print('=' * 50)