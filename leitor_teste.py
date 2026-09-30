import requests


URL_API = "http://127.0.0.1:8000/smartcheckout/ler"


def validar_gtin(codigo):
    codigo = codigo.strip()

    if not codigo.isdigit():
        return False

    tamanho = len(codigo)

    if tamanho not in (8, 12, 13, 14):
        return False

    digitos = [int(digito) for digito in codigo]

    digito_verificador = digitos[-1]
    digitos_base = digitos[:-1]

    soma = 0
    multiplicador = 3

    for digito in reversed(digitos_base):
        soma += digito * multiplicador

        if multiplicador == 3:
            multiplicador = 1
        else:
            multiplicador = 3

    calculado = (10 - (soma % 10)) % 10

    return calculado == digito_verificador


def identificar_tipo(leitura):
    leitura = leitura.strip()

    if leitura.lower().startswith(("http://", "https://")):
        return "qrcode"

    if validar_gtin(leitura):
        return "codigo_barras"

    if leitura.isdigit():
        return "codigo_barras"

    return "desconhecido"


print("===================================")
print("      SMARTCHECKOUT - LEITOR")
print("===================================")
print()
print("Simulador de entrada do SmartCheckout")
print("O tipo da leitura será identificado automaticamente.")
print("Digite 'sair' para encerrar.")
print()


while True:
    leitura = input("Leitura: ").strip()

    if leitura.lower() == "sair":
        print("Encerrando simulador.")
        break

    if not leitura:
        print("Nenhuma leitura informada.")
        print()
        continue

    tipo = identificar_tipo(leitura)

    print(f"Tipo identificado: {tipo}")
    print()

    try:
        resposta = requests.post(
            URL_API,
            json={
                "leitura": leitura,
                "tipo": tipo
            }
        )

        print(f"HTTP {resposta.status_code}")
        print(resposta.text)

    except requests.exceptions.RequestException as erro:
        print("Erro ao conectar com a API.")
        print(erro)

    print()