import unittest, sys, os

#Método para conseguir importar um módulo externo ao diretório do arquivo atual
sys.path.append(os.getcwd())
import programa


class testes(unittest.TestCase):
    """
    Casos de testes vem aqui.

    A estrutura de cada função que roda um teste é a seguinte:
    Ao utiliar o método assertEqual, é passado o valor esperado e o valor obtido, que no caso, é o resultado da função.

    Caso o restultado obtido difira do esperado, o teste falha, retornando a mensagem do terceiro parametro.
    """

    def teste_soma(self):
        self.assertEqual(5, programa.somar(2, 3), "Erro na soma")
    
    def teste_subtracao(self):
        self.assertEqual(3, programa.subtrair(5, 2), "Erro na subtracao")

    def teste_multiplicacao(self):
        self.assertEqual(10, programa.multiplicar(2, 5), "Erro na multiplicacao")
    
    def teste_divisao(self):
        self.assertEqual(5, programa.dividir(10, 2), "Erro na divisao")


def main():
    """Cria a suite de testes (uma coletanea com todos os testes acima)"""
    suite = unittest.TestLoader().loadTestsFromTestCase(testes)

    """Executa os testes, de forma verbosa"""
    unittest.TextTestRunner(verbosity=2).run(suite)

main()