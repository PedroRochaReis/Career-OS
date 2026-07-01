# Guia para Documentar uma Experiência Profissional

> Objetivo: registrar uma experiência profissional de forma completa.
>
> Não se preocupe com texto bonito ou linguagem de currículo. Escreva tudo o que lembrar. Depois esse material poderá ser transformado em currículo, LinkedIn, respostas STAR, entrevistas e portfólio.
>
> Nem todas as perguntas precisam ser respondidas.

---

# 1. Contexto da empresa

## Sobre a empresa

- Qual era a empresa?
Grupo Fleury
- Em qual setor ela atuava?
Pricing
- Qual era o tamanho da empresa?
Grande vale por volta de uns 8.5 bilhões de reais
- Startup, Scale-up, Big Tech, Consultoria ou empresa tradicional?
empresa tradicional
- Como a empresa ganhava dinheiro?
No setor que eutrabalhava a empresa ganhava dinheiro vendendo analise de exames para laboratorios terceiros, ou seja um laboratorio coletava o que seria analisado, sangue, urina, fezes, mandava para fleury/pardini e os laboratorios analisavam e devolviam os resultado do exame, ganhavamos dinheiro por exame processado

## Seu time

- Qual era sua área?
Trabalhava com ciencia de dados
- Para quem você respondia?
time de princing B2B da pardini
- Existiam outros times envolvidos?
Existia o time de vendas que trabalhavamos juntos para forneçer os leads de vendas
- Aproximadamente quantas pessoas havia no time?
6 pessoas no time

---

# 2. Seu cargo

## Informações básicas

Cargo:Estagiario

Período:jan/2024 - dez/2024

Modelo de trabalho:hibrido


## Seu papel

Explique, com suas palavras, qual era sua principal responsabilidade.
Eu entrei e pensando aqui nunca houve algo como uma responsabilidade ou missão que eu entrei ou sabiam o que eu ia fazer, o que é engraçado, mas o que eu acabei fazendo, depois de conversar com o gestor senior o que planejamos foi que eu estaria mais focado em uma parte de analise e ciencia de dados para a area de princing do B2B pardini de venda de exames médicos, já que o gestor sabia que eu manjava disso e tudo mais 
Se alguém perguntasse "o que você fazia?", como responderia?
Eu analisava as bases de consumo/compra de serviços de analises de exames do setor B2B do pardini da empresas terceiras que compravam com a analise de exames conosco

---

# 3. O produto, serviço ou processo

O que exatamente você ajudava a construir ou operar?
Eu colocaria como um serviço interno em que nos analisavamos, identificavamos padrões e encontravamos clientes que eram possiveis Leads comerciais para um tipo expecifico de exame que vendemos para o time comercial atuar sobre


### Quem utilizava?
Time comercial de vendas B2B

### Qual problema era resolvido?

Explique o problema de negócio.
Antes o time cormercial apenas olhava por cima e usando muito mais a intuição para saber quais exames deveria tentar vender para os cliente, sem nenhum tipo de analise ou suporte por traz para ajudalos, depois do projeto eles tinham na plataforma de CRM deles descrições com de qual exame poderia vender e a volumetria que aquele exame tem potencial de vender

---

# 4. Seu escopo

Descreva o ambiente onde você trabalhava.
Eu era quase que o unico no time analitico para esse trabalho, o analista senior me ajudava com comunição com o time comercial e o fetch de dados do banco que eu não tinha acesso, foi um ambiente bem dificil no começo pois quanto eu entre tinhamos apenas 1 gestor senior que não tinha muito tempo livre para a gente e um gerente que foi demitido logo depois, então o time de pricing concistia, por um tempo, de mim e um analista senior apenas, sem liderança direta, então pensar que consegui trazer um trabalho novo como produto nesse ambiente foi bem relevante, já que era minha primeira experiencia de trabalho e eu estava bem sem orientação, apenas 1 ou 2 horas por semana que conseguia com meu gestor senior, no maximo, mas ainda sim eu gostava muito do pessoal do time, foi um pessoal que ganhei muita afinidade bem rapido

---

# 5. Suas responsabilidades

Marque tudo que fazia.

## Estratégia

- Discovery -check
- Estratégia de produto -check

## Execução

- Desenvolvimento -check
- Programação -check
- Modelagem -check
- Análise de dados -check
- Escrita de documentação -check

## Qualidade

- Testes -check

---

# 6. Tecnologias, ferramentas e metodologias

Liste tudo que utilizava.

Linguagens:Python e SQL

Ferramentas:DataBricks

AI:Tesseract(biblioteca de OCR python)

Banco de dados:SQLServer

---

# 7. Principais iniciativas

Liste absolutamente tudo que você entregou.

Não filtre.

Exemplos:

- Projeto
- Feature
- Plataforma
- Dashboard
- API
- Automação
- Processo
- Migração
- Modelo estatístico
- Pipeline
- Arquitetura
- Integração
- MVP
- Produto
- Sistema
- Ferramenta interna

Para cada iniciativa, responda:

## Nome
Projeto de Leads para time de vendas
## Qual era o problema?
O time comercial de vendas B2B do pardini não tinha suporte de inteligencia sobre as vendas e nem clientes que tinham, ele apenas usavam algumas planilhas e consultavam o que os cliente consumiam, e por intuição e experiencia decidiam o que esse cliente poderia comprar e tentava vender para eles, a falta de suporte de inteligencia fazia a operação ser extremamente baseada em experiencia e mesmo os mais experientes poderiam acabar passando por oportunidades sem saber
## O que foi feito?
Criei um analise do consumo historico de todos os exames de todos os cliente para encontrar pares de exames com alta correlação, existiam uma grande quantidade de exames que tinham o costume de andar juntos por serem, geralmente, requisitados juntos, exemplo seria analise de Sodio e analise de potassio no sangue, eram dois exames diferentes que eram pedidos comumente juntos, analisando mais de 5000 exames diferentes encontramos varios pares de exames que poderiam estar sendo vendido para nossos cliente mas por algum motivo não tinham consumo ou eram pouco consumido de acordo com a metrificação que fiz, todos esses exames entravam em uma analise de regressão linear para aferir quantos exames existe em potencial para vender para dado cliente e nos informavamos o time de vendas pela plataforma de CRM como Leads especificos para eles analisarem e tratarem

## Qual foi sua participação?
Eu fiz toda a parte de analise e teste desses dados, analsie de correlação de previsão por regressão linear

## Quem participou?
Eu e mais um analista senior, esse analista me ajduava com a comunicação com o time comercial e me dava insights de negocios que eu utilizava na minha analise

## Quais tecnologias foram utilizadas?
Majoritariamente Python para analise e SQL para o fecth dos dados na base, usei analise de correlação, PCA, regressão linear, tratamento de outliers por IQ e z score

---

# 8. Resultados

O que mudou depois das entregas?
Pela primeira vez existia um suporte de inteligencia para o time comercial do grupo fleury, a primeira campanha que fizemos com esse modelo gerou um resulta de aumento em 2 milhões anualisados na receita de venda de exames, isso comparado com nosso grupo controle que não apresentou mudanças significativas além de ter sido a abertura para um horizonte de possibilidades de produtos de inteligencia para o time de negocio dando incio a um projeto gerido pelop time de dados fora de pricing depois

---

# 9. Decisões importantes

Quais decisões relevantes você tomou?
Toda parte de analise fui eu que construi, as gerações de leads fui eu que fiz e nos então nos fomos mostrar o que encontramos para o time de comercial de regionais em uma apresentação que montei e apresentei para validarmos juntos se estava fazendo sentido as analises no qual durante a reunião conversando com o time de regional de vendas se provou bem precisa acertando em um exame expecifico que ele tinham acabado de tratar sobre um cliente que tinha apenas 50% do consumo com a gente e o restante com a concorrencia e acertamos exatamente essa previsão que poderiamos dobrar nosso faturamente com o cliente

---

# 12. Stakeholders

Com quem você trabalhava?
Trabalhava junto ao time comercial e ao timne de princing que era onde eu estava, sempre tive um relacionamento otimo com todos mas principalmente com nosso time de princing, nós nos ajudavamos em tudo sempre buscando melhorar o que tinhamos, eles contavam muito comigo e com todos os outros e sempre podemos ter momentos de descrotação conversando bastante depois de alguma reunião, nos tinhamos uma afinidade muito grande

---

# 13. Métricas

Quais métricas você acompanhava?

Principal métrica que acompanhava era sobre o desempenho das campanhas de venda e os leads que apontamos para entender se estava sendo efetivo ou não as decisões que tomamos, a principal métrica era receita incremental que geramos que em certo ponto atingiu 2 milhões de reais em uma unica campanha

---

# 15. Lições aprendidas

O que essa experiência ensinou?
Foi minha primeira experiencia profissional, aprendi bastante coisa na fleury mas em geral meu maior aprendizado foi com questão de uso de python para analise e conceitos de analise de dados mais bem estruturado na minha cabeça

---

# Resultado esperado

Ao final deste documento teremos uma descrição completa da experiência profissional.

Esse material poderá ser convertido em:

- Currículo para Big Tech
- Currículo para Startup
- LinkedIn
- Portfólio
- Respostas STAR
- Histórias para entrevistas
- Casos de liderança
- Product Sense
- Behavioral Interviews
- Banco de conquistas profissionais