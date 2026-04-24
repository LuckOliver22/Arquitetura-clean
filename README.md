# Arquitetura-clean
Exercicio 7.4 - Engenharia de software

# 📚 Livraria - Clean Architecture

Este repositório contém a implementação de um sistema de gestão de livraria desenvolvido para o **Laboratório 7 da disciplina de Engenharia de Software**. O objetivo principal é demonstrar a aplicação prática dos princípios da **Arquitetura Limpa (Clean Architecture)** e do **DIP (Dependency Inversion Principle)**.

## 🎯 Objetivos do Projeto

- Implementar a lógica de negócio de forma isolada de tecnologias externas.
- Utilizar arquivos **.txt** para persistência de dados.
- Aplicar a Inversão de Dependência para que o núcleo do sistema não dependa da implementação específica do banco de dados/arquivo.

---

## 🏗️ Arquitetura

O projeto está dividido seguindo as camadas propostas por Robert C. Martin:

1.  **Entities (Entidades):** Regras de negócio globais (ex: Classe `Livro`).
2.  **Use Cases (Casos de Uso):** Regras de negócio específicas da aplicação (ex: `AdicionarLivro`, `ListarLivros`).
3.  **Interface Adapters (Adaptadores):** Convertem dados entre o formato das entidades e o formato exigido externamente.
4.  **Frameworks & Drivers (Infraestrutura):** Ferramentas externas como o sistema de arquivos (TXT).

### 🛠️ Inversão de Dependência (DIP)

Para cumprir os requisitos académicos, o núcleo da aplicação interage com uma **Interface (Abstração)** e não com a implementação direta do arquivo TXT. Isso permite que, no futuro, o sistema de arquivos seja substituído por um banco de dados SQL ou NoSQL sem alterar uma única linha de código da lógica de negócio.

---

## 📁 Estrutura de Pastas

```text
src/
├── entities/          # Objetos de domínio e regras básicas
├── use_cases/         # Lógica da aplicação e interfaces (ports)
├── adapters/          # Controllers e apresentadores
└── infrastructure/    # Implementação do repositório (Persistência TXT)
main.py                # Ponto de entrada e Injeção de Dependência
livros.txt             # Arquivo de persistência
