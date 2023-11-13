# calculadora simples de 4 operações (soma, subtração, multiplicação e divisão) usando estrutura de código orientada a objetos:

class Calculadora:  # Define a classe 'calculadora'.

    # define o método 'menu' (através da função def) da classe 'Calculadora'.
    # o parâmetro 'SELF' é uma referência à instância da classe 'Calculadora'.
    def menu(self):

      # imprime a mensagem do menu
        print('Escolha a operação:')
        print('[1] - Soma')
        print('[2] - Subtração')
        print('[3] - Multiplicação')
        print('[4] - Divisão')

        # Solicita ao usuário que digite a opção desejada e armazena o valor na variável 'escolha'.
        escolha = input('Digite a opção da operação desejada (1-4):')

        # verifica se a escolha do usuário está entre 1 e 4.
        if escolha in ('1', '2', '3', '4'):
            # solicita que o usuário digite o primeiro e segundo números e converte o valor para float(ponto flutuante).
            n1 = float(input('Digite o primeiro número: '))
            n2 = float(input('Digite o segundo número: '))

            # Através da condição IF,  - Verifica a escolha do usuário.
            if escolha == '1':
              # Calcula a soma de n1 e n2 chamando o método instânciado na classe Calculadora e armazena a mensagem formatada em resultado.
                resultado = (
                    f'O resultado da soma entre {n1} e {n2} é: {self.soma(n1,n2)}')
            elif escolha == '2':
                resultado = (
                    f'O resultado da subtração entre {n1} e {n2} é: {self.subtracao(n1,n2)}')
            elif escolha == '3':
                resultado = (
                    f'O resultado da multiplicação entre {n1} e {n2} é: {self.multiplicacao(n1,n2)}')
            elif escolha == '4':
                resultado = (
                    f'O resultado da divisão entre {n1} e {n2} é: {self.divisao(n1,n2)}')
        #  Se a escolha do usuário não foi '1', '2', '3' ou '4', executa o bloco de código abaixo.
        else:
            print('Opção inválida. Tente novamente.')
            resultado = None
        # - Verifica se resultado não é None(vazio).
        if resultado is not None:
            print(f'{resultado}')
    # Define os métodos e instancia eles na classe Calculadora, que recebe dois parâmetros, n1 e n2, e retorna o resultado deles.

    def soma(self, n1, n2):

        return n1 + n2

    def subtracao(self, n1, n2):

        return n1 - n2

    def multiplicacao(self, n1, n2):

        return n1 * n2

    def divisao(self, n1, n2):
        if n2 != 0:
            return n1 / n2
        else:
            print('Erro: divisão por zero!')
            return None


#  cria uma instância da classe Calculadora atribuindo-a à variável calc.
# Isso significa que agora existe um objeto calc que possui todas as propriedades e métodos definidos na classe Calculadora.
calc = Calculadora()
# chama o método menu da instância calc da classe Calculadora.
# Isso significa que o código dentro do método menu será executado.
calc.menu()
