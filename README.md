# Career-OS
Esse será um repositório para documentar a minha carreira profissional completa

command line para executar um currículo específico:
typst compile ./Template/resume.typ ./Curriculos/CV_Pedro_Reis_teste.pdf --root .

carta apresentação
typst compile ./Template/carta_apresentacao.typ ./Curriculos/CA_Pedro_Reis.pdf --root .

command line para gerar todos os 6 currículos (pt/en × bigtech/scaleup/startup):
powershell -ExecutionPolicy Bypass -File .\generate_all.ps1
