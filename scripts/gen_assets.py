"""Gera o banner e os cards do README (versões clara e escura) com a marca do assisfreitas.dev.

Uso: python3 scripts/gen_assets.py   (gera os SVGs em assets/)
"""
import os
from xml.sax.saxutils import escape as e

OUT = os.path.join(os.path.dirname(__file__), "..", "assets")

THEMES = {
    "light": dict(bg="#f3efe6", soft="#ebe5d8", panel="#faf7f0", border="#d8d0bf", ink="#1c1a17", muted="#655e53", chip="#e6dfd0", accent="#c2410c"),
    "dark": dict(bg="#141311", soft="#1a1916", panel="#1e1c19", border="#34302a", ink="#ede7da", muted="#a59d8e", chip="#2a2723", accent="#f0743a"),
}
SERIF = "Fraunces, 'Iowan Old Style', 'Palatino Linotype', Georgia, serif"
SANS = "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

# Monograma AF (mesmo desenho do site, grade 64x64).
def logo(x, y, size, ink, accent, sw=6.5):
    k = size / 64
    return f'''<g transform="translate({x} {y}) scale({k})">
    <g fill="none" stroke="{ink}" stroke-width="{sw}" stroke-linecap="square" stroke-linejoin="miter">
      <path d="M10 54 L31 10 V54"/><path d="M31 10 H54"/><path d="M18 36 H48"/>
    </g>
    <rect x="46" y="47" width="8" height="8" fill="{accent}"/>
  </g>'''

ICONS = {
    "bot": '<path d="M12 8V4H8"/><rect width="16" height="12" x="4" y="8" rx="2"/><path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/>',
    "book": '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>',
    "coins": '<circle cx="8" cy="8" r="6"/><path d="M18.09 10.37A6 6 0 1 1 10.34 18"/><path d="M7 6h1v4"/><path d="m16.71 13.88.7.71-2.82 2.82"/>',
}


def banner(c):
    W, H, S = 1200, 300, 8  # S = deslocamento da sombra sólida
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <rect x="{S}" y="{S}" width="{W - S - 1}" height="{H - S - 1}" rx="14" fill="{c["ink"]}"/>
  <rect x="0.5" y="0.5" width="{W - S - 1}" height="{H - S - 1}" rx="14" fill="{c["bg"]}" stroke="{c["ink"]}"/>
  <text x="64" y="86" font-family="{MONO}" font-size="19" fill="{c["muted"]}"><tspan fill="{c["accent"]}">~/assis-freitas</tspan> $ whoami <tspan fill="{c["accent"]}">▋<animate attributeName="opacity" values="1;1;0;0" dur="1.1s" repeatCount="indefinite"/></tspan></text>
  <text x="60" y="166" font-family="{SERIF}" font-size="66" font-weight="600" fill="{c["ink"]}" letter-spacing="-1.5">Assis de Freitas<tspan fill="{c["accent"]}">.</tspan></text>
  <text x="64" y="212" font-family="{SANS}" font-size="23" fill="{c["muted"]}">Engenheiro de software sênior</text>
  <text x="64" y="250" font-family="{MONO}" font-size="16" fill="{c["muted"]}">java · spring boot · php · laravel · vue · <tspan fill="{c["accent"]}">ia</tspan></text>
  <line x1="880" y1="48" x2="880" y2="{H - S - 48}" stroke="{c["border"]}"/>
  {logo(944, 64, 164, c["ink"], c["accent"])}
</svg>'''


def card(c, title, lines, tags, icon):
    W, H, S = 400, 228, 6
    body = "".join(
        f'<text x="26" y="{110 + i * 23}" font-family="{SANS}" font-size="15.5" fill="{c["muted"]}">{e(l)}</text>'
        for i, l in enumerate(lines)
    )
    chips, x = "", 26
    for tag in tags:
        w = int(len(tag) * 7.5 + 22)
        chips += (
            f'<rect x="{x}" y="174" width="{w}" height="25" rx="12.5" fill="{c["chip"]}"/>'
            f'<text x="{x + w / 2}" y="191" text-anchor="middle" font-family="{MONO}" font-size="12" fill="{c["muted"]}">{e(tag)}</text>'
        )
        x += w + 7
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <rect x="{S}" y="{S}" width="{W - S - 1}" height="{H - S - 1}" rx="12" fill="{c["ink"]}"/>
  <rect x="0.5" y="0.5" width="{W - S - 1}" height="{H - S - 1}" rx="12" fill="{c["panel"]}" stroke="{c["ink"]}"/>
  <rect x="1" y="1" width="64" height="3" fill="{c["accent"]}"/>
  <rect x="26" y="34" width="40" height="40" rx="9" fill="{c["soft"]}" stroke="{c["border"]}"/>
  <g transform="translate(35 43) scale(0.9167)" fill="none" stroke="{c["accent"]}" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">{ICONS[icon]}</g>
  <text x="80" y="63" font-family="{SERIF}" font-size="24" font-weight="600" fill="{c["ink"]}">{e(title)}</text>
  <rect x="298" y="41" width="70" height="23" rx="11.5" fill="none" stroke="{c["border"]}"/>
  <text x="333" y="57" text-anchor="middle" font-family="{MONO}" font-size="11.5" fill="{c["muted"]}">privado</text>
  {body}
  {chips}
</svg>'''


CARDS = {
    "chico-ai": ("Chico AI", ["Assistente pessoal: agenda, e-mail,", "lembretes e digest de notícias."], ["Vue 3", "Spring AI", "Postgres"], "bot"),
    "ia-learn": ("IA Learn", ["Plataforma de aprendizado", "multi-tenant com permissões."], ["Laravel 13", "Inertia", "Vue"], "book"),
    "token-converter": ("TokenConverter", ["Conversão de tokens com contas", "de pagamento e comprovantes."], ["Laravel", "Vue", "Docker"], "coins"),
}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, c in THEMES.items():
        with open(os.path.join(OUT, f"banner-{name}.svg"), "w") as f:
            f.write(banner(c))
        for slug, (title, lines, tags, icon) in CARDS.items():
            with open(os.path.join(OUT, f"card-{slug}-{name}.svg"), "w") as f:
                f.write(card(c, title, lines, tags, icon))
    print("ok:", sorted(os.listdir(OUT)))
