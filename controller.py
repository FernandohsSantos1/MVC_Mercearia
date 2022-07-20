#Arquivo do back-end, fazer validações etc

#Importações das classes da mdoels e da DAO
from DAO import *
from models import *
from datetime import datetime

class ControllerCategoria:

    def cadastrarCategoria(self, novaCategoria):
        
        existe = False
        x = DaoCategoria.ler()
        
        for i in x:
            if i.categoria == novaCategoria:
                existe = True

        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print('Categoria cadastrada com sucesso!')
        else:
            print('A categoria já existe.')

    def removerCategoria(self, removeCategoria):
        
        x = DaoCategoria.ler()

        cat = list(filter(lambda x: x.categoria == removeCategoria, x))

        if len(cat) == 0:
            print('A categoria não existe!')
       
        else:
            for i in range(len(x)):
                if x[i].categoria == removeCategoria:
                    del x[i]
                    break
            print('Categoria removida com sucesso!')
        
            with open('Categoria.txt','w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')

        estoque = DaoEstoque.ler()

        estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.valor, "Sem categoria"), x.quantidade)
                           if (x.produto.categoria == removeCategoria) else (x), estoque))

        with open('Estoque.txt', 'w') as arq:
            for i in estoque:
                arq.writelines(i.produto.nome+'|'+str(i.produto.valor)+'|'
                              +i.produto.categoria+'|'+str(i.quantidade))
                arq.writelines('\n')

    def alterarCategoria(self, alteraCategoria, CategoriaAlterada):
        
        x = DaoCategoria.ler()

        cat = list(filter(lambda x: x.categoria == alteraCategoria, x))
        
        if len(cat) == 0:
            print('A categoria não existe!')
       
        else:
            catAlterada = list(filter(lambda x: x.categoria == CategoriaAlterada, x))
            
            if len(catAlterada) == 0:
                x = list(map(lambda x: Categoria(CategoriaAlterada) if (x.categoria == alteraCategoria) else(x), x))

                print('Categoria alterada com sucesso!')
            
                with open('Categoria.txt','w') as arq:
                    for i in x:
                        arq.writelines(i.categoria)
                        arq.writelines('\n')

                estoque = DaoEstoque.ler()

                estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.valor, CategoriaAlterada), x.quantidade)
                           if (x.produto.categoria == alteraCategoria) else (x), estoque))

                with open('Estoque.txt', 'w') as arq:
                    for i in estoque:
                        arq.writelines(i.produto.nome+'|'+str(i.produto.valor)+'|'
                                      +i.produto.categoria+'|'+str(i.quantidade))
                        arq.writelines('\n')
            
            else:
                print('Categoria já existe')

    def exibirCategoria(self):
        
        x = DaoCategoria.ler()
        for i in range(1,len(x)+1):
            print(f'Categoria {i}: {x[i-1].categoria}')

class ControllerEstoque:
    
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x : x.categoria == categoria, y))
        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(h) > 0:
            
            if len(est) == 0:
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print('Produto cadastrado com sucesso')

            else:
                print('Produto já cadastrado no estoque')
        
        else:
            print('Categoria inexistente')
    
    def removerProduto(self, removeProduto):
        x = DaoEstoque.ler()
        est = list(filter(lambda x: x.produto.nome == removeProduto, x))

        if len(est) == 0:
            print('Produto inexistente')

        else:
            for i in range(len(x)):
                if x[i].produto.nome == removeProduto:
                    del x[i]
                    break
            print('Produto removido com sucesso')
        
        with open('Estoque.txt','w') as arq:
                for i in x:
                    arq.writelines(i.produto.nome+'|'+str(i.produto.valor)+'|'
                                  +i.produto.categoria+'|'+str(i.quantidade))
                    arq.writelines('\n')
    
    def alterarProduto(self, alteraNome, nome, valor, categoria, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == categoria, y))

        if len(h) > 0:
            est = list(filter(lambda x: x.produto.nome == alteraNome, x))
            
            if len(est) > 0:
                est = list(filter(lambda x: x.produto.nome == nome, x))
                
                if len(est) == 0:
                    x = list(map(lambda x: Estoque(Produtos(nome, valor, categoria), quantidade) if(x.produto.nome == alteraNome) else(x), x))
                    print('Produto alterado com sucesso')

                else:
                    print('Já existe um produto com este nome')

            else:
                print('Nome do produto inexistente')
            
            with open('Estoque.txt','w') as arq:
                for i in x:
                    arq.writelines(i.produto.nome+'|'+str(i.produto.valor)+'|'
                                  +i.produto.categoria+'|'+str(i.quantidade))
                    arq.writelines('\n')  
        
        else:
            print('A categoria informada não existe')

    def exibirEstoque(self):
        est = DaoEstoque.ler()

        if len(est) == 0:
            print('Estoque vazio')

        else:
            print(f'{"="*10} ESTOQUE {"="*10}\n')
            for i in range(len(est)):
                print(f'{"-"*10} Produto {i+1} {"-"*10}')
                print(f'Nome: {" ":<16} {est[i].produto.nome}')
                print(f'Valor: {" ":<15} {est[i].produto.valor}')
                print(f'Categoria: {" ":<11} {est[i].produto.categoria}')
                print(f'Quantidade: {" ":<10} {est[i].quantidade}')

class ControllerVenda:

    def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
        
        x = DaoEstoque.ler()
        temp = []
        existe = False
        quantidade = False

        for i in x:
            if existe == False:
                if i.produto.nome == nomeProduto:
                    existe = True
                    if i.quantidade >= int(quantidadeVendida):
                        quantidade = True
                        i.quantidade = int(i.quantidade) - int(quantidadeVendida)

                        vendido = Venda(Produtos(i.produto.nome, i.produto.valor, i.produto.categoria), vendedor, comprador, quantidadeVendida)

                        valorCompra = quantidadeVendida * int(i.produto.valor)
                    
                        DaoVendas.salvar(vendido)


            temp.append([Produtos(i.produto.nome, i.produto.valor, i.produto.categoria), i.quantidade])

        arq = open('Estoque.txt', 'w')
        arq.writelines("")

        for i in temp:
                with open('Estoque.txt', 'a') as arq:
                    arq.writelines(i[0].nome + "|" + i[0].valor + "|" + i[0].categoria + "|" + str(i[1]))
                    arq.writelines('\n')
            
        if existe == False:
            print('O produto nao existe')
            return 1
        
        elif not quantidade:
            print('A quantidade vendida nao contem em estoque')
            return 2

        else:
            print('Venda efetuada com sucesso')
            return valorCompra

    def relatorioProdutos(self):
        vendas = DaoVendas.ler()
        produtos = []

        for i in vendas:
            nome = i.itensVendido.nome
            quantidade = int(i.quantidadeVendida)
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))
            if len(tamanho) > 0:
                produtos = list(map(lambda x: {'produto': nome, 'quantidade': x['quantidade'] + quantidade} 
                if(x['produto'] == nome )else(x), produtos))
            else:
                produtos.append({'produto': nome, 'quantidade': quantidade})

        ordenado = sorted(produtos, key = lambda k: k['quantidade'], reverse=True)

        print('Esses são os produtos mais vendidos')

        for i in ordenado:
            print('--------------------------------')
            print(f'Produto:      {i["produto"]}\n'
                  f'Quntidade:    {i["quantidade"]}\n')

    def exibirVenda(self, dataIncio, dataFim):
        vendas = DaoVendas.ler()
        dataIncioA = datetime.strptime(dataIncio, '%d/%m/%Y')
        dataFimA = datetime.strptime(dataFim, '%d/%m/%Y')

        vendasSelecionadas = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= dataIncioA
                                         and datetime.strptime(x.data, '%d/%m/%Y') <= dataFimA, vendas))

        count = 1
        total = 0
        
        for i in vendasSelecionadas:
            print(f'============ Venda {count} ============')
            print(f'Nome:                       {i.itensVendido.nome}\n'
                  f'Categoria:                  {i.itensVendido.categoria}\n'
                  f'Data:                       {i.data}\n'
                  f'Quantidade:                 {i.quantidadeVendida}\n'
                  f'Cliente:                    {i.comprador}\n'
                  f'Vendedor:                   {i.vendedor}\n')
            total += int(i.itensVendido.valor) * int(i.quantidadeVendida)
            count += 1
        
        print(f'Total vendido: R$ {total}')

class ControllerFornecedor:
    
    def cadastrarFornecedor(self, fornecedor: Fornecedor):
        
        x = DaoFornecedor.ler()
        existe = False
        for i in x:
            if i.cnpj == fornecedor.cnpj:
                existe = True
                print('O fornecedor já existe')
                break
        if not existe:
            DaoFornecedor.salvar(fornecedor)    
            print('Fornecedor cadastrado')

    def removerFornecedor(self, removecnpj):

        x = DaoFornecedor.ler()
        rfor = list(filter(lambda x: x.cnpj == removecnpj, x))
        
        if len(rfor) == 0:
            print('Não existe fornecedor com este cnpj.')
        
        else:
            for i in range(len(x)):
                if x[i].cnpj == removecnpj:
                    del x[i]
                    break
                   
        with open('Fornecedor.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome+'|'+i.cnpj+'|'
                          +i.telefone+'|'+i.categoria+'|')
                arq.writelines('\n')
        print('Fornecedor removido com sucesso!')

    def alterarFornecedor(self, alteranome, fornecedor: Fornecedor):

        x = DaoFornecedor.ler()
        xfor = list(filter(lambda x: x.nome == alteranome, x))
        xcnpj = list(filter(lambda x: x.cnpj == fornecedor.cnpj, x))
        
        if len(xcnpj) == 0:
            if len(xfor) == 0:
                print('Nome não encontrado em cadastro')
            else:
                for i in range(len(x)):
                    if  x[i].nome == alteranome:
                        x[i].nome = fornecedor.nome
                        x[i].cnpj = fornecedor.cnpj
                        x[i].telefone = fornecedor.telefone
                        x[i].categoria = fornecedor.categoria
            
            with open('Fornecedor.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.nome+'|'+i.cnpj+'|'
                            +i.telefone+'|'+i.categoria+'|')
                    arq.writelines('\n')
            print('Fornecedor alterado com sucesso!')
        
        else:
            print('Cnpj já existe no banco de dados!')

    def exibirFornecedor(self):

        x = DaoFornecedor.ler()
        
        print(f'{"="*15}Fornecedores{"="*15}')
        for i in x:
            print(f'Categoria fornecida:         {i.categoria}\n'
                  f'Nome:                        {i.nome}\n'
                  f'Cnpj:                        {i.cnpj}\n'
                  f'Telefone:                    {i.telefone}\n'
                  f'---------------------------------------'
            )

class ControllerCliente:

    def cadastrarCliente(self, cliente: Cliente):

        x = DaoCliente.ler()
        cls = list(filter(lambda x: x.cpf == cliente.cpf, x))

        if len(cls) == 0:
            DaoCliente.salvar(cliente)
            print('Cliente cadastrado com sucesso')
        
        else:
            print('Cliente já está cadastrado!')

    def alterarCliente(self, alteracpf, cliente: Cliente):

        x = DaoCliente.ler()
        cls = list(filter(lambda x: x.cpf == alteracpf, x))
        clsA = list(filter(lambda x: x.cpf == cliente.cpf, x))
        
        if len(cls) > 0 and len(clsA) == 0:
            x = list(map(lambda x: Cliente(cliente.nome, cliente.telefone, cliente.cpf, cliente.email, cliente.endereco)
             if (x.cpf == alteracpf) else (x), x))
        
            with open('Cliente.txt', 'w') as arq:
                for cliente in x:
                    arq.writelines(cliente.nome+'|'+cliente.telefone+'|'
                            +cliente.cpf+'|'+cliente.email+'|'
                            +cliente.endereco)
                    arq.writelines('\n')
            
            print('Cliente alterado com sucesso')
        
        elif len(clsA) > 0:
            print('O cpf para qual voce deseja alterar já esta em uso')
        
        else:
            print('Cpf inexistente')

    def removerCliente(self, removecpf):

        x = DaoCliente.ler()
        cls = list(filter(lambda x: x.cpf == removecpf, x))
        
        if len(cls) > 0:
            for i in range(len(x)):
                if x[i].cpf == removecpf:
                    del x[i]
                    print('Cliente removido com sucesso!')
                    break
        
        else:
            print('Cpf não encontrado')

        with open('Cliente.txt', 'w') as arq:
                for cliente in x:
                    arq.writelines(cliente.nome+'|'+cliente.telefone+'|'
                            +cliente.cpf+'|'+cliente.email+'|'
                            +cliente.endereco)
                    arq.writelines('\n')
        
    def exibirCliente(self):

        x = DaoCliente.ler()
        
        print(f'{"="*15} Clientes {"="*15}')
        for i in x:
            print(f'Nome:                        {i.nome}\n'
                  f'Telefone:                    {i.telefone}\n'
                  f'Cpf:                         {i.cpf}\n'
                  f'Email:                       {i.email}\n'
                  f'Endereco:                    {i.endereco}\n'
                  f'---------------------------------------'
            )

class ControllerFuncionario:

    def cadastrarFuncionario(self, funcionario: Funcionario):

        x = DaoFuncionario.ler()
        cpf = list(filter(lambda x: x.cpf == funcionario.cpf, x))
        clt = list(filter(lambda x: x.clt == funcionario.clt, x))

        if len(cpf) > 0:
            print('Já existe um funcionário com esse cpf')
        
        elif len(clt) > 0:
            print('Já existe um funcionario com está clt')
        
        else:
            DaoFuncionario.salvar(funcionario)
            print('Funcionario cadastrado com sucesso')
        
    def alterarFuncionario(self, alteraCpf, funcionario: Funcionario):

        x = DaoFuncionario.ler()
        cpf = list(filter(lambda x: x.cpf == alteraCpf, x))
        cpfA = list(filter(lambda x: x.cpf == funcionario.cpf, x))

        if len(cpf) == 0:
            print('Não existe um funcionário com esse cpf')

        elif len(cpfA) > 0:
            print('Já existe um funcionário com esse cpf')
        
        else:
            x = list(map(lambda x: Funcionario(funcionario.clt, funcionario.nome, funcionario.telefone,
                                               funcionario.cpf, funcionario.email, funcionario.endereco)
                        if (x.cpf == alteraCpf) else (x), x))
            
            print('Funcionario alterado')
            
            with open('Funcionario.txt', 'w') as arq:
                for funcionario in x:
                    arq.writelines(funcionario.clt+'|'+funcionario.nome+'|'
                                  +funcionario.telefone+'|'+funcionario.cpf+'|'
                                  +funcionario.email+'|'+funcionario.endereco)
                    arq.writelines('\n')

    def removerFuncionario(self, removeCpf):

        x = DaoFuncionario.ler()
        cpf = list(filter(lambda x: x.cpf == removeCpf, x))

        if len(cpf) == 0:
            print('Cpf não encontrado')
        
        else: 
            for i in range(len(x)):
                if x[i].cpf == removeCpf:
                    del x[i]
                    print('Funcionario removido com sucesso')
                    break

            with open('Funcionario.txt', 'w') as arq:
                for funcionario in x:
                    arq.writelines(funcionario.clt+'|'+funcionario.nome+'|'
                                  +funcionario.telefone+'|'+funcionario.cpf+'|'
                                  +funcionario.email+'|'+funcionario.endereco)
                    arq.writelines('\n')

    def exibirFuncionario(self):

        x = DaoFuncionario.ler()

        print(f'{"="*13} Funcionarios {"="*13}')
        for i in x:
            print(f'Nome:                        {i.nome}\n'
                  f'Telefone:                    {i.telefone}\n'
                  f'Cpf:                         {i.cpf}\n'
                  f'Clt:                         {i.clt}\n'
                  f'Email:                       {i.email}\n'
                  f'Endereco:                    {i.endereco}\n'
                  f'-----------------------------------------'
            ) 
                   