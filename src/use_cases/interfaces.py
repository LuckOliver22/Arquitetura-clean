from abc import ABC, abstractmethod

class IRepositorioLivro(ABC):
    @abstractmethod
    def salvar(self, livro):
        pass

    @abstractmethod
    def listar_todos(self):
        pass