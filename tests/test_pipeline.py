import subprocess
import sys
import tempfile
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "orchestrator.py"
CONTEXT = ROOT / "tests" / "fixtures" / "raw_context.md"


class OrchestratorTests(unittest.TestCase):
    def test_runs_pipeline_and_creates_outputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            output_dir = pathlib.Path(tmp)
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(CONTEXT), str(output_dir)],
                capture_output=True,
                text=True,
                check=True,
            )

            self.assertIn("Pipeline concluída", result.stdout)
            self.assertTrue((output_dir / "context_summary.md").exists())
            self.assertTrue((output_dir / "experience_knowledge_base.md").exists())
            self.assertTrue((output_dir / "generated_bullets.typ").exists())
            self.assertTrue((output_dir / "resume_preview.typ").exists())
            self.assertTrue((output_dir / "pipeline_manifest.json").exists())

            summary_text = (output_dir / "experience_knowledge_base.md").read_text(encoding="utf-8")
            self.assertIn("Grupo Fleury", summary_text)
            self.assertIn("Pricing", summary_text)
            self.assertIn("Projeto de Leads para time de vendas", summary_text)
            self.assertIn("R$ 2.000.000", summary_text)

            bullets_text = (output_dir / "generated_bullets.typ").read_text(encoding="utf-8")
            self.assertIn("#let bigtech =", bullets_text)
            self.assertIn("Grupo Fleury", bullets_text)
            self.assertIn("CRM", bullets_text)
            self.assertIn("2 milhões", bullets_text)

            preview_text = (output_dir / "resume_preview.typ").read_text(encoding="utf-8")
            self.assertIn("Projeto de Leads", preview_text)

            manifest_text = (output_dir / "pipeline_manifest.json").read_text(encoding="utf-8")
            self.assertIn("experiance_prompt.md", manifest_text)
            self.assertIn("bullets_prompt.md", manifest_text)


if __name__ == "__main__":
    unittest.main()
