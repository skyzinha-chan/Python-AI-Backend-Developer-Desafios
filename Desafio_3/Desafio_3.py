# Modelando o Sistema Bancário em POO com Python - PARTE 3
# Adicionando Decoradores, Iteradores e Geradores propostos seguindo a resolução do professor.
# Não foram implementadas formas de conferir o cpf, data nascimento, escolha de conta e opções de contas e taxas
import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
from pathlib import Path

import pytz

ROOT_PATH = Path(__file__).parent


class ContasIterador:
    def __init__(self, contas):
        self.contas = contas
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self.contas[self._index]
            return f"""\
            Agência:\t{conta.agencia}
            Número:\t\t{conta.numero}
            Titular:\t{conta.cliente.nome}
            Saldo:\t\tR$ {conta.saldo:.2f}
        """
        except IndexError:
            raise StopIteration
        finally:
            self._index += 1


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        self.indice_conta = 0

    def realizar_transacao(self, conta, transacao):
        if len(conta.historico.transacoes_do_dia()) >= 10:
            print("\n Você excedeu o número de transações permitidas para hoje!!")
            return

        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: \nCliente: ('{self.nome}', \nCPF: '{self.cpf}')>"


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n Operação falhou! Você não tem saldo suficiente. ")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n Operação falhou! O valor informado é inválido. ")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n Operação falhou! O valor informado é inválido. ")
            return False

        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    @classmethod
    def nova_conta(cls, cliente, numero, limite, limite_saques):
        return cls(numero, cliente, limite, limite_saques)

    def sacar(self, valor):
        numero_saques = len(
            [
                transacao
                for transacao in self.historico.transacoes
                if transacao["tipo"] == Saque.__name__
            ]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n Operação falhou! O valor do saque excede o limite. ")

        elif excedeu_saques:
            print("\n Operação falhou! Número máximo de saques excedido. ")

        else:
            return super().sacar(valor)

        return False

    def __repr__(self):
        return f"<{self.__class__.__name__}: ('{self.agencia}', \n\t'{self.numero}', \n\t'{self.cliente.nome}')>"

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now(pytz.timezone("America/Manaus")).strftime(
                    "%d/%m/%Y %H:%M:%S"
                ),
            }
        )

    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self._transacoes:
            if (
                tipo_transacao is None
                or transacao["tipo"].lower() == tipo_transacao.lower()
            ):
                yield transacao

    def transacoes_do_dia(self):
        data_hoje = datetime.now(pytz.timezone("America/Manaus")).strftime(
            "%d/%m/%Y %H:%M:%S"
        )
        transacoes = []
        for transacao in self._transacoes:
            data_transacao = datetime.strptime(
                transacao["data"], "%d/%m/%Y %H:%M:%S")
            if data_hoje == data_transacao:
                transacoes.append(transacao)
        return transacoes


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


def log_transacao(func):
    def decorador(*args, **kwargs):
        resultado = func(*args, **kwargs)
        data_movimentada = datetime.now(pytz.timezone("America/Manaus")).strftime(
            "%d/%m/%Y %H:%M:%S"
        )
        try:
            with open(
                ROOT_PATH / "imprimir_movimentacoes.txt", "a", encoding="utf-8"
            ) as arquivo:
                arquivo.write(
                    f" \tFunção '{
                        func.__name__}' executada, com argumentos \n\t\t{args} e \n\t\t{kwargs}. [{data_movimentada}]\n"
                    f"Retornou {resultado}\n\n"
                )
        except IOError as exc:
            print(f"Erro ao abrir o arquivo {exc}")
        except UnicodeDecodeError as exc:
            print(exc)
        return resultado

    return decorador


# Menu do Sistema Bancário


def menu():
    menu = """\n
    ================ MENU ================
    SELECIONE A OPÇÃO DESEJADA:

        [1] - Depositar;
        [2] - Sacar;
        [3] - Extrato;
        [4] - Criar Novo Usuário;
        [5] - Criar Nova Conta;
        [6] - Contas Existentes;
        [0] - Sair.

=> """
    return input(textwrap.dedent(menu))


def confere_usuario_existe(cpf, usuario):
    usuarios_filtrados = [usuario for usuario in usuario if usuario.cpf == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n Cliente não possui conta! ")
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]


@log_transacao
def depositar(usuario):
    cpf = input("Informe o CPF do cliente: ")
    cliente = confere_usuario_existe(cpf, usuario)

    if not cliente:
        print("\n Cliente não encontrado! ")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


@log_transacao
def sacar(usuario):
    cpf = input("Informe o CPF do usuário: ")
    cliente = confere_usuario_existe(cpf, usuario)
    if not cliente:
        print("\n Cliente não encontrado! ")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


@log_transacao
def mostrar_extrato(usuario):
    cpf = input("Informe o CPF do cliente: ")
    cliente = confere_usuario_existe(cpf, usuario)

    if not cliente:
        print("\n Cliente não encontrado! ")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")

    extrato = ""
    transacao_realizada = False
    for transacao in conta.historico.gerar_relatorio():
        transacao_realizada = True
        extrato += f"\n{transacao['data']}\n{transacao['tipo']
                                             }:\n\tR$ {transacao['valor']:.2f}\n"

    if not transacao_realizada:
        extrato = "Não foram realizadas movimentações."

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}\n")
    print("==========================================")


@log_transacao
def novo_usuario(usuario):
    cpf = input("Informe o CPF (somente números): ")
    cliente = confere_usuario_existe(cpf, usuario)

    if cliente:
        print("\n Já existe cliente com esse CPF!! ")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): "
    )

    cliente = PessoaFisica(
        nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco
    )

    usuario.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")


def contas_existentes(contas):
    if not contas:
        print("\n Não há contas cadastradas.")
    else:
        for conta in ContasIterador(contas):
            print("=" * 100)
            print(textwrap.dedent(str(conta)))


@log_transacao
def criar_nova_conta(numero_conta, usuario, contas):
    cpf = input("Informe o CPF do usuário: ")
    cliente = confere_usuario_existe(cpf, usuario)

    if not cliente:
        print("\n Cliente não encontrado, fluxo de criação de conta encerrado! ")
        return

    conta = ContaCorrente.nova_conta(
        cliente=cliente, numero=numero_conta, limite=500, limite_saques=3
    )
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")


def main():
    usuario = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            depositar(usuario)

        elif opcao == "2":
            sacar(usuario)

        elif opcao == "3":
            mostrar_extrato(usuario)

        elif opcao == "4":
            novo_usuario(usuario)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            criar_nova_conta(numero_conta, usuario, contas)

        elif opcao == "6":
            contas_existentes(contas)

        elif opcao == "0":
            print("\n Obrigado por usar nosso sistema bancário, até logo!\n")
            break

        else:
            print(
                "\n Operação inválida, por favor selecione novamente a operação desejada."
            )


main()
