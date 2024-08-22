# 🔖 ALUNOS

- [Andrei Rech | 23102140](https://github.com/AndreiRech) 
- [Urien Nolasco | 23102720](https://github.com/UrienNolasco)

# 📚 INTRODUÇÃO

Criação de algoritmos WebCrawleres.

# 🛠 PRÉ REQUISITOS

É necessário possuir a linguagem [Python](https://www.python.org/downloads/) instalada no computador (de preferência 3.12.x - mas pode funcionar em superiores).

Outra ferramente muito importante é o gerenciador de pacotes do Python, o [Pip](https://pypi.org/project/pip/).

Para a conseguir abrir a aplicação que será retirado os dados no primeiro programa, é necessária a criação de um ambiente virtual no [Anaconda](https://www.anaconda.com/download) com o a versão **2.7** do Python.

Por fim, a utilização do [JupyterLab](https://jupyter.org/) ou do [Google Colab](https://colab.google/) é necessária para a utilização do programa (Caso deseje, é possível utilizar o [VSCode](https://code.visualstudio.com/)).


# ⚙ INICIALIZAÇÃO

Para a realização do projeto, utilizamos alguns pacotes adicionais. Segue a baixo a lista de pacotes a serem instalados e seus comandos:

- *BeautifulSoup*
```
pip install beautifulsoup4
```

Por fim, caso esteja utilizando o **JupyterLab**, abra o mesmo pelo terminal utilizando:
```
jupyter lab
```

# O QUE FAZER

### ATIVIDADE 1
- [X] Faça um crawler capaz de navegar por todas as páginas de países e acessar seus HTML
- [X] Faça scraping dos HTMLs das páginas para armazenar os seguintes dados dos países em um arquivo CSV:
    - [X] Nome do país
    - [X] Nome da moeda
    - [X] Nome do continente
    - [X] Nome de todos os países vizinhos (Nome != Sigla)
    - [X] Salvar uma coluna extra no csv contendo um timestamp do momento no qual os dados foram obtidos
- [ ] Faça um crawler que monitore as páginas de países e procure por atualizações. Caso algum registro tenha sido atualizado desde sua obtenção, esse registro deve ser atualizado no arquivo CSV, caso contrário manter a versão anterior.

### ATIVIDADE 2
- [ ] Faça scraping para obter os filmes presentes no Calendário de Lançamentos do IMDB
    - [ ] Título do filme
    - [ ] Data de lançamento
    - [ ] Gênero(s)
    - [ ] Link para página da série
- [ ] Faça scraping das páginas específicas dos filmes obtidos no item anterior
    - [ ] Nomes dos diretores
    - [ ] Lista de atores principais
- [ ] Salve as informações em um arquivo de tipo JSON.
