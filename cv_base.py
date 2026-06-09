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
    # Embed at high resolution (no downscale) — ReportLab scales visually, stays sharp
    photo.save(buf,'JPEG',quality=95,optimize=True); buf.seek(0)
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
