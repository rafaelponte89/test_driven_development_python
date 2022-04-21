from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    # método disparado antes do teste iniciar, configurações do teste
    def setUp(self):
        self.browser = webdriver.Firefox()

    # método disparado após o teste terminar
    def tearDown(self):
        self.browser.quit()


    # método de teste
    def test_start_a_list_and_retrieve_it_later(self):
        # Edith tem ouvido sobre um app de tarefas online legal. Ela vai conferir sua página inicial
        self.browser.get('http://localhost:8000')

        # Ela observa que o título da página e o cabeçalho mencionam listas de tarefas
        self.assertIn('To-Do', self.browser.title) # compara se 'To-Do' encontra-se no título da janela
        self.fail('Finish the test!') # quando o teste termina

        # Ela é convidada a inserir uma tarefa imediatamente

        # Ela digita "Comprar penas de pavão" em uma caixa de texto
        # Hobby de Edith é amarrar iscas de pescas com mosca

        # Quando ela aperta enter, a página atualiza, e agora a página lista
        # "1:Compre penas de pavão" como um item em uma lista de tarefas

        # Ainda há uma caixa de texto convidando-a a adicionar outro item.
        # Ela digita "Use penas de pavão para fazer uma mosca" (Edith é muito metódica)

        # A página é atualizada novamente e agora mostra os dois itens da lista dela

        # Edith se pergunta se o site vai lembrar dela.
        # Então ela vê que o site gerou um URL exclusivo para ela -
        # há alguns textos explicativos nesse sentido.

        # Ela visita esse URL - sua lista de tarefas está lá.

        # Satisfeita, ela volta a dormir.

if __name__ == '__main__':
    unittest.main(warnings='ignore') # faz chamada ao teste (test runner), encontrando classes e métodos de teste





