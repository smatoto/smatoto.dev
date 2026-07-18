---
id: W6
title: "Foundations for Builders: Getting Started with Claude Code"
summary: "A beginner, hands-on introduction to Claude Code — the agentic loop, the feature ladder from chat to agent teams, CLAUDE.md, Plan Mode, Skills, and MCP — plus the habits that make it useful day to day."
type: Workshop
category: AI
status: Delivered
level: Beginner
duration: 75
language: English
tags: ["AI - Agents", "Claude Code", "Anthropic", "Developer Tools"]

# Event history for Impact Analytics
events:
  - name: "AI Pilipinas Meetup #33: Claude Code Masterclass"
    organizer: "AI Pilipinas (in partnership with iACADEMY)"
    date: 2026-07-18
    location: "iACADEMY Nexus Campus, 7434 Yakal, Makati City, Metro Manila, Philippines"
    attendees: 70
    url:
      name: "Event Page"
      link: "https://luma.com/oz1kt1rg"
    slides:
      name: "Slide Deck"
      link: "https://docs.google.com/presentation/d/e/2PACX-1vQbEmMM4rlb6dCEx3jUnK4I2hNT5q4zkMesdHcOMFWcGu734c2fz_ja95lVzgZ2TTUFe8aiSASswDTU/pub?start=false&loop=false&delayms=3000"

# Links for the Portfolio Site
resources:
  github:
    name: "GitHub Repository"
    link: ""
  blog:
    name: "Blog Post"
    link: ""
  recording:
    name: "Session Recording"
    link: ""

# Dynamic QR code (construct based on path)
qr_code: "https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=https://smatoto.dev/2026/claude-code-masterclass/"
---

## Abstract

Claude Code is not a chat window you paste code into — it's an agent that lives where your code lives: reading files on its own, deciding what needs to change, making the edit, and checking whether it worked. This beginner, hands-on session walks developers, researchers, and innovators through the agentic loop (Read, Decide, Act, Observe) and the feature ladder — from chat plus copy-paste, through terminal use, CLAUDE.md, Skills, Hooks and MCP, up to subagents and orchestrated agent teams — so attendees can match the right rung to the problem in front of them rather than reaching for the heaviest tool on day one.

We cover setup and a live CLI tour, how to pick the right model for a task, CLAUDE.md as the README for the AI, Plan Mode for architectural changes and unfamiliar codebases, the anatomy of a Skill (including the SKILL.md progressive-disclosure structure), the vocabulary distinction between skill, plugin, and subagent, and a fast introduction to MCP as a standard protocol for connecting Claude Code to external tools and data. The session closes with six before/after "rookie move" habit pairs — CLAUDE.md, Plan Mode, `/clear`, auto-accept, not pasting stack traces, and using Claude Code beyond bug-fixing — that even experienced users tend to miss.

Attendees leave with a working mental model of the tool, a checklist of setup steps, and habits they can apply in their very next coding session.

## Agenda

- **Opening** — who's presenting, what the session covers
- **Foundations** — what Claude Code is, the agentic loop (Read, Decide, Act, Observe), who it's for
- **Setup** — live install, a quick CLI tour, picking the right model for the job (Fable, Opus, Sonnet, Haiku)
- **The Primitive + Maturity Ladder** — the six-step loop behind every task, and the seven-rung feature ladder from chat plus copy-paste to agent teams
- **Why It Matters** — how Anthropic uses Claude Code internally, the workflow shift it enables, how it augments the SDLC, and where it runs
- **CLAUDE.md + Plan Mode** — teaching Claude your repo once; reviewing an approach before any files are touched
- **Skills** — anatomy of a Skill, prompt engineering vs. context engineering, structure of a SKILL.md file
- **Vocabulary + Subagents** — skill vs. plugin vs. subagent, and how subagents protect your main context
- **MCP** — Model Context Protocol as a standard way to connect Claude Code to external tools and data
- **Rookie Moves** — six before/after habit pairs for getting more out of Claude Code day to day
- **Closing + Q&A**

## Key Takeaways

- Claude Code is an agent, not autocomplete — it reads, decides, acts, and observes in a closed loop, and you stay in review at each step
- Match the rung to the problem: chat plus copy-paste, terminal use, CLAUDE.md, Skills and slash commands, Hooks and MCP, subagents and plugins, and agent teams are different tools for different-sized problems, not a ladder you must climb
- CLAUDE.md is the highest-leverage habit — five minutes once means every future session starts pre-briefed instead of re-explaining the repo
- Plan Mode pays off most on the changes where mistakes are costly to undo — it front-loads review before any files are touched
- A Skill is know-how (instructions); a subagent is a worker with its own context window — a subagent can use a skill, but a skill doesn't spawn anything on its own
- MCP is a standard protocol for connecting Claude Code to external tools and data sources, running under your own credentials and audit surface
- Model choice matters: Sonnet for most day-to-day work, Opus for gnarly refactors or unfamiliar codebases, Haiku for cheap and fast background work, Fable for multi-hour autonomous tasks
