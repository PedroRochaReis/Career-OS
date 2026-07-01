1 O Produto de multas era o seguinte, na Mottu (empresa), 
Contexto
Clientes alugam/financiam nossas motos, por essas motos estarem no nome da empresa ainda toda multa de transito que os clientes recebem caem para a empresa, a area de multas era responsavel por fazer a captação, indicação e pagamento das multas que os clientes tomam, além de identificar qual o cliente que recebeu a multa e cobralo na parcela dele

Produtos que eu era responsavel:

Captação de multas:
Todas as multas que os clientes recebem precisavam ser captadas, a forma que faziamos era integrações com os sistemas da SERPRO como recebimento de eventos das multas de transito por webhooks deles, esse sistema era solido e meio que nossa unica alternativa não tem muito a mais disso, recebiamos eventos de multas, identificavamos quem erao condutor no momento e cobravamos na parcela dele a multa

Indicação e Produto NIC:
Aproximadamente 80%-90% das multas tinham necessidade de nos da empresa fazermos a indicação de real condutor infrator da multa, pois toda multa feito em um veiculo da empresa cai no nome da empresa, logo precisamos indicar o condutor que cometeu a multa para o mesmo receber os pontos na carteira, caso não o fizessemos nos Mottu recebemos uma multa de duas vezes o valor da multa original, ou seja uma multa de 130 sem ser indicada recebe uma multa de 260 no nome da mottu, que se torna prejuizo para nós
Na area tinhamos que fazer essa indicação que contemplava o envio de 2 a 8 documentos diferentes para o orgão autuador que emitiu a multa, sendo que existem mais de 630 orgão diferentes até então que multa nossa motos, de acordo com onde as motos passam, essas indicações poderiam acontecer, por email, online por sites ou enviada por correios, eram cerca de 35mil indicações por mês a serem feitas com possibilidade de perda de 8-10 milhões de reais por mes
O Produto NIC vem para os clientes que não querem receber os pontos na carteira, ao assinar o produto NIC nos não fazemos a indicação de condutor dele e em troca nos acrescentamos uam cobrança na parcela dele para lidar com o prejuizo que iremos arcar, esse produto gerava em torno de 500mil a 1 milhão de reais por mes de receita após pagamento das multas que recebemos por não indicação

Multas méxico:
Eu era responsavel pelo controle completo das multas do méxico que era captação, cobrança do cliente e pagamento não ha indicação no mexico

Validação de CNH:
Responsavel pelo sistema de validação de CNHs dos clientes do Brasil, o sistema recebia uma CNH digital ou um foto da fisica e tinha como responsabilidade verificar se a CNH era valida ou era uma possivel fraude esse sistema era responsavel por impedir praticamente 100% das tentativas de fraude por documento enviadas pelos possiveis clientes

Usuarios:
Para todos os 4 produtos nossa base de clientes era 100% dos clientes da Mottu, todos eles deviram passar pela validação de documento e todos eles passariam pelo setor de multas se tomassem alguma multa em algum momento, apra indicação tinhamos mais o fator orgão publico que deveriam sempre estar condizentes as necessidades que ele requisitavam

Problema que resolvia já esta na definição do produto

Eram todos produtos internos e externos ao mesmo tempo, interno pois eram areas regulatorias que a empresa tinha que ter se não a empresa teria prejuizo mas externos tambem pois todas tinham relação direta com os clientes 

2-Eu era PM de um Squad sim eu tinha um time de 
1 operacional  
1 estagiario  
3 desenvolvedores  
1 Tech Lead  
6 pessoas no total

3-Minhas responsabilidade eram todas
Fazia discovery e teste de novas possibilidades e tecnologias para implantarmos, realizava MVPs simples com scripts e plataformas de low-code e no-code, fazia validação e testes do que estava sendo implementado, criava as USs dos desenvolvedores e fazia a gestão de prioridade deles do Backlog, fazia as analises para ver como o produto esta andando se esta correto a que deveria estar acontecendo, criava os KPIs e acompanhamentos diarios e semanais da nossa performace, fazia analise do PNL da area, definição de OKRs, refinamento técnico, gestão da operação e até desenvolvia codigo eu mesmo mudando algumas regras de negocio, fazer minor fixes e melhorias não que eu encontrava ou arrumando o que estava errado

4-Projetos (Não são todos necessariamente projetos mas foram o que me dediquei)
Melhora nos dashboards e acompanhamento de KPIs
Pré minha entrada a area sempre começava a semana com 80-90% das multas da semana indicadas e tinha que correr para não perder o prazo de muitas muitas que ainda estavam por indicar, e chegava no maximo a 94% de indicação na semana, apos a minha entrada conseguimos não só começar a semana com 99% com maximo historico de 99,1% de indicação, nos tinhamos as proximas duas semana para frente já em ~98,5% já criando maior responsabilidade, melhor cenario apra lidar com mudanças de orgãos e mais tempo para lidar com erros de sistema esse salto de 94% para 99% equivalia a um prevensão de exposição de mais 500mil reais por mês que seriam perdidos, além de agir com mais responsabilidade e mais precisão os outros 8-10milhoes em multas, isso tudo foi resultado de melhoras no sistema, resolver problemas de sistema na causa raiz, melhorar acompanhamento de dashboard, explorar dados com mais profundidade e melhora de sistema 

Multas méxico:
O sistema de mutlas méxico estava completamente parado a alguns meses, estava ruim não funcionava e minha lider me pediu para lidar com isso, em cerca de 2 semana consegui resolver por completo, 1 semana entendi o problema, estudei formas de captação de multas e plataforma e durante a 1 e 2 semana desenvolvi um MVP que por meio de um crawler e um fluxo no N8N fazi toda a captação de mutlas do méxico, identificação de clietne e cobraça na aprcela da multa que o mesmo havia recebido, nesse projeto durante a 3 semana em que agora estava rodando fizemos a captação de 4 milhões de pesos em multas e cobrança dos usuarios e agora um sistema que roda automaticamente que estava parado a meses concluido em 3 semanas, a velocidade foi enorme

Fluxo de pagamentos de multas méxico:
Com a captação rodando por motivos de problemas por plataforma do méxico mesmo as multas eram pagas de forma manual pelo operacionais do mexico, trabalhei com eles para alinhar um fluxo de pagamento de multas gerido por cards no pipefy com envio de multa que deve ser paga, pagamento pelo lado deles, anexo de comprovante, sistema automatico de faturamento de pagamento npara o méxico e depois cadastro de pagamento no nosso sistema

fluxo de comunicação com o cliente sobre CNHs:
Tinhamos um problema que era grande quantidade de CNHs enviadas por fotos do documento fisico, e por motivos regulatorio de multas era preferivel que a CNH fosse digital e estivesse valida, não vencida,
criei um fluxo de comunicação automatico para todos os clientes que tinham cnh como foto fisca e cnh vencida para melhorar nosso numeros e facilitar nosso trabalho operacional, saimos de cerca de 75% de cnhs digitais para 90% e saimos de 5,2% de CNHs vencidas para 1,7%, essas melhoras ajudavam principalmente o fluxo de indicação

Criação com desenvolvedores nova arquitetura de indicação orientada a eventos, ao invez de exigir alguem olahndo a arquitetura conteria todas as regras de negocio para fluir sozinho sem trabalho manual

Melhora no fluxo de validação de documentação:
Tinhamos um problema enorme que era validação de documentação para possibilidade de indicação da multa do cliente, essa validação era morosa e pelo fato de estarmos crescendo rapidamente começamos a ter muuuuitos documentos para serem validados, criamos um sistema de validação automatico de que conseguia validar 99% dos documentos digitais automaticamente sem necessidade de intervenção humana ou seja reduzimos o trabalho operacional em 90% e antes que precisamaos de um operacional apenas para isso precimos de apenas 20 minutos por dia, para essa validação usamos 3 AIs (YOLO, Flux, ESGARN) diferentes e um sistema de validação matematico para automatizar o processo totalmente

Criamos um sistema de comunicação com o cliente sobre multas indevidas não causadas por ele e sido causadas por possivel clonagem de placa ou erro do governo, esse sistema contemplava um chatbot que verificava a validade de recurso da multa sob o criterio de multa indevida, orienta o cliente a como abrir recurso e o fornece documentos como ping do gps no momento da multa e local da multa para ajudar no recurso da multa

Fiz a migração de três sistemas, indicação, documentos (CNHs) e multas méxico da nossa antiga arquitetura em monolito para a nova arquitetura de micro-serviços com auxilio dos desenvolvedores



O Projeto mais dificil foi o de migrar o sistema de indicação do monolito para o micro-serviço transformando em um fluxo baseado em eventos 

Foi dificil pois era um sistema muito delicado que erros pequenos causavam perdas nas casas de centenas de milhares de reais o maior dos pilares da area de multas, então tudo precisava ser feito com extremo cuidado, testado diversas vezes, checvado e re-checado, acompanhando e cruzando dados de ambos os bancos antigo e novo para validar continuamente se estava indo tudo certo

As decisão e construção total da arquitetura foram feitas por mim em conjunto com o Tech Lead da area, todas as USs foram feitas por mim algumas mais complexas refinadas pelo Tech Lead, a forma que abordamos foi traduzir tudo que tinhamos em um sistema baseado em eventos de forma que pontos criticos que podessem acontecer erros fossem feitos de forma a observalidade fosse facil para termos controle completo do fluxo

temos um sistema muito mais solido que a arquitetura baseada em eventos agora pode mostra para nos exatamente onde cada multa está no fluxo identificando rapidamente se existem problemas travando multas no caminho como por exemplo em checagens de documentos que era em geral 90% das falhas que precisava de mão humana olhando consistentemente para tratar dos erros agora o sistema já mostra todos os problemas e podemos atacalos com muito mais eficiencia