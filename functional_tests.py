import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Ela é convidada a inserir uma tarefa imediatamente
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # Ela digita "Comprar penas de pavão" em uma caixa de texto
        # Hobby de Edith é amarrar iscas de pescas com mosca
        inputbox.send_keys('Buy peacock feathers')

        # Quando ela aperta enter, a página atualiza, e agora a página lista
        # "1:Compre penas de pavão" como um item em uma lista de tarefas
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # Ainda há uma caixa de texto convidando-a a adicionar outro item.
        # Ela digita "Use penas de pavão para fazer uma mosca" (Edith é muito metódica)

        # A página é atualizada novamente e agora mostra os dois itens da lista dela

        # Edith se pergunta se o site vai lembrar dela.
        # Então ela vê que o site gerou um URL exclusivo para ela -
        # há alguns textos explicativos nesse sentido.

        # Ela visita esse URL - sua lista de tarefas está lá.

        # Satisfeita, ela volta a dormir.

        self.fail('Finish the test!') # quando o teste termina


if __name__ == '__main__':
    unittest.main(warnings='ignore') # faz chamada ao teste (test runner), encontrando classes e métodos de teste





