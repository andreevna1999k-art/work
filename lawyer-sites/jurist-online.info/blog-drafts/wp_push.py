import json, subprocess, pathlib
SITE = "https://jurist-online.info"
def curl(method, path, data=None, headers=None, binary=None):
    cmd = ["curl", "-s", "-X", method, SITE + "/?rest_route=/wp/v2/" + path]
    for h in (headers or []): cmd += ["-H", h]
    if binary: cmd += ["--data-binary", "@" + binary]
    elif data is not None: cmd += ["-H", "Content-Type: application/json", "--data-binary", "@-"]
    r = subprocess.run(cmd, input=(json.dumps(data) if data is not None and not binary else None), capture_output=True, text=True)
    try: return json.loads(r.stdout)
    except Exception: raise SystemExit("bad response: " + r.stdout[:300])

def run(ART, meta, render, R):
    mp = R / "wp-ids.json"
    for a in ART:
        key = a["slug"]; info = meta.setdefault(key, {})
        if "media_id" not in info:
            fn = a["img"].name
            m = curl("POST", "media", headers=["Content-Type: image/webp", f"Content-Disposition: attachment; filename={fn}"], binary=str(a["img"]))
            assert "id" in m, m
            info["media_id"] = m["id"]; info["img_url"] = m["source_url"]
            curl("POST", f"media/{m['id']}", data={"alt_text": a["alt"], "title": a["_P"]["h1"]})
            print("media", m["id"], m["source_url"])
        if "id" not in info:
            r = curl("POST", "pages", data={"title": a["_P"]["h1"], "slug": key, "status": "future", "parent": 2675, "template": "elementor_canvas",
                                           "date": a["date"] + "T09:00:00", "content": "<p>shell</p>"})
            assert "id" in r, r
            info["id"] = r["id"]; print("page", r["id"], r["status"], r["date"])
        mp.write_text(json.dumps(meta, ensure_ascii=False, indent=1))
        page, st = render(a, a["_P"], img_url=info["img_url"], pid=info["id"])
        (R / "preview" / f"{a['n']:02d}-{a['slug']}.html").write_text(page, encoding="utf-8")
        r = curl("POST", f"pages/{info['id']}", data={"title": a["_P"]["h1"], "slug": key, "status": "future", "parent": 2675, "template": "elementor_canvas",
                 "date": a["date"] + "T09:00:00", "content": page, "excerpt": a["_P"]["desc"], "featured_media": info["media_id"]})
        assert r.get("id") == info["id"], r
        print("updated", r["id"], r["status"], r["date"], r["date_gmt"], r["link"])
