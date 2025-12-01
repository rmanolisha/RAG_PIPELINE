import subprocess
import os

def convert_pdf_to_markdown(pdf_path: str, output_dir: str) -> str:
    # Example using docling CLI; adjust as needed for your setup
    md_filename = os.path.splitext(os.path.basename(pdf_path))[0] + ".md"
    md_path = os.path.join(output_dir, md_filename)
    subprocess.run(["docling", pdf_path, "-o", md_path], check=True)
    return md_path