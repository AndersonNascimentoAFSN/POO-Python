# Programação estruturada:

def criar_conta(numero, titular, saldo, limite):
    conta = {
      "numero": numero,
      "titular": titular,
      "saldo": saldo,
      "limite": limite
    }
    return conta


def deposita(conta, valor):
    conta["saldo"] += valor
    return conta


def saca(conta, valor):
    conta['saldo'] -= valor
    return conta


def extrato(conta):
    print("O saldo da conta é " + conta['saldo'])
