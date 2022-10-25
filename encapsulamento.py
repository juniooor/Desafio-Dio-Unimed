class Conta:
    def __init__(self, nr_agencia, saldo):
        self._saldo = saldo
        self.nr_agencia = nr_agencia
        
    def depositar(self,valor):
        self._saldo += valor
    
    def sacar(self, valor):
        self._saldo -= valor
    
    def saldo(self):
        return self._saldo
    

if __name__ == '__main__':
    
    conta = Conta('0001',100)
    conta.depositar(100)
    print(conta.saldo())
    

    