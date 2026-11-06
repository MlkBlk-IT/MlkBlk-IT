"""Corrige la ligne 'What's new' d'OSIRIS dans le profil GitHub.

Remplace la ligne v0.1.2 (backticks echappes par un passage PowerShell et
double point dans le paragraphe 'By the numbers') par une version propre.

    python scripts/fix_osiris_row.py
"""

from __future__ import annotations

import pathlib
import re

README = pathlib.Path(__file__).resolve().parents[1] / "README.md"

ROW = (
    "| **2026-11-06** | **[Osiris](https://github.com/MlkBlk-IT/osiris) v0.1.2** | "
    "Release hardening: npm publication fixed (setup-node `registry-url` was writing an empty "
    "`_authToken`, skipping the OIDC exchange and producing an anonymous PUT 404 — the OIDC "
    "exchange is now verified before publish, npm pinned to v11); dashboard refuses any "
    "non-loopback bind unless `--allow-remote` + token, and `/api/*` returns 401 without it; "
    "SQLite schema versioned by `PRAGMA user_version` with numbered transactional migrations "
    "(a failed migration rolls back instead of being swallowed); CI matrix on Windows + Linux "
    "× Python 3.12/3.13; and the distributed wheel is now tested after a clean install "
    "(it was missing `liquid.css` and `live.js`). **146 tests.** "
    "[Release](https://github.com/MlkBlk-IT/osiris/releases/tag/v0.1.2) |"
)


def main() -> int:
    text = README.read_text(encoding="utf-8")
    original = text

    # 1. Ligne 'What's new' d'OSIRIS v0.1.2.
    # Elle a ete coupee en deux par un retour chariot parasite : on matche
    # sur la ligne complete (avec CR eventuel) puis on remplace.
    pattern = re.compile(
        r"^\| \*\*2026-11-06\*\* \| \*\*\[Osiris\]\(https://github\.com/MlkBlk-IT/osiris\) v0\.1\.2\*\* \|.*?"
        r"(?:egistry-url.*?)?$",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(text)
    if not match:
        print("ligne What's new OSIRIS v0.1.2 introuvable")
        return 1
    # La coupee peut avoir laisse une ligne orpheline juste apres.
    end = match.end()
    tail = text[end:]
    if tail.startswith("egistry-url"):
        cut = tail.find("\n")
        tail = tail[cut + 1 :] if cut != -1 else ""
        end += cut + 1
    text = text[: match.start()] + ROW + tail

    # 1b. Ligne orphelin : le reste de l'ancienne ligne (qui debordait sur
    # une 2e ligne a cause d'un retour chariot parasite).
    text = re.sub(r"^egistry-url.*$\n?", "", text, flags=re.MULTILINE)

    # 2. Double point dans le paragraphe 'By the numbers'.
    text = text.replace("— 146 tests..", "— 146 tests.")

    if text == original:
        print("README deja correct")
        return 0

    README.write_text(text, encoding="utf-8", newline="")
    print("README corrige")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
