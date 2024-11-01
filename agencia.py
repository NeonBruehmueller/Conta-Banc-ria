class Agencia:
    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print("Caixa abaixo do nível recomendado. Caixa Atual: {}".format(self.caixa))
        else:
            print("O valor de Caixa está ok. Caixa Atual: {}".format(self.caixa))


    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
            print("Emprestimos efetuado")
        else:
            print("Empréstimos não é possivel. DInheiro não disponível em caixa")

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))

class AgenciaVirtual(Agencia):

    def __init__(self, site, telefone, cnpj, numero):
        self.site = site
        super().__init__(telefone, cnpj, numero)

class AgenciaComum(Agencia):
    def __init__(self, telefone, cnpj, randint):
        super().__init__(telefone, cnpj, randint(1001, 9999))
        self.caixa = 1000000
    
class AgenciaPremium(Agencia):
    def __init__(self, telefone, cnpj, randint):
        super().__init__(telefone, cnpj, randint(1001, 9999))
        self.caixa = 10000000

agencia1 = Agencia(22223333, 200000000, 4568)

agencia1.caixa = 1000000

print(agencia1.__dict__)

agencia1.verificar_caixa()

agencia1.emprestar_dinheiro(10, 11122233344, 0.1)

agencia1.adicionar_cliente('Lira', 11122233344, 1000)
print(agencia1.clientes)

agencia_virtual = AgenciaVirtual('www.agenciavirtual.com.br',22224444, 1520000000, 1000)
agencia_virtual.verificar_caixa()
print("\n", agencia_virtual.__dict__)

agencia_comum = AgenciaComum(33334444, 222000000)
agencia_comum.verificar_caixa()
print(agencia_comum.__dict__)

agencia_premium = AgenciaPremium(33333333, 3000000000000)
print('agencia_premium:')
print(agencia_premium.__dict__)