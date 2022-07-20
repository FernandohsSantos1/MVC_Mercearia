#Arquivo para armazenamento, alteração ou remoção de dados dos arquivos persistentes

#importar arquivos da models
from models import *

class DaoCategoria:
    
    @classmethod
    def salvar(cls, categoria):
        with open('Categoria.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('Categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()
        
        #Para tirar o \n basta relaizar uma funcao replace, através de cade item da lista, alterando para uma string vazia
        cls.categoria = list(map(lambda x: x.replace('\n',''), cls.categoria))
        
        listaCat = []
        for i in cls.categoria:
            listaCat.append(Categoria(i))
        
        #Retorna uma lista de instancias de objetos
        return listaCat

class DaoVendas:
    
    @classmethod
    def salvar(cls, venda: Venda):
        with open('Vendas.txt', 'a') as arq:
            arq.writelines(venda.itensVendido.nome+'|'+str(venda.itensVendido.valor)+'|'
                          +venda.itensVendido.categoria+'|'+venda.vendedor+'|'
                          +venda.comprador+'|'+str(venda.quantidadeVendida)+'|'
                          +venda.data)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('Vendas.txt', 'r') as arq:
            cls.venda = arq.readlines()

        cls.venda = list(map(lambda x: x.replace('\n',''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))

        listaVend = []
        for i in cls.venda:
            listaVend.append(Venda(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))
        
        #Retorna uma lista de instancias de objetos
        return listaVend

class DaoEstoque:

    @classmethod
    def salvar(cls, produto: Produtos, quantidade):
        with open('Estoque.txt', 'a') as arq:
            arq.writelines(produto.nome+'|'+str(produto.valor)+'|'
                          +produto.categoria+'|'+str(quantidade))
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('Estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()
        
        cls.estoque = list(map(lambda x: x.replace('\n',''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))
        
        listaEst = []
        for i in cls.estoque:
            listaEst.append(Estoque(Produtos(i[0], i[1], i[2]), int(i[3])))
        
        #Retorna uma lista de instancias de objetos
        return listaEst

class DaoFornecedor:

    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('Fornecedor.txt', 'a') as arq:
            arq.writelines(fornecedor.nome+'|'+fornecedor.cnpj+'|'
                          +fornecedor.telefone+'|'+fornecedor.categoria+'|')
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('Fornecedor.txt', 'r') as arq:
            cls.fornecedor = arq.readlines()

        cls.fornecedor = list(map(lambda x: x.replace('\n',''), cls.fornecedor))
        cls.fornecedor = list(map(lambda x: x.split('|'), cls.fornecedor))
    
        listaFor = []
        for i in cls.fornecedor:
            listaFor.append(Fornecedor(i[0], i[1], i[2], i[3]))

        return listaFor

class DaoCliente:

    @classmethod
    def salvar(cls, cliente: Cliente):
        with open('Cliente.txt', 'a') as arq:
            arq.writelines(cliente.nome+'|'+cliente.telefone+'|'
                          +cliente.cpf+'|'+cliente.email+'|'
                          +cliente.endereco)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('Cliente.txt', 'r') as arq:
            cls.cliente = arq.readlines()

        cls.cliente = list(map(lambda x: x.replace('\n',''), cls.cliente))
        cls.cliente = list(map(lambda x: x.split('|'), cls.cliente))

        listaCli = []
        for i in cls.cliente:
            listaCli.append(Cliente(i[0], i[1], i[2], i[3], i[4]))

        return listaCli

class DaoFuncionario:

    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('Funcionario.txt', 'a') as arq:
            arq.writelines(funcionario.clt+'|'+funcionario.nome+'|'
                          +funcionario.telefone+'|'+funcionario.cpf+'|'
                          +funcionario.email+'|'+funcionario.endereco)
            arq.writelines('\n')
        
    @classmethod
    def ler(cls):
        with open('Funcionario.txt', 'r') as arq:
            cls.funcionario = arq.readlines()

        cls.funcionario = list(map(lambda x: x.replace('\n', ''), cls.funcionario))
        cls.funcionario = list(map(lambda x: x.split('|'), cls.funcionario))

        listaFunc = []
        for i in cls.funcionario:
            listaFunc.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5]))

        return listaFunc
