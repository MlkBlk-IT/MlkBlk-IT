import json, os, re, urllib.request
USER = "MlkBlk-IT"
REPOS = ["osiris", "icy-loom", "icycache", "mcp-loom-mcp"]
H = {"User-Agent": "profile-bot", "Accept": "application/vnd.github+json"}
if os.environ.get("GITHUB_TOKEN"):
    H["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=H), timeout=30) as r:
        return json.load(r)
rows = []
for repo in REPOS:
    rel = get("https://api.github.com/repos/%s/%s/releases?per_page=1" % (USER, repo))
    if rel:
        r = rel[0]
        rows.append((r["published_at"][:10], repo, r["tag_name"], r["html_url"]))
rows.sort(reverse=True)
block = "\n".join("- `%s` **[%s](%s)** %s" % (d, repo, url, tag) for d, repo, tag, url in rows)
text = open("README.md", encoding="utf-8").read()
new = re.sub(r"(<!-- releases:start -->).*?(<!-- releases:end -->)", lambda m: m.group(1) + "\n" + block + "\n" + m.group(2), text, flags=re.S)
if new != text:
    open("README.md", "w", encoding="utf-8", newline="\n").write(new)
print(block)