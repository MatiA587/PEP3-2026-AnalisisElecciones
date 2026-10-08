from pathlib import Path
from pypdf import PdfReader
from docx import Document

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "documentacion" / "originales"
OUTPUT_DIR = ROOT / "documentacion" / "texto"
EXTENSIONES = {".pdf", ".docx"}


def nombre_salida(path: Path) -> Path:
    return OUTPUT_DIR / f"{path.stem}.md"


def convertir_pdf(path: Path) -> str:
    reader = PdfReader(str(path))
    partes = []
    for numero, page in enumerate(reader.pages, start=1):
        texto = (page.extract_text() or "").strip()
        partes.append(f"## Página {numero}

")
        partes.append(texto if texto else "_[La página no contiene texto extraíble.]_")
        partes.append("

")
    return "".join(partes)


def convertir_docx(path: Path) -> str:
    doc = Document(str(path))
    partes = []
    for parrafo in doc.paragraphs:
        texto = parrafo.text.strip()
        if texto:
            partes.append(texto)
    for tabla_num, tabla in enumerate(doc.tables, start=1):
        partes.append(f"
## Tabla {tabla_num}
")
        filas = []
        for fila in tabla.rows:
            filas.append([celda.text.replace("
", " ").strip() for celda in fila.cells])
        if filas:
            partes.append("| " + " | ".join(filas[0]) + " |")
            partes.append("| " + " | ".join(["---"] * len(filas[0])) + " |")
            for fila in filas[1:]:
                partes.append("| " + " | ".join(fila) + " |")
    return "

".join(partes)


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    documentos = [
        path for path in SOURCE_DIR.rglob("*")
        if path.is_file() and path.suffix.lower() in EXTENSIONES
    ]
    if not documentos:
        print("No se encontraron PDF o DOCX en documentacion/originales/.")
        return
    for path in documentos:
        if path.suffix.lower() == ".pdf":
            contenido = convertir_pdf(path)
        else:
            contenido = convertir_docx(path)
        salida = nombre_salida(path)
        titulo = path.stem.replace("_", " ")
        salida.write_text(
            f"# {titulo}

"
            f"> Versión de texto generada automáticamente a partir de {path.name}.

"
            + contenido,
            encoding="utf-8"
        )
        print(f"Convertido: {path} -> {salida}")


if __name__ == "__main__":
    main()
