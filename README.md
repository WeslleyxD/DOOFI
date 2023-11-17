# Índice
- [Descrição](#descrição)
- [Tecnologias](#tecnologias)
- [Instalação](#instalação)
  - [Requisitos](#requisitos)
  - [Iniciando](#iniciando)
- [Contato](#contato)


# Descrição
`DOOFI`, projeto construindo no final da faculdade com o intuito de ser o back-end de um aplicativo de delivery. Na qual consta com sistema de autenticação, registro empresas parceiras e usuários, listagem dos produtos disponíveis nos diversos estabelecimentos, controle de estoque, entre outros. <br>
<img src="https://github.com/WeslleyxD/Django-Agenda/assets/93230531/065402c5-fc73-40d6-a048-edd6c6a31cfb" width="50%">


# Tecnologias
  <div style="display: inline-block">
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
    <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JS">
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green">
    <img src="https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white" alt="DjangoRest">
  </div>


# Instalação
  ### Requisitos
  > [!WARNING]\
  > Precisa ter Python3.9 ou superior instalado.
  
  ### Iniciando
  
  1. Clone o repositório
     ```sh
     git clone https://github.com/WeslleyxD/DOOFI.git
     ```
  2. Acesse o diretório
     ```sh
     cd DOOFI
     ```
  3. Instale o ambiente virtual
     ```sh
     python3 -m venv venv
     ```
  4. Acesse o ambiente virtual
     ```sh
     . venv/bin/activate
     ```
  5. Instale todas as biblioticas do projeto
     ```sh
     pip3 -r requirements.txt
     ```
  6. Migrações das tabelas
     ```sh
     python3 manage.py makemigrations
     ```
     ```sh
     python3 manage.py migrate
     ```
  7. Crie um superusuário para poder se autenticar
     ```sh
     python3 manage.py createsuperuser
     ```
  8. Inicialize o servidor e faça o login com usuário criado na etapa 7
     ```sh
     python3 manage.py runserver
     ```
  9. Pronto, agora você pode explorar o projeto por completo!!!


# Contato
  <div style="display: inline-block">
    <a href="www.linkedin.com/in/weslley-pablo" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Python"></a>
  </div>
