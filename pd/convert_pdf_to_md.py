from pathlib import Path
import fitz
import re

ROOT = Path('/Users/yikepingguo/Desktop/h-ag/pd')
OUT = ROOT / 'md'
ASSETS = ROOT / 'assets'
OUT.mkdir(exist_ok=True)
ASSETS.mkdir(exist_ok=True)

BAD = re.compile(r'[\\/:*?"<>|\s]+')
def safe_name(s: str) -> str:
    return BAD.sub('_', s).strip('_') or 'document'

def esc_md(text: str) -> str:
    return text.replace(chr(0), '').rstrip()

def line_text(line):
    return ''.join(span.get('text', '') for span in line.get('spans', []))

def line_font_size(line):
    sizes = [span.get('size', 0) for span in line.get('spans', []) if span.get('text', '').strip()]
    return max(sizes) if sizes else 0

def block_text(block):
    lines = []
    for line in block.get('lines', []):
        t = line_text(line).rstrip()
        if t.strip():
            lines.append(t)
    return '\n'.join(lines).strip()

def classify(text: str, size: float, page_no: int) -> str:
    if page_no == 1 and size >= 18:
        return '# '
    if size >= 17:
        return '## '
    if size >= 14:
        return '### '
    return ''

summary = []
for pdf in sorted(ROOT.glob('*.pdf')):
    doc = fitz.open(pdf)
    stem = pdf.stem
    stem_safe = safe_name(stem)
    asset_dir = ASSETS / stem_safe
    asset_dir.mkdir(exist_ok=True)
    md_path = OUT / f'{stem}.md'
    parts = []
    parts.append(f'# {stem}\n')
    parts.append(f'> 来源 PDF：`../{pdf.name}`  \n> 页数：{doc.page_count}\n')

    image_count = 0
    seen_image_bytes = set()
    text_chars = 0

    for page_index, page in enumerate(doc, start=1):
        parts.append(f'\n---\n\n## 第 {page_index} 页\n')
        data = page.get_text('dict', sort=True)
        blocks = data.get('blocks', [])
        for block_i, block in enumerate(blocks, start=1):
            btype = block.get('type')
            if btype == 0:
                txt = esc_md(block_text(block))
                if not txt:
                    continue
                text_chars += len(txt)
                max_size = 0
                for line in block.get('lines', []):
                    max_size = max(max_size, line_font_size(line))
                prefix = classify(txt, max_size, page_index)
                if prefix:
                    lines = txt.splitlines()
                    parts.append(prefix + lines[0].strip() + '\n')
                    if len(lines) > 1:
                        parts.append('\n'.join(lines[1:]) + '\n')
                else:
                    parts.append(txt + '\n')
            elif btype == 1:
                img_bytes = block.get('image')
                if not img_bytes:
                    continue
                digest = (page_index, len(img_bytes), hash(img_bytes))
                if digest in seen_image_bytes:
                    continue
                seen_image_bytes.add(digest)
                ext = block.get('ext') or 'png'
                image_count += 1
                img_name = f'p{page_index:03d}_img{image_count:03d}.{ext}'
                (asset_dir / img_name).write_bytes(img_bytes)
                rel = Path('..') / 'assets' / stem_safe / img_name
                parts.append(f'\n![第 {page_index} 页图片 {image_count}]({rel.as_posix()})\n')

        for img_i, img in enumerate(page.get_images(full=True), start=1):
            xref = img[0]
            try:
                info = doc.extract_image(xref)
            except Exception:
                continue
            ib = info.get('image')
            if not ib:
                continue
            digest = (page_index, len(ib), hash(ib))
            if digest in seen_image_bytes:
                continue
            seen_image_bytes.add(digest)
            ext = info.get('ext') or 'png'
            image_count += 1
            img_name = f'p{page_index:03d}_xref{xref}_img{image_count:03d}.{ext}'
            (asset_dir / img_name).write_bytes(ib)
            rel = Path('..') / 'assets' / stem_safe / img_name
            parts.append(f'\n![第 {page_index} 页嵌入图片 {image_count}]({rel.as_posix()})\n')

    md_path.write_text('\n'.join(parts).replace('\n\n\n\n', '\n\n\n'), encoding='utf-8')
    summary.append((pdf.name, doc.page_count, text_chars, image_count, md_path.name))

print('转换完成：')
for row in summary:
    print(f'{row[0]}\tpages={row[1]}\ttext_chars={row[2]}\timages={row[3]}\tmd={row[4]}')
