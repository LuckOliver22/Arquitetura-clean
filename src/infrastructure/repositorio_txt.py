from src.use_cases.interfaces import IRepositorioLivro
from src.entities.livro import Livro

class RepositorioLivroTxt(IRepositorioLivro):
    def __init__(self, arquivo="livros.txt"):
        self.arquivo = arquivo

    def salvar(self, livro):
        with open(self.arquivo, "a") as f:
            f.write(f"{livro.id};{livro.titulo};{livro.autor};{livro.preco}\n")

    def listar_todos(self):
        # Lógica para ler o TXT e converter em lista de objetos Livro
        pass