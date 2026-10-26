<div align="center">

<img src="https://raw.githubusercontent.com/MlkBlk-IT/MlkBlk-IT/main/assets/banner.png" width="100%" alt="MALIK — AI Builder · MCP · Cyber · Homelab" />

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=15&pause=1200&color=00FF9C&center=true&vCenter=true&random=false&width=650&lines=%24+whoami+%E2%86%92+AI+builder+%7C+IT+Support+DEP+%7C+Self-taught;%24+uptime+%E2%86%92+self-taught+since+May+2026+%F0%9F%9B%A0%EF%B8%8F;%24+constraints+%E2%86%92+100%25+CPU+%C2%B7+0+GPU+%C2%B7+0+paid+API;%24+philosophy+%E2%86%92+%22The+disk+is+your+proof.%22" alt="typing" />

<br/>

## 🚀 LATEST RELEASES

<a href="https://github.com/MlkBlk-IT/icycache/releases/tag/v0.3.0">
  <img src="https://img.shields.io/badge/%F0%9F%9A%80_ICYCache_v0.3.0_%E2%9E%89_RELEASED-e10600?style=for-the-badge&labelColor=0d0d0d&logo=github&logoColor=00ff9c" height="42" alt="IcyCache v0.3.0 - released, pip and npm installable" />
</a>

<a href="https://github.com/MlkBlk-IT/Mcp-Loom/releases/tag/v0.1.1">
  <img src="https://img.shields.io/badge/%F0%9F%94%81_Mcp--Loom_v0.1.1_%E2%9E%89_RELEASED-e10600?style=for-the-badge&labelColor=0d0d0d&logo=github&logoColor=00ff9c" height="42" alt="Mcp-Loom v0.1.1 - released, pip and npm installable" />
</a>

### 🔴 `Mcp-CacheForge` &nbsp;➡️&nbsp; 🟢 [`IcyCache`](https://github.com/MlkBlk-IT/icycache) — now **v0.3.0**

**« I see cache, I burn cache »** — the LLM gateway with a semantic cache changed its name.
The old `Mcp-CacheForge` links **redirect automatically** to **IcyCache**, which is published
on GitHub Releases and installable with `pip install icycache` or `npx icycache-mcp`.

<br/>

<a href="https://github.com/MlkBlk-IT?tab=followers"><img src="https://img.shields.io/github/followers/MlkBlk-IT?label=Followers&style=for-the-badge&color=e10600&labelColor=0d0d0d&logo=github" /></a>
<a href="https://github.com/MlkBlk-IT?tab=repositories"><img src="https://img.shields.io/badge/Projects-8-00ff9c?style=for-the-badge&logo=github&logoColor=0d0d0d&labelColor=0d0d0d" /></a>
<img src="https://komarev.com/ghpvc/?username=MlkBlk-IT&label=PROFILE+VIEWS&style=for-the-badge&color=00ff9c&labelColor=0d0d0d" />
<img src="https://img.shields.io/badge/Open%20to-INTERNSHIP%20%2F%20APPRENTICESHIP-e10600?style=for-the-badge&labelColor=0d0d0d" />
<img src="https://img.shields.io/badge/Local%20AI-100%25%20CPU%20%C2%B7%200%20GPU-00ff9c?style=for-the-badge&labelColor=0d0d0d" />

</div>

---

## 🚀 Latest releases — both installable

| | Project | Install | Release |
|---|---|---|---|
| 🔴 | **[Mcp-Loom](https://github.com/MlkBlk-IT/Mcp-Loom)** | `pip install loom-mcp` · `npx loom-mcp` | [**v0.1.1**](https://github.com/MlkBlk-IT/Mcp-Loom/releases/tag/v0.1.1) |
| 🟢 | **[IcyCache](https://github.com/MlkBlk-IT/icycache)** | `pip install icycache` · `npx icycache-mcp` | [**v0.3.0**](https://github.com/MlkBlk-IT/icycache/releases/tag/v0.3.0) |

**IcyCache v0.3.0 — DELTA-002** — a universal multi-upstream gateway on `:8080` routing to **18 upstreams** (OmniRoute, LM Studio, Ollama, OpenAI, Anthropic, NVIDIA, Groq, Cerebras, OpenRouter, Copilot, …), with a normalized cache (**1122** Aho-Corasick rules, number words → digits), **11 MCP tools**, live WebSocket metrics and a 3D dashboard. New in this release: **upstream resilience** — the gateway recycles and retries instead of staying stuck on `502` — and an **opt-in semantic cache** (embeddings + Qdrant, **disabled by default**).

**Mcp-Loom v0.1.1** — **17 MCP tools** that move bulky context *out of the prompt* and into a local SQLite drawer, byte for byte. No summarization, no lossy compression in the default profile. Ships an admin CLI (`loom health`, `loom stats`, `loom vacuum`, `loom search`…) built on top of the MCP tools.

Both are **CPU-only and API-free** — the whole point. The installed package never writes into `site-packages`: data goes to `%LOCALAPPDATA%` on Windows, `~/.local/share` elsewhere.

```bash
pip install loom-mcp     # context server
pip install icycache     # LLM gateway
```

> Both ship an honest status page ([`PROGRESS.md`](https://github.com/MlkBlk-IT/Mcp-Loom/blob/main/PROGRESS.md), [`UPDATE-NOTES.md`](https://github.com/MlkBlk-IT/icycache/blob/main/UPDATE-NOTES.md)) listing what is green, what is broken, and what the next task is. **Alpha means alpha** — IcyCache's semantic cache ships disabled, and Loom's test suite is not green (83 passed / 19 failed / 1 collection error). Both are documented, not hidden.

**Discussions are open on every repo** — questions, bug reports, and "how would you use this" are all welcome.

---

## ⭐ Featured — `cat ~/flagships`

| | Project | Why it matters |
|--|---------|----------------|
| 🟢 | [**IcyCache**](https://github.com/MlkBlk-IT/icycache) <sub>(ex-CacheForge)</sub> | Local LLM proxy with **semantic cache** — Aho-Corasick normalization (1122 rules), 11 MCP tools, 18 upstreams, live metrics dashboard. Cuts token cost & latency on CPU-only setups. |
| 🔴 | [**Mcp-Loom**](https://github.com/MlkBlk-IT/Mcp-Loom) 🚧 | Moves LLM context **out of the prompt losslessly** (zero summarization). SQLite + FTS5, 17 MCP tools. |

> If you like CPU-first, no-paid-API AI engineering → **⭐ star the repos** and **follow**.

## 🧠 `what_i_do()`

IT student (IT Support DEP, EMICA Montréal) — but **AI is the direction**: agents, MCP servers, local LLM systems. Everything I ship runs **on CPU, no paid API**. First computer: **May 2026**. Self-taught by building, measuring, documenting.

<div align="center">

| Domain | Stack |
|--------|-------|
| 🤖 **AI / Agents** | MCP servers · orchestration · prompt caching · context management · CPU LoRA |
| 🧪 **ML Engineering** | PyTorch · PEFT/LoRA · dataset distillation · LM Studio · hallucination tests |
| ⚙️ **Backend** | Python · FastAPI · SQLite/FTS5 · async httpx · REST + SSE |
| 🖥️ **Systems** | Windows Server 2025 · Hyper-V · PowerShell · Linux (kernel, netns, eBPF) |
| 🔐 **Security** | Hardening · Sysmon/DFIR · forensic audits · Active Directory |
| 🎓 **Studying** | CompTIA Network+ N10-009 · Security+ SY0-701 · CCNA |

<br/>

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" />
<img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
<br/>
<img src="https://img.shields.io/badge/PowerShell-5391FE?style=for-the-badge&logo=powershell&logoColor=white" />
<img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=0d0d0d" />
<img src="https://img.shields.io/badge/Windows%20Server-0078D6?style=for-the-badge&logo=windows&logoColor=white" />
<img src="https://img.shields.io/badge/Hyper--V-0089D6?style=for-the-badge&logo=microsoft&logoColor=white" />
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />

</div>

## 🚀 Projects — `ls ~/builds`

| | Project | Pitch | Stack |
|--|---------|-------|-------|
| 🟢 | [**IcyCache**](https://github.com/MlkBlk-IT/icycache) <sub>(ex-CacheForge)</sub> | Local LLM proxy with **semantic cache** — Aho-Corasick normalization (1122 rules), MCP gateway, metrics dashboard. | Python · FastAPI · SQLite |
| 🔴 | [**Mcp-Loom**](https://github.com/MlkBlk-IT/Mcp-Loom) 🚧 | Moves LLM context out of the prompt **losslessly** (zero summary). SQLite + FTS5, 17 MCP tools. | Python · FastMCP · SQLite |
| 🟢 | [**Mcp-QadGraph**](https://github.com/MlkBlk-IT/Mcp-QadGraph) | **3D similarity dashboard** for Qdrant + read-only MCP server (9 tools). Python stdlib only. | JS · Python · Qdrant |
| 🟢 | [**OpenClaw**](https://github.com/MlkBlk-IT/OpenClaw) | Hybrid local+cloud agentic architecture — V1 (tech debt) → V2 (clean slate, machine contracts). | LM Studio · Agents |
| ⚪ | [**LoFT**](https://github.com/MlkBlk-IT/LoFT) | CPU LoRA fine-tuning (Qwen3) with dataset distillation + hallucination test runs. | PyTorch · PEFT |
| ⚪ | [**Redmi-Note-10-HomeLab**](https://github.com/MlkBlk-IT/Redmi-Note-10-HomeLab) | An Android phone turned into a **Linux server** — kernel, netns, eBPF, zram, exit-node VM. | Linux · eBPF · OpenVPN |
| ⚪ | [**Lab-SRV1**](https://github.com/MlkBlk-IT/Lab-SRV1) | Cyber lab: Hyper-V double-NAT — hardened SRV1 vs vulnerable SRV2, AD, firewall hardening. | Windows Server · PS · AD |

## 📊 By the numbers

<div align="center">
<img height="160" src="https://github-readme-stats.vercel.app/api?username=MlkBlk-IT&show_icons=true&hide_border=true&bg_color=0d0d0d&title_color=e10600&icon_color=00ff9c&text_color=c9d1d9&ring_color=e10600" />
<img height="160" src="https://github-readme-streak-stats.herokuapp.com?user=MlkBlk-IT&hide_border=true&background=0d0d0d&ring=e10600&fire=e10600&currStreakLabel=00ff9c&sideLabels=00ff9c&dates=8b949e&currStreakNum=c9d1d9" />
</div>

```text
⏱️ 5 months  self-taught (May → Oct 2026)     📦 8 projects  published
🤖 29 LLMs   benchmarked locally               💿 14 ISOs     Linux + Windows Server labs
```

> *"The disk is your proof."* — every project documented, timestamped, reproducible.

---

<div align="center">

## 🤝 Let's connect — `contact`

**Open to internships · apprenticeships · open-source collaboration.**
Montréal, QC · French / English

<a href="https://github.com/MlkBlk-IT?tab=repositories"><img src="https://img.shields.io/badge/%F0%9F%82%97_All_projects-00ff9c?style=for-the-badge&labelColor=0d0d0d" /></a>
<a href="https://github.com/MlkBlk-IT/icycache"><img src="https://img.shields.io/badge/%F0%9F%9F%80_IcyCache-e10600?style=for-the-badge&labelColor=0d0d0d" /></a>
<a href="https://github.com/MlkBlk-IT/Mcp-Loom"><img src="https://img.shields.io/badge/%F0%9F%94%81_Mcp--Loom-e10600?style=for-the-badge&labelColor=0d0d0d" /></a>

<br/><br/>

**⭐ If a project helps you → a star costs nothing and helps me a lot.**
**🔔 Follow me for the next MCP servers & CPU-only AI systems.**

<sub>
`mcp` · `mcp-server` · `local-llm` · `llm-cache` · `semantic-cache` · `prompt-caching` · `context-engineering` ·
`ai-agents` · `llm-proxy` · `qdrant` · `vector-database` · `fastapi` · `sqlite` · `python` · `cpu-only` ·
`self-hosted` · `local-first` · `homelab` · `cybersecurity` · `active-directory` · `sysmon` · `dfir` ·
`hyper-v` · `powershell` · `windows-server` · `linux-kernel` · `ebpf` · `lora` · `fine-tuning` · `pytorch` ·
`openclaw` · `loft` · `loom` · `icycache` · `cacheforge`
</sub>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00ff9c,50:1a0505,100:e10600&height=90&section=footer" width="100%" />

</div>
