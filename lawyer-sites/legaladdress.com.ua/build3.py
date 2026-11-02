"""Variant 3 (navy + gold, Prata/Nunito): builds home3.wp.html from src/home3.body.html + bz3.css."""
import pathlib, build
R = pathlib.Path(__file__).parent
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&family=Prata&display=swap">')
body = build.sub((R / "src/home3.body.html").read_text(encoding="utf-8"), False)
css = (R / "bz3.css").read_text(encoding="utf-8")
(R / "home3.wp.html").write_text(
    f"{build.HEAD}\n{FONTS}\n<style>\n{css}\n.bz3{{width:100%;margin:0;min-height:100vh}}\nhtml,body{{margin:0!important;padding:0!important;background:#F1F1F5!important}}\nhtml{{scroll-behavior:smooth}}\n</style>\n{body}",
    encoding="utf-8")
print("ok v3")
