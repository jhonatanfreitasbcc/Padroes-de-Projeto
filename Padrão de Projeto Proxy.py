class Servico:
    def operacao(self):
        print("Executando operação no serviço real...")

class ProxyServico:
    def __init__(self):
        self.servico = Servico()

    def operacao(self):
        print("Proxy: verificando permissões antes da operação.")
        self.servico.operacao()

proxy = ProxyServico()
proxy.operacao()
