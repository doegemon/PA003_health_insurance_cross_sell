# PA003_health_insurance_cross_sell
Os objetivos desse projeto de Ciência de Dados são:

- Realizar a Análise Exploratória de Dados (EDA) de parte da base de clientes da seguradora; 
- Descobrir e demonstrar a probabilidade de um cliente adquirir um novo produto da seguradora (seguro de automóvel); e
- Tornar o modelo e a lista de clientes interessados acessível para o time de Produto/Vendas através do Google Sheets.

# 01. Problema de Negócio
A Insurance All é uma empresa que somente fornece seguro de saúde para seus clientes, e o time de produtos está analisando a possibilidade de ofertar um novo produto: seguro de automóvel.

Para tanto, foi feita uma entrevista com alguns dos clientes sobre o interesse em adquirir esse novo seguro. Assim, todos os entrevistados demonstraram interesse ou não, e essas respostas foram salvas em um banco de dados, junto com outros atributos pessoais.

Existem outros clientes que não responderam à pesquisa e, portanto, os times de produto e vendas querem oferecer o novo seguro para eles. Contudo, por questões de pessoal e orçamento, o time de vendas terá a capacidade de realizar 20.000 ligações para oferecer o novo produto. 

Assim, como Cientista de Dados da empresa, fui encarregado de organizar essa lista de clientes que não responderam à pesquisa, priorizando aqueles com maior interesse em adquirir o novo seguro de automóvel, de forma a maximizar o retorno dessa campanha de vendas. 

# 02. Resultados Financeiros
O Modelo de Machine Learning adotado ordenou a lista de clientes de modo que os primeiros 20.000 clientes abrangem aproximadamente 70% dos clientes interessados em adquirir o seguro de automóvel, representando uma performance aproximadamente 3 vezes melhor do que ligar de forma aleatória (demonstrado através da Curva de *Lift*).

# 03. Premissas de Negócio
- As variáveis/atributos originais (e seus significados) do conjunto de dados são:

|    Atributos        |                         Significado                          |
| :-----------------: | :----------------------------------------------------------: |
|id                   |identificador único do cliente|
|gender               |gênero do cliente|
|age                  |idade do cliente |
|region_code          |identificador da região do cliente|
|policy_sales_channel |código anônimo para o canal de comunicação com o cliente (ex.: por e-mail, por telefone, pessoalmente, etc.)|
|driving_license      |indica se o cliente tem ou não carteira de habilitação (0 = cliente não tem; 1 = cliente tem)|
|vehicle_age          |'idade' do veículo|
|vehicle_damage       |indica se o cliente já bateu o carro ou não no passado (0 = cliente não bateu o carro; 1 = cliente já bateu o carro)|
|previously_insured   |indica se o cliente já teve/tem seguro de carro (0 = cliente não tem/teve; 1 = cliente tem/teve)|
|annual_premium       |o valor que o cliente precisa pagar de prêmio anualmente|
|vintage              |número de dias que a pessoa é cliente da companhia|
|response             |resposta da pesquisa sobre o seguro de carro (0 = cliente não está interessado; 1 = cliente está interessado)|

# 04. Etapas do Projeto
Para conduzir o projeto, utilizei as etapas do CRISP:
1. Entender o problema de negócio apresentado pelo time de produto; 
2. Entender o modelo de negócio da Insurance All (Seguradora); 
3. Coletar os dados (*queries* no SQL); 
4. Limpeza dos dados - análise descritiva dos dados; 
5. Análise Exploratória de Dados - levantamento e validação de hipóteses; 
6. Preparação e modelagem dos dados - seleção de variáveis (*feature selection*)
7. *Machine Learning*; 
8. Avaliação dos modelos de *Machine Learning*; e
9. *Deploy* do Modelo escolhido. 

# 05. Hipóteses de Negócio
Entre as 07 hipóteses de negócio levantadas e analisadas, as 03 que considero principais foram: 
1. Clientes com veículos mais velhos tem mais interesse em adquirir o seguro do que os que possuem veículos mais novos;
2. Clientes que não tem/tiveram seguro de automóvel tem mais interesse em adquirir um do que aqueles que já tem/tiveram; e
3. Clientes com menos de 06 meses de tempo de vida com a seguradora tem mais interesse no novo produto do que aqueles que já são clientes há mais de 06 meses.

# 06. *Machine Learning*
Para fazer a Classificação e Ordenação dos clientes pela probabilidade de adquirir o novo seguro, utilizei dos seguintes algoritmos de Machine Learning: 
- *KNN*
- *Logistic Regression*
- *Extra Trees Classifier*
- *Random Forest Classifier*
- *LGBM Classifier*
- *XGBoost Classifier*

Após fazer o treinamento dos modelos sobre os dados de treino e ter feito o Cross-Validation, bem como analisar o *Precision @k*, o *Recall @k* e a *accuracy*, optei por utilizar o *LGBM Classifier*. 

Depois de realizar o *hyperparemeter fine tunning*, os resultados para um *k = 2000* foram:

|         Modelo          |  Precision @k   |  Recall @k  | Accuracy   |
| :---------------------: | :------------:  | :--------:  | :--------: |
|     LGBM Classifier     |     0.412794    |  0.087639   |  0.876663  |

# 07. Google Sheets
Demonstração da lista ordenada pela probabilidade em adquirir o novo produto através de uma planilha no Google Sheets:

![sheets](https://user-images.githubusercontent.com/97055919/208264610-ff074f26-7756-436d-b6f1-e3344e6dea0a.png)

Através do botão *Prediction*, incluído por meio de um script do próprio Google Sheets, é feita uma requisição para a API que contém o modelo, retornando a probabilidade de cada cliente em adquirir o seguro de automóvel. 

Com os valores, é só ordenar de forma decrescente e o time de vendas terá uma lista ordenada para fazer as ligações da campanha. 

# 08. Conclusões
Feita a Classificação e Ordenação dos clientes com relação à probabilidade de adquirirem o novo seguro de automóvel a ser ofertado pela seguradora, a visualização da lista ordenada através de uma planilha do Google Sheets permite que o time de vendas se organize e seja muito mais assertivo em abordar os clientes do que simplesmente ligar de forma aleatória, maximizando os retornos da campanha.  

Ainda, as hipóteses levantadas e validadas na Análise Exploratória de Dados trazem informações importantes para a tomada de decisões e forma de condução de negócios.

# 09. Próximos Passos
Em um próximo ciclo do CRISP, posso: 
- Criar novas *features* com base nas já existentes para melhorar o treinamento dos modelos; 
- Testar outros algoritmos de *Machine Learning*;
- Utilizar outra estratégia para o *Hyperparemeter Fine Tunning*; e 
- Melhorar o funcionamento do script no Google Sheets.

# Referências
- Conjunto de Dados: https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction
