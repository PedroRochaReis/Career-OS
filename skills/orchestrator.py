from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import List


ROOT = Path(__file__).resolve().parents[1]
EXPERIANCE_PROMPT = ROOT / "experiance_prompt.md"
BULLETS_PROMPT = ROOT / "bullets_prompt.md"


def read_context(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def read_prompt(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def create_context_summary(text: str) -> str:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    summary_lines = [
        "# Resumo do contexto",
        "",
        f"- Total de linhas: {len(lines)}",
        f"- Caracteres: {len(text)}",
        "- Fonte: contexto de entrada do usuário",
        "",
        "## Conteúdo detectado",
    ]

    for line in lines[:10]:
        summary_lines.append(f"- {line}")

    if len(lines) > 10:
        summary_lines.append("- ...")

    return "\n".join(summary_lines) + "\n"


def build_experience_knowledge_base(context_text: str) -> str:
    prompt_text = read_prompt(EXPERIANCE_PROMPT)
    lines = [line.strip() for line in context_text.splitlines() if line.strip()]
    context_snapshot = [line for line in lines if "Grupo Fleury" in line or "Pricing" in line or "Estagiario" in line or "Projeto de Leads" in line or "2 milhões" in line or "Python" in line]

    return "\n".join([
        "# Experiência estruturada (gerada a partir do contexto)",
        "",
        "## Prompt usado",
        f"- {EXPERIANCE_PROMPT.name}",
        "",
        "## Resumo da experiência",
        "- Empresa: Grupo Fleury",
        "- Setor: Pricing B2B para exames médicos",
        "- Cargo: Estagiário de Ciência de Dados",
        "- Papel principal: desenvolver análises e modelos para identificar leads comerciais e apoiar decisões de vendas.",
        "- Resultado principal: geração de uma nova inteligência comercial que elevou a receita de uma campanha em aproximadamente R$ 2 milhões anuais.",
        "- Tecnologias: Python, SQL, SQL Server, DataBricks, Tesseract.",
        "",
        "## Evidências extraídas do contexto",
        *[f"- {item}" for item in context_snapshot],
        "",
        "## Instruções aplicadas",
        prompt_text.splitlines()[0],
        "",
        "Esta saída é um primeiro passo estruturado para alimentar a geração de bullets e currículo.",
        "",
    ])


def create_bullets_stub(context_text: str) -> str:
    prompt_text = read_prompt(BULLETS_PROMPT)
    base_bullets = [
        "Construí e implementei uma solução de análise de dados para identificar leads comerciais de exames médicos, permitindo que o time de vendas atuasse com maior precisão e base em dados.",
        "Desenvolvi uma análise de consumo histórico e correlações entre exames, apoiando a descoberta de oportunidades de venda e a priorização de clientes com maior potencial.",
        "Usei Python, SQL e técnicas estatísticas para transformar dados operacionais em uma inteligência comercial aplicável ao CRM e à equipe comercial.",
        "A primeira campanha baseada nesse trabalho gerou impacto financeiro significativo, com incremento de receita estimado em aproximadamente R$ 2 milhões anuais.",
    ]

    bigtech = [
        base_bullets[0].replace("Construí", "Construí e escalei"),
        base_bullets[1].replace("Desenvolvi", "Estruturei"),
        base_bullets[2].replace("Usei", "Apliquei"),
        base_bullets[3].replace("A primeira campanha", "A primeira campanha validada em produção"),
    ]

    scaleup = [
        base_bullets[0].replace("Construí", "Criei"),
        base_bullets[1].replace("Desenvolvi", "Transformei"),
        base_bullets[2].replace("Usei", "Combinei"),
        base_bullets[3].replace("impacto financeiro", "impacto comercial e financeiro"),
    ]

    startup = [
        base_bullets[0].replace("Construí", "Levantei"),
        base_bullets[1].replace("Desenvolvi", "Entreguei"),
        base_bullets[2].replace("Usei", "Implementei"),
        base_bullets[3].replace("A primeira campanha", "O primeiro MVP comercial"),
    ]

    return "\n".join([
        "#let position = (",
        "  pt: (\"Estagiário de Ciência de Dados – Grupo Fleury (JAN/2024 – DEZ/2024)\"),",
        "  en: (\"Data Science Intern – Grupo Fleury (JAN/2024 – DEC/2024)\")",
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
