```markdown
# Atualização de Arquivo CSV com Pandas

Este repositório contém um script Python que realiza a leitura de um arquivo CSV, faz algumas transformações na data e salva um novo arquivo CSV atualizado.

## Requisitos

- Python 3.x
- Pandas

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd seu-repositorio
   ```
3. Instale as dependências necessárias:
   ```bash
   pip install pandas
   ```

## Uso

1. Coloque seu arquivo CSV no caminho especificado no script ou ajuste o caminho de acordo com suas necessidades.
2. Execute o script:
   ```bash
   python seu_script.py
   ```

## Descrição do Script

O script realiza as seguintes operações:

1. **Leitura do Arquivo CSV**:
   ```python
   df = pd.read_csv(r'V:\10 - NÉXIA\Eric\teste\indicadores_leitura_old2.csv', delimiter=";")
   ```

2. **Conversão da Coluna 'REFER' para Datetime**:
   ```python
   df['REFER'] = pd.to_datetime(df['REFER'], format='%d/%m/%Y %H:%M')
   ```

3. **Criação de uma Nova Coluna 'REFER2' no Formato AnoMês**:
   ```python
   df['REFER2'] = df['REFER'].dt.strftime('%Y%m')
   ```

4. **Salvamento do DataFrame Atualizado em um Novo Arquivo CSV**:
   ```python
   df.to_csv(r'V:\10 - NÉXIA\Eric\teste\seu_arquivo_atualizado_conferir.csv', index=False)
   ```

5. **Mensagem de Conclusão**:
   ```python
   print("Concluído")
   ```

## Contribuição

1. Faça um fork do projeto
2. Crie uma nova branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Envie para a branch (`git push origin feature/nova-funcionalidade`)
5. Crie um novo Pull Request

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
```
