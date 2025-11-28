# OMNISTACK - Gestão Automatizada de Laboratórios Virtuais

Este repositório contém a entrega do MVP (N2) da disciplina de **Ferramentas de Desenvolvimento para Web**, do curso de Segurança da Informação da Fatec São Caetano do Sul.

O projeto consiste na containerização da plataforma **AWX** para orquestração de infraestrutura.

## 👥 Integrantes
* Arthur Versiani Silva
* Enzo Stachovski Ribeiro
* Guilherme Nascimento Faria
* Pedro Henrique Coelho Machado

## 📄 Documentação
Os artefatos documentais exigidos encontram-se na raiz deste repositório:
* [Proposta Técnica (PDF)](./Proposta_Tecnica.pdf)
* [Relatório Técnico (PDF)](./Relatorio_Tecnico.pdf)
* [Plano de Testes (PDF)](./Plano_de_Testes.pdf)

## 🚀 Como Rodar o Projeto

### Pré-requisitos
* Docker
* Docker Compose

### Passo a Passo
1. Clone este repositório:
   ```bash
   git clone [https://github.com/stxch/fatec-scs-fdw-2025-2-omnistack.git](https://github.com/stxch/fatec-scs-fdw-2025-2-omnistack.git)
   cd fatec-scs-fdw-2025-2-omnistack
2. Suba o ambiente com o Docker Compose:
    ```bash
    sudo docker-compose up -d
3. Aguarde a inicialização (pode levar alguns minutos para as migrações do banco de dados).

    Acesse no navegador:

        URL: http://localhost:8080

        Usuário: admin

        Senha: admin
🛠 Tecnologias Utilizadas

    AWX (Ansible Tower Open Source) - Versão 17.1.0

    Docker & Docker Compose

    PostgreSQL 12

    Redis 6
