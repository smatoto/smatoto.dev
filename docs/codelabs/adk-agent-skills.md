# Build a Skill-Powered ADK Agent

## Overview

**Duration:** 60-90 minutes | **Level:** Intermediate

In this codelab, you'll build an AI agent using Google's **Agent Development Kit (ADK)** that uses **skills** — reusable, on-demand knowledge modules — instead of cramming everything into a monolithic system prompt. By the end, your agent will dynamically load domain expertise only when it needs it, cutting baseline context usage by up to 90%.

You'll implement four skill patterns, progressively building from simple inline definitions to a self-extending agent that generates its own new skills.

### What you'll build

A blog-writing assistant agent that:

- Loads an **SEO checklist** skill defined directly in Python code
- Loads a **blog-writer** skill from a local `SKILL.md` file with reference documents
- Loads a **content-research** skill sourced from an external repository
- Loads a **skill-creator** meta-skill that generates new skill definitions on demand

### What you'll learn

- The difference between **MCP tools** (actions) and **agent skills** (knowledge)
- The **progressive disclosure** pattern: L1 metadata, L2 instructions, L3 resources
- How **SkillToolset** auto-registers `list_skills`, `load_skill`, and `load_skill_resource` tools
- Four skill patterns: inline, file-based, external, and meta-skills
- How to test and debug agents with ADK's built-in dev UI

### What you'll need

- Python 3.10+
- A Google AI API key ([Get one here](https://aistudio.google.com/apikey))
- A terminal and text editor
- Basic familiarity with Python and Markdown

---

## Step 1 — Understand the Core Concept

Before writing code, let's understand **why** skills exist.

### The problem with monolithic prompts

A typical approach to giving an agent domain knowledge is stuffing everything into the system prompt. For an agent with 10 knowledge areas, that means **~10,000 tokens loaded on every single call** — whether the user asks about SEO optimization or just says "hello."

### Progressive disclosure

Skills solve this with a three-level loading strategy:

| Level | What's loaded | When | Cost |
|-------|--------------|------|------|
| **L1 — Metadata** | Skill names + descriptions | Always (auto-injected) | ~100 tokens per skill |
| **L2 — Instructions** | Full skill content | On demand via `load_skill` | Varies per skill |
| **L3 — Resources** | Reference files, guides, specs | On demand via `load_skill_resource` | Varies per file |

**Result:** The agent starts with ~1,000 tokens of L1 metadata and loads L2/L3 content only when needed.

### Skills vs. MCP Tools

This distinction is important:

- **MCP Tools** give agents the ability to **do things** — call APIs, query databases, execute code
- **Agent Skills** give agents **knowledge** — domain expertise, guidelines, and reference material loaded on demand

Skills don't replace tools — they complement them. An agent can load a "code-review" skill for knowledge of review best practices, then use an MCP tool to actually fetch the pull request.

---

## Step 2 — Set Up Your Project

### 1. Create the project directory

```bash
mkdir -p adk-skills-lab/app/skills
cd adk-skills-lab
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate    # Windows
```

### 3. Install dependencies

```bash
pip install google-adk python-dotenv
```

### 4. Configure your API key

Create the environment file:

```bash
cat > app/.env << 'EOF'
GOOGLE_API_KEY=your-key-here
EOF
```

Replace `your-key-here` with your actual Google AI API key.

> **Important:** Don't commit API keys to version control. Add `.env` to your `.gitignore` before continuing. Alternatively, skip the file and export `GOOGLE_API_KEY` in your shell instead.

### 5. Create the package init file

```bash
cat > app/__init__.py << 'EOF'
from . import agent
EOF
```

### 6. Verify your directory structure

At this point, your project should look like this:

```
adk-skills-lab/
└── app/
    ├── __init__.py
    ├── .env
    └── skills/          # empty for now
```

---

## Step 3 — Create an Inline Skill (Pattern 1)

Inline skills are Python dictionaries defined directly in code. They're best for **small, stable rules** that don't need external files.

### 1. Create `app/agent.py` with the following content

```python
"""Blog Skills Agent — Demonstrates progressive skill loading with ADK."""

import pathlib

from google.adk import Agent
from google.adk.skills import load_skill_from_dir
from google.adk.skills import models
from google.adk.tools.skill_toolset import SkillToolset


# ---------------------------------------------------------------------------
# Pattern 1: Inline Skill — defined directly in Python code
# Best for: simple, stable rules that don't need external files
# ---------------------------------------------------------------------------
seo_skill = models.Skill(
    frontmatter=models.Frontmatter(
        name="seo-checklist",
        description=(
            "SEO optimization checklist for blog posts. Covers title tags,"
            " meta descriptions, heading structure, keyword placement,"
            " and readability best practices."
        ),
    ),
    instructions=(
        "When optimizing a blog post for SEO, check each item:\n\n"
        "1. **Title**: 50-60 chars, primary keyword near the start\n"
        "2. **Meta description**: 150-160 chars, includes a call-to-action\n"
        "3. **Headings**: H2/H3 hierarchy, keywords in 2-3 headings\n"
        "4. **First paragraph**: Primary keyword in first 100 words\n"
        "5. **Keyword density**: 1-2%, never forced or awkward\n"
        "6. **Paragraphs**: 2-3 sentences max, use bullet lists often\n"
        "7. **Links**: 2-3 internal + 3-5 external to authoritative sources\n"
        "8. **Images**: Alt text with keywords, compressed, descriptive names\n"
        "9. **URL slug**: Short, keyword-rich, hyphenated\n\n"
        "Review the content against each item and suggest specific improvements."
    ),
)
```

**Key points:**
- `name` and `description` form the **L1 metadata** — this is what the agent sees at all times
- `instructions` is the **L2 content** — loaded only when the agent calls `load_skill`
- The description should be specific enough that the LLM knows **when** to load this skill

### 2. Wire up the SkillToolset and Agent

Add the following to the bottom of `app/agent.py`:

```python
# ---------------------------------------------------------------------------
# Assemble: Package skills into a SkillToolset
# ---------------------------------------------------------------------------
skill_toolset = SkillToolset(
    skills=[seo_skill]
)

root_agent = Agent(
    model="gemini-2.5-flash",
    name="blog_skills_agent",
    description="A blog-writing agent powered by reusable skills.",
    instruction=(
        "You are a blog-writing assistant with specialized skills.\n\n"
        "When the user asks you to write, research, or optimize a blog post:\n"
        "1. Load the relevant skill(s) to get detailed instructions\n"
        "2. Use `load_skill_resource` to access reference materials\n"
        "3. Follow the skill's step-by-step instructions\n\n"
        "Always explain which skill you're using and why."
    ),
    tools=[skill_toolset],
)
```

### 3. Test it with the ADK dev UI

```bash
adk web .
```

> **Note:** Use `.` (current directory), not `app/`. This prevents ADK from discovering the `skills/` subdirectories as separate agent applications.

Open the dev UI in your browser and try this prompt:

> *"Review this blog post title for SEO: 'My Thoughts on Python'"*

**What to observe:**
- The agent calls `list_skills` to see available skills (L1)
- It calls `load_skill("seo-checklist")` to get the full instructions (L2)
- It applies the checklist to your query
- Check the **function calls** panel to see the progressive loading in action

---

## Step 4 — Create a File-Based Skill (Pattern 2)

File-based skills store knowledge in directories with a `SKILL.md` file and optional reference materials. They're best for **complex skills with supporting documents**.

### 1. Create the blog-writer skill directory

```bash
mkdir -p app/skills/blog-writer/references
```

### 2. Create `app/skills/blog-writer/SKILL.md`

```markdown
---
name: blog-writer
description: Blog post writing skill with structure templates and style guidelines. Guides the agent through writing well-structured, engaging technical blog posts with proper formatting, section flow, and reader engagement techniques.
---

# Blog Writer Instructions

When asked to write a blog post, follow these steps:

## Step 1: Structure
Use `load_skill_resource` to read `references/style-guide.md` for the writing style rules.

## Step 2: Outline First
Before writing, create a brief outline with:
- **Hook**: Opening that grabs attention (question, bold claim, or relatable problem)
- **Context**: Why this topic matters now
- **Core sections**: 3-5 sections that build on each other
- **Takeaway**: What the reader walks away knowing

## Step 3: Write Each Section
For each section:
1. Start with a clear subheading (H2)
2. Lead with the key point, then support it
3. Include code examples where relevant (use fenced code blocks with language tags)
4. Keep paragraphs to 2-3 sentences
5. Use bullet lists for steps or comparisons

## Step 4: Polish
- Add transition sentences between sections
- Ensure consistent tone throughout
- Verify all code examples are complete and runnable
- End with a clear call-to-action or next steps
```

### 3. Create `app/skills/blog-writer/references/style-guide.md`

This is the **L3 resource** — loaded only when the agent explicitly requests it:

```markdown
# Blog Writing Style Guide

## Voice
- **Conversational but authoritative** — write like you're explaining to a smart colleague
- Use "you" and "we" — never "one should"
- Share opinions backed by experience: "I've found that..." or "In practice..."

## Structure Rules
- **Title**: Action-oriented, includes the technology name (e.g., "Building X with Y")
- **Introduction**: Max 3 paragraphs. State the problem, your solution, what the reader will learn
- **Sections**: Each H2 section should be independently valuable
- **Code blocks**: Always show complete, runnable code — never pseudocode
- **Conclusion**: Summarize key points, suggest next steps, link to resources

## Formatting
- Use H2 (`##`) for main sections, H3 (`###`) for subsections
- Bold key terms on first use
- Use tables for comparisons (3+ items)
- Use numbered lists for sequential steps
- Use bullet lists for non-sequential items
- Add alt text to all images

## Anti-Patterns
- Never start with "In today's rapidly evolving..."
- Never use "leverage" when "use" works
- Never say "it's important to note that" — just state the thing
- Never write walls of text without subheadings
- Never show incomplete code snippets
```

### 4. Load the file-based skill in `agent.py`

Add this below the inline skill definition:

```python
# ---------------------------------------------------------------------------
# Pattern 2: File-Based Skill — loaded from a local directory
# Best for: complex skills with reference docs, templates, or scripts
# ---------------------------------------------------------------------------
blog_writer_skill = load_skill_from_dir(
    pathlib.Path(__file__).parent / "skills" / "blog-writer"
)
```

### 5. Update the SkillToolset to include the new skill

```python
skill_toolset = SkillToolset(
    skills=[seo_skill, blog_writer_skill]
)
```

### 6. Test the three-level loading

Restart the dev UI (`adk web .`) and try:

> *"Write a blog post about getting started with ADK"*

**What to observe:**
- The agent loads the `blog-writer` skill (L2 instructions)
- It then calls `load_skill_resource("blog-writer", "references/style-guide.md")` to get the style guide (L3)
- It follows the step-by-step writing process from the skill
- The agent applies style rules from the reference document

This is the power of progressive disclosure: the style guide is **only** loaded when the agent actually needs to write.

---

## Step 5 — Add an External Skill (Pattern 3)

External skills come from community repositories or shared team libraries. They use the exact same `SKILL.md` format — the only difference is where the files come from.

### 1. Create the content-research-writer skill directory

```bash
mkdir -p app/skills/content-research-writer/references
```

### 2. Create `app/skills/content-research-writer/SKILL.md`

```markdown
---
name: content-research-writer
description: Content research and SEO writing methodology. Guides the agent through topic research, keyword identification, competitive analysis, and writing SEO-optimized content that ranks well and provides genuine value to readers.
---

# Content Research & Writer Instructions

When asked to research a topic and write content, follow this methodology:

## Phase 1: Topic Research
1. Identify the **primary topic** and break it into subtopics
2. List 3-5 **key questions** the target audience would ask
3. Identify the **target keyword** and 3-5 related keywords
4. Note what makes this content **unique** — what angle hasn't been covered?

## Phase 2: Content Planning
1. Define the **content type**: tutorial, deep-dive, comparison, or opinion
2. Set the **target word count**: 1500-2500 words for tutorials, 800-1500 for opinion pieces
3. Plan **code examples** if technical (at least 2-3 per tutorial)
4. Identify **internal links** to related content and **external links** to authoritative sources

## Phase 3: SEO Optimization
Read `references/seo-guidelines.md` for detailed SEO rules using `load_skill_resource`.

Apply these during writing:
- Primary keyword in title, first paragraph, and 2-3 subheadings
- Natural keyword density (1-2%, never forced)
- Meta description draft (150-160 chars)
- URL slug suggestion (short, keyword-rich)

## Phase 4: Writing
1. Write the **hook** first — make the reader care in 2 sentences
2. Deliver on the **promise** of the title in every section
3. Use the **inverted pyramid**: most important info first in each section
4. End with **actionable takeaways** the reader can apply immediately

## Phase 5: Quality Check
- Does every section add unique value?
- Are all claims supported by evidence or code?
- Would you share this with a colleague? If not, what's missing?
```

### 3. Create `app/skills/content-research-writer/references/seo-guidelines.md`

```markdown
# SEO Guidelines Reference

## On-Page SEO Checklist

### Title Tag
- 50-60 characters
- Primary keyword near the beginning
- Include a power word (Build, Master, Complete, Essential)
- Format: "[Action] [Topic] with [Technology] — [Benefit]"

### Meta Description
- 150-160 characters
- Include primary keyword naturally
- End with a call-to-action or value proposition
- Make it a complete, compelling sentence

### Headings (H2/H3)
- H2 for main sections (5-8 per post)
- H3 for subsections within H2
- Include keywords in 2-3 headings naturally
- Make headings scannable — reader should understand the post from headings alone

### Content Structure
- First 100 words must include the primary keyword
- Use short paragraphs (2-3 sentences max)
- Include bullet/numbered lists every 300-400 words
- Add a table of contents for posts over 2000 words
- Bold key terms and definitions

### Internal & External Links
- 2-3 internal links to related content
- 3-5 external links to authoritative sources
- Use descriptive anchor text (not "click here")
- Open external links in new tab

### Images
- Alt text with relevant keywords
- Descriptive file names (not IMG_001.png)
- Compress to under 200KB
- Use WebP format when possible

## Keyword Strategy
- **Primary keyword**: Use 3-5 times naturally
- **Secondary keywords**: Use 1-2 times each
- **LSI keywords**: Related terms that appear naturally in good content
- **Never keyword stuff** — if it reads awkwardly, remove the keyword
```

### 4. Load the external skill in `agent.py`

Add this below the file-based skill:

```python
# ---------------------------------------------------------------------------
# Pattern 3: External Skill — loaded from a downloaded/cloned repository
# Best for: community skills, shared org standards, third-party capabilities
# Same as file-based, but the source is an external repo
# ---------------------------------------------------------------------------
content_researcher_skill = load_skill_from_dir(
    pathlib.Path(__file__).parent / "skills" / "content-research-writer"
)
```

### 5. Update the SkillToolset

```python
skill_toolset = SkillToolset(
    skills=[seo_skill, blog_writer_skill, content_researcher_skill]
)
```

### 6. Test multi-skill loading

Restart the dev UI and try:

> *"Research the topic of AI agents and write an SEO-optimized blog post about it"*

**What to observe:**
- The agent loads **multiple skills** — possibly in parallel
- It uses the content-research skill's methodology for research phases
- It pulls in SEO guidelines from the reference document
- It may also load the blog-writer skill for structure guidance

> **Tip:** Try asking about something the agent doesn't have a skill for:
> *"Can you help me design a database schema?"*
> A well-built agent will check its available skills and honestly say it doesn't have that capability — rather than hallucinating an answer.

---

## Step 6 — Create a Meta Skill (Pattern 4)

This is where it gets powerful. A **meta skill** teaches the agent how to create new skills — making it **self-extending**.

### 1. Add the skill-creator to `agent.py`

Add this below the external skill:

```python
# ---------------------------------------------------------------------------
# Pattern 4: Meta Skill — a skill that creates new skills
# Best for: self-extending agents that generate new capabilities on demand
# ---------------------------------------------------------------------------
skill_creator = models.Skill(
    frontmatter=models.Frontmatter(
        name="skill-creator",
        description=(
            "Creates new ADK-compatible skill definitions from requirements."
            " Generates complete SKILL.md files following the Agent Skills"
            " specification at agentskills.io."
        ),
    ),
    instructions=(
        "When asked to create a new skill, generate a complete SKILL.md file.\n\n"
        "Read `references/skill-spec.md` for the format specification.\n"
        "Read `references/example-skill.md` for a working example.\n\n"
        "Follow these rules:\n"
        "1. Name must be kebab-case, max 64 characters\n"
        "2. Description must be under 1024 characters\n"
        "3. Instructions should be clear, step-by-step\n"
        "4. Reference files in references/ for detailed domain knowledge\n"
        "5. Keep SKILL.md under 500 lines — put details in references/\n"
        "6. Output the complete file content the user can save directly\n"
    ),
    resources=models.Resources(
        references={
            "skill-spec.md": (
                "# Agent Skills Specification (agentskills.io)\n\n"
                "## SKILL.md Format\n"
                "Every skill directory must contain a SKILL.md file.\n\n"
                "### Frontmatter (YAML)\n"
                "```yaml\n"
                "---\n"
                "name: my-skill-name          # kebab-case, max 64 chars\n"
                "description: What this skill does.  # max 1024 chars\n"
                "---\n"
                "```\n\n"
                "### Body (Markdown)\n"
                "The body contains the skill instructions. Write clear,\n"
                "step-by-step instructions the agent will follow.\n\n"
                "### Directory Structure\n"
                "```\n"
                "my-skill-name/\n"
                "  SKILL.md           # Required: metadata + instructions\n"
                "  references/        # Optional: detailed reference docs\n"
                "  assets/            # Optional: templates, data files\n"
                "  scripts/           # Optional: executable scripts\n"
                "```\n\n"
                "### Key Rules\n"
                "- Directory name MUST match the `name` field in frontmatter\n"
                "- Name must be kebab-case: ^[a-z0-9]+(-[a-z0-9]+)*$\n"
                "- Description is what the LLM uses to decide when to load "
                "the skill\n"
                "- Keep instructions actionable — tell the agent WHAT to do\n"
                "- Use `load_skill_resource` references for detailed docs\n"
            ),
            "example-skill.md": (
                "# Example: Code Review Skill\n\n"
                "```markdown\n"
                "---\n"
                "name: code-review\n"
                "description: Reviews Python code for correctness, style, "
                "and performance. Checks for common bugs, PEP 8 compliance, "
                "and suggests optimizations.\n"
                "---\n\n"
                "# Code Review Instructions\n\n"
                "When asked to review code:\n\n"
                "## Step 1: Read the Guidelines\n"
                "Use `load_skill_resource` to read "
                "`references/review-checklist.md`.\n\n"
                "## Step 2: Analyze\n"
                "Check the code against each item in the checklist.\n\n"
                "## Step 3: Report\n"
                "Provide findings organized by severity:\n"
                "- **Critical**: Bugs, security issues\n"
                "- **Warning**: Style violations, performance concerns\n"
                "- **Info**: Suggestions for improvement\n"
                "```\n"
            ),
        }
    ),
)
```

**Key points:**
- The `resources` field provides **L3 references** — the spec and an example
- The agent reads these references to understand how to generate valid `SKILL.md` files
- Generated skills follow the [agentskills.io](https://agentskills.io) specification, making them portable across any compatible agent

### 2. Update the SkillToolset and Agent instruction

Replace your `skill_toolset` and `root_agent` definitions with the final version:

```python
# ---------------------------------------------------------------------------
# Assemble: Package all skills into a single SkillToolset
# The toolset auto-registers list_skills, load_skill, and load_skill_resource
# ---------------------------------------------------------------------------
skill_toolset = SkillToolset(
    skills=[seo_skill, blog_writer_skill, content_researcher_skill, skill_creator]
)

root_agent = Agent(
    model="gemini-2.5-flash",
    name="blog_skills_agent",
    description="A blog-writing agent powered by reusable skills.",
    instruction=(
        "You are a blog-writing assistant with specialized skills.\n\n"
        "You have four skills available:\n"
        "- **seo-checklist**: SEO optimization rules (load for SEO review)\n"
        "- **blog-writer**: Writing structure and style guide (load for writing)\n"
        "- **content-research-writer**: Research methodology (load for research)\n"
        "- **skill-creator**: Generate new skill definitions (load to create skills)\n\n"
        "When the user asks you to write, research, or optimize a blog post:\n"
        "1. Load the relevant skill(s) to get detailed instructions\n"
        "2. Use `load_skill_resource` to access reference materials\n"
        "3. Follow the skill's step-by-step instructions\n"
        "4. Apply multiple skills together when appropriate\n\n"
        "When the user asks you to create a new skill:\n"
        "1. Load the skill-creator skill\n"
        "2. Read the specification and example references\n"
        "3. Generate a complete SKILL.md that follows the spec\n\n"
        "Always explain which skill you're using and why."
    ),
    tools=[skill_toolset],
)
```

### 3. Test the meta skill

Restart the dev UI and try:

> *"Create a new skill for reviewing Python code for security vulnerabilities"*

**What to observe:**
- The agent loads the `skill-creator` skill (L2)
- It calls `load_skill_resource` to read `skill-spec.md` and `example-skill.md` (L3)
- It generates a complete, valid `SKILL.md` file you could save directly into `app/skills/`

> **Tip:** Try asking the agent to create a skill for a domain you care about — API design review, Kubernetes troubleshooting, or technical interview prep. The generated skill follows the agentskills.io spec and can be used by any compatible agent.

---

## Step 7 — Verify the Final Project

### Your complete directory structure

```
adk-skills-lab/
└── app/
    ├── __init__.py
    ├── .env
    ├── agent.py
    └── skills/
        ├── blog-writer/
        │   ├── SKILL.md
        │   └── references/
        │       └── style-guide.md
        └── content-research-writer/
            ├── SKILL.md
            └── references/
                └── seo-guidelines.md
```

### Your complete `agent.py`

The final file should contain all four skill patterns wired into a single `SkillToolset` and `Agent`. Review your file against this checklist:

- [ ] **Imports**: `Agent`, `load_skill_from_dir`, `models`, `SkillToolset`
- [ ] **Pattern 1**: `seo_skill` — inline `models.Skill` with frontmatter + instructions
- [ ] **Pattern 2**: `blog_writer_skill` — `load_skill_from_dir` pointing to `skills/blog-writer`
- [ ] **Pattern 3**: `content_researcher_skill` — `load_skill_from_dir` pointing to `skills/content-research-writer`
- [ ] **Pattern 4**: `skill_creator` — inline `models.Skill` with `resources.references`
- [ ] **SkillToolset**: All four skills packaged together
- [ ] **Agent**: Wired with the toolset and clear instructions

### Test scenarios to try

| Prompt | Expected behavior |
|--------|-------------------|
| "List your available skills" | Agent calls `list_skills`, returns L1 metadata for all 4 skills |
| "Review this title for SEO: 'Python Tips'" | Loads `seo-checklist` skill, applies the 9-point checklist |
| "Write a blog post about Docker containers" | Loads `blog-writer` + `seo-checklist`, fetches `style-guide.md` |
| "Research and write about serverless computing" | Loads `content-research-writer`, fetches `seo-guidelines.md` |
| "Create a skill for reviewing API designs" | Loads `skill-creator`, fetches spec + example references |
| "Help me design a database schema" | Checks skills, admits it doesn't have that capability |

---

## Step 8 — What's Next

Congratulations! You've built an agent that dynamically loads knowledge on demand using four skill patterns. Here's where to go from here:

### Extend the agent

- **Add more skills**: Create `SKILL.md` files for your own domains (DevOps runbooks, code review checklists, writing standards)
- **Share skills**: Skills following the [agentskills.io](https://agentskills.io) spec are portable — share them via git repositories
- **Build a team library**: Distribute standardized skills across your organization

### Explore advanced patterns

- **Script execution**: Use `RunSkillScriptTool` to let skills execute code
- **Multi-agent pipelines**: Create specialized agents with different skill sets that collaborate
- **Community skills**: Browse [awesome-claude-skills](https://github.com/anthropics/awesome-claude-skills) and ADK Core Skills for ready-made capabilities

### Resources

- [ADK Documentation](https://google.github.io/adk-docs/)
- [Agent Skills Specification](https://agentskills.io)
- [Companion Repository](https://github.com/lavinigam-gcp/build-with-adk/tree/main/adk-agent-skills-tutorial) — complete working code for this codelab
- Blog series by Lavi Nigam:
    - [Part 1: Progressive Disclosure with SkillToolset](https://lavinigam.com/posts/adk-agent-skills-part1/)
    - [Part 2: File-Based & External Skills](https://lavinigam.com/posts/adk-agent-skills-part2/)
    - [Part 3: Self-Extending Meta Skills](https://lavinigam.com/posts/adk-agent-skills-part3/)

---

## (Optional) Clean Up

To remove the project and its dependencies:

```bash
deactivate                  # exit the virtual environment
cd ..
rm -rf adk-skills-lab       # delete the project directory
```

To revoke your API key, visit [Google AI Studio](https://aistudio.google.com/apikey) and delete the key you created.
