
def buscar_cep(cep):
    url = f"https://brasilapi.com.br/api/cep/v1/{cep}"

    try:
        response = requests.get(url)

        response.raise_for_status()

        dados = response.json()

        print("\n📍 Endereço Encontrado:")
        print(f"CEP: {dados.get('cep')}")
        print(f"RUA: {dados.get('street')}")
        print(f"BAIRRO: {dados.get('neighborhood')}")
        print(f"CIDADE: {dados.get('city')}")
        print(f"ESTADO: {dados.get('state')}")

    except requests.exceptions.HTTPError:
            print("❌ CEP não encontrado ou inválido.")


    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao acessar a API: {e}")


if __name__ == "__main__":
    print("\ Buscar Endereço pelo CEP /")

    cep = input("Digite um cep(somente números: ").strip()

    cep.replace("-", "").replace(" ", "")

    #verificar se o cep tem 8 digitos

if len(cep) == 8 and cep.isdigit():
    buscar_cep(cep)
else:
    print("❌ CEP inválido. Digite exatamente 8 dígitos.")

