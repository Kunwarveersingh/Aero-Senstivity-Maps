"""Build a dependency-free Word report from docs/REPORT.md. Run from repo root."""
from pathlib import Path
from xml.sax.saxutils import escape
from zipfile import ZipFile, ZIP_DEFLATED
import re

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'results/project-documentation/Formula_Student_Aerodynamic_Mapping_Report.docx'
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'

def clean(s):
    s = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', s)
    return s.replace('`', '').replace('**', '')

def p(text='', style=None, page=False):
    props = (f'<w:pStyle w:val="{style}"/>' if style else '')
    if page:
        props += '<w:pageBreakBefore/>'
    return f'<w:p><w:pPr>{props}</w:pPr><w:r><w:t xml:space="preserve">{escape(clean(text))}</w:t></w:r></w:p>'

def table(rows):
    widths = [2200, 3600, 3400]
    xml = '<w:tbl><w:tblPr><w:tblW w:w="9200" w:type="dxa"/><w:tblBorders>'
    for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        xml += f'<w:{edge} w:val="single" w:sz="4" w:color="CBD5E1"/>'
    xml += '</w:tblBorders><w:tblLayout w:type="fixed"/></w:tblPr><w:tblGrid>'
    xml += ''.join(f'<w:gridCol w:w="{width}"/>' for width in widths) + '</w:tblGrid>'
    for idx, row in enumerate(rows):
        xml += '<w:tr><w:trPr><w:cantSplit/>' + ('<w:tblHeader/>' if idx == 0 else '') + '</w:trPr>'
        for width, cell in zip(widths, row):
            xml += f'<w:tc><w:tcPr><w:tcW w:w="{width}" w:type="dxa"/>'
            if idx == 0:
                xml += '<w:shd w:fill="E8EEF4"/>'
            xml += '</w:tcPr>' + p(cell, 'TableHeader' if idx == 0 else 'TableText') + '</w:tc>'
        xml += '</w:tr>'
    return xml + '</w:tbl>'

body = [p('AERODYNAMIC PERFORMANCE', 'Title'), p('AND SENSITIVITY MAPPING', 'Title'),
        p('FOR A FORMULA STUDENT CAR', 'Subtitle'), p(),
        p('Working Project Report', 'CoverText'),
        p('Strohm und Söhne e.V. Noris Racing', 'CoverText'),
        p('Technische Hochschule Nürnberg Georg Simon Ohm', 'CoverText'),
        p('26 October 2026', 'CoverText'), p(),
        p('Status: initial research and study planning', 'CoverText'),
        p('This report documents agreed scope, literature context, and open decisions. '
          'It does not present completed CFD simulations or validated results for this car.', 'CoverText')]
lines = (ROOT / 'docs/REPORT.md').read_text().splitlines()
i = 0
first = True
while i < len(lines):
    line = lines[i].strip()
    if not line or line.startswith('# '):
        i += 1
        continue
    if line.startswith('## '):
        body.append(p(line[3:], 'Heading1', page=first))
        first = False
        i += 1
    elif line.startswith('|'):
        rows = []
        while i < len(lines) and lines[i].strip().startswith('|'):
            cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
            if not all(re.fullmatch(r'[:\- ]+', c) for c in cells):
                rows.append(cells)
            i += 1
        body.append(table(rows))
    else:
        paragraph = [line]
        i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].startswith(('#', '|')):
            if re.match(r'^\d+\. ', lines[i]):
                break
            paragraph.append(lines[i].strip())
            i += 1
        body.append(p(' '.join(paragraph)))

styles = f'''<w:styles xmlns:w="{W}">
<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="24"/><w:lang w:val="en-GB"/></w:rPr></w:rPrDefault><w:pPrDefault><w:pPr><w:spacing w:after="140" w:line="300" w:lineRule="auto"/><w:widowControl/></w:pPr></w:pPrDefault></w:docDefaults>
<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/></w:style>
<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:pPr><w:keepNext/><w:spacing w:before="300" w:after="140"/><w:outlineLvl w:val="0"/></w:pPr><w:rPr><w:b/><w:color w:val="203850"/><w:sz w:val="30"/></w:rPr></w:style>
'''
for name, size, bold in [('Title', 42, True), ('Subtitle', 28, False), ('CoverText', 24, False), ('TableText', 20, False), ('TableHeader', 20, True)]:
    center = '<w:jc w:val="center"/>' if name in ('Title', 'Subtitle', 'CoverText') else ''
    styles += f'<w:style w:type="paragraph" w:styleId="{name}"><w:name w:val="{name}"/><w:basedOn w:val="Normal"/><w:pPr>{center}<w:spacing w:after="160"/></w:pPr><w:rPr><w:sz w:val="{size}"/>{"<w:b/>" if bold else ""}</w:rPr></w:style>'
styles += '</w:styles>'
sect = '<w:sectPr><w:footerReference w:type="default" r:id="rId2"/><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1440" w:right="1353" w:bottom="1440" w:left="1353" w:header="720" w:footer="720"/><w:titlePg/></w:sectPr>'
document = f'<w:document xmlns:w="{W}" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><w:body>{"".join(body)}{sect}</w:body></w:document>'
footer = f'<w:ftr xmlns:w="{W}"><w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:rPr><w:sz w:val="18"/></w:rPr><w:t>Working project report · </w:t></w:r><w:fldSimple w:instr="PAGE"><w:r><w:t>1</w:t></w:r></w:fldSimple></w:p></w:ftr>'
rels_ns = 'http://schemas.openxmlformats.org/package/2006/relationships'
reltype = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/'
parts = {
    '[Content_Types].xml': '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/><Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/><Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/></Types>',
    '_rels/.rels': f'<Relationships xmlns="{rels_ns}"><Relationship Id="rId1" Type="{reltype}officeDocument" Target="word/document.xml"/></Relationships>',
    'word/_rels/document.xml.rels': f'<Relationships xmlns="{rels_ns}"><Relationship Id="rId1" Type="{reltype}styles" Target="styles.xml"/><Relationship Id="rId2" Type="{reltype}footer" Target="footer1.xml"/></Relationships>',
    'word/document.xml': document,
    'word/styles.xml': styles,
    'word/footer1.xml': footer,
}
OUT.parent.mkdir(parents=True, exist_ok=True)
with ZipFile(OUT, 'w', ZIP_DEFLATED) as archive:
    for name, contents in parts.items():
        archive.writestr(name, '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' + contents)
print(OUT)
