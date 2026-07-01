#set page(
  paper: "a4",
  margin: (x: 25mm, y: 25mm),
)

#set text(
  font: "Segoe UI",
  size: 11pt,
  lang: "pt",
  region: "br",
)

#set par(justify: true, leading: 0.8em)

// --- Cabeçalho ---
#align(left)[
  #text(size: 18pt, weight: "bold")[Pedro Augusto Rocha Reis] \
  #v(2pt)
  #text(size: 9pt, fill: gray.darken(50%))[
    São Paulo – SP #h(4pt) | #h(4pt) (11) 97106-4000 \
    reis.r.pedroaugusto\@gmail.com \
    #link("https://www.linkedin.com/in/pedro-augusto-rocha-reis-571959203")[linkedin.com/in/pedro-augusto-rocha-reis]
  ]
]

#v(40pt)

// --- Data e Local ---
#let formatar-data(data) = {
  let meses = (
    "janeiro",
    "fevereiro",
    "março",
    "abril",
    "maio",
    "junho",
    "julho",
    "agosto",
    "setembro",
    "outubro",
    "novembro",
    "dezembro",
  )

  [#data.day() de #meses.at(data.month() - 1) de #data.year()]
}

#text(weight: "bold")[
  São Paulo, #formatar-data(datetime.today())
]
#v(20pt)

// --- Saudação ---
Prezados(as),

#v(10pt)

Gostaria de me candidatar à oportunidade de *Especialista de Dados*.

Ao longo da minha carreira, construí uma trajetória pouco convencional que hoje considero meu maior diferencial. Iniciei atuando em pesquisa e desenvolvimento de software em um projeto conjunto entre Petrobras, UNESP e USP, evoluí para Ciência de Dados no Grupo Fleury, onde desenvolvi soluções analíticas para inteligência comercial, e atualmente atuo como Product Manager, liderando produtos digitais voltados para automação, plataformas e eficiência operacional.

Essa combinação me permite transitar com naturalidade entre tecnologia, dados e negócio. Gosto de compreender profundamente um problema, estruturar soluções junto às áreas envolvidas e conduzir sua execução até que gerem impacto mensurável. Ao longo desse caminho, liderei produtos responsáveis por operações críticas, implementei soluções baseadas em IA e automação, desenvolvi plataformas internas e conduzi iniciativas que redesenharam processos de alto impacto financeiro, reduziram riscos operacionais, eliminaram atividades manuais e aumentaram significativamente a eficiência das operações. Também participei da criação de novas capacidades analíticas para suportar decisões comerciais e estratégicas, sempre buscando transformar dados em resultados concretos para o negócio.

Tenho especial interesse por ambientes que valorizam autonomia, aprendizado contínuo e desafios complexos. São contextos nos quais consigo contribuir não apenas com gestão de produto, mas também com minha capacidade técnica para acelerar decisões, facilitar a comunicação entre engenharia e negócio e transformar ideias em soluções escaláveis.

Acredito que minha experiência e perfil possam agregar valor ao time. Ficarei muito satisfeito em conversar sobre como posso contribuir para os desafios da empresa e gerar impacto desde os primeiros projetos.

Agradeço pela consideração e coloco-me à disposição para uma conversa.

#v(30pt)

Atenciosamente,

#v(10pt)

#text(weight: "bold", size: 12pt)[Pedro Augusto Reis]
