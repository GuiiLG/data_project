
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

  - [X] Criar automaticamente o diretório de saída.
  - [X] Validar se o arquivo processado foi criado.
  - [ ] Conferir a quantidade de registros gravados.
  - [X] Garantir que executar duas vezes não duplica registros.
  - [X] Tratar o caso de dataset vazio.

  ### Download

  - [X] Remover o import não utilizado de `KaggleDatasetAdapter`.
  - [X] Criar uma função `main()` em `download_data.py`.
  - [X] Usar `if __name__ == "__main__":`.
  - [] Tratar erros de download com mensagens mais específicas.

  ### Testes

  - [ ] Criar testes para conversão de altura.
  - [ ] Criar testes para conversão de peso.
  - [ ] Criar testes para conversão monetária.
  - [ ] Criar testes para valores vazios.
  - [ ] Criar testes para formatos inválidos.
  - [ ] Criar teste para IDs duplicados.
  - [ ] Criar pelo menos um teste do pipeline com CSV pequeno.

  ### README

  - [X] Corrigir `cd data_projetc/` para o nome correto do diretório.
  - [X] Explicar o objetivo do projeto.
  - [X] Explicar a fonte dos dados.
  - [ ] Explicar as transformações.
  - [ ] Explicar as regras para dados inválidos.
  - [ ] Explicar as validações.
  - [ ] Explicar onde ficam os arquivos de saída.
  - [ ] Documentar o relatório de qualidade.
  - [ ] Documentar limitações conhecidas.
  - [X] Testar todos os comandos do README.

  ### Git

  - [X] Adicionar `__pycache__/` ao `.gitignore`.
  - [X] Adicionar `.venv/` ao `.gitignore`.
  - [X] Decidir se `data/` será totalmente ignorado ou se apenas os dados brutos serão ignorados.


  Corrigir duplicatas por ID — você já implementou isso em check_for_duplicates.py.
  - Criar main() no download — já está feito.
  - Corrigir o README básico, .gitignore e comandos — já estão marcados como concluídos.
  - Criar relatório de qualidade agora — deixaria para depois das correções principais.
  - Melhorar muito a documentação agora — primeiro deixaria o pipeline confiável.
  - Fazer otimizações ou adicionar bibliotecas — neste momento não são necessárias.

  As próximas tarefas que eu te daria, nesta ordem, seriam:

  1. Corrigir check_for_nulls, porque ele remove itens durante o loop.
  2. Corrigir clean_data para não quebrar com None ou valores vazios.
  3. Ajustar a ordem do pipeline: validar nulos antes de limpar.
  4. Corrigir reader para sempre retornar uma lista, mesmo quando o arquivo não existe.
  5. Usar newline="" e validar a quantidade de registros gravados.
  6. Criar testes básicos para conversões e duplicatas.
  7. Só depois criar o quality_report.json e completar o README.

  A correção de duplicatas foi um avanço real, mas ainda há um problema importante: check_for_nulls continua usando
  dataset.remove(player) dentro do for, então alguns registros inválidos podem escapar.
