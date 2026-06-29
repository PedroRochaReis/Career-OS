# Experiência: Estagiário de Data Science — Grupo Fleury (Pricing B2B Pardini)

## Overview

Atuação como estagiário de Data Science no time de Pricing B2B do Grupo Fleury, responsável por criar uma solução analítica para gerar leads e apoiar o time comercial regional na venda de exames laboratoriais a clientes terceirizados.

---

## Business Context

- Empresa: Grupo Fleury (área de Pricing / prestação de serviços de análises laboratoriais)
- Indústria: Saúde / Diagnósticos laboratoriais
- Produto/serviço: Serviços de análise de exames (processamento e análise laboratorial para laboratórios terceiros)
- Clientes: Laboratórios terceiros que contratavam o Fleury/Pardini para processamento de exames
- Modelo de receita: Cobrança por exame processado
- Regulatório/operacional: Operação tradicional em grande empresa; trabalho atrelado a bases de consumo de exames e integração com times comerciais e de dados existentes

---

## Team

- Área: Ciência de Dados no time de Pricing B2B (Pardini)
- Tamanho aproximado do time: 6 pessoas (no escopo do time de pricing havia 6, mas a equipe analítica direta era muito reduzida durante parte do período)
- Reporting: Respondia ao gestor sênior do time de pricing
- Estrutura e contexto: Durante o período houve instabilidade de liderança (gerente demitido), o time analítico ficou reduzido a um analista sênior e o estagiário, com supervisão limitada do gestor sênior
- Parceiros cross-funcionais: Time comercial/regional de vendas, área de dados responsável pelo fetch de dados

---

## Responsabilidades

- Propriedade analítica e execução: condução completa das análises estatísticas e modelos de previsão usados para gerar leads para o time comercial B2B.
- Coleta e preparação de dados (com apoio do analista sênior quando necessário para acesso ao banco).
- Desenvolvimento de pipelines analíticos (exploração, correlação, tratamento de outliers, modelagem por regressão linear, PCA quando aplicável).
- Documentação e comunicação dos resultados para o time comercial e apresentação para validação regional.
- Testes e validação de hipóteses e campanhas comerciais (controle vs campanha).

Observação: não houve uma missão formal definida ao ingressar; as responsabilidades foram negociadas com o gestor sênior e foram atribuídas ao estagiário conforme confiança técnica.

---

## Product Portfolio

Produto principal (interno): Serviço analítico de geração de Leads para vendas B2B

- Propósito: identificar exames com potencial de aumento de vendas e clientes prospectáveis para o time comercial regional
- Usuários: Time comercial de vendas B2B (regionais)
- Impacto de negócio: suporte inteligente a campanhas comerciais, redução de decisões baseadas apenas em intuição
- Características técnicas: pipelines em Python, queries SQL para SQL Server, execução em DataBricks; uso de técnicas estatísticas (correlação, PCA, regressão linear, tratamento de outliers)
- Stakeholders: Time de Pricing, analista sênior, equipes regionais de vendas, times de dados (para extração)
- Dependências: acesso aos dados do SQL Server, CRM da equipe de vendas para entrega dos leads
- KPIs: receita incremental gerada pela campanha de leads, quantidade/qualidade de leads, performance de conversão das campanhas

---

## Major Initiatives

### Projeto de Leads para time de vendas

#### Contexto

O time comercial B2B do Pardini não possuía suporte analítico estruturado para identificar quais exames deveriam ser ofertados a cada cliente; as decisões eram majoritariamente intuitivas e baseadas em planilhas simples.

#### Problema

Falta de inteligência comercial estruturada que gerasse indicações de exames com potencial de venda por cliente; oportunidades eram perdidas por ausência de análise granular.

#### Constraints (Restrições)

- Equipe analítica reduzida (estagiário + analista sênior) com supervisão limitada do gestor
- Acesso restrito a dados (fetchs realizados pelo analista sênior/DBA em alguns momentos)
- Tempo de gestor sênior limitado (1-2 horas semanais disponíveis para orientação)

#### Alternativas consideradas

Não especificadas no documento bruto.

#### Solution (Solução implementada)

- Análise do consumo histórico de exames por cliente para identificar pares de exames com alta correlação (ex.: sódio e potássio)
- Mapeamento de exames que costumam ocorrer juntos e identificação de pares/exames com potencial não realizado em cada cliente
- Modelagem por regressão linear para estimar o potencial incremental de exames a vender para cada cliente
- Tratamento de outliers por IQR e Z-score; uso de PCA e análise de correlação para redução de dimensionalidade e melhoria das features de entrada
- Geração de listas de leads específicas e entrega ao time comercial via CRM (leads com descrição dos exames e volumetria potencial)

#### Meu papel

- Condução integral da análise e dos testes de dados: exploração, correlação, engenharia de features, aplicação de PCA, regressão linear, tratamento de outliers
- Preparação dos artefatos para apresentação e validação com o time comercial regional

#### Tecnologias

- Python (análise, modeling)
- SQL (SQL Server) para extração de dados
- DataBricks como ambiente de execução
- Tesseract (OCR) — citado como tecnologia usada pelo time/na stack

#### Stakeholders

- Eu (estagiário), analista sênior (apoio em comunicação com comercial e fetch de dados), time comercial regional, gestor sênior de pricing

#### Decisions made

- Escolha de técnicas estatísticas e modelos (correlação, PCA, regressão linear); decisão de tratar outliers por IQR e Z-score
- Entrega do output como leads estruturados para CRM do time de vendas

#### Risks

- Risco de baixa adoção pelo time comercial caso as predições não se mostrassem precisas
- Risco operacional por limitações de qualidade/acesso aos dados

#### Trade-offs

- Simplicidade vs. precisão: uso de modelos lineares e técnicas estatísticas interpretáveis em vez de modelos mais complexos que exigiriam mais dados/tempo de validação

#### Metrics

- Receita incremental gerada pela primeira campanha: R$ 2.000.000 (anualizados) atribuída à campanha com o modelo de leads
- Métricas operacionais acompanhadas: performance das campanhas, conversão dos leads, receita incremental por campanha

#### Outcome

- Implementação do primeiro suporte analítico ao time comercial: campanha inicial com resultado de ~R$ 2 milhões anualizados em receita incremental
- Validação qualitativa com equipes regionais (acerto de previsão em cliente com 50% de consumo com Fleury vs concorrência)
- Geração de interesse para expansão do trabalho de inteligência comercial dentro do grupo de dados além do escopo de pricing

#### Lessons Learned (da iniciativa)

- Mesmo com supervisão limitada e equipe reduzida é possível criar impacto significativo com análises bem focadas
- A validação direta com comerciais regionais é crítica para calibrar hipóteses e ganhar confiança operacional

---

## Technical Decisions

- Uso de análises de correlação para identificar pares de exames que ocorrem conjuntamente
- Aplicação de PCA para redução de dimensionalidade quando necessário
- Modelagem por regressão linear para estimativa do potencial incremental por cliente
- Tratamento de outliers por IQR e Z-score

Observação: o documento bruto descreve as técnicas aplicadas, mas não registra comparações detalhadas com alternativas mais complexas.

---

## Product Decisions

- Entregar o resultado como leads acionáveis no CRM do time comercial (formato operacional escolhido para maximizar adoção)
- Priorizar modelos interpretáveis e pipelines reprodutíveis para facilitar a comunicação com negócios

---

## Leadership

- Influência: condução autônoma de um projeto com pouca orientação, negociação com gestor sênior para definir escopo e priorização
- Comunicação: apresentação dos resultados para times regionais de vendas para validação e alinhamento
- Mentoria: trabalho próximo com analista sênior que atuou como principal apoio em comunicação e acesso a dados

---

## Operations

- Responsabilidades operacionais: execução de pipelines analíticos, teste de campanhas, acompanhamento de métricas de campanha (conversão, receita incremental)
- Dashboards/monitoramento: o documento bruto menciona acompanhamento de desempenho das campanhas, sem detalhar ferramentas específicas de dashboard
- SLAs/Incident: não relatados no documento bruto

---

## Metrics

- Receita incremental da campanha piloto: R$ 2.000.000 (anualizados)
- Métricas acompanhadas: performance das campanhas, conversão dos leads, qualidade dos leads

---

## Technologies

- Linguagens: Python, SQL
- Frameworks/ambiente: DataBricks
- Banco de dados: SQL Server
- AI/Tools: Tesseract (OCR) citado
- Técnicas/arquitetura: Correlação, PCA, Regressão Linear, tratamento de outliers (IQR, Z-score)

---

## Skills Demonstrated

- Technical Skills: Python, SQL, análise estatística, modelagem (regressão), tratamento de dados, uso de DataBricks
- Product Skills: definição de problema, tradução de análise em produto acionável (leads para CRM), priorização focada em impacto
- Leadership Skills: autonomia, comunicação com stakeholders, apresentação e validação com times comerciais
- Business Skills: entendimento do processo comercial B2B, mensuração de impacto em receita
- Communication Skills: preparação e apresentação de resultados para times regionais
- Analytical Skills: exploração de dados, correlação, PCA, engenharia de features

---

## Stakeholders

- Internos: gestor sênior de pricing, analista sênior (colaborador direto), time de pricing, área de dados (para extração), times regionais de vendas
- Externos: clientes (laboratórios terceiros) — como alvos das campanhas comerciais

---

## Challenges

- Problema: trabalhar com equipe analítica reduzida e supervisão limitada
  - Por que difícil: pouca disponibilidade do gestor para orientação, gerente demitido, dependência de outro analista para fetch dos dados
  - Decisão: conduzir investigação autônoma e estruturar entregáveis acionáveis (leads) para validação rápida
  - Execução: desenvolvimento analítico end-to-end com validação direta com comerciais
  - Outcome: entregas validadas com impacto de receita

---

## Mistakes

- O documento bruto não descreve falhas técnicas explícitas. Há menção a dificuldades de organização e supervisão, mas sem relatos de falhas de projeto específicas.

---

## Lessons Learned

- Projetos analíticos focados em problemas concretos de negócios podem gerar impacto financeiro significativo mesmo com recursos limitados
- Validação direta com stakeholders de negócios é essencial para calibrar modelos e ganhar adoção
- Técnicas interpretáveis são valiosas quando o público-alvo são times comerciais que precisam entender a justificativa das recomendações
- Experiência consolidou conhecimentos práticos em Python, análise de dados e técnicas estatísticas

---

## Keywords (para ATS)

Estagiário Data Science, Pricing, B2B, Leads, Análise de Consumo, Correlação, PCA, Regressão Linear, Tratamento de Outliers, IQR, Z-score, Python, SQL, SQL Server, DataBricks, Tesseract, CRM, Inteligência Comercial, Validação com Vendas, Revenue Impact, Fleury, Pardini
