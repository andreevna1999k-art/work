#!/usr/bin/env python3
"""photos-src/NN-*.webp (1536x1024) -> photos/<slug>.webp 760x507 (3:2), q74. Нумерація NN = № статті."""
import os, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from articles import ARTICLES
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); os.makedirs(os.path.join(H,'photos'), exist_ok=True)
for a in ARTICLES:
    f = glob.glob(os.path.join(H, 'photos-src', f'{a[0]:02d}-*.webp'))[0]
    im = Image.open(f).convert('RGB').resize((760,507), Image.LANCZOS)
    im.save(os.path.join(H,'photos',a[2]+'.webp'), quality=74, method=6)
print('ok', sum(os.path.getsize(p) for p in glob.glob(os.path.join(H,'photos','*.webp')))//1024, 'KB')
