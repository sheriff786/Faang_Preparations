from pathlib import Path
import html
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    KeepTogether,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


BASE_DIR = Path(__file__).parent
SOURCE_PATH = BASE_DIR / "linked_list_revision_guide.md"
OUTPUT_PATH = BASE_DIR / "linked_list_revision_guide.pdf"


def format_inline(text):
    escaped = html.escape(text)
    escaped = re.sub(r"`([^`]+)`", r"<font name='Courier'>\1</font>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", escaped)
    return escaped


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="GuideTitle",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=24,
            leading=29,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#16324F"),
            spaceAfter=14,
        )
    )
    styles.add(
        ParagraphStyle(
            name="GuideSubtitle",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=10,
            leading=14,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#52606D"),
            spaceAfter=18,
        )
    )
    styles.add(
        ParagraphStyle(
            name="GuideH1",
            parent=styles["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=16,
            leading=20,
            textColor=colors.HexColor("#16324F"),
            spaceBefore=12,
            spaceAfter=7,
        )
    )
    styles.add(
        ParagraphStyle(
            name="GuideH2",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=12,
            leading=15,
            textColor=colors.HexColor("#087E8B"),
            spaceBefore=9,
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="GuideBody",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9.4,
            leading=13.2,
            textColor=colors.HexColor("#263238"),
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="GuideBullet",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9.2,
            leading=12.5,
            leftIndent=12,
            firstLineIndent=-7,
            textColor=colors.HexColor("#263238"),
            spaceAfter=3,
        )
    )
    styles.add(
        ParagraphStyle(
            name="GuideCode",
            parent=styles["Code"],
            fontName="Courier",
            fontSize=7.6,
            leading=9.5,
            leftIndent=8,
            rightIndent=8,
            textColor=colors.HexColor("#263238"),
            backColor=colors.HexColor("#F1F5F7"),
            borderColor=colors.HexColor("#D5E0E5"),
            borderWidth=0.5,
            borderPadding=6,
            spaceBefore=4,
            spaceAfter=8,
        )
    )
    return styles


def parse_markdown(lines, styles):
    story = []
    index = 0
    first_heading = True

    while index < len(lines):
        line = lines[index].rstrip("\n")

        if not line.strip():
            index += 1
            continue

        if line.startswith("```"):
            code_lines = []
            index += 1
            while index < len(lines) and not lines[index].startswith("```"):
                code_lines.append(lines[index].rstrip("\n"))
                index += 1
            story.append(Preformatted("\n".join(code_lines), styles["GuideCode"]))
            index += 1
            continue

        heading_match = re.match(r"^(#{1,2})\s+(.+)$", line)
        if heading_match:
            level, title = len(heading_match.group(1)), heading_match.group(2)
            if first_heading:
                story.append(Paragraph(format_inline(title), styles["GuideTitle"]))
                story.append(
                    Paragraph(
                        "A pattern-first study guide for linked-list interviews and revision.",
                        styles["GuideSubtitle"],
                    )
                )
                first_heading = False
            else:
                story.append(Paragraph(format_inline(title), styles["GuideH1" if level == 1 else "GuideH2"]))
            index += 1
            continue

        if line.startswith("|"):
            table_lines = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                if not re.match(r"^\s*\|\s*:?-+", lines[index]):
                    table_lines.append(lines[index].strip())
                index += 1
            rows = []
            for table_line in table_lines:
                cells = [cell.strip() for cell in table_line.strip("|").split("|")]
                rows.append([Paragraph(format_inline(cell), styles["GuideBody"]) for cell in cells])
            if rows:
                table = Table(rows, repeatRows=1, hAlign="LEFT")
                table.setStyle(
                    TableStyle(
                        [
                            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#DCEFF1")),
                            ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#B8C8CE")),
                            ("VALIGN", (0, 0), (-1, -1), "TOP"),
                            ("LEFTPADDING", (0, 0), (-1, -1), 5),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                            ("TOPPADDING", (0, 0), (-1, -1), 4),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                        ]
                    )
                )
                story.append(table)
                story.append(Spacer(1, 5))
            continue

        if re.match(r"^\s*[-*]\s+", line):
            bullet_text = re.sub(r"^\s*[-*]\s+", "", line)
            story.append(Paragraph("&#8226; " + format_inline(bullet_text), styles["GuideBullet"]))
            index += 1
            continue

        number_match = re.match(r"^\s*\d+\.\s+(.+)$", line)
        if number_match:
            story.append(Paragraph(format_inline(line.strip()), styles["GuideBullet"]))
            index += 1
            continue

        paragraph_lines = [line]
        index += 1
        while index < len(lines):
            next_line = lines[index].rstrip("\n")
            if (
                not next_line.strip()
                or next_line.startswith("```")
                or re.match(r"^(#{1,2})\s+", next_line)
                or next_line.startswith("|")
                or re.match(r"^\s*[-*]\s+", next_line)
                or re.match(r"^\s*\d+\.\s+", next_line)
            ):
                break
            paragraph_lines.append(next_line)
            index += 1
        story.append(Paragraph(format_inline(" ".join(paragraph_lines)), styles["GuideBody"]))

    return story


def add_page_number(canvas, document):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#6B7785"))
    canvas.drawRightString(A4[0] - 18 * mm, 12 * mm, f"Linked Lists Revision Guide | {document.page}")
    canvas.restoreState()


def main():
    styles = build_styles()
    lines = SOURCE_PATH.read_text(encoding="utf-8").splitlines()
    story = parse_markdown(lines, styles)
    document = SimpleDocTemplate(
        str(OUTPUT_PATH),
        pagesize=A4,
        rightMargin=17 * mm,
        leftMargin=17 * mm,
        topMargin=16 * mm,
        bottomMargin=18 * mm,
        title="Linked Lists: FAANG / MAANG Revision Guide",
        author="GitHub Copilot",
    )
    document.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(OUTPUT_PATH)


if __name__ == "__main__":
    main()
