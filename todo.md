
• Minha avaliação, pensando em nível estágio:

  - Projeto completo considerando tudo que falta: 4,5/10
  - O que você implementou até agora: 5,5/10

  Você já tem uma base boa: separou responsabilidades em módulos, está usando Python puro, lê CSV, transforma
  altura/peso/dinheiro, mantém raw e processed separados e criou um fluxo de pipeline. Isso já demonstra
  fundamentos importantes.

  A nota ainda não é maior porque existem problemas de confiabilidade que podem gerar resultados errados sem
  avisar.

  ### Principais problemas atuais

  1. check_for_duplicates compara a linha inteira, mas deveria verificar duplicidade pelo ID.
  2. Você remove itens da lista enquanto percorre a própria lista:

  for player in dataset:
      dataset.remove(player)

  Isso pode fazer registros serem pulados.

  3. check_for_nulls transforma "N/A" em None, mas testa o valor antigo. Portanto, alguns registros inválidos não
     são removidos.

  4. clean_data chama .strip() antes de tratar valores nulos. Se houver None, o pipeline quebra.
  5. As funções de conversão apenas imprimem erro. Elas não informam qual jogador, linha, coluna ou valor
     apresentou problema.

  6. O leitor não valida:

  - arquivo vazio;
  - colunas obrigatórias;
  - erros de encoding;
  - erros no CSV.

  7. O arquivo de saída não é validado e não usa newline="".
  8. Ainda não existe relatório de qualidade.
  9. Não existem testes automatizados.
  10. O download ainda executa automaticamente ao importar o módulo e captura Exception de forma muito ampla.

  ### O que já está feito no seu TODO

  - [x] Escolha do dataset principal.
  - [x] Separação entre dados brutos e processados.
  - [x] Leitura básica do CSV.
  - [x] Limpeza de espaços, quebras de linha e símbolos.
  - [x] Conversão de altura.
  - [x] Conversão de peso.
  - [x] Conversão de valores monetários.
  - [x] Tentativa inicial de validação de nulos.
  - [x] Tentativa inicial de detecção de duplicatas.
  - [x] Geração básica do CSV processado.
  - [x] Execução básica do pipeline.

  ### Checklist que ainda falta

  Você pode atualizar o TODO com isto:

  ### Correções de qualidade

  - [ ] Corrigir a remoção de registros inválidos sem alterar a lista durante o loop.
  - [ ] Detectar duplicatas usando o campo `ID`.
  - [ ] Corrigir o tratamento de valores `None`, vazios e `"N/A"`.
  - [ ] Fazer as funções de transformação tratarem formatos inválidos explicitamente.
  - [ ] Informar jogador, coluna e valor quando ocorrer um erro.
  - [ ] Validar o resultado depois das transformações.

  ### Leitura

  - [ ] Usar `pathlib.Path` na abertura dos arquivos.
  - [ ] Abrir CSVs usando `newline=""`.
  - [ ] Verificar se o arquivo existe.
  - [ ] Verificar se o arquivo está vazio.
  - [ ] Verificar se as colunas obrigatórias existem.
  - [ ] Tratar erros de encoding e CSV.

  ### Relatório

  - [ ] Criar `reports/quality_report.json`.
  - [ ] Registrar quantidade de registros recebidos.
  - [ ] Registrar quantidade de registros processados.
  - [ ] Registrar quantidade de registros rejeitados.
  - [ ] Registrar IDs duplicados.
  - [ ] Registrar valores nulos relevantes.
  - [ ] Registrar problemas encontrados.
  - [ ] Registrar transformações realizadas.
  - [ ] Registrar data e status da execução.

  ### Carga

  - [ ] Criar automaticamente o diretório de saída.
  - [ ] Validar se o arquivo processado foi criado.
  - [ ] Conferir a quantidade de registros gravados.
  - [ ] Garantir que executar duas vezes não duplica registros.
  - [ ] Tratar o caso de dataset vazio.

  ### Download

  - [ ] Remover o import não utilizado de `KaggleDatasetAdapter`.
  - [ ] Criar uma função `main()` em `download_data.py`.
  - [ ] Usar `if __name__ == "__main__":`.
  - [ ] Tratar erros de download com mensagens mais específicas.

  ### Testes

  - [ ] Criar testes para conversão de altura.
  - [ ] Criar testes para conversão de peso.
  - [ ] Criar testes para conversão monetária.
  - [ ] Criar testes para valores vazios.
  - [ ] Criar testes para formatos inválidos.
  - [ ] Criar teste para IDs duplicados.
  - [ ] Criar pelo menos um teste do pipeline com CSV pequeno.

  ### README

  - [ ] Corrigir `cd data_projetc/` para o nome correto do diretório.
  - [ ] Explicar o objetivo do projeto.
  - [ ] Explicar a fonte dos dados.
  - [ ] Explicar as transformações.
  - [ ] Explicar as regras para dados inválidos.
  - [ ] Explicar as validações.
  - [ ] Explicar onde ficam os arquivos de saída.
  - [ ] Documentar o relatório de qualidade.
  - [ ] Documentar limitações conhecidas.
  - [ ] Testar todos os comandos do README.

  ### Git

  - [ ] Adicionar `__pycache__/` ao `.gitignore`.
  - [ ] Adicionar `.venv/` ao `.gitignore`.
  - [ ] Decidir se `data/` será totalmente ignorado ou se apenas os dados brutos serão ignorados.