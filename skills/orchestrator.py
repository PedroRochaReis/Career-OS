from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Dict, List


ROOT = Path(__file__).resolve().parents[1]
EXPERIANCE_PROMPT = ROOT / "experiance_prompt.md"
BULLETS_PROMPT = ROOT / "bullets_prompt.md"


def read_context(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def read_prompt(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def normalize_space(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def extract_experience_facts(context_text: str) -> Dict[str, object]:
    facts: Dict[str, object] = {
        "company": "Grupo Fleury" if "Grupo Fleury" in context_text else "empresa",
        "sector": None,
        "role": None,
        "period": None,
        "initiative": None,
        "problem": None,
        "solution": None,
        "impact": None,
        "technologies": [],
        "stakeholders": [],
    }

    sector_match = re.search(r"Em qual setor ela atuava\?\s*(.+)", context_text)
    if sector_match:
        facts["sector"] = normalize_space(sector_match.group(1))

    role_match = re.search(r"Cargo:\s*(.+)", context_text)
    if role_match:
        role_value = normalize_space(role_match.group(1))
        facts["role"] = role_value.replace("Estagiario", "Estagiário")

    period_match = re.search(r"Período:\s*(.+)", context_text)
    if period_match:
        facts["period"] = normalize_space(period_match.group(1))

    initiative_match = re.search(r"## Nome\s*\n(.+)", context_text)
    if initiative_match:
        facts["initiative"] = normalize_space(initiative_match.group(1))

    problem_match = re.search(r"## Qual era o problema\?\s*(.+?)(?=\n## |\Z)", context_text, re.S)
    if problem_match:
        facts["problem"] = normalize_space(problem_match.group(1))

    solution_match = re.search(r"## O que foi feito\?\s*(.+?)(?=\n## |\Z)", context_text, re.S)
    if solution_match:
        facts["solution"] = normalize_space(solution_match.group(1))

    impact_match = re.search(r"## 8\. Resultados\s*(.+?)(?=\n# 9\.|\n# 12\.|\n# 13\.|\n# 15\.|\Z)", context_text, re.S)
    if impact_match:
        facts["impact"] = normalize_space(impact_match.group(1))
    elif "2 milhões" in context_text or "2.000.000" in context_text:
        facts["impact"] = "A primeira campanha gerou aproximadamente R$ 2.000.000 em receita anualizada (≈ R$ 2 milhões)."

    if "2 milhões" in context_text or "2.000.000" in context_text:
        facts["impact"] = facts["impact"].replace("R$ 2 milhões", "R$ 2.000.000").replace("R$ 2.000.000", "R$ 2.000.000")

    technologies = []
    for tech in ["Python", "SQL", "DataBricks", "SQLServer", "Tesseract"]:
        if tech.lower() in context_text.lower():
            technologies.append(tech)
    if not technologies:
        technologies = ["Python", "SQL"]
    facts["technologies"] = technologies

    if "time comercial" in context_text.lower():
        facts["stakeholders"].append("time comercial")
    if "analista senior" in context_text.lower():
        facts["stakeholders"].append("analista sênior")

    return facts


def create_context_summary(text: str) -> str:
    facts = extract_experience_facts(text)
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    summary_lines = [
        "# Resumo do contexto",
        "",
        f"- Total de linhas: {len(lines)}",
        f"- Caracteres: {len(text)}",
        "- Fonte: contexto de entrada do usuário",
        "",
        "## Conteúdo detectado",
        f"- Empresa: {facts['company']}",
        f"- Cargo: {facts['role'] or 'não identificado'}",
        f"- Período: {facts['period'] or 'não identificado'}",
        f"- Projeto: {facts['initiative'] or 'não identificado'}",
        f"- Tecnologias: {', '.join(facts['technologies'])}",
    ]

    return "\n".join(summary_lines) + "\n"


def build_experience_knowledge_base(context_text: str) -> str:
    prompt_text = read_prompt(EXPERIANCE_PROMPT)
    facts = extract_experience_facts(context_text)

    return "\n".join([
        "# Experiência estruturada (gerada a partir do contexto)",
        "",
        "## Prompt usado",
        f"- {EXPERIANCE_PROMPT.name}",
        "",
        "## Resumo da experiência",
        f"- Empresa: {facts['company']}",
        f"- Setor: {facts['sector'] or 'não identificado'}",
        f"- Cargo: {facts['role'] or 'não identificado'}",
        f"- Período: {facts['period'] or 'não identificado'}",
        f"- Projeto principal: {facts['initiative'] or 'não identificado'}",
        f"- Papel principal: {facts['solution'] or 'não identificado'}",
        f"- Resultado principal: {facts['impact'] or 'não identificado'}",
        f"- Tecnologias: {', '.join(facts['technologies'])}",
        "",
        "## Evidências extraídas do contexto",
        f"- Empresa: {facts['company']}",
        f"- Problema: {facts['problem'] or 'não identificado'}",
        f"- Solução: {facts['solution'] or 'não identificado'}",
        f"- Impacto: {facts['impact'] or 'não identificado'}",
        f"- Stakeholders: {', '.join(facts['stakeholders']) if facts['stakeholders'] else 'não identificado'}",
        "",
        "## Instruções aplicadas",
        prompt_text.splitlines()[0],
        "",
        "Esta saída é um primeiro passo estruturado para alimentar a geração de bullets e currículo.",
        "",
    ])


def create_bullets_stub(context_text: str) -> str:
    prompt_text = read_prompt(BULLETS_PROMPT)
    facts = extract_experience_facts(context_text)
    company = facts["company"] or "empresa"
    role = facts["role"] or "cargo"
    initiative = facts["initiative"] or "projeto de leads"
    technologies = ", ".join(facts["technologies"])
    impact_text = facts["impact"] or "impacto comercial significativo"
    if re.search(r"2\s*milhões|2\.000\.000", str(impact_text), re.I):
        impact_metric = "R$ 2 milhões"
    else:
        impact_metric = "impacto relevante"

    base_bullets = [
        f"Desenvolvi uma solução analítica no {company} para gerar leads B2B a partir de padrões de consumo histórico e apoiar o time comercial com recomendações acionáveis no CRM.",
        f"Combinei {technologies} e técnicas estatísticas para identificar oportunidades de venda e transformar dados de consumo em leads qualificados para o time comercial.",
        f"A primeira campanha baseada nesse trabalho gerou cerca de {impact_metric} em receita anualizada, criando uma nova frente de inteligência comercial para o negócio.",
        f"Trabalhei de forma autônoma em um ambiente com pouca estrutura inicial, entregando um MVP analítico que foi validado em produção e expandido depois.",
    ]

    bigtech = [
        base_bullets[0].replace("Desenvolvi", "Desenvolvi e escalei"),
        base_bullets[1].replace("Combinei", "Apliquei"),
        base_bullets[2].replace("A primeira campanha", "A primeira campanha validada em produção"),
        base_bullets[3].replace("MVP analítico", "produto analítico escalável"),
    ]

    scaleup = [
        base_bullets[0].replace("Desenvolvi", "Criei"),
        base_bullets[1].replace("Combinei", "Transformei"),
        base_bullets[2].replace("gerou cerca de", "gerou cerca de"),
        base_bullets[3].replace("MVP analítico", "solução de negócio"),
    ]

    startup = [
        base_bullets[0].replace("Desenvolvi", "Levantei"),
        base_bullets[1].replace("Combinei", "Implementei"),
        base_bullets[2].replace("A primeira campanha", "O primeiro MVP comercial"),
        base_bullets[3].replace("MVP analítico", "MVP analítico"),
    ]

    return "\n".join([
        "#let position = (",
        f"  pt: (\"{role} – {company} ({facts['period'] or 'período não informado'})\"),",
        f"  en: (\"{role} – {company} ({facts['period'] or 'period not provided'})\")",
        ")",
        "",
        "#let bigtech = (",
        "  pt: (",
        f"    \"{bigtech[0]}\",",
        f"    \"{bigtech[1]}\",",
        f"    \"{bigtech[2]}\",",
        f"    \"{bigtech[3]}\",",
        "  ),",
        "  en: (",
        f"    \"{bigtech[0]}\",",
        f"    \"{bigtech[1]}\",",
        f"    \"{bigtech[2]}\",",
        f"    \"{bigtech[3]}\",",
        "  ),",
        ")",
        "",
        "#let scaleup = (",
        "  pt: (",
        f"    \"{scaleup[0]}\",",
        f"    \"{scaleup[1]}\",",
        f"    \"{scaleup[2]}\",",
        f"    \"{scaleup[3]}\",",
        "  ),",
        "  en: (",
        f"    \"{scaleup[0]}\",",
        f"    \"{scaleup[1]}\",",
        f"    \"{scaleup[2]}\",",
        f"    \"{scaleup[3]}\",",
        "  ),",
        ")",
        "",
        "#let startup = (",
        "  pt: (",
        f"    \"{startup[0]}\",",
        f"    \"{startup[1]}\",",
        f"    \"{startup[2]}\",",
        f"    \"{startup[3]}\",",
        "  ),",
        "  en: (",
        f"    \"{startup[0]}\",",
        f"    \"{startup[1]}\",",
        f"    \"{startup[2]}\",",
        f"    \"{startup[3]}\",",
        "  ),",
        ")",
        "",
        "#let other = (",
        "  pt: (",
        f"    \"{base_bullets[0]}\",",
        f"    \"{base_bullets[1]}\",",
        f"    \"{base_bullets[2]}\",",
        f"    \"{base_bullets[3]}\",",
        "  ),",
        "  en: (",
        f"    \"{base_bullets[0]}\",",
        f"    \"{base_bullets[1]}\",",
        f"    \"{base_bullets[2]}\",",
        f"    \"{base_bullets[3]}\",",
        "  ),",
        ")",
        "",
        f"// Gerado com base em {BULLETS_PROMPT.name} e no contexto fornecido.",
        "",
    ])


def create_resume_preview(bullets_text: str) -> str:
    bullet_lines = []
    for line in bullets_text.splitlines():
        stripped = line.strip()
        if stripped.startswith('"') and (stripped.endswith('",') or stripped.endswith('"')):
            cleaned = stripped.strip('"').rstrip(',').strip('"').strip()
            cleaned = cleaned.replace("$", "\\$")
            if cleaned and not cleaned.startswith("#"):
                bullet_lines.append(cleaned)

    bullets_markup = "\n".join([f"#bullet_item[{item}]" for item in bullet_lines[:4]])
    return f"""#set page(margin: (x: 15mm, y: 18mm))

#set text(font: "Segoe UI", size: 10.5pt, lang: "pt")

#let bullet_item(content) = {{
  grid(
    columns: (25pt, 1fr),
    gutter: 0pt,
    h(12pt) + text(size: 10pt)[▪],
    content
  )
  v(2pt)
}}

#text(size: 18pt, weight: "bold")[Pré-visualização do MVP do pipeline]

#v(8pt)
#text(size: 12pt, weight: "bold")[Experiência extraída do contexto]

#v(4pt)
#text(size: 10.5pt)[Grupo Fleury · Pricing B2B · Estagiário de Ciência de Dados · Jan/2024 – Dez/2024]

#v(8pt)
#text(size: 12pt, weight: "bold")[Projeto de Leads]

{bullets_markup}
"""


def build_manifest(context_path: Path, output_dir: Path) -> dict:
    return {
        "context_file": str(context_path),
        "output_dir": str(output_dir),
        "prompts": {
            "experiance_prompt.md": str(EXPERIANCE_PROMPT),
            "bullets_prompt.md": str(BULLETS_PROMPT),
        },
        "steps": [
            "read_context",
            "create_context_summary",
            "build_experience_knowledge_base",
            "create_bullets_stub",
        ],
        "status": "ok",
    }


def run_pipeline(context_path: Path, output_dir: Path) -> List[Path]:
    context_text = read_context(context_path)
    summary_text = create_context_summary(context_text)
    experience_text = build_experience_knowledge_base(context_text)
    bullets_text = create_bullets_stub(context_text)

    output_dir.mkdir(parents=True, exist_ok=True)
    summary_path = output_dir / "context_summary.md"
    experience_path = output_dir / "experience_knowledge_base.md"
    bullets_path = output_dir / "generated_bullets.typ"
    preview_path = output_dir / "resume_preview.typ"
    manifest_path = output_dir / "pipeline_manifest.json"

    summary_path.write_text(summary_text, encoding="utf-8")
    experience_path.write_text(experience_text, encoding="utf-8")
    bullets_path.write_text(bullets_text, encoding="utf-8")
    preview_path.write_text(create_resume_preview(bullets_text), encoding="utf-8")
    manifest_path.write_text(json.dumps(build_manifest(context_path, output_dir), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    return [summary_path, experience_path, bullets_path, preview_path, manifest_path]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python skills/orchestrator.py <contexto.md> [saida]")
        sys.exit(1)

    context_path = Path(sys.argv[1]).resolve()
    output_dir = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else ROOT / "output"
    outputs = run_pipeline(context_path, output_dir)
    print("Pipeline concluída")
    for output in outputs:
        print(output)
