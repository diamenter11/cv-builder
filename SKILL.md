---
name: cv-generator
description: >
  Génère un CV PDF pour Nathanael Gangnimaze. Déclencheur : "cv/" suivi d'une offre.
  Enrichissement : "enrichis le skill". Fonctionne sans aucun upload préalable.
---

## Context Management (anti-token-waste)

**Nouveau chat** : exécuter le Setup (photo + cv_base.py) avant tout.
**Longue session** : NE PAS relire la conversation. Toutes les règles sont dans ce skill.
**Candidatures passées** : disponibles dans Notion (base `0b37f41a-f4f0-40ac-9f1d-524f855ff4bc`).
**État session** : ne stocker AUCUNE info dans le contexte de conversation — tout est dans le skill ou Notion.

# CV Generator — Nathanael Gangnimaze

## Setup (nouvelles sessions uniquement)
Si `/home/claude/photo_cv.png` ou `/home/claude/cv_base.py` n'existent pas :

```bash
# 1. Récupérer la photo
curl -s https://raw.githubusercontent.com/diamenter11/cv-builder/main/photo.b64 | python3 -c "import base64,sys,os; os.makedirs('/home/claude',exist_ok=True); open('/home/claude/photo_cv.png','wb').write(base64.b64decode(sys.stdin.read().strip()))"

# 2. Récupérer le template
curl -s https://raw.githubusercontent.com/diamenter11/cv-builder/main/cv_base.py -o /home/claude/cv_base.py
```
Setup complet en 2 commandes, ~1 seconde, 0 token gaspillé.
---

## Context Management (anti-token-waste)

**Nouveau chat** : exécuter le Setup (photo + cv_base.py) avant tout.
**Longue session** : NE PAS relire la conversation. Toutes les règles sont dans ce skill.
**Candidatures passées** : disponibles dans Notion (base `0b37f41a-f4f0-40ac-9f1d-524f855ff4bc`).
**État session** : ne stocker AUCUNE info dans le contexte de conversation — tout est dans le skill ou Notion.

# CV Generator — Nathanael Gangnimaze

## Setup (nouvelles sessions uniquement)
Si `/home/claude/photo_cv.png` ou `/home/claude/cv_base.py` n'existent pas, les recréer depuis les blocs ci-dessous avant toute génération.

### Photo (base64)
```python
import base64, os
os.makedirs('/home/claude', exist_ok=True)
open('/home/claude/photo_cv.png','wb').write(base64.b64decode("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"))
```

### cv_base.py
```python
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from PIL import Image
import io, json, sys, os

pdfmetrics.registerFont(TTFont('Pop',  '/usr/share/fonts/truetype/google-fonts/Poppins-Regular.ttf'))
pdfmetrics.registerFont(TTFont('PopB', '/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf'))
pdfmetrics.registerFont(TTFont('PopI', '/usr/share/fonts/truetype/google-fonts/Poppins-Italic.ttf'))
pdfmetrics.registerFont(TTFont('PopM', '/usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf'))
pdfmetrics.registerFont(TTFont('PopL', '/usr/share/fonts/truetype/google-fonts/Poppins-Light.ttf'))

W,H=A4
NAVY=(0.05,0.13,0.22);ACCENT=(0.12,0.44,0.92);GOLD=(0.79,0.66,0.30)
DARK=(0.10,0.11,0.18);MID=(0.38,0.42,0.52);LTBLUE=(0.84,0.90,0.95)
WHITE=(1,1,1);OFFWHT=(0.97,0.97,0.98)
SW=172;MX_=173;PAD=13;R_PAD=16
SB=8.2;SM=8.6;SE=9.2;SS=9.0

def sc(c,col): c.setFillColorRGB(*col)
def wrap(c,t,f,s,w):
    words=t.split(' ');lines,line=[],''
    for w2 in words:
        tt=(line+' '+w2).strip()
        if c.stringWidth(tt,f,s)<=w: line=tt
        else:
            if line: lines.append(line)
            line=w2
    if line: lines.append(line)
    return lines
def ssec(c,y,t):
    c.setFont('PopB',SB);c.setFillColorRGB(*GOLD);c.drawString(PAD,y,t.upper());y-=5
    c.setStrokeColorRGB(*GOLD);c.setLineWidth(0.8);c.line(PAD,y,SW-PAD,y);return y-9
def msec(c,y,t):
    c.setFont('PopB',SS);c.setFillColorRGB(*ACCENT);c.drawString(MX_+R_PAD,y,t.upper());y-=5
    c.setStrokeColorRGB(*ACCENT);c.setLineWidth(1.0);c.line(MX_+R_PAD,y,W-10,y);return y-13
def bull(c,x,y,text):
    bw=W-10-x-10;sc(c,DARK);c.setFont('PopB',SM+0.5);c.drawString(x,y+0.8,'•')
    c.setFont('Pop',SM);bx=x+9;lns=wrap(c,text,'Pop',SM,bw-9);lh=SM+2.2
    for i,l in enumerate(lns): c.drawString(bx,y-i*lh,l)
    return len(lns)
def exph(c,x,y,ti,co,pe):
    c.setFont('PopB',SE);sc(c,DARK);c.drawString(x,y,ti);tw=c.stringWidth(ti,'PopB',SE)
    if co:
        c.setFont('PopM',SE-0.8);sc(c,ACCENT);c.drawString(x+tw+5,y,co)
        cw=c.stringWidth(co,'PopM',SE-0.8);sx=x+tw+5+cw+5
    else: sx=x+tw+5
    c.setFont('PopI',SE-1.5);sc(c,MID);c.drawString(sx,y,pe)
def lnk(c,x,y,w,h,url): c.linkURL(url,(x,y,x+w,y+h))

def generate(data_file, out_file):
    d = json.load(open(data_file, encoding='utf-8'))

    c = canvas.Canvas(out_file, pagesize=A4)
    c.setTitle(d.get('title','CV'))

    # Backgrounds
    c.setFillColorRGB(*NAVY);  c.rect(0,0,SW,H,fill=1,stroke=0)
    c.setFillColorRGB(*WHITE); c.rect(SW,0,W-SW,H,fill=1,stroke=0)
    c.setFillColorRGB(*OFFWHT);c.rect(SW,H-90,W-SW,90,fill=1,stroke=0)

    # Photo
    photo=Image.open('/home/claude/photo_cv.png').convert('RGB')
    pw,ph=92,112; buf=io.BytesIO()
    photo.resize((pw,ph),Image.LANCZOS).save(buf,'JPEG',quality=75,optimize=True); buf.seek(0)
    px=(SW-pw)/2; py=H-14-ph
    c.drawImage(ImageReader(buf),px,py,width=pw,height=ph,preserveAspectRatio=True,mask='auto')
    c.setStrokeColorRGB(*GOLD); c.setLineWidth(1.2); c.rect(px,py,pw,ph,fill=0,stroke=1)

    sy = py - 20

    # ── SIDEBAR ──
    # Contact
    sy = ssec(c,sy,"Contact" if not d.get('en') else "Contact")
    for icon,val in [("📞", d['phone']),("✉", d['email']),("📍", d['location'])]:
        c.setFont('Pop',SB); sc(c,LTBLUE); lt=icon+"  "+val
        if c.stringWidth(lt,'Pop',SB)>SW-2*PAD and '@' in val:
            c.drawString(PAD,sy,icon+"  "+val[:val.index('@')]); sy-=SB+2.5
            c.drawString(PAD+12,sy,val[val.index('@'):])
        else: c.drawString(PAD,sy,lt)
        sy-=SB+3.5
    c.setFont('PopM',SB); c.setFillColorRGB(0.42,0.70,0.95); c.drawString(PAD,sy,"🔗  LinkedIn")
    lnk(c,PAD,sy-2,c.stringWidth("🔗  LinkedIn",'PopM',SB)+4,SB+2,"https://www.linkedin.com/in/nathanael-gangnimaze/")
    sy-=SB+6

    # Languages
    lang_title = "Languages" if d.get('en') else "Langues"
    sy = ssec(c,sy,lang_title)
    for l in d['languages']:
        c.setFont('Pop',SB); sc(c,LTBLUE); c.drawString(PAD,sy,l); sy-=SB+3.5
    sy-=3

    # Skills
    skills_title = "Skills" if d.get('en') else "Compétences"
    sy = ssec(c,sy,skills_title)
    for theme,items in d['skills']:
        c.setFont('PopB',SB-0.2); c.setFillColorRGB(*GOLD); c.drawString(PAD,sy,theme); sy-=SB+1.5
        lns=wrap(c,"  ·  ".join(items),'PopL',SB-0.8,SW-2*PAD-4)
        c.setFont('PopL',SB-0.8); sc(c,LTBLUE)
        for ln in lns: c.drawString(PAD+4,sy,ln); sy-=SB+1.5
        sy-=3

    # Certs
    cert_title = "Certifications"
    sy = ssec(c,sy,cert_title)
    for line in d['certs']:
        c.setFont('Pop',SB-0.4); sc(c,LTBLUE); c.drawString(PAD,sy,line); sy-=SB+3.5
    sy-=3

    # Qualities
    qual_title = "Qualities" if d.get('en') else "Qualités"
    sy = ssec(c,sy,qual_title)
    for q in d['qualities']:
        c.setFont('Pop',SB); sc(c,LTBLUE); c.drawString(PAD+3,sy,"·  "+q); sy-=SB+3.5
    sy-=3

    # Interests
    int_title = "Interests" if d.get('en') else "Centre d'intérêt"
    sy = ssec(c,sy,int_title)
    c.setFont('Pop',SB); sc(c,LTBLUE)
    awale_txt = "♟  Strategy games — Awalé" if d.get('en') else "♟  Jeux de stratégie — Awalé"
    c.drawString(PAD,sy,awale_txt); sy-=SB+3
    c.setFont('PopM',SB-0.5); c.setFillColorRGB(0.42,0.70,0.95); c.drawString(PAD+6,sy,"clubawale.com")
    lnk(c,PAD+6,sy-2,c.stringWidth("clubawale.com",'PopM',SB-0.5)+4,SB+2,"https://www.clubawale.com")
    sy-=SB+3; c.setFont('Pop',SB); sc(c,LTBLUE)
    cinema_txt = "🎬  Cinema" if d.get('en') else "🎬  Cinéma"
    c.drawString(PAD,sy,cinema_txt)

    # ── MAIN ──
    mx=MX_+R_PAD; mw=W-10-mx
    ny=H-20; c.setFont('PopB',24); sc(c,NAVY); c.drawString(mx,ny,"Nathanael Gangnimaze"); ny-=20
    c.setFont('PopI',11); sc(c,MID); c.drawString(mx,ny,d['job_title'])
    c.setStrokeColorRGB(*GOLD); c.setLineWidth(1.5); c.line(mx,ny-4,mx+mw,ny-4); ny-=18

    # Profil
    c.setFont('Pop',8.4); sc(c,MID)
    for l in wrap(c,d['profil'],'Pop',8.4,mw): c.drawString(mx,ny,l); ny-=11.5
    ny-=8

    # Formation
    edu_title = "Education" if d.get('en') else "Formation"
    ny = msec(c,ny,edu_title)
    for ti,sc_,pe in d['education']:
        c.setFont('PopB',SS); sc(c,DARK); c.drawString(mx,ny,ti)
        c.setFont('Pop',SS-1); sc(c,MID); c.drawString(mx+4,ny-13,sc_+"  •  "+pe); ny-=33
    ny-=8

    # Experiences
    exp_title = "Professional Experience" if d.get('en') else "Expériences Professionnelles"
    ny = msec(c,ny,exp_title)
    lh=SM+2.2
    for exp in d['experiences']:
        exph(c,mx,ny,exp['t'],exp['co'],exp['p']); ny-=17
        for b in exp['b']: n=bull(c,mx+2,ny,b); ny-=n*lh+4
        ny-=13
    ny-=4

    # Projects
    proj_title = d.get('projects_title', "Data Projects" if d.get('en') else "Projets Data")
    ny = msec(c,ny,proj_title)
    for proj in d['projects']:
        exph(c,mx,ny,proj['t'],"",proj['p']); ny-=17
        for b in proj['b']: n=bull(c,mx+2,ny,b); ny-=n*lh+4
        ny-=13

    c.save()
    print(f"Done — bottom {ny:.1f}pt — size: {os.path.getsize(out_file)//1024}K")

if __name__=="__main__":
    generate(sys.argv[1], sys.argv[2])

```

---

## Workflow en 4 étapes (optimisé tokens)

### ÉTAPE 1 — Compression de l'offre (JD Compressor)
Avant toute chose, extraire uniquement :
```
INTITULÉ: [titre simplifié]
CONTRAT: [CDI/Alternance/Stage]
VILLE: [ville] → IDF? → "Paris" sinon ville exacte
STACK: [outils/langages mentionnés]
MISSIONS: [3-5 mots-clés des missions principales]
EXCLUSIONS: [technos à ne pas mettre]
```
Ne jamais traiter l'offre brute — toujours compresser d'abord.

### ÉTAPE 2 — 4 questions (si infos manquantes après compression)
Poser uniquement ce qui n'est pas dans la JD compressée :
1. Intitulé → proposer, valider
2. Exclusions supplémentaires ?
3. Indication personnelle ?
4. Mobilité (si ville absente de l'offre)
**Si pas de réponse = oui par défaut.**

### ÉTAPE 3 — Générer le PATCH JSON (diff uniquement)
Partir du blueprint ci-dessous. Ne générer **que les champs qui changent** :
```json
{
  "location": "...",
  "job_title": "...",
  "profil": "...",
  "skills": [...],          ← si stack différente du blueprint
  "experiences[1].t": "...",← intitulé SID adapté
  "experiences[1].b": [...],← bullets SID reformulés
  "projects_title": "...",
  "projects": [...]
}
```
**Ne jamais réécrire** : education, languages, certs, qualities, photo, contact, La Poste (sauf intitulé), Building Cluster.

### ÉTAPE 4 — Générer et livrer
1. Merger le patch sur le blueprint → écrire le JSON complet
2. `python3 /home/claude/cv_base.py /home/claude/cv_data.json /home/claude/CV_OUT.pdf`
3. Copier vers outputs, livrer
4. Ajouter dans Notion (parent: `0b37f41a-f4f0-40ac-9f1d-524f855ff4bc`)
5. Annoncer le % de correspondance

---

## Blueprint (base fixe — ne jamais réécrire dans les patches)

```json
{
  "en": false,
  "phone": "07 51 14 94 17",
  "email": "nathanaelgangnimaze@gmail.com",
  "languages": ["Français — natif", "Anglais — TOEIC B2"],
  "certs": ["Google Data Analytics (2024)", "AWS Data Engineer — En cours"],
  "qualities": ["Curieux","Autonome","Sociable"],
  "education": [
    ["Mastère Spécialisé Data & IA for Business","EFREI, Villejuif","2026 – 2027"],
    ["M2 — Data Engineering & IA","EFREI, Villejuif","2024 – 2026"],
    ["Bachelor — Conception des Systèmes d'Information","IUC, Douala","2023 – 2024"]
  ],
  "experiences": [
    {
      "t":"[ADAPTER À L'OFFRE] – Alternance","co":"La Poste","p":"Sept. 2025 – Déc. 2025",
      "b":[
        "Ingestion des données sur la plateforme interne et alimentation des flux de données",
        "Maintenance du catalogue de données : mise à jour des métadonnées, contrôle qualité et documentation",
        "Proposition de KPIs métier et conception de tableaux de bord Power BI à destination des équipes opérationnelles",
        "Requêtage SQL pour l'extraction et la transformation des données à des fins d'analyse et de reporting"
      ]
    },
    {
      "t":"Stagiaire Data Analyst","co":"SID Conseil","p":"Jan. 2024 – Juil. 2024",
      "b":["[TOUJOURS ADAPTER CES BULLETS À L'OFFRE]"]
    },
    {
      "t":"Développeur Web Full Stack – Stage","co":"Building Cluster Company","p":"Jan. 2023 – Juin 2023",
      "b":["Développement d'une plateforme de gestion des archives et cours en ligne (Node.js, Express.js, MongoDB, API RESTful)"]
    }
  ],
  "projects_title": "Projets Data",
  "projects": ["[TOUJOURS ADAPTER AUX MISSIONS DE L'OFFRE — sources publiques uniquement]"]
}
```

### Stack par défaut (modifier seulement si l'offre l'exige)
```
Langages        : Python · SQL · DAX
Analyse & BI    : Power BI · PowerQuery · Excel
Transformation  : ETL/ELT · Pandas · DBT
Bases de données: PostgreSQL · SQL Server · Oracle · MongoDB
Modélisation    : Data Warehouse · Lakehouse
Orchestration   : Airflow · DBT · Git
Gouvernance     : Qualité des données · Data Catalog · Data Regulation
```
**Jamais** : NumPy · MySQL · Superset · Ingestion API dans Orchestration · Spark/FastAPI dans Orchestration

---

## Règles métier (condensées)

**Contrat/Profil** :
- CDI → `"Étudiant en M2 Data Engineering & IA (EFREI), je recherche un CDI en [intitulé]"`
- Alternance → `"Étudiant en M2 Data Engineering & IA (EFREI), je recherche une alternance d'un an pour débuter mon Mastère Spécialisé Data & IA for Business. Rythme : 2 semaines en entreprise / 1 semaine à l'école (EFREI) ou 4 jours en entreprise / 1 jour à l'école (OpenClassrooms). Disponible dès septembre."`
- Stage → `"Étudiant en M2 Data Engineering & IA (EFREI), je recherche un stage en [intitulé], disponible du 10 juillet à novembre"`
- Finance → ajouter `"Passionné par la finance, je souhaite mettre mes compétences data au service d'enjeux financiers concrets."` si poste finance
- **Jamais "pour valider"** · **Toujours M2** (jamais Master 2)

**Localisation** : IDF → "Paris" · Hors IDF → ville exacte · Pas de ville → demander

**La Poste** : intitulé adaptable, bullets INCHANGEABLES :
- Ingestion données plateforme interne
- Maintenance catalogue de données
- Proposition KPIs + dashboards Power BI
- Requêtage SQL

**SID Conseil** : enrichir librement, cohérent stage data/conseil

**Projets** : 2 projets · sources publiques UNIQUEMENT (Kaggle, Yahoo Finance, INSEE, SNCF Open Data, data.gouv.fr, DARES, ACPR...) · 3 bullets min · impact mesurable · reproductibles avant entretien

**Correspondance** : 80-85% cible · jamais 100% · garder 2-3 technos hors offre

**Notion** : ajouter à chaque CV · parent_id: `0b37f41a-f4f0-40ac-9f1d-524f855ff4bc` · date = aujourd'hui · colonnes: Entreprise, Poste, Contrat, Statut, Projets présentés, Stack mise en avant, Lien offre, Date candidature

---

## Enrichissement du skill
Si "enrichis le skill" ou "mets à jour le skill" :
1. Modifier ce fichier
2. `cd /home/claude && zip -r /mnt/user-data/outputs/cv-generator.skill cv-generator/`
3. `present_files`

