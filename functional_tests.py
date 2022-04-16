from selenium import webdriver




browser = webdriver.Firefox()

# Edith tem ouvido sobre um app de tarefas online legal. Ela vai conferir sua página inicial
browser.get('http://localhost:8001')

# Ela observa que o título da página e o cabeçalho mencionam listas de tarefas
assert 'To-Do' in browser.title

# Ela é convidada a inserir uma tarefa imediatamente

# Ela digita "Comprar penas de pavão" em uma caixa de texto
# Hobby de Edith está amarrando iscas de pesca com mosca

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
browser.quit()




