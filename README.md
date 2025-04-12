# 📊 Filtro de Pedidos por Valor Líquido

Este projeto em Python utiliza a biblioteca **pandas** para ler, filtrar e processar pedidos de um arquivo `.csv`, separando os pedidos com base no valor líquido.

## 🔍 O que o script faz?

1. Lê um arquivo `.csv` com informações de pedidos.
2. Remove entradas com formas de pagamento indesejadas:
   - "A definir na retirada do pedido"
   - "Pix"
   - "Cartão - Pagamento na Central"
3. Converte a coluna `ValorLiquido` de string para número (`float`).
4. Filtra e exibe os pedidos com:
   - Valor **acima de 300**
   - Valor **igual ou abaixo de 300**
5. Exibe os resultados formatados no terminal.
6. Salva o arquivo filtrado como `arquivo_filtrado.csv` (opcional, você pode adicionar essa linha no código).

## 🧾 Exemplo de entrada

O script espera um arquivo `.csv` com pelo menos as seguintes colunas:

- `PlanoPagamento`
- `ValorLiquido`
- `CodigoPedido`

**Separador:** `;`  
**Codificação:** `latin1`

## ▶️ Como usar

1. Instale a biblioteca necessária (se ainda não tiver):

```bash
pip install pandas
Salve o script Python em um arquivo, por exemplo: filtro_pedidos.py.

Certifique-se de que o arquivo matheus(Pag).csv está na mesma pasta do script.

Execute o script:
python filtro_pedidos.py

📂 seu_projeto/
├── filtro_pedidos.py
├── matheus(Pag).csv
└── arquivo_filtrado.csv  # (opcional, se você adicionar o salvamento no script)