#!/usr/bin/env bash
# ==============================================================================
# Script: generate-pdfs.sh
# Purpose: Compiles bilingual Markdown lessons (lesson.md & lesson.tr.md) to PDF
# Tools supported: marp-cli, md-to-pdf, pandoc
# ==============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

echo "=== Domain-Driven Design Masterclass: PDF Generator ==="

# Check available tool
PDF_ENGINE=""
if command -v marp &> /dev/null; then
    PDF_ENGINE="marp"
elif npx --yes @marp-team/marp-cli --version &> /dev/null; then
    PDF_ENGINE="npx-marp"
elif command -v md-to-pdf &> /dev/null; then
    PDF_ENGINE="md-to-pdf"
elif command -v pandoc &> /dev/null; then
    PDF_ENGINE="pandoc"
else
    echo "Notice: Neither marp-cli, md-to-pdf, nor pandoc is installed globally."
    echo "Falling back to npx @marp-team/marp-cli..."
    PDF_ENGINE="npx-marp"
fi

echo "Selected Engine: ${PDF_ENGINE}"

generate_pdf() {
    local input_file="$1"
    local output_file="${input_file%.md}.pdf"

    if [[ ! -f "${input_file}" ]]; then
        return
    fi

    echo "Converting: ${input_file} -> ${output_file}"

    case "${PDF_ENGINE}" in
        "marp")
            marp --pdf --allow-local-files "${input_file}" -o "${output_file}"
            ;;
        "npx-marp")
            npx --yes @marp-team/marp-cli --pdf --allow-local-files "${input_file}" -o "${output_file}"
            ;;
        "md-to-pdf")
            md-to-pdf "${input_file}"
            ;;
        "pandoc")
            pandoc "${input_file}" -o "${output_file}" --pdf-engine=xelatex
            ;;
    esac
}

# Scan modules
MODULE_FILTER="${1:-all}"

for module_dir in "${ROOT_DIR}"/modules/module-*; do
    if [[ -d "${module_dir}" ]]; then
        module_name="$(basename "${module_dir}")"
        if [[ "${MODULE_FILTER}" != "all" && "${module_name}" != *"${MODULE_FILTER}"* ]]; then
            continue
        fi

        echo "Processing ${module_name}..."
        if [[ -f "${module_dir}/docs/lesson.md" ]]; then
            generate_pdf "${module_dir}/docs/lesson.md"
        fi
        if [[ -f "${module_dir}/docs/lesson.tr.md" ]]; then
            generate_pdf "${module_dir}/docs/lesson.tr.md"
        fi
    fi
done

# Process Capstone
if [[ "${MODULE_FILTER}" == "all" || "${MODULE_FILTER}" == "capstone" ]]; then
    if [[ -f "${ROOT_DIR}/capstone-order-fulfillment-platform/docs/lesson.md" ]]; then
        echo "Processing Capstone..."
        generate_pdf "${ROOT_DIR}/capstone-order-fulfillment-platform/docs/lesson.md"
        generate_pdf "${ROOT_DIR}/capstone-order-fulfillment-platform/docs/lesson.tr.md"
    fi
fi

echo "=== PDF Generation Completed Successfully! ==="
