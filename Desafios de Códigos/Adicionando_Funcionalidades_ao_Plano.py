# TODO: Crie a classe PlanoTelefone, seu método de inicialização e encapsule os atributos, 'nome' e 'saldo':
class PlanoTelefone:
    def __init__(self, nome, saldo):
        self.nome = nome
        self._saldo = saldo

# TODO: Crie um método 'verificar_saldo' para verificar o saldo do plano sem acessar diretamente o atributo:
    def verificar_saldo(self):
        if self._saldo <= 10:
            mensagem_personalizada = "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
            return mensagem_personalizada
        elif self._saldo >= 50:
            mensagem_personalizada = "Parabéns! Continue aproveitando seu plano sem preocupações."
            return mensagem_personalizada
        else:
            mensagem_personalizada = "Seu saldo está razoável. Aproveite o uso moderado do seu plano."
            return mensagem_personalizada

      

# Classe UsuarioTelefone:


class UsuarioTelefone:
    def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano

# TODO: Crie um método para verificar o saldo do usuário e gerar uma mensagem personalizada:
    def verificar_saldo_e_gerar_mensagem(self):
        return self.plano.verificar_saldo()


# Recebendo as entradas do usuário (nome, plano, saldo):
nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

# Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial)
usuario = UsuarioTelefone(nome_usuario, plano_usuario)

# Chamada do método para verificar_saldo sem acessar diretamente os atributos do plano:
mensagem_usuario = usuario.verificar_saldo_e_gerar_mensagem()
print(mensagem_usuario)
