"""Variant 2 (light, khaki, Montserrat): builds home2.wp.html from src/home2.body.html + bz2.css."""
import pathlib, build
R = pathlib.Path(__file__).parent
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600&display=swap">')
body = build.sub((R / "src/home2.body.html").read_text(encoding="utf-8"), False)
css = (R / "bz2.css").read_text(encoding="utf-8")
(R / "home2.wp.html").write_text(
    f"{build.HEAD}\n{FONTS}\n<style>\n{css}\n.bz2{{width:100%;margin:0;min-height:100vh}}\nhtml,body{{margin:0!important;padding:0!important;background:#fff!important}}\nhtml{{scroll-behavior:smooth}}\n</style>\n{body}",
    encoding="utf-8")
print("ok v2")
