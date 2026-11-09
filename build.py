"""将 data.json 写入 index.html 中的 const DATA（页面为单文件、可直接打开）。用法：python3 build.py"""
import json, re, pathlib
root = pathlib.Path(__file__).parent
d = json.loads((root / "data.json").read_text(encoding="utf-8"))
p = root / "index.html"
h = p.read_text(encoding="utf-8")
blob = json.dumps(d, ensure_ascii=False).replace("</", "<\\/")
h, n = re.subn(r"const DATA=.*?;\nconst STAGES", lambda m: "const DATA=" + blob + ";\nconst STAGES", h, count=1, flags=re.S)
assert n == 1, "未找到 const DATA"
p.write_text(h, encoding="utf-8")
print("index.html 已更新")
