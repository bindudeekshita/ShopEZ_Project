from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak

root = Path(__file__).resolve().parent
readme_path = root / 'README.md'
pdf_path = root / 'SHOPEZ.pdf'

text = readme_path.read_text(encoding='utf-8')
lines = text.splitlines()





styles = getSampleStyleSheet()
if 'Title' not in styles.byName:
    styles.add(ParagraphStyle(name='Title', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=24, leading=28, spaceAfter=10, textColor=colors.HexColor('#113b94')))
if 'Section' not in styles.byName:
    styles.add(ParagraphStyle(name='Section', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=13, leading=16, spaceAfter=6, textColor=colors.HexColor('#111827')))
if 'Body' not in styles.byName:
    styles.add(ParagraphStyle(name='Body', parent=styles['BodyText'], fontName='Helvetica', fontSize=10.5, leading=13.5, textColor=colors.HexColor('#111827'), spaceAfter=5))
if 'Bullet' not in styles.byName:
    styles.add(ParagraphStyle(name='Bullet', parent=styles['BodyText'], fontName='Helvetica', fontSize=10.5, leading=13.5, leftIndent=12, bulletIndent=0, spaceAfter=3, textColor=colors.HexColor('#111827')))
if 'Quote' not in styles.byName:
    styles.add(ParagraphStyle(name='Quote', parent=styles['BodyText'], fontName='Helvetica-Oblique', fontSize=10.5, leading=13.5, textColor=colors.HexColor('#4b5563'), spaceAfter=8))

story = []
for line in lines:
    stripped = line.strip()
    if not stripped:
        continue
    if stripped.startswith('# '):
        story.append(Paragraph(stripped[2:], styles['Title']))
    elif stripped.startswith('## '):
        story.append(Paragraph(stripped[3:], styles['Section']))
    elif stripped.startswith('### '):
        story.append(Paragraph(stripped[4:], styles['Section']))
    elif stripped.startswith('* ') or stripped.startswith('- '):
        story.append(Paragraph(stripped[2:], styles['Bullet']))
    elif stripped.startswith('> '):
        story.append(Paragraph(stripped[2:], styles['Quote']))
    elif stripped.startswith('```'):
        continue
    else:
        story.append(Paragraph(stripped.replace('`', ''), styles['Body']))

# Add a small footer-like spacer before saving
story.append(Spacer(1, 12))

# Create PDF
pdf_file = SimpleDocTemplate(str(pdf_path), pagesize=letter, rightMargin=54, leftMargin=54, topMargin=54, bottomMargin=54)
pdf_file.build(story)
print(f'Generated {pdf_path}')
