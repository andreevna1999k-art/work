#!/usr/bin/env python3
"""Збирає й заливає макет блогу argument-consulting.com.ua у ЧЕРНЕТКИ. Живу головну (id 700) не чіпає.
python3 run.py            зібрати out/*.html, залити хаб і блок-превʼю
python3 run.py home [id]  створити/оновити чернетку-копію головної з шапкою і блоком"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_blog-kit'))
import kit
from config import cfg
if len(sys.argv) > 1 and sys.argv[1] == 'home':
    bk = os.path.join(cfg['dir'], f"backup-page{cfg['live_id']}-live-20261102.json")
    if not os.path.exists(bk):
        live = kit.get(cfg['site'], f"pages/{cfg['live_id']}?context=edit&_fields=meta,content,template,title"); json.dump(live, open(bk, 'w', encoding='utf-8'), ensure_ascii=False)
    live = json.load(open(bk, encoding='utf-8'))
    r, anchors = kit.home_draft(cfg, live, sys.argv[2] if len(sys.argv) > 2 else None)
    print('anchors:', anchors); print({k: r.get(k) for k in ('id', 'status', 'slug', 'code', 'message', 'raw')})
else:
    kit.build_pages(cfg); print(kit.upload_pages(cfg))
