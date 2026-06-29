#set page(
  paper: "a4",
  margin: (x: 15mm, y: 18mm),
)

#set text(
  font: "Segoe UI", // Usando Liberation Sans como alternativa comum
  size: 10.5pt,
  lang: "pt",
)

// Configuração de parágrafo para justificado
#set par(justify: true, leading: 0.6em)


// ------ Helper Functions ------

#let section_title(title) = {
  v(12pt, weak: true)
  block(width: 100%, stroke: (bottom: 1.2pt + black), inset: (bottom: 2pt))[
    #text(size: 12.5pt, weight: "bold")[#title]
  ]
  v(8pt, weak: true)
}

#let summary_item(content) = {
  grid(
    columns: (25pt, 1fr),
    gutter: 0pt,
    text(size: 12pt)[➢],
    content
  )
  v(4pt)
}

#let company_header(name, period) = {
  v(10pt, weak: true)
  grid(
    columns: (1fr, auto),
    text(size: 11.5pt, weight: "bold")[#upper(name)],
    text(size: 11pt, weight: "bold")[#period]
  )
}

#let job_position(title) = {
  v(4pt)
  h(12pt)
  text(size: 10pt, weight: "bold")[
    #text(size: 11pt, weight: "regular")[○] #h(4pt) #upper(title)
  ]
  v(2pt)
}

#let bullet_item(content) = {
  grid(
    columns: (25pt, 1fr),
    gutter: 0pt,
    h(12pt) + text(size: 10pt)[▪],
    content
  )
  v(2pt)
}

#let edu_item(sym, content) = {
  grid(
    columns: (25pt, 1fr),
    gutter: 0pt,
    text(size: 12pt)[#sym],
    content
  )
  v(4pt)
}


// ------ Profile ------
#import "../Profiles/profile.typ": profile
#let t(x) = x.at(profile.language)

// ------ Header ------

#align(center)[
  #text(size: 24pt, weight: "regular")[#profile.name]

  #v(-8pt)
  #line(length: 100%, stroke: 1.2pt + black)
  #v(-4pt)

  #text(size: 8.5pt)[
    #profile.location
    #h(4pt) • #h(4pt)
    (11) 97106-4000
    #h(4pt) • #h(4pt)
    #profile.email
    #h(4pt) • #h(4pt)
    #link(profile.linkedin_link)[#profile.linkedin_name]
  ]
]

// --- Headline ---

#v(12pt)
#align(center)[
  #text(size: 12pt, weight: "bold")[GESTÃO DE PRODUTOS E DADOS NO MERCADO DE TECNOLOGIA]
  
  #v(2pt)
  #text(size: 11pt, style: "italic", fill: rgb("#333333"))[
    Profissional com experiência em gestão de produtos, dados e automação, atuando em empresas de tecnologia e inovação com foco em eficiência operacional, escalabilidade e geração de valor.
  ]
]

// --- Resumo Profissional ---

#section_title("Resumo profissional")

#summary_item[Trajetória em gestão de produtos e dados, com atuação em empresas de tecnologia e inovação, liderando equipes multidisciplinares e entregando soluções de alto impacto operacional e financeiro.]

#summary_item[Experiência no desenvolvimento e gestão de plataformas digitais, APIs e sistemas de automação, unindo visão de negócio e profundidade técnica em Python, BigQuery e ferramentas de dados.]

#summary_item[Atuação em ambientes de alta complexidade e escala, com gestão de riscos financeiros superiores a R\$ 8 milhões mensais e geração de receita incremental de até R\$ 2 milhões em campanhas únicas.]

#summary_item[Vivência em ciência de dados e analytics, com desenvolvimento de modelos preditivos, análises de churn, correlação de produtos e geração de leads qualificados para equipes comerciais.]

#summary_item[Perfil analítico, orientado a dados e à entrega de resultados, com habilidade para transitar entre áreas técnicas e de negócio em ambientes dinâmicos e de rápido crescimento.]



// --- Experiência Profissional ---

#import "../Profiles/companies.typ": companies
#section_title("Experiência profissional")


// MOTTU
#let company1 = t(companies.mottu)
#company_header(company1.name, company1.period)

#import "../Bullets/product_manager_bullets.typ" as exp
#let experiences = (
  bigtech: exp.bigtech,
  scaleup: exp.scaleup,
  startup: exp.startup,
  other: exp.other,
)

#job_position(t(exp.position))
#let experience = t(experiences.at(profile.experience_type))
#for bullet in experience {
  bullet_item[#bullet]
}



#import "../Bullets/trainee_bullets.typ" as exp2
#let experiences2 = (
  bigtech: exp2.bigtech,
  scaleup: exp2.scaleup,
  startup: exp2.startup,
  other: exp2.other,
)

#job_position(t(exp2.position))
#let experience = t(experiences2.at(profile.experience_type))
#for bullet in experience {
  bullet_item[#bullet]
}



#pagebreak()

// GRUPO FLEURY
#let company2 = t(companies.fleury)
#company_header(company2.name, company2.period)


#import "../Bullets/estagiario_data_science.typ" as exp3
#let experiences3 = (
  bigtech: exp3.bigtech,
  scaleup: exp3.scaleup,
  startup: exp3.startup,
  other: exp3.other,
)

#job_position(t(exp3.position))
#let experience = t(experiences3.at(profile.experience_type))
#for bullet in experience {
  bullet_item[#bullet]
}

// PETROBRAS
#company_header("Petrobras / FDTE", "(JAN/2020 – JUN/2022)")
#job_position("Pesquisador Bolsista")
#bullet_item[Desenvolvimento de softwares para otimização de processos de inspeção de equipamentos submarinos (Projeto RBI – Petrobras/LabRisco-EP USP/FDTE).]
#bullet_item[Utilização de Java para coleta de dados e Python com redes neurais para otimização de planos de manutenção.]

// --- Formação ---

#section_title("Formação acadêmica e complementar")

#edu_item("✓")[Bacharelado em Engenharia de Produção – UNESP – Universidade Estadual Paulista (2019 – 2024)]

#edu_item("•")[Membro Pesquisador do Grupo de Simulação e Modelagem Computacional (CNPq/UNESP) (2021 – 2022)]

#edu_item("•")[Inglês: Nativo]
