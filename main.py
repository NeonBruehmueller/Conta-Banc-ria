from ContaBancaria import ContaCorrente, CartaoCredito

#Programa
conta_lira = ContaCorrente("Lira", "111.222.333-45", "1182", "12365")
conta_lira.consultar_saldo()
conta_maeLira = ContaCorrente("Mãe Lira", "984.257.278-24", "8538", "987456")

#Depositar um dinheiro na conta:
conta_lira.depositar_dinheiro(10000)
conta_lira.consultar_saldo()

#Sacando um dinheiro da conta:_
conta_lira.sacar_dinheiro(1500)
conta_lira.consultar_saldo()

#Tranferindo dinheiro:
conta_lira.transferir(1000, conta_maeLira)

conta_lira.consultar_historico__transacoes()

#Cartão de Crédito

#Criando uma nova instancia da classe ContaCorrente (conta_lira)
conta_lira = ContaCorrente("Lira", "111.222.333-45", "1182", "12365")

#Cria uma nova instancia da classe CartaoCredito (cartao_lira)
cartao_lira= CartaoCredito("Lira", conta_lira)

print("\n",cartao_lira.__dict__)
#Cria um número aleatório de cartão apenas para o exemplo
cartao_lira.numero=123

#Retorna o número da conta associada ao cartao_lira
print("\nCartão de\n", cartao_lira.conta_corrente._num_conta)
#Retorna a lista de cartões associados a conta corrente (conta_lira)
print(conta_lira._cartoes)

#Acessando o primeiro item da lista
print(conta_lira._cartoes[0].numero)