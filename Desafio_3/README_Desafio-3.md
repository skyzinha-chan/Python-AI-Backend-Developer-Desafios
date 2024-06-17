# <div align="center">Python AI Backend Developer </div>

Desafio desenvolvido como parte de um projeto educacional da [DIO](https://www.dio.me/sign-up?ref=13JYL0Y2AV) (Digital Innovation One) no bootcamp: **_Python AI Backend Developer_**. Seguindo as orientações e passo a passo dos conceitos com o professor Guilherme Carvalho.


## <div align="center"> Objetivo Geral</div>


Criar um sistema bancário com as operações: _sacar, depositar
e visualizar extrato_. 
<br>O objetivo é aprimorar a estrutura e a eficiência do sistema realizado no [Desafio 1](https://github.com/skyzinha-chan/Python-AI-Backend-Developer-Desafios/blob/main/Desafio_1/Desafio_1.py), implementando as operações de depósito, saque e extrato em funções específicas. Bem como criar novas funções:
- Cadastrar usuário(cliente);
- Cadastrar Conta Bancária;
- Listar Contas Existentes Criadas.

## <div align="center"> Desafio</div>


Fomos contratados por um grande banco para desenvolver o
seu novo sistema. Esse banco deseja modernizar suas
operações e para isso escolheu a linguagem Python. 
<br>Para essa segunda versão do sistema devemos implementar ao todo 5
operações.
- [x] Depósito;
- [x] Saque;
- [x] Extrato;
- [x] Novo Usuário;
- [x] Nova Conta.

## <div align="center"> Operação de DEPÓSITO</div>
<br>

- [x] Deve ser possível depositar valores **_positivos_** para a minha
conta bancária. 

<br>Todos os depósitos
devem ser armazenados em uma variável e exibidos na
operação de extrato.

## <div align="center"> Operação de SAQUE</div>
<br>

- [x] O sistema deve permitir realizar **_3 saques diários com limite
máximo de R$ 500,00 por saque_**. 

<br>Caso o usuário não tenha
saldo em conta, ou o valor informado seja inválido ou superior ao permitido, o sistema deve exibir uma mensagem
informando que não será possível sacar o dinheiro mostrando seu respectivo erro. Todos os saques devem ser armazenados em uma
variável e exibidos na operação de extrato.

## <div align="center"> Operação de EXTRATO</div>
<br>

- [x] Essa operação deve **_listar todos os depósitos e saques
realizados na conta_**. No fim da listagem deve ser exibido o
saldo atual da conta. Se o extrato estiver em branco, exibir a
mensagem: Não foram realizadas movimentações.

<br>Os valores devem ser exibidos utilizando o formato R$ XXXX.XX,
exemplo:
1500.45  R$ 1500.45


## <div align="center"> Operação de NOVO USUÁRIO</div>
<br>

Deve-se armazenar os usuários em uma lista, composto por: 
- [x]  **_Nome;_**
- [x]  **_Data Nascimento;_**
- [x]  **_CPF(somente números);_**
- [x]  **_Endereço: (Logradouro, Nrº - Bairro - Cidade/Sigla Estado)._**

<br>Na V2 do projeto tem-se a opção de criar usuário, porém ainda não é necessário identificar qual
é o número da agência e conta bancária que esta sendo movimentada.

<br>Importante lembrar que, nesta versão não pode existir dois usuários com o mesmo <b>CPF</b>, porém o usuário pode ter mais de uma conta cadastrada, para realizar essa verificação, dentro do código tem a chamada da função em que se compara se o usuário (CPF) já foi cadastrado.

## <div align="center"> Operação de CADASTRAR CONTA</div>
<br>

Deve-se armazenar as contas em uma lista, composta por: 

- [x] **_Agência;_**
- [x] **_Número de conta;_** 
- [x] **_Usuário_**

<br>O número da conta é sequencial, iniciando em 1. E a Agência é fixa: "0001", o usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

<br>Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informando para cada usuário da lista.

***
# <div align="center"> **_Talita Mendonça Marquês_** </div>


















