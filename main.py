from src.infrastructure.repositorio_txt import RepositorioLivroTxt
from src.use_cases.gerenciar_livros import AdicionarLivro
from src.entities.livro import Livro

# Injeção de Dependência
repositorio = RepositorioLivroTxt()
caso_de_uso = AdicionarLivro(repositorio)

novo_livro = Livro(1, "Engenharia de Software", "Rodrigo Juliani", 99.90)
caso_de_uso.executar(novo_livro)