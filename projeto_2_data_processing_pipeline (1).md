# Projeto 2 — Data Processing Pipeline

## Objetivo

Construir, usando **Python sem pandas**, um pequeno pipeline de processamento de dados utilizando dados reais de e-commerce.

O pipeline deverá:

```text
dados brutos
    ↓
ingestão
    ↓
validação
    ↓
limpeza
    ↓
transformação
    ↓
relacionamento
    ↓
agregação/análise
    ↓
exportação
```

O foco é aprender a manipular dados diretamente com Python antes de introduzir pandas, SQL, APIs e bancos de dados.

---

# 1. Dataset escolhido

## Brazilian E-Commerce Public Dataset by Olist

Fonte:

**Kaggle — Brazilian E-Commerce Public Dataset by Olist**

https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

O dataset foi disponibilizado pela Olist e contém aproximadamente **100 mil pedidos realizados entre 2016 e 2018**, com informações de pedidos, clientes, produtos, pagamentos, frete, localização, vendedores e avaliações. Os dados comerciais são reais, mas foram anonimizados. 

O dataset oficial contém **9 arquivos CSV**:

```text
olist_customers_dataset.csv
olist_geolocation_dataset.csv
olist_order_items_dataset.csv
olist_order_payments_dataset.csv
olist_order_reviews_dataset.csv
olist_orders_dataset.csv
olist_products_dataset.csv
olist_sellers_dataset.csv
product_category_name_translation.csv
```

Neste projeto **não será necessário utilizar todos eles**.

---

# 2. Arquivos que serão utilizados

Para manter o projeto desafiador sem ficar desnecessariamente gigantesco, comece com estes arquivos:

```text
olist_customers_dataset.csv
olist_orders_dataset.csv
olist_order_items_dataset.csv
olist_products_dataset.csv
olist_order_reviews_dataset.csv
product_category_name_translation.csv
```

Os demais arquivos ficam como material opcional para uma segunda etapa.

---

# 3. O papel de cada arquivo

## `olist_customers_dataset.csv`

Informações sobre clientes e localização.

Principais campos:

```text
customer_id
customer_unique_id
customer_zip_code_prefix
customer_city
customer_state
```

Uma particularidade importante do dataset é que `customer_id` identifica o registro do cliente associado ao pedido, enquanto `customer_unique_id` permite identificar o mesmo consumidor em diferentes pedidos.

Isso será importante para análises de recompra.

---

## `olist_orders_dataset.csv`

Informações dos pedidos.

Campos importantes:

```text
order_id
customer_id
order_status
order_purchase_timestamp
order_approved_at
order_delivered_carrier_date
order_delivered_customer_date
order_estimated_delivery_date
```

Será uma das principais fontes do pipeline.

---

## `olist_order_items_dataset.csv`

Itens individuais de cada pedido.

Campos importantes:

```text
order_id
order_item_id
product_id
seller_id
shipping_limit_date
price
freight_value
```

Um pedido pode possuir vários itens.

Isso é importante:

```text
1 pedido
    ↓
vários itens
```

Não trate `order_id` como se aparecesse apenas uma vez nesse arquivo.

---

## `olist_products_dataset.csv`

Informações dos produtos.

Campos importantes:

```text
product_id
product_category_name
product_name_lenght
product_description_lenght
product_photos_qty
product_weight_g
product_length_cm
product_height_cm
product_width_cm
```

Esse arquivo permitirá trabalhar com:

- valores ausentes;
- categorias;
- valores numéricos;
- relacionamento por `product_id`.

---

## `olist_order_reviews_dataset.csv`

Avaliações dos pedidos.

Campos importantes:

```text
review_id
order_id
review_score
review_comment_title
review_comment_message
review_creation_date
review_answer_timestamp
```

Este arquivo será particularmente importante para:

- valores ausentes;
- texto;
- Unicode;
- UTF-8;
- limpeza de strings;
- regex;
- análise de avaliações.

---

## `product_category_name_translation.csv`

Relaciona nomes de categorias em português com seus equivalentes em inglês.

Campos:

```text
product_category_name
product_category_name_english
```

Esse arquivo servirá como uma fonte adicional para praticar relacionamento entre dados.

---

# 4. Estrutura inicial do projeto

Comece com:

```text
project/
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│
└── README.md
```

Coloque os arquivos originais do Kaggle em:

```text
data/raw/
```

### Regra importante

Os arquivos dentro de `raw/` são os dados originais.

**Não altere esses arquivos.**

Todo resultado produzido pelo seu programa deverá ser colocado em:

```text
data/processed/
```

---

# 5. Regra principal

## NÃO usar pandas

O projeto deverá ser desenvolvido sem:

```python
import pandas
```

Também não utilizar bibliotecas externas para resolver automaticamente as etapas de limpeza e transformação.

Pode utilizar a biblioteca padrão do Python, incluindo:

```python
csv
json
re
pathlib
collections
datetime
```

e outras bibliotecas padrão que façam sentido.

---

# 6. Estrutura de dados principal

A estrutura principal de manipulação deverá ser:

```python
list[dict]
```

Exemplo:

```python
[
    {
        "order_id": "...",
        "customer_id": "...",
        "status": "delivered"
    },
    {
        "order_id": "...",
        "customer_id": "...",
        "status": "canceled"
    }
]
```

Você poderá utilizar outras estruturas auxiliares quando necessário.

Por exemplo:

```python
dict
set
tuple
```

---

# 7. Etapa 1 — Ingestão

Crie uma forma de carregar os arquivos CSV.

Você deverá:

- abrir os arquivos;
- identificar o encoding adequado;
- lidar com o delimitador;
- ler o cabeçalho;
- transformar os registros em estruturas Python;
- lidar com possíveis problemas de leitura.

Não utilize `pandas.read_csv()`.

O resultado deverá ser uma estrutura que você consiga manipular diretamente em Python.

---

# 8. Etapa 2 — Validação

Antes de limpar os dados, faça uma etapa de inspeção.

Você deverá descobrir problemas como:

- valores ausentes;
- registros incompletos;
- IDs ausentes;
- IDs duplicados quando deveriam ser únicos;
- tipos armazenados como texto;
- relacionamentos quebrados;
- datas inválidas;
- valores inesperados.

Crie uma forma de registrar ou contabilizar esses problemas.

### Regra

Não simplesmente delete dados problemáticos.

Primeiro descubra:

> Qual é o problema?

Depois:

> Qual deveria ser o comportamento correto?

---

# 9. Etapa 3 — Limpeza

Faça a limpeza necessária nos dados.

Alguns exemplos de problemas que podem ser encontrados:

```text
strings vazias
None
espaços extras
categorias inconsistentes
campos ausentes
valores numéricos representados como texto
datas representadas como strings
```

Você deverá estabelecer regras para cada tipo de problema.

---

# 10. Etapa 4 — Valores ausentes

Trabalhe especificamente com os valores ausentes.

Você deverá identificar:

- quais campos possuem valores ausentes;
- quantos registros são afetados;
- quais campos são essenciais;
- quais podem receber um tratamento diferente.

Nem todo valor ausente deve necessariamente resultar na exclusão do registro.

Decida caso a caso.

---

# 11. Etapa 5 — Duplicatas

Identifique registros duplicados.

Mas não assuma que duas linhas iguais são sempre o único tipo de duplicata possível.

Pense em critérios de unicidade.

Por exemplo:

```text
review_id
order_id
product_id
```

podem possuir regras diferentes de unicidade dependendo do arquivo.

Documente suas decisões.

---

# 12. Etapa 6 — Transformação

Transforme os dados para que possam ser analisados.

Possíveis transformações:

- strings;
- datas;
- números;
- categorias;
- identificadores;
- valores monetários;
- campos derivados.

Exemplo conceitual:

```text
"  delivered "
       ↓
"delivered"
```

Ou:

```text
"2018-08-02 10:26:34"
       ↓
objeto/data adequada
```

O objetivo é que os dados processados tenham tipos e formatos coerentes.

---

# 13. Etapa 7 — Relacionamento entre os arquivos

Esta é uma das partes mais importantes do projeto.

Você deverá relacionar os arquivos utilizando os identificadores existentes.

Exemplo:

```text
orders
   │
   │ customer_id
   ↓
customers
```

E:

```text
orders
   │
   │ order_id
   ↓
order_items
   │
   │ product_id
   ↓
products
```

E:

```text
products
   │
   │ product_category_name
   ↓
product_category_name_translation
```

Você deverá descobrir como realizar esses relacionamentos eficientemente.

### Desafio

Evite simplesmente percorrer uma lista inteira toda vez que precisar encontrar um registro relacionado.

Pense em estruturas auxiliares que possam facilitar essas buscas.

---

# 14. Etapa 8 — Regex

Regex deverá ser usada para resolver problemas reais dos dados.

Utilize:

```python
import re
```

Praticar:

- busca de padrões;
- extração;
- grupos;
- classes;
- quantificadores;
- validação.

As avaliações possuem campos textuais que poderão ser utilizados para isso.

Não crie um exercício artificial de regex separado do projeto.

Procure um problema real nos dados que possa ser resolvido com padrões.

---

# 15. Etapa 9 — Encoding

O projeto deverá envolver explicitamente:

- ASCII;
- Unicode;
- UTF-8;
- encoding;
- decoding;
- problemas comuns de encoding.

Observe principalmente os campos textuais em português, como:

```text
customer_city
product_category_name
review_comment_message
```

Você deverá entender por que caracteres como:

```text
ã
ç
é
õ
```

podem apresentar problemas quando o encoding é tratado incorretamente.

---

# 16. Etapa 10 — Filtragem

Crie operações para selecionar subconjuntos dos dados.

Exemplos:

- pedidos de determinado estado;
- pedidos com determinado status;
- produtos de determinada categoria;
- avaliações com determinada nota;
- pedidos acima de determinado valor;
- clientes que fizeram mais de uma compra.

Os filtros devem utilizar as estruturas Python, sem pandas.

---

# 17. Etapa 11 — Ordenação

Crie análises que exijam ordenação.

Exemplos:

- produtos com maior número de vendas;
- categorias com maior faturamento;
- clientes com mais pedidos;
- maiores valores de frete;
- melhores/piores avaliações.

Praticar:

```python
sorted()
key=
lambda
```

---

# 18. Etapa 12 — Agregação e contagem

Produza informações agregadas.

Exemplos:

### Pedidos

- quantidade total;
- quantidade por status;
- quantidade por estado;
- quantidade por mês.

### Produtos

- produtos mais vendidos;
- categorias mais vendidas;
- quantidade de itens por categoria.

### Clientes

- quantidade de clientes;
- clientes com múltiplos pedidos;
- quantidade média de pedidos por cliente.

### Avaliações

- média das notas;
- distribuição das notas;
- quantidade de avaliações por nota;
- quantidade de avaliações com comentário.

Você deverá decidir quais métricas fazem sentido.

---

# 19. Etapa 13 — Análises de negócio

Depois do processamento, produza algumas conclusões baseadas nos dados.

Por exemplo:

- Qual categoria possui maior volume de vendas?
- Qual estado possui mais pedidos?
- Qual é o ticket médio?
- Qual é a distribuição das avaliações?
- Produtos mais vendidos possuem melhores avaliações?
- Existe diferença relevante entre estados?
- Quanto o frete representa em relação ao preço dos produtos?
- Qual período teve maior volume de pedidos?

Não é necessário responder todas essas perguntas.

Escolha um conjunto que seja suficiente para demonstrar que você sabe trabalhar com os dados.

---

# 20. Etapa 14 — TXT

O projeto deverá produzir pelo menos um arquivo `.txt`.

Por exemplo:

```text
data/processed/data_quality_report.txt
```

Esse arquivo poderá conter:

```text
RELATÓRIO DE QUALIDADE DOS DADOS

Total de pedidos: ...
Pedidos inválidos: ...
Valores ausentes: ...
Duplicatas: ...

...
```

O formato e o conteúdo exatos ficam por sua conta.

---

# 21. Etapa 15 — JSON

O projeto deverá produzir pelo menos um arquivo `.json`.

Por exemplo:

```text
data/processed/summary.json
```

Ele deverá conter resultados estruturados do processamento.

Exemplo conceitual:

```json
{
    "total_orders": 0,
    "average_order_value": 0,
    "top_categories": [],
    "orders_by_state": {}
}
```

Os campos reais deverão ser definidos por você.

---

# 22. Etapa 16 — CSV

O projeto deverá produzir pelo menos um CSV processado.

Exemplo:

```text
data/processed/orders_processed.csv
```

Esse arquivo deverá representar uma versão tratada dos dados.

Você deverá decidir:

- quais campos manter;
- quais campos transformar;
- quais campos derivados criar;
- qual será a estrutura final.

---

# 23. Resultado esperado

Ao executar o projeto, o fluxo deverá ser aproximadamente:

```text
data/raw/
    ↓
leitura
    ↓
validação
    ↓
limpeza
    ↓
transformação
    ↓
relacionamento
    ↓
análise
    ↓
data/processed/
```

O resultado final deverá conter dados processados e relatórios que possam ser utilizados posteriormente.

---

# 24. O que NÃO entra neste projeto

De propósito:

- SQL
- banco de dados
- API
- pandas
- NumPy
- Spark
- Docker
- cloud
- asyncio
- threading
- OOP obrigatória
- arquitetura complexa

Esses assuntos ficam para projetos posteriores.

---

# 25. Organização do código

A estrutura inicial será simples:

```text
project/
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│
└── README.md
```

**Não será fornecida uma arquitetura pronta para `src/`.**

Conforme o projeto crescer, você deverá decidir quando separar responsabilidades.

Se, por exemplo, seu arquivo principal começar a ficar enorme, esse será um problema para você resolver.

---

# 26. Critério de conclusão

O projeto estará concluído quando você conseguir:

- [ ] Ler os arquivos sem pandas.
- [ ] Trabalhar com CSV.
- [ ] Trabalhar com JSON.
- [ ] Trabalhar com TXT.
- [ ] Trabalhar com delimitadores.
- [ ] Trabalhar com encoding/decoding.
- [ ] Entender UTF-8 e Unicode.
- [ ] Manipular listas de dicionários.
- [ ] Filtrar dados.
- [ ] Ordenar dados.
- [ ] Transformar dados.
- [ ] Agregar dados.
- [ ] Contar ocorrências.
- [ ] Detectar e tratar duplicatas.
- [ ] Tratar valores ausentes.
- [ ] Relacionar diferentes arquivos.
- [ ] Utilizar regex em um problema real.
- [ ] Gerar dados processados.
- [ ] Gerar um relatório TXT.
- [ ] Gerar um resumo JSON.
- [ ] Gerar pelo menos um CSV processado.
- [ ] Documentar as principais decisões tomadas durante o processamento.

---

# 27. Próximo projeto

Depois deste projeto, o próximo será deliberadamente mais próximo de uma pipeline de Engenharia de Dados:

```text
API
 ↓
JSON
 ↓
Python
 ↓
transformação
 ↓
SQL
 ↓
banco de dados
 ↓
consultas
```

Depois podemos evoluir para tecnologias como:

```text
Docker
orquestração
cloud
ETL/ELT
```

Mas **não antecipar essas tecnologias agora**.

O objetivo deste projeto é dominar a matéria-prima:

> **dados + arquivos + Python + transformação.**
