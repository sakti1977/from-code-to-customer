# Latest: what has changed since the book was printed

The printed book (First Edition, November 2026) teaches patterns that last. Tool
names and standards move faster than print. This page is the living layer:
newest entries first, each with a primary source. Last reviewed: **8 November 2026**.

> Rule of thumb: patterns last, tool names expire. Before you rely on any entry,
> open the primary source and check its date.

## How to read an entry
Each entry says what changed, why a builder should care, and which of the book's
five questions it touches (Reach, Power, Ground, Verdict, Carry).

## November 2026 review

| Topic | What to know | Five questions | Primary source |
|---|---|---|---|
| MCP (Model Context Protocol) | The 2026-07-28 specification made the protocol stateless, added header-based routing, hardened authorization and moved long-running Tasks into an extension. Read the current spec, not an older tutorial. | Reach, Power | https://blog.modelcontextprotocol.io/posts/2026-07-28/ |
| MCP security | OWASP publishes an MCP Top 10 (beta) and an MCP Security Cheat Sheet. Treat tool descriptions and tool results as untrusted data. | Power, Ground | https://owasp.org/projects/mcp-top-10 and https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html |
| Agent Skills | Published as an open standard in December 2025; donated to the Agentic AI Foundation in October 2026. A skill is a folder with a `SKILL.md`. Install only from sources you trust. | Power, Carry | https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills |
| AGENTS.md | An open, README-style file for coding agents, now stewarded by the Agentic AI Foundation. | Carry | https://agents.md/ |
| Agentic AI Foundation | Added Agent Skills, Open Responses, OpenEnv and OpenSandbox on 22 October 2026. | Power, Verdict | https://www.linuxfoundation.org/press/agentic-ai-foundation-announces-four-new-projects-agent-skills-open-responses-openenv-and-opensandbox |
| Context engineering | Treat what the model sees as an engineering surface: instructions, tools, retrieval, memory, history. | Reach, Carry | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents |
| Long-running agents | Setup session plus small steps that leave notes; separate the model loop, the sandbox and the session log. | Carry | https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents and https://www.anthropic.com/engineering/managed-agents |
| Agent security | OWASP Top 10 for Agentic Applications (2026). | Reach, Power | https://genai.owasp.org/owasp-genai-frameworks/owasp-top-10-for-agentic-applications-2026/ |
| Evals | Repeat runs, read traces, report a pass-all rate; do not trust one lucky run. | Verdict | https://hamel.dev/blog/posts/evals-faq/ |

## A note on older articles
Anthropic's *Building effective agents* (December 2024) now carries a note that
much of its tooling description has changed since publication. Its patterns
(simple workflows before agents, composable steps) still hold.
https://www.anthropic.com/research/building-effective-agents

## How this page is kept current
- Open an issue or pull request with: the change, the date, the primary source.
- Do not add a claim without a primary source. Do not paste long passages from
  other publishers; link and summarise in your own words.
- Entries older than twelve months are re-checked or removed at each review.

## Book errata
- None yet. Corrections to the First Edition will be listed here with the page number.
