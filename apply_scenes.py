from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).parent))
from scenes_a import S as SA
from scenes_b import S as SB
from scenes_c import S as SC
from scenes_e import S as SE
from scenes_f import S as SF
import scenes_d as SD
S={**SA,**SB,**SC,**SE,**SF,**SD.S}
root=Path(__file__).parent; pages=root/'pages'
if not pages.exists():
    raise SystemExit('run generate.py first to create items/pages')
items=[p.name.split('-',1) for p in sorted(pages.glob('*.html'))]
titles={'01':'Orbit Desk','02':'Morrow Coffee','03':'Northstar Studio','04':'Field Notes','05':'Lumen House','06':'Packet Zero','07':'Soft Signal','08':'Common Thread','09':'Good Measure','10':'Wild Fig','11':'Relay','12':'Ember Objects','13':'Cedar & Co','14':'The Long View','15':'Cloudline','16':'Signal Fire','17':'Aster','18':'Good Company','19':'Ledgerly','20':'Sunday Index','21':'Tandem','22':'Woven','23':'Brightwork','24':'After Hours','25':'Mile Marker','26':'Rook','27':'Tidepool','28':'Open Door','29':'Gauge','30':'The Kitchen Table','31':'Hearth','32':'Vale','33':'Keystone','34':'Small Hours','35':'Vector','36':'Good Friction','37':'Mica','38':'The Assembly','39':'Plainspoken','40':'Field Guide','41':'Arc','42':'Nook','43':'Counterpart','44':'The Margin','45':'Pace','46':'Harbor','47':'Melt','48':'Gather','49':'True North','50':'The Index Card','51':'Lantern','52':'Stonefruit','53':'Clearwater','54':'The Workshop','55':'Loop','56':'Ironwood','57':'Kite','58':'Commonplace','59':'Bloom','60':'Night School','61':'Prism','62':'Brass & Pine','63':'Mainspring','64':'Westward','65':'Nest','66':'Redwood','67':'Fable','68':'The Commons','69':'Pulse','70':'Low Tide','71':'Canvas','72':'Juniper','73':'Second Wind','74':'The Practical','75':'Drift','76':'Anchor Point','77':'Alto','78':'The Table','79':'Northwind','80':'The Commonplace','81':'Foundry','82':'Sea Glass','83':'Good Signal','84':'The Quiet Office','85':'Current','86':'Bluebird','87':'Orchard','88':'The Relay','89':'Compass','90':'The Open Road','91':'Studio 9','92':'Kindred','93':'Switchboard','94':'The Bright Hour','95':'Monument','96':'Basin','97':'First Principles','98':'The Ledger','99':'Mosaic','100':'Daybreak'}
themes=[('#0b1020','#f6c453','#f7f4ed','Space Grotesk'),(' #151515','#ff6b4a','#fff7f1','DM Sans'),('#102a24','#b8e986','#eff8ee','Manrope'),('#f4eee4','#a64b2a','#1f2937','Fraunces'),('#21143b','#e5b8ff','#fff8ff','Syne'),('#062d45','#63d8e6','#f3fbfc','Sora'),('#30110d','#f5a25d','#fff5e9','Libre Baskerville'),('#191d29','#a7b5ff','#f4f5ff','IBM Plex Sans'),('#2a1d12','#e8c27d','#fffaf0','Cormorant Garamond'),('#101a16','#f2f0df','#f8f8f1','Plus Jakarta Sans')]
kinds={}
for i,(num,slug) in enumerate(items):
    num=num.strip()
    kind=['saas','product','service','blog'][i%4]
    bg,accent,paper,font=themes[i%len(themes)]; bg=bg.strip()
    title=titles.get(num)
    if not title: print('no title',num); continue
    scene=S.get(num)
    if not scene: print('NO SCENE for',num); continue
    tagline={'saas':'Software with a point of view','product':'Made well. Made once.','service':'Help that actually helps','blog':'Words worth your time'}[kind]
    desc={'saas':'A small, thoughtful tool built by people who use it every day — no dashboards for the sake of dashboards.',
          'product':'Designed slowly, made carefully, and priced honestly. Fewer things, chosen well.',
          'service':'Senior help without the agency theater. You work directly with the person doing the work.',
          'blog':'Essays and notes published when there is something real to say — never on a content calendar.'}[kind]
    cta={'saas':'Start free','product':'Browse the shop','service':'Book an intro call','blog':'Read the latest'}[kind]
    fn=f'{num}-{title.lower().replace(" ","-").replace("&","and")}.html'
    html_doc=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} — {tagline}</title><meta name="description" content="{desc}"><link href="https://fonts.googleapis.com/css2?family={font.replace(' ','+')}:wght@400;500;600;700;800&display=swap" rel="stylesheet"><style>
:root{{--bg:{bg};--accent:{accent};--paper:{paper}}}*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--paper);font-family:'{font}',sans-serif;overflow-x:hidden}}
nav{{display:flex;justify-content:space-between;align-items:center;padding:26px 6vw;font-size:14px}}.logo{{font-weight:800;font-size:20px;letter-spacing:-.03em}}nav a{{color:inherit;text-decoration:none;margin-left:22px;opacity:.72}}nav a:hover{{opacity:1}}
.hero{{min-height:calc(100vh - 84px);display:flex;align-items:center;justify-content:center;gap:min(7vw,90px);padding:60px 6vw;flex-wrap:wrap}}
.copy{{max-width:520px}}.eyebrow{{text-transform:uppercase;letter-spacing:.22em;font-size:11px;color:var(--accent);font-weight:700}}h1{{font-size:clamp(2.7rem,6vw,4.6rem);line-height:.98;letter-spacing:-.05em;margin:18px 0 20px}}.lead{{font-size:1.08rem;opacity:.78;line-height:1.6;margin-bottom:30px}}
.cta{{display:inline-block;background:var(--accent);color:{bg};padding:15px 28px;border-radius:999px;text-decoration:none;font-weight:700;transition:transform .25s,box-shadow .25s}}.cta:hover{{transform:translateY(-3px);box-shadow:0 12px 32px {accent}66}}
.stage{{flex:0 0 auto;display:flex;align-items:center;justify-content:center}}
.strip{{background:var(--paper);color:{bg};padding:16px 6vw;display:flex;gap:6vw;justify-content:center;font-size:12px;letter-spacing:.09em;text-transform:uppercase;flex-wrap:wrap}}
.below{{padding:80px 8vw;display:grid;grid-template-columns:repeat(3,1fr);gap:18px;background:var(--paper);color:{bg}}}.below h3{{margin:.4rem 0}}.card{{border-left:3px solid {accent};padding-left:18px}}@media(max-width:900px){{.below{{grid-template-columns:1fr}}.hero{{min-height:auto;padding-top:20px}}}}
footer{{padding:34px 6vw;font-size:13px;opacity:.6;text-align:center}}
</style></head><body>
<nav><div class="logo">{title}</div><div><a href="#story">Story</a><a href="#contact">Contact</a></div></nav>
<main class="hero">
  <div class="copy"><div class="eyebrow">{kind} · no. {int(num)}</div><h1>{title}</h1><p class="lead">{tagline}. {desc}</p><a class="cta" href="#contact">{cta}</a></div>
  <div class="stage">{scene}</div>
</main>
<div class="strip"><span>Independent</span><span>Small batch</span><span>Built to last</span></div>
<section class="below" id="story">
<div class="card"><h3>Why we exist</h3><p>Because most options in this space are loud, complicated, or indifferent. This is the quiet alternative.</p></div>
<div class="card"><h3>How it works</h3><p>Simple onboarding, clear pricing, and a direct line to a human who can actually change something.</p></div>
<div class="card" id="contact"><h3>Say hello</h3><p><a style="color:inherit" href="mailto:hello@example.com">hello@example.com</a> — real replies, usually within a day.</p></div>
</section>
<footer>© 2026 {title} · A concept page from the 100 Living Landings gallery</footer>
</body></html>'''
    (pages/fn).write_text(html_doc)
print('rewrote',len(items),'pages with bespoke scenes')
