# Projeto 2 — Data Processing Pipeline

## Objetivo

Construir, usando **Python sem pandas**, um pequeno pipeline capaz de pegar dados reais de diferentes arquivos, **ler, validar, limpar, transformar, analisar e gerar novos dados**.

A ideia não é construir um sistema para um usuário. É construir um **processamento de dados**.

```text
dados brutos → pipeline → dados tratados → análise
```

---

## 1. Fonte dos dados

Utilizar **dados reais**, preferencialmente do Kaggle ou outra fonte pública.

O projeto deverá trabalhar com **mais de um arquivo/fonte**, para que exista algum relacionamento entre os dados.

Estrutura conceitual:

```text
data/
├── raw/
│   ├── ...
│   ├── ...
│   └── ...
│
└── processed/
    ├── ...
    └── ...
```

A escolha específica do dataset será feita separadamente.

---

## 2. Regra principal

### NÃO usar pandas.

Também não utilizar uma biblioteca externa para resolver automaticamente cada problema.

Pode utilizar a biblioteca padrão do Python, por exemplo:

- `csv`
- `json`
- `re`
- `pathlib`
- `collections`

A ideia é conseguir trabalhar diretamente com os dados usando Python.

A estrutura principal de manipulação deverá envolver **listas de dicionários**.

Exemplo conceitual:

```python
[
    {"id": 1, "name": "...", "value": "..."},
    {"id": 2, "name": "...", "value": "..."},
]
```

---

## 3. Etapa 1 — Ingestão

O programa deverá conseguir ler os arquivos fornecidos.

Trabalhar com pelo menos:

- CSV
- JSON
- TXT

Durante a leitura, identificar e lidar com:

- delimitador utilizado;
- encoding;
- estrutura dos dados;
- campos existentes;
- possíveis problemas de leitura.

Os dados deverão ser convertidos para estruturas Python apropriadas.

---

## 4. Etapa 2 — Validação

Antes de limpar os dados, o programa deverá identificar registros problemáticos.

Exemplos:

- registros incompletos;
- valores ausentes;
- tipos incorretos;
- IDs inválidos;
- registros duplicados;
- valores impossíveis;
- relacionamentos que não podem ser encontrados.

### Regra

Não simplesmente apagar um dado problemático sem saber por quê.

Você deverá decidir o que fazer com cada tipo de problema:

- corrigir;
- descartar;
- marcar como inválido;
- atribuir um valor padrão;
- ou outra estratégia justificável.

---

## 5. Etapa 3 — Limpeza

Trabalhar com problemas reais encontrados nos dados.

### Strings

Normalizar, quando necessário:

- espaços;
- maiúsculas/minúsculas;
- caracteres;
- nomes;
- categorias;
- outros campos textuais.

### Valores ausentes

Estabelecer regras para diferentes tipos de campos.

Por exemplo:

```text
campo obrigatório → registro inválido
campo opcional → valor padrão
```

As regras específicas deverão ser definidas por você de acordo com os dados.

### Duplicatas

Detectar e remover duplicatas de acordo com um critério lógico.

Não utilizar simplesmente `set()` em registros completos.

Pense:

> O que faz dois registros serem considerados duplicados?

---

## 6. Etapa 4 — Transformação

Transformar os dados brutos em uma estrutura consistente.

Exemplos possíveis:

```text
"  São Paulo "
        ↓
"São Paulo"
```

```text
"R$ 1.299,90"
        ↓
1299.90
```

```text
"21"
        ↓
21
```

Também podem existir transformações de:

- datas;
- categorias;
- identificadores;
- valores numéricos;
- strings;
- outros campos.

Praticar principalmente:

- funções;
- listas;
- dicionários;
- list comprehensions;
- `map`;
- strings.

Evitar criar expressões excessivamente complexas apenas para reduzir o número de linhas.

---

## 7. Etapa 5 — Regex

Regex não deverá ser utilizada apenas como exercício isolado.

Ela deverá resolver problemas reais encontrados nos dados.

Utilizar:

```python
import re
```

Praticar:

- busca de padrões;
- extração de dados;
- validação;
- grupos;
- classes;
- quantificadores.

Exemplo conceitual:

```text
"Cliente: João - Tel: (79) 99999-9999"
```

poderia exigir a extração de:

```text
nome
telefone
```

O problema real deverá ser determinado pelo dataset.

---

## 8. Etapa 6 — Relacionamento entre dados

Os arquivos deverão possuir algum relacionamento entre seus registros.

Exemplo:

```text
clientes
vendas
produtos
```

Você deverá descobrir como relacionar esses dados.

Perguntas importantes:

- Como relacionar uma venda a um cliente?
- Como relacionar uma venda a um produto?
- O que fazer quando um ID não existe?
- É melhor procurar diretamente na lista ou criar alguma estrutura auxiliar?

Você deverá decidir a melhor abordagem.

---

## 9. Etapa 7 — Agregação e análise

Depois da limpeza, o programa deverá produzir informações úteis.

Exemplos:

- quantidade de registros;
- quantidade por categoria;
- soma;
- média;
- mínimo;
- máximo;
- ranking;
- agrupamentos;
- métricas relacionadas aos dados.

O objetivo é transformar:

```text
dados
```

em:

```text
informação
```

---

## 10. Etapa 8 — Ordenação e filtros

Gerar diferentes visões dos dados.

Exemplos:

- maiores valores;
- menores valores;
- registros de determinada categoria;
- registros acima de determinado valor;
- ranking por quantidade;
- outros filtros relevantes.

Praticar:

- `sorted()`;
- `key=`;
- `lambda`;
- filtragem;
- compreensão das estruturas de dados.

O foco não é apenas saber usar `sorted()`, mas entender **qual critério está sendo aplicado aos dados**.

---

## 11. Etapa 9 — Exportação

Depois de processar os dados, gerar novos arquivos.

Exemplo:

```text
data/
├── raw/
│
└── processed/
    ├── cleaned_data.csv
    ├── summary.json
    └── invalid_records.txt
```

Praticar novamente:

- serialização;
- CSV;
- JSON;
- TXT;
- encoding;
- delimitadores.

### Regra importante

**Não modificar os dados originais.**

O fluxo deve ser conceitualmente:

```text
RAW
 ↓
PROCESSING
 ↓
PROCESSED
```

---

## 12. Organização do projeto

A estrutura inicial pode ser simples:

```text
project/
├── data/
├── src/
└── README.md
```

A estrutura final **não será fornecida antecipadamente**.

Conforme o código crescer, você deverá perceber quando é necessário separar responsabilidades.

Por exemplo, se um único arquivo começar a concentrar muitas responsabilidades, esse será um momento para pensar em refatoração.

O objetivo é que você tome as decisões de arquitetura conforme os problemas aparecem.

---

## 13. O que NÃO entra neste projeto

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
- arquitetura complexa
- OOP obrigatória

Esses assuntos ficarão para projetos posteriores.

---

## 14. O que você deverá aprender

Ao terminar, você deverá conseguir olhar para:

```text
CSV
JSON
TXT
```

e pensar:

> Consigo pegar isso, transformar em estruturas Python, limpar, validar, relacionar, transformar, agregar e devolver dados úteis.

Esse é o objetivo principal deste projeto.

---

## Progressão dos projetos

```text
PROJETO 1 — Biblioteca
Python + OOP + arquivos
        ↓
PROJETO 2 — Data Processing
Python + CSV/JSON/TXT
+ estruturas de dados
+ limpeza + transformação + regex
        ↓
PROJETO 3 — Data Pipeline
API + Python + SQL + banco de dados
+ ETL/ELT
        ↓
PROJETO DE PORTFÓLIO
Pipeline mais completo
+ Docker + cloud/orquestração etc.
```

Este segundo projeto é um **laboratório de manipulação de dados**.

Não é necessário deixá-lo com aparência de sistema comercial ou transformá-lo em um projeto de portfólio.

O foco é aprender a trabalhar com dados de forma sólida antes de adicionar banco de dados, APIs e outras tecnologias.
