#Sistema de Controle de Estoque
#Engenharia de Software
#Ryan Masami - RU:5218086

from datetime import datetime
estoque = {}
# Registra um novo produto e verifica se já existe antes de cadastrar
def cadastrar_produto():
    print("\n--- CADASTRAR PRODUTO ---")
    nome = input("Nome do produto: ").strip()

    if nome in estoque:
        print(f"Atenção, o produto '{nome}' já está cadastrado.")
        return
    
    # Produto cadastrado com quantidade inicial zero   
    estoque[nome] = {
        "quantidade": 0,
        "movimentacoes": []
    }
    print(f"Produto '{nome}' cadastrado com sucesso!")

# Registra a entrada de um produto e atualiza a quantidade disponível automaticamente
def registrar_entrada():
    print("\n--- REGISTRAR ENTRADA ---")

    # Verifica se há produtos cadastrados   
    if not estoque:
        print("Nenhum produto cadastrado. Cadastre um produto primeiro")
        return
    
    print("Produtos cadastrados: ")
    for produto in estoque:
        print(f" - {produto} (estoque atual: {estoque [produto]['quantidade']})")

    nome = input("\nNome do produto para entrada: ").strip()

    # Valida se o produto existe
    if nome not in estoque:
        print(f"Produto '{nome}' não encontrado.")
        return
    
    # Valida se a quantidade informada é um número positivo
    try:
        quantidade = int(input("Quantidade recebida: "))
        if quantidade <= 0:
            print("A quantidade deve ser maior que zero;")
            return
    except ValueError:
        print("Quantidade inválida. Digite um número inteiro")
        return
    
    responsavel = input("Nome do responsável: ").strip()
    # Registra a data e hora atual automaticamente
    data = datetime.now().strftime("%d/%m/%y %H:%M")

    # Atualiza o saldo do estoque
    estoque[nome]["quantidade"] += quantidade

    # Registra a movimentação no histórico
    estoque[nome]["movimentacoes"].append({
        "tipo": "ENTRADA",
        "quantidade": quantidade,
        "data": data,
        "responsavel": responsavel
    })
    print(f"Entrada registrada! Novo saldo de '{nome}': {estoque[nome]['quantidade']} unidades.")

# Registra a saída de um produto e valida se há quantidade suficiente antes de confirmar
def registrar_saida():
    print("\n--- REGISTRAR SAÍDA ---")

    # Verifica se há produtos cadastrado
    if not estoque:
        print(" Nenhum produto cadastrado. Cadastre um produto primeiro.")
        return
    print("Produtos cadastrados: ")
    for produto in estoque:
        print(f" - {produto} (estoque atual: {estoque[produto]['quantidade']})")

    nome = input('\nNome do produto para saída: ').strip()

    # Valida se o produto existe
    if nome not in estoque:
        print(f"Produto '{nome}' não encontrado.")
        return
    
    # Valida se a quantidade informada é um número positivo
    try:
        quantidade = int(input("Quantidade retirada: "))
        if quantidade <= 0:
            print("A quantidade deve ser maior que zero;")
            return
    except ValueError:
        print("Quantidade inválida. Digite um número inteiro")
        return
    # Validação crítica: impede saída maior que o saldo disponível
    if quantidade > estoque[nome]["quantidade"]:
        print(f"Estoque insuficiente! Saldo atual: {estoque[nome]['quantidade']} unidades.")
        return
    
    responsavel = input("Nome do responsável: ").strip()
    # Registra a data e hora atual automaticamente
    data = datetime.now().strftime("%d/%m/%y %H:%M")

    # Atualiza o saldo do estoque
    estoque[nome]["quantidade"] -= quantidade

    # Registra a movimentação no histórico
    estoque[nome]["movimentacoes"].append({
        "tipo": "SAÍDA",
        "quantidade": quantidade,
        "data": data,
        "responsavel": responsavel
    })
    print(f"Saída registrada! Novo saldo de '{nome}': {estoque[nome]['quantidade']} unidades.")

# Exibe todos os produtos e o histórico de movimentações
def visualizar_estoque():
    print("\n--- ESTOQUE ATUAL ---")

    # Verifica se há produtos cadastrados
    if not estoque:
        print("Nenhum produto cadastrado")
        return
    for nome, dados in estoque.items():
        print(f"\n Produto: {nome}")
        print(f"  Quantidade disponível {dados['quantidade']} unidades")

        # Exibe o histórico de movimentações se existir
        if dados["movimentacoes"]:
            print("  Histórico:")
            for mov in dados["movimentacoes"]:
                print(f"  [{mov['tipo']}] {mov['quantidade']} un. - {mov['data']} - Resp: {mov['responsavel']}")
        
        else:
            print("  Sem movimentações registradas.")


#Exibe o menu principal e direciona para cada operação
def menu():
    print("  SISTEMA DE CONTROLE DE ESTOQUE")
    print("=" * 50)

    while True:
        print("\n[1] Cadastrar produto")
        print("[2] Registrar entrada")
        print("[3] Registrar saída")
        print("[4] Visualizar estoque")
        print("[5] Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            registrar_entrada()
        elif opcao == "3":
            registrar_saida()
        elif opcao == "4":
            visualizar_estoque()
        elif opcao == "5":
            print("\nSistema encerrado. Até logo!")
            break
        else:
            print("⚠️  Opção inválida. Digite um número entre 1 e 5.")

if __name__ == "__main__":
    menu()