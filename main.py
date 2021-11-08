# cmd.exe
# "C:\Program Files (x86)\FontForgeBuilds\bin\ffpython.exe" main.py
# API: https://fontforge.org/docs/scripting/python/fontforge.html
# Download: https://fontforge.org/en-US/
import fontforge
font = fontforge.open("font.ttf")
for name in font:
    glyph = font[name]
    fullnamepng = "./output/" + name +  ".png"
    glyph.export(fullnamepng, 1024)