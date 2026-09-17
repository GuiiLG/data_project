# ETL de FIFA 21 — Checklist de boas práticas para portfólio

## Objetivo

Construir uma pipeline ETL simples, confiável e bem documentada para usar como projeto de portfólio em candidaturas a estágio em Dados/Engenharia de Dados.

A meta não é criar uma plataforma de produção. A meta é demonstrar que você sabe:

- extrair dados;
- entender o schema;
- transformar dados com regras claras;
- validar a qualidade;
- registrar o que aconteceu;
- carregar o resultado;
- testar as partes importantes;
- documentar como executar o projeto.

---

## 1. Escopo recomendado para este projeto

Use apenas um dataset principal do FIFA 21.

O segundo dataset pode ser removido da leitura por enquanto. Ele possui outro formato e outras colunas, portanto não deve ser processado silenciosamente pela mesma lógica.

### Fluxo esperado

```text
Dataset bruto
    ↓
Leitura
    ↓
Validação estrutural
    ↓
Limpeza e transformação
    ↓
Validação do resultado
    ↓
CSV processado + relatório de qualidade
```

---

## 2. O que realmente precisa ser implementado

### 2.1. Extração

- Ler o arquivo CSV usando `csv.DictReader`.
- Usar `pathlib.Path` para os caminhos.
- Manter os dados brutos separados dos dados processados.
- Abrir arquivos CSV com `newline=""`.
- Verificar se o arquivo existe.
- Verificar se o arquivo não está vazio.
- Verificar se as colunas obrigatórias estão presentes.

Não é necessário, neste projeto, criar uma arquitetura sofisticada de ingestão ou suportar vários fornecedores de dados.

---

### 2.2. Transformação

Criar funções específicas para as transformações principais:

- altura de pés/polegadas para metros;
- peso de libras para quilogramas;
- valores monetários com `K` e `M`;
- limpeza de espaços, quebras de linha e símbolos;
- conversão de idade e outras colunas numéricas.

As funções devem:

- receber um valor;
- retornar o valor transformado;
- tratar valores vazios;
- tratar formatos inválidos de forma explícita;
- não depender de uma conversão implícita feita em outro lugar.

Exemplo de comportamento esperado:

```text
Valor válido → valor convertido
Valor vazio → None ou outro valor definido pela regra
Valor inválido → registro de erro ou rejeição
```

Documente no README qual decisão foi tomada para valores inválidos.

---

### 2.3. Validação básica de qualidade

Implemente uma etapa de validação simples, mas real.

Verifique pelo menos:

- colunas obrigatórias;
- valores nulos em campos importantes;
- tipos ou formatos esperados;
- alturas e pesos inválidos;
- valores monetários negativos, se negativos não fizerem sentido;
- IDs duplicados;
- linhas incompletas;
- quantidade de registros recebidos;
- quantidade de registros processados;
- quantidade de registros rejeitados.

No dataset atual, existe pelo menos uma duplicata de ID identificada durante a análise. O pipeline deve detectar e registrar esse tipo de problema, em vez de simplesmente ignorá-lo.

### Decisão sobre registros inválidos

Escolha e documente uma regra. Por exemplo:

- rejeitar o registro quando um campo essencial estiver inválido;
- manter o registro quando o problema estiver em um campo não essencial;
- substituir valores ausentes por `None` quando isso for apropriado;
- registrar o motivo da rejeição.

Não é necessário criar um sistema genérico para todos os tipos de erro. Basta tratar os problemas relevantes para as colunas deste dataset.

---

### 2.4. Relatório de qualidade

Gere um relatório simples em `reports/`, por exemplo:

```text
reports/quality_report.json
```

O relatório deve conter, no mínimo:

- nome do arquivo de entrada;
- data ou horário da execução;
- registros recebidos;
- registros processados;
- registros rejeitados;
- quantidade de IDs duplicados;
- quantidade de valores nulos relevantes;
- transformações realizadas;
- problemas encontrados;
- status final da execução.

O relatório pode ser JSON. Não precisa criar dashboard, sistema de observabilidade ou ferramenta externa.

---

### 2.5. Carga

- Criar automaticamente o diretório de saída.
- Gravar o CSV processado em um caminho previsível.
- Usar `csv.DictWriter`.
- Validar que o arquivo de saída foi criado.
- Conferir se a quantidade de linhas gravadas faz sentido.
- Manter o dataset original intacto.

Para este projeto, sobrescrever o arquivo processado a cada execução é suficiente. Isso também evita duplicações causadas por várias execuções.

---

### 2.6. Idempotência em nível simples

O pipeline deve produzir o mesmo resultado quando executado novamente com a mesma entrada.

Para o seu caso:

- não adicionar registros ao CSV processado indefinidamente;
- recomeçar a transformação a partir do arquivo bruto;
- escrever o resultado em um caminho determinístico;
- não modificar o dataset bruto.

Você não precisa implementar `MERGE`, particionamento, checkpoints ou cargas incrementais neste projeto.

---

### 2.7. Tratamento de erros

Trate os erros mais prováveis com mensagens úteis:

- `FileNotFoundError`;
- `UnicodeDecodeError`;
- `csv.Error`;
- `ValueError`;
- `KeyError`.

As mensagens devem indicar, quando possível:

- arquivo;
- linha;
- coluna;
- valor problemático;
- motivo do erro.

Não é necessário capturar todas as exceções indiscriminadamente. Evite simplesmente usar:

```python
except Exception:
    pass
```

Isso esconde problemas e dificulta a investigação.

---

### 2.8. Testes automatizados

Crie testes para as funções de transformação mais importantes:

- conversão de altura;
- conversão de peso;
- conversão monetária;
- valores vazios;
- formatos inválidos;
- remoção de símbolos;
- comportamento esperado para registros inválidos.

Também vale criar pelo menos um teste do pipeline usando um CSV pequeno de exemplo.

Os testes não precisam cobrir cada linha do projeto. Eles devem verificar as regras mais importantes e os casos que podem quebrar a execução.

---

### 2.9. README

Corrija os comandos para refletirem a estrutura real do projeto.

Inclua:

- descrição do projeto;
- objetivo;
- fonte dos dados;
- estrutura dos diretórios;
- como instalar as dependências;
- como executar o download;
- como executar o pipeline;
- quais transformações são realizadas;
- quais validações são executadas;
- onde ficam o CSV processado e o relatório;
- exemplos de problemas encontrados;
- limitações conhecidas.

Verifique se os comandos apontam para `scripts/` ou mova os arquivos para `src/`. Escolha uma estrutura e mantenha a documentação consistente.

Remova o import não utilizado de `KaggleDatasetAdapter`, se ele realmente não for necessário.

O download não deve acontecer automaticamente apenas porque o módulo foi importado. Organize-o em uma função `main()` protegida por:

```python
if __name__ == "__main__":
    main()
```

---

## 3. Organização sugerida

```text
fifa21-etl/
├── data/
│   ├── raw/
│   └── processed/
├── reports/
│   └── quality_report.json
├── scripts/
│   ├── download_data.py
│   └── pipeline.py
├── src/
│   ├── reader.py
│   ├── clean_data.py
│   ├── processed.py
│   └── check_for_nulls.py
├── tests/
│   ├── test_clean_data.py
│   └── test_pipeline.py
├── README.md
├── pyproject.toml
└── .gitignore
```

A estrutura pode ser diferente, desde que as responsabilidades estejam claras e os comandos do README funcionem.

---

## 4. O que não é necessário neste primeiro projeto

Não coloque como requisito de conclusão:

- processamento de múltiplos schemas;
- Pandas ou NumPy, caso a restrição do projeto continue valendo;
- Docker;
- Airflow;
- dbt;
- cloud;
- banco de dados de produção;
- cargas incrementais;
- retries automáticos;
- checkpoints;
- monitoramento em tempo real;
- dashboards de observabilidade;
- sistema genérico de validação;
- cobertura de testes de 100%;
- tratamento de todos os erros imagináveis.

Esses assuntos podem aparecer em projetos futuros. Eles não são necessários para demonstrar uma boa base de ETL em um projeto de portfólio para estágio.

---

## 5. Checklist final

### Extração

- [ ] O pipeline lê o dataset correto.
- [ ] O arquivo bruto é preservado.
- [ ] O arquivo é validado antes do processamento.
- [ ] As colunas obrigatórias são verificadas.
- [ ] Erros de leitura geram mensagens úteis.

### Transformação

- [ ] As conversões estão separadas em funções.
- [ ] Valores vazios são tratados.
- [ ] Formatos inválidos são tratados.
- [ ] As regras de transformação estão documentadas.
- [ ] A limpeza não altera desnecessariamente os dados de entrada.

### Qualidade

- [ ] Valores nulos são verificados.
- [ ] IDs duplicados são detectados.
- [ ] Valores inválidos são identificados.
- [ ] Registros rejeitados são contabilizados.
- [ ] O resultado é validado antes da carga final.

### Carga

- [ ] O diretório de saída é criado automaticamente.
- [ ] O CSV processado é gerado.
- [ ] O arquivo de saída é validado.
- [ ] Executar novamente não cria duplicatas.

### Relatório

- [ ] Existe um relatório em `reports/`.
- [ ] O relatório mostra registros recebidos.
- [ ] O relatório mostra registros processados.
- [ ] O relatório mostra registros rejeitados.
- [ ] O relatório registra problemas encontrados.
- [ ] O relatório registra as transformações principais.

### Testes e documentação

- [ ] Existem testes das conversões.
- [ ] Existem testes para valores inválidos.
- [ ] Existe pelo menos um teste do pipeline.
- [ ] O README explica como executar o projeto.
- [ ] Os comandos do README foram testados.
- [ ] O `.gitignore` exclui `__pycache__/` e arquivos que não devem ser versionados.

---

## 6. Critério de conclusão para portfólio

Considere o projeto pronto quando você conseguir responder:

1. De onde vêm os dados?
2. Qual é o schema de entrada?
3. Quais transformações são realizadas?
4. Por que cada transformação é necessária?
5. Como o pipeline identifica dados inválidos?
6. O que acontece com um registro rejeitado?
7. Quantos registros entraram e quantos saíram?
8. Como você sabe que o resultado está correto?
9. O que acontece se executar o pipeline duas vezes?
10. Como outra pessoa pode executar o projeto usando apenas o README?

Se você consegue explicar e demonstrar essas respostas, o projeto já mostra competências relevantes para uma vaga de estágio em Dados ou Engenharia de Dados.

---

## 7. Próximo passo recomendado

Não refatore tudo de uma vez.

Implemente nesta ordem:

1. escolher definitivamente o dataset principal;
2. corrigir as funções de transformação;
3. implementar a validação básica;
4. gerar o relatório de qualidade;
5. corrigir o README e o download;
6. criar os testes;
7. executar o pipeline completo e revisar os resultados.

A prioridade é transformar o protótipo em uma pipeline pequena, compreensível e verificável.