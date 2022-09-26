import unittest, sys, os

#Método para conseguir importar um módulo externo ao diretório do arquivo atual
sys.path.append(os.getcwd())
import programa

class testes(unittest.TestCase):
    """Classe de Testes Unitários"""
    
    def teste_01_idade_e_formacao_aceitaveis(self):
        idade = 26
        formacao = "engenharia"
        self.assertEqual(True, programa.validarAprovacao(idade, formacao), "Teste de idade e formacao aceitaveis falhou")

    def teste_02_idade_aceitavel_formacao_inaceitavel(self):
        idade = 26
        formacao = "psicologia"
        self.assertEqual(False, programa.validarAprovacao(idade, formacao), "Teste de idade aceitavel e formacao inaceital falhou")

    def teste_03_idade_inaceitavel(self):
        idade = 25
        formacao = "informatica"
        self.assertEqual(False, programa.validarAprovacao(idade, formacao), "Teste de idade inaceitavel falhou")


def main():
    #Criação da suite de testes
    suite = unittest.TestLoader().loadTestsFromTestCase(testes)

    #Execução da suite de testes
    unittest.TextTestRunner(verbosity=2).run(suite)

main()