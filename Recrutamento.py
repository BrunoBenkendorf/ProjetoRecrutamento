import json
import urllib.request

def formatar_cpf(cpf):
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

def formatar_telefone(telefone):
    if len(telefone) == 10:  # Formato (xx) xxxx-xxxx
        return f"({telefone[:2]}) {telefone[2:6]}-{telefone[6:]}"
    elif len(telefone) == 11:  # Formato (xx) xxxxx-xxxx
        return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
    else:
        return telefone  # Retorna o telefone sem formatação se o tamanho for inválido

def main():
    recrutados = []

    while True:
        recrutado = {}

        while True:
            nome = input("\nDigite o nome do recrutado: ")
            if nome.strip():  # Verifica se o nome não está vazio
                recrutado["nome"] = nome
                break
            else:
                print("Nome inválido. Tente novamente.")
                
        while True:
            sobrenome = input("Digite o sobrenome do recrutado: ")
            if sobrenome.strip():
                recrutado["sobrenome"] = sobrenome
                break
            else:
                print("Sobrenome inválido. Tente novamente.")
                
        while True:
            sexo = input("Digite o sexo do recrutado (M/F): ")
            if sexo in ['M', 'F']:
                recrutado["sexo"] = sexo
                break
            else:
                print("Sexo inválido. Tente novamente.")
                
        while True:
            cep = input("Digite o cep: ")
            if len(cep) == 8 and cep.isdigit():
                link = f"https://viacep.com.br/ws/{cep}/json/"
                try:
                    with urllib.request.urlopen(link) as response:
                        data = json.loads(response.read().decode())
                        if "erro" not in data:
                            print("CEP: ", data["cep"])
                            print("Logradouro: ", data["logradouro"])
                            print("Bairro: ", data["bairro"])
                            print("Cidade: ", data["localidade"])
                            print("Estado: ", data["uf"])
                            recrutado["cep"] = data["cep"]
                            recrutado["logradouro"] = data["logradouro"]
                            recrutado["bairro"] = data["bairro"]
                            recrutado["cidade"] = data["localidade"]
                            recrutado["estado"] = data["uf"]
                            break
                        else:
                            print("CEP não encontrado.")
                except urllib.error.URLError as e:
                    print("Erro ao acessar o serviço de CEP:", e)
            else:
                print("CEP deve conter 8 dígitos numéricos.")

        while  True:
            numero = input("Número: ")
            if numero.isdigit() and int(numero) > 0:
                recrutado["numero"] = int(numero)
                break

        while True:
            telefone = input(
                "Digite o telefone do recrutado (apenas números): ")
            if telefone.isdigit() and (len(telefone) == 10 or len(telefone) == 11):
                recrutado["telefone"] = formatar_telefone(telefone)
                break
            else:
                print("Telefone inválido. Tente novamente.")

        while True:
            cpf = input("Digite o CPF do recrutado (apenas números): ")
            if cpf.isdigit() and len(cpf) == 11:
                recrutado["cpf"] = formatar_cpf(cpf)
                break
            else:
                print("CPF inválido. Tente novamente.")

        while True:
            idade = input("Digite a idade do recrutado: ")
            if idade.isdigit() and int(idade) > 0:
                recrutado["idade"] = int(idade)
                break
            else:
                print("Idade inválida. Tente novamente.")

        while True:
            formacao = input(
                "Digite a formação do recrutado (EF/I,EF/C,EM/I, EM/C, ES/C, ES/I, TEC, POS): ")
            if formacao in ("EF/I", "EF/C", "EM/I", "EM/C", "ES/C", "ES/I", "TEC", "POS"):
                recrutado["formacao"] = formacao
                break
            else:
                print("Escolaridade inválida. Tente novamente.")

        while True:
            nacionalidade = input("Digite a nacionalidade do recrutado: ")
            if nacionalidade.strip():
                recrutado["nacionalidade"] = nacionalidade
                break
            else:
                print("Nacionalidade inválida. Tente novamente.")

        if recrutado["idade"] >= 18:
            while True:
                recrutado["vaga"] = input(
                    "\nVagas para maiores de 18 (Gerente de vendas, Almoxarife, Vendedor, Produção, Apoio industrial, Marketing, Segurança do Trabalho): ")
                if recrutado["vaga"] in ["Gerente de vendas", "Vendedor", "Almoxarife", "Produção", "Apoio industrial", "Marketing", "Segurança do Trabalho"]:
                    recrutado["experiencia"] = input(
                        "Recrutado tem experiência na área? (s/n): ")
                    recrutado["pcd"] = input(
                        "Recrutado tem alguma necessidade especial? (s/n): ")
                    if recrutado["pcd"] in ["s"]:
                        defi = input("Qual? ")
                        recrutado["defi"] = defi
                    criterios = input(
                        "Recrutado atende a todos os requisitos? (s/n): ")
                    break
                else:
                    print("Vaga inválida. Tente novamente.")
        else:
            if recrutado["idade"] < 14:
                criterios = "n"
                print("Idade inválida para ser recrutado!!!")
            else:
                while True:
                    recrutado["vaga"] = input(
                        "\nVagas para menor aprendiz (Aux.Adm, Aux.Geral, Aux.Prod): ")
                    if recrutado["vaga"] in ["Aux.Adm", "Aux.Geral", "Aux.Prod"]:
                        recrutado["pcd"] = input(
                            "Recrutado tem alguma necessidade especial? (s/n): ")
                        if recrutado["pcd"] in ["s"]:
                            defi = input("Qual? ")
                            recrutado["defi"] = defi
                            criterios = input(
                                "Recrutado atende a todos os requisitos? (s/n): ")
                        break
                    else:
                        print("Vaga inválida. Tente novamente.")

        if criterios == "s":
            recrutados.append(recrutado)
            print("\nRecrutado registrado")
            print("Vaga:", recrutado["vaga"])
            print("Nome:", recrutado["nome"], recrutado["sobrenome"])
            print("Sexo:", recrutado["sexo"])
            print("CEP:", recrutado["cep"])
            print("Endereço:", recrutado["logradouro"], recrutado["numero"], ",", recrutado["bairro"], ",", recrutado["cidade"], "-", recrutado["estado"])
            print("Telefone:", recrutado["telefone"])
            print("Nacionalidade:", recrutado["nacionalidade"])
            print("CPF:", recrutado["cpf"])
            print("Idade:", recrutado["idade"])
            print("Experiência:", recrutado.get("experiencia", "n/a"))
            print("Formação:", recrutado["formacao"])
            print("Necessidade especial:", recrutado["pcd"])
            print("Qual:", recrutado.get("defi", "n/a"))
        else:
            print("Impossível cadastrar !!!")

        finalizar = input("\nDeseja finalizar? (s/n): ")
        if finalizar == "s":
            break

    mostrar_recrutados = input("\nDeseja mostrar todos os recrutados? (s/n): ")
    if mostrar_recrutados == "s":
        for i in recrutados:
            print("\n--- Recrutado ---")
            print("Vaga:", i["vaga"])
            print("Nome:", i["nome"], i["sobrenome"])
            print("Sexo:", i["sexo"])
            print("CEP:", i["cep"])
            print("Endereço:", i["logradouro"], i["numero"], ",", i["bairro"], ",", i["cidade"], "-", i["estado"])
            print("Telefone:", i["telefone"])
            print("Nacionalidade:", i["nacionalidade"])
            print("CPF:", i["cpf"])
            print("Idade:", i["idade"])
            print("Experiência:", i.get("experiencia", "n/a"))
            print("Formação:", i["formacao"])
            print("Necessidade especial:", i["pcd"])
            print("Qual:", i.get("defi", "n/a"))

if __name__ == "__main__":
    main()