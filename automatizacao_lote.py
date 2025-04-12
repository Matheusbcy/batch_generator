import pandas as pd

caminho_arquivo = 'matheus(Pag).csv'

df = pd.read_csv(caminho_arquivo, encoding='latin1', sep=';')

valores_indesejados = ["A definir na retirada do pedido", "Pix", "Cartão - Pagamento na Central"]
df_filtrado = df[~df["PlanoPagamento"].isin(valores_indesejados)]

df_filtrado.loc[:, "ValorLiquido"] = (
    df_filtrado["ValorLiquido"]
    .str.replace('.', '', regex=False)
    .str.replace(',', '.', regex=False)
    .astype(float)
)

pedidos_acima_300 = df_filtrado[df_filtrado["ValorLiquido"] > 300]["CodigoPedido"]

pedidos_abaixo_300 = df_filtrado[df_filtrado["ValorLiquido"] <= 300]["CodigoPedido"]

print("=" * 50)
print("RESULTADOS DOS PEDIDOS FILTRADOS".center(50))
print("=" * 50)

print("\nPedidos com ValorLiquido acima de 300:")
print("-" * 50)
if not pedidos_acima_300.empty:
    print(";\n".join(pedidos_acima_300.astype(str)) + ";")
else:
    print("Nenhum pedido encontrado.")
print("-" * 50)

print("\nPedidos com ValorLiquido abaixo de 300:")
print("-" * 50)
if not pedidos_abaixo_300.empty:
    print(";\n".join(pedidos_abaixo_300.astype(str)) + ";")
else:
    print("Nenhum pedido encontrado.")
print("-" * 50)

print("\n" + "=" * 50)
print("Arquivo filtrado salvo como 'arquivo_filtrado.csv'.".center(50))
print("=" * 50)