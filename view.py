from importlib.resources import path
from controller import *
import os.path

def criarArquivos(*args):
    for i in args:
        if not os.path.exists(i):
            with open(i , 'w') as arq:
                arq.writelines('')

print('\n        Bem-Vindo a Mercearia!\n')

criarArquivos('Categoria.txt', 'Cliente.txt', 'Estoque.txt',
              'Fornecedor.txt', 'Funcionarios.txt', 'Vendas.txt')

print('Iniciando sistema...')

if __name__ == '__main__':
    
    while True:
        
        print('\nDigite 1 para acessar ( Categorias )\n'
              'Digite 2 para acessar ( Estoque )\n'
              'Digite 3 para acessar ( Vendas )\n'
              'Digite 4 para acessar ( Fornecedores )\n'
              'Digite 5 para acessar ( Clientes )\n'
              'Digite 6 para acessar ( Funcionarios )\n'
              'Digite 7 para acessar ( Produtos mais vendidos )\n'
              'Digite 0 para Encerrar o sistema.\n')
        
        opcao = int(input('Opção selecionada: '))

        if opcao == 1:
            cat = ControllerCategoria()

            while True:
                
                print('\nDigite 1 para cadastrar Categoria\n'
                      'Digite 2 para alterar Categoria\n'
                      'Digite 3 para remover Categoria\n'
                      'Digite 4 para exibir Categorias\n'
                      'Digite 0 para sair\n')
                
                decisao = int(input('Opção selecionada: '))

                if decisao == 1:
                    categoria = input('Digite a categoria que deseja cadastrar: ')
                    print('')
                    cat.cadastrarCategoria(categoria)
                
                elif decisao == 2:
                    alteraCategoria = input('Digite a categoria que deseja alterar: ')
                    novaCategoria = input('Digite para qual categoria será alterada: ')
                    print('')
                    cat.alterarCategoria(alteraCategoria, novaCategoria)
                
                elif decisao == 3:    
                    removeCategoria = input('Digite a categoria que deseja remover:')
                    print('')
                    cat.removerCategoria(removeCategoria)
                
                elif decisao == 4:
                    print('')
                    cat.exibirCategoria()

                elif decisao == 0:
                    print('Voltando para o menu principal...')
                    break

                else:
                    print('Opção inválida! Tente novamente')    

        elif opcao == 2:
            est = ControllerEstoque()

            while True:
                
                print('\nDigite 1 para cadastrar Produto\n'
                      'Digite 2 para alterar Produto\n'
                      'Digite 3 para remover Produto\n'
                      'Digite 4 para exibir Estoque\n'
                      'Digite 0 para sair\n')
                
                decisao = int(input('\nOpção selecionada: '))

                if decisao == 1:
                    print('\nCadastrar produto: ')                    
                    nome = input('Digite o nome: ')
                    valor = input('Digite o valor: ')
                    cat = input('Digite a categoria: ')
                    qnt = input('Digite a quantidade: ') 
                    print('')
                    est.cadastrarProduto(nome, valor, cat, qnt)
                
                elif decisao == 2:
                    alteraProduto = input('\nDigite o nome do produto que deseja alterar: ')
                    novoNome = input('Digite o novo nome: ')
                    novoValor = input('Digite o valor: ')
                    novaCat = input('Digite a categoria: ')
                    novaQnt = input('Digite a quantidade: ')
                    print('')
                    est.alterarProduto(alteraProduto, novoNome, novoValor, novaCat, novaQnt)
                
                elif decisao == 3:    
                    removeNome = input('\nDigite o nome do produto que deseja remover:')
                    print('')
                    est.removerProduto(removeNome)
                
                elif decisao == 4:
                    print('')
                    est.exibirEstoque()

                elif decisao == 0:
                    print('\nVoltando para o menu principal...')
                    break

                else:
                    print('\nOpção inválida! Tente novamente')

        elif opcao == 3:
            vend = ControllerVenda()

            while True:
                
                print('Digite 1 para cadastrar vendas\n'
                      'Digite 2 para exibir vendas\n'
                      'Digite 0 para sair')
                decisao = int(input('\nOpção selecionada: '))

                if decisao == 1:
                    print('\nCadastrar venda')
                    produto = input('Digite o nome do produto: ')
                    quantidade = input('Digite a quantidade vendida: ')
                    comprador = input('Digite o nome do cliente: ')
                    vendedor = input('Digite o vendedor que realizou a venda: ')
                    print('')
                    vend.cadastrarVenda(produto, vendedor, comprador, quantidade)

                elif decisao == 2:
                    inicio = input('\nDigite a data de inicio (dd/mm/aaaa): ')
                    fim = input('Digite a data limite: ')
                    print('')
                    vend.exibirVenda(inicio, fim)
                
                elif decisao == 0:
                    print('\nVoltando para o menu principal...')
                    break

                else:
                    print('\nOpção invalida!')
            
        elif opcao == 4:
            fornecedores = ControllerFornecedor()

            while True:
                
                print('\nDigite 1 para cadastrar Fornecedor\n'
                      'Digite 2 para alterar Fornecedor\n'
                      'Digite 3 para remover Fornecedor\n'
                      'Digite 4 para exibir Fornecedores\n'
                      'Digite 0 para sair\n')
                decisao = int(input('Opção selecionada: '))

                if decisao == 1:
                    print('\nCadastrar Fornecedor')
                    nome = input('Digite o nome: ')
                    cnpj = input('Digite o cnpj: ')
                    telefone = input('Digite o telefone: ')
                    categoria = input('Digite a categoria: ')
                    print('')
                    fornecedores.cadastrarFornecedor(Fornecedor(nome, cnpj, telefone, categoria))

                elif decisao == 2:
                    print('\nAlterar Fornecedor')
                    alterarNome: input('Digite o nome do fornecedor que deseja alterar')
                    nome = input('Digite o nome: ')
                    cnpj = input('Digite o cnpj: ')
                    telefone = input('Digite o telefone: ')
                    categoria = input('Digite a categoria: ')
                    print('')
                    fornecedores.alterarFornecedor(alterarNome, Fornecedor(nome, cnpj, telefone, categoria))

                elif decisao == 3:
                    print('\nRemover Fornecedor')
                    removecnpj = input('Digite o cnpj do fornecedor que deseja remover: ')
                    print('')
                    fornecedores.removerFornecedor(removecnpj)

                elif decisao == 4:
                    print('')
                    fornecedores.exibirFornecedor()

                elif decisao == 0:
                    print('\nVoltando para o menu principal...')
                    break

                else:
                    print('\nOpção invalida!')

        elif opcao == 5:
            cliente = ControllerCliente()

            while True: 
                
                print('\nDigite 1 para cadastrar Cliente\n'
                      'Digite 2 para alterar Cliente\n'
                      'Digite 3 para remover Cliente\n'
                      'Digite 4 para exibir Clientes\n'
                      'Digite 0 para sair\n')
                decisao = int(input('Opção selecionada: '))

                if decisao == 1:
                    print('\nCadastrar Cliente')
                    nome = input('Digite o nome: ')
                    cpf = input('Digite o cpf: ')
                    telefone = input('Digite o telefone: ')
                    email = input('Digite o email: ')
                    endereco = input('Digite o endereco: ')
                    print('')
                    cliente.cadastrarCliente(Cliente(nome, telefone, cpf, email, endereco))

                elif decisao == 2:
                    print('\nAlterar Cliente')
                    alterarcpf: input('Digite o cpf do cliente que deseja alterar')
                    nome = input('Digite o nome: ')
                    cpf = input('Digite o cpf: ')
                    telefone = input('Digite o telefone: ')
                    email = input('Digite o email: ')
                    endereco = input('Digite o endereco: ')
                    print('')
                    cliente.alterarCliente(alterarcpf, Cliente(nome, telefone, cpf, email, endereco))

                elif decisao == 3:
                    print('\nRemover Cliente')
                    removecpf = input('Digite o cpf do cliente que deseja remover: ')
                    print('')
                    cliente.removerCliente(removecpf)

                elif decisao == 4:
                    print('')
                    cliente.exibirCliente()

                elif decisao == 0:
                    print('\nVoltando para o menu principal...')
                    break

                else:
                    print('\nOpção invalida!')

        elif opcao == 6:
            func = ControllerFuncionario()

            while True: 
                
                print('\nDigite 1 para cadastrar Funcionario\n'
                      'Digite 2 para alterar Funcionario\n'
                      'Digite 3 para remover Funcionario\n'
                      'Digite 4 para exibir Funcionarios\n'
                      'Digite 0 para sair\n')
                decisao = int(input('Opção selecionada: '))

                if decisao == 1:
                    print('\nCadastrar Funcionario')
                    nome = input('Digite o nome: ')
                    cpf = input('Digite o cpf: ')
                    clt = input('Digite a clt: ')
                    telefone = input('Digite o telefone: ')
                    email = input('Digite o email: ')
                    endereco = input('Digite o endereco: ')
                    print('')
                    func.cadastrarFuncionario(Funcionario(clt, nome, telefone, cpf, email, endereco))

                elif decisao == 2:
                    print('\nAlterar Funcionario')
                    alterarcpf: input('Digite o cpf do funcionario que deseja alterar')
                    nome = input('Digite o nome: ')
                    cpf = input('Digite o cpf: ')
                    clt = input('Digite a clt: ')
                    telefone = input('Digite o telefone: ')
                    email = input('Digite o email: ')
                    endereco = input('Digite o endereco: ')
                    print('')
                    func.alterarFuncionario(alterarcpf, Funcionario(clt, nome, telefone, cpf, email, endereco))

                elif decisao == 3:
                    print('\nRemover Funcionario')
                    removecpf = input('Digite o cpf do funcionario que deseja remover: ')
                    print('')
                    func.removerFuncionario(removecpf)

                elif decisao == 4:
                    print('')
                    func.exibirFuncionario()

                elif decisao == 0:
                    print('\nVoltando para o menu principal...')
                    break

                else:
                    print('\nOpção invalida!')

        elif opcao == 7:
            venda = ControllerVenda()
            venda.relatorioProdutos()
            print('')
            continua = input('Deseja continuar?')

        elif opcao == 0:
            print('\nEncerrando sistema...')
            break

        else: 
            print('\nOpção inválida!')
