# AI Resume Tailor

**A Python system that reads a job description, analyzes what the recruiter actually wants, and rewrites my CV to match — keyword by keyword, bullet by bullet — in one page.**

Every resume it produces is generated from this pipeline. No manual editing per job. No templates. No generic bullets. Each run starts from the job description and ends with a tailored DOCX + PDF.

---

## Why I built this

Fresh-grad job search means applying to dozens of postings a week. Each requires a slightly different CV — different keywords, different project emphasis, different tone. Doing this by hand is slow and inconsistent: you forget to bold the right words, you reuse stale bullets, you miss what the recruiter searched for.

So I built a system that does the boring part deterministically and uses an LLM for the judgement calls. It encodes rules I learned from career coaches, recruiters, and repeated failure — so every CV that leaves this pipeline passes the same bar.

---

## Architecture — 4-Agent Pipeline

```
Job Description
      │
      ▼
┌─────────────────────────┐
│ Agent 3: Analyzer       │   extracts Must-Have / Day-to-Day / Nice-to-Have
│ (keyword mining)        │   ranks which of my projects best match this job
└──────────┬──────────────┘
           ▼
┌─────────────────────────┐
│ Agent 1: Writer         │   writes About + Skills + Project bullets
│ (Claude Sonnet, CAR     │   uses exact keywords verbatim, bolds them
│  method, numbers rule)  │   every bullet: Challenge → Action → Result
└──────────┬──────────────┘
           ▼
┌─────────────────────────┐
│ Agent 2: QA Reviewer    │   checks all 21 rules before generation:
│ (rule-based gate)       │   - one page
└──────────┬──────────────┘   - numbers on every bullet
           │                  - banned tools not present
           ▼                  - hyperlinks work
┌─────────────────────────┐   - military title verbatim
│ DOCX + PDF generator    │   - GPA honest, not inflated
│ (python-docx, docx2pdf) │   - max 30% bold per section
└──────────┬──────────────┘
           ▼
┌─────────────────────────┐
│ Agent 4: Tracker        │   logs the application in Excel with
│ (OpenPyXL)              │   folder path, file names, date, status
└─────────────────────────┘
```

---

## The 21 Rules

The QA agent blocks any CV that violates these. Summarized highlights — full list in [`CV-MASTER-RULES-UPDATED.txt`](./CV-MASTER-RULES-UPDATED.txt):

1. **CAR method** — every project bullet is Challenge → Action → Result, with measurable outcome and "so what"
2. **Numbers everywhere** — every bullet has at least one concrete number (frequency, cells, yield, FPS, accuracy...)
3. **Ownership verbs** — Led, Owned, Drove, Resolved, Achieved, Delivered. Never Performed / Participated / Assisted
4. **Bold the exact job keywords** — if the posting says "troubleshooting", I bold `troubleshooting` (not "debugging"). Max 30% bold per section
5. **One page** — enforced by layout constants
6. **No banned tools** — each profile declares tools it will never claim to know; the AI cannot inject them
7. **Hyperlinks clickable** — LinkedIn + GitHub always render as links, never plain text
8. **Military title verbatim** — always the exact string, no paraphrasing
9. **Volunteering label format** — `Volunteering: <description>`
10. **GPA honest** — never inflated to meet a posting's cutoff. If the cutoff is 85 and mine is 84, the cover note addresses it honestly
11. **Every word maps to a job requirement** — Rule 21: if a sentence doesn't map to Must-Have / Day-to-Day / Soft Skills / Nice-to-Have, it's cut

---

## Keyword Intelligence

The analyzer distinguishes three tiers:

| Tier              | Treatment                                                        |
|-------------------|-------------------------------------------------------------------|
| **Exact keyword** | Used verbatim + **bolded**                                        |
| **Synonym**       | Woven naturally in the same sentence, **not bolded**              |
| **Implied task**  | Added to bullets even if not stated (e.g. "verification" implies testbench coverage, corner cases) |

Example — posting says *"troubleshooting"*:

> "Resolved timing violations through systematic **troubleshooting** and root-cause analysis."

`troubleshooting` is bolded because the recruiter searched for that exact word. `root-cause analysis` is the synonym — it reinforces meaning without double-bolding.

---

## Company DNA

Bullets are tuned per company based on what that company actually values. A few examples baked into the agents:

- **Intel** — silicon lifecycle, pre-silicon validation, systematic methodology
- **NVIDIA** — PPA optimization, edge performance, fast EDA learner
- **Elbit / defense** — mission-critical systems, multi-disciplinary integration, rigor under uncertainty
- **Applied Materials** — testing, calibration, system integration
- **HPC accelerator startups** — compute acceleration, software-defined hardware, hands-on dual design+verification

---

## Repo layout

```
ai-resume-tailor/
├── README.md                       ← you're here
├── CV-MASTER-RULES-UPDATED.txt     ← the 21 rules in full
├── matcher/
│   ├── resume_builder.py           ← DOCX + PDF renderer, AI orchestration
│   └── cv_rules.py                 ← layout constants, skill pool, styling
├── cv_agents/
│   ├── agent_orchestrator.md       ← top-level flow
│   ├── agent_1_cv_writer.md        ← content generation rules
│   ├── agent_2_qa_reviewer.md      ← 21-rule QA gate
│   ├── agent_3_project_analyzer.md ← keyword mining + project ranking
│   └── agent_4_excel_manager.md    ← tracker update logic
└── examples/
    └── profile.example.json        ← sanitized profile template
```

---

## How a CV gets built — end to end

1. **Input**: job description (text) + `profile.json` (my data)
2. **Analyze**: extract Must-Have / Day-to-Day / Nice-to-Have keywords; score projects against them
3. **Write**: Claude Sonnet generates About (3 sentences), Skills (3 grouped lines), and Project bullets (CAR format, numbers enforced)
4. **QA**: 21-rule check — any violation blocks generation with an explanation
5. **Render**: python-docx builds the DOCX with exact fonts, spacing, colors, hyperlinks
6. **Export**: docx2pdf converts to PDF
7. **Track**: Excel row added — folder path, file names, submission date, status

Each run takes ~30 seconds and produces:
- `Amos_Sarusi_CV_<JobTitle>_<Company>.docx`
- `Amos_Sarusi_CV_<JobTitle>_<Company>.pdf`
- `Amos_Sarusi_Keywords_<JobTitle>_<Company>.xlsx` (keyword coverage matrix)
- `Cover_Note_<JobTitle>_<Company>.txt`

---

## Running it yourself

This repo is primarily a reference showing how the system works. If you want to adapt it:

```bash
pip install python-docx docx2pdf anthropic openpyxl python-dotenv
cp examples/profile.example.json profile.json   # fill in your data
echo "ANTHROPIC_API_KEY=sk-ant-..." > .env
python -m matcher.resume_builder --job "path/to/job_description.txt"
```

---

## What I learned building this

- LLMs are great at rewriting bullets to emphasize a keyword, but bad at judging what NOT to include — that's what the rule engine is for.
- Rules that sound obvious ("every bullet has a number") catch 80% of bad CVs. Stating them explicitly made the AI actually follow them.
- Separating the writer from the QA reviewer matters — the writer optimizes for resonance, the reviewer enforces discipline. Bundling them into one prompt made both worse.
- Bold is a signal to the 6-second recruiter scan, not decoration. Treating it as UX changed how I write.

---

## License

MIT — fork it, adapt it for your own profile.
