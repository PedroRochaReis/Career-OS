$root = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $root

$profilePath = Join-Path $root 'Profiles\profile.typ'
[string]$origContent = Get-Content $profilePath -Raw

$langs = @('pt', 'en')
$types = @('bigtech', 'scaleup', 'startup')
$outputDir = Join-Path $root 'Curriculos'
$resumePath = Join-Path $root 'Template\resume.typ'

if (-not (Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir | Out-Null
}

try {
    foreach ($lang in $langs) {
            foreach ($type in $types) {
                $profileText = [regex]::Replace($origContent, 'experience_type:\s*".*?"', 'experience_type: "' + $type + '"')
                $profileText = [regex]::Replace($profileText, 'language:\s*".*?"', 'language: "' + $lang + '"')

                Set-Content -Path $profilePath -Value $profileText -Encoding UTF8
            $outputName = "CV_Pedro_Reis_{0}_{1}.pdf" -f $lang, $type
            Write-Host "Compiling $outputName ..."
            typst compile "./Template/resume.typ" "./Curriculos/$outputName" --root .
        }
    }
}
finally {
    Set-Content -Path $profilePath -Value $origContent -Encoding UTF8
    Write-Host 'Restored original Profiles/profile.typ'
}
