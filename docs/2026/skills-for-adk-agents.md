---
id: W5
title: "Skills for ADK Agents: Optimizing Context with Progressive Disclosure"
summary: "Learn how to build efficient AI agents using ADK SkillToolset and progressive disclosure instead of massive system prompts. Discover how to reduce token consumption while optimizing agent context through layered knowledge architecture."
type: Workshop
category: AI
status: Delivered # Draft, Upcoming, or Delivered
level: Intermediate
duration: 45
language: English
tags: ["AI - Agent Development Kit (ADK)","AI - Agents","AI - Gemini","Google Cloud","Build with AI"]

# Event history for Impact Analytics
events:
  - name: "Build with AI Manila 2026: Beyond the Prompt"
    organizer: "GDG Manila"
    date: 2026-04-11
    location: "Accenture People Hub, Uptown Mall, Taguig, Philippines"
    attendees: 80
    url:
      name: "Event Page"
      link: "https://gdg.community.dev/events/details/google-gdg-manila-presents-build-with-ai-manila-2026-beyond-the-prompt/"
    slides:
      name: "Slide Deck"
      link: "https://docs.google.com/presentation/d/e/2PACX-1vRlfYmnGdoakSThoE1QwpmSKVeBH4BqLDvGsSOxP0LO3e0VQuo3hRn-J7N75IXavGnenm9UXMsKW6fa/pub?start=false&loop=false&delayms=3000"

# Links for the Portfolio Site
resources:
  codelab:
    name: "Codelab"
    link: "https://smatoto.dev/codelabs/adk-agent-skills/"
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
qr_code: "https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=https://smatoto.dev/2026/skills-for-adk-agents/"
---

## Abstract

As AI agents take on more tasks, developers often rely on massive, token-heavy system prompts to provide domain knowledge. This session presents a highly efficient alternative using the ADK SkillToolset. By breaking knowledge down into L1 metadata, L2 instructions, and L3 resources, we can implement progressive disclosure to drastically reduce token consumption. We will walk through building inline, file-based, external, and meta skills, culminating in a hands-on codelab where attendees build a fully optimized agent that pulls in expertise exactly when a task requires it.

## Outline

- **The Problem: Monolithic Prompts**
    - What AI agents are and how they work (model + tools)
    - Prompt engineering vs. context engineering: why the distinction matters
    - The U-shaped attention curve and the "lost in the middle" problem

- **The Solution: Progressive Disclosure**
    - Static context (traditional) vs. skill approach (progressive disclosure)
    - Three-tier architecture: L1 Metadata, L2 Instructions, L3 Resources
    - Structure of a SKILL.md file: YAML frontmatter + Markdown body
    - Token impact (approximate; varies by model and skill content): 20 skills = ~20,000 tokens (monolithic) vs. ~1,000 tokens (L1 only)

- **Implementation: Skill Patterns with SkillToolset**
    - Agent Development Kit (ADK): build fast, multimodal, open, scalable
    - Four skill patterns: Inline, File-Based, External, Meta
    - SkillToolset wiring: auto-generates `list_skills`, `load_skill`, `load_skill_resource` tools

- **Demo: Building Optimized Agents**
    - Hands-on codelab: Build a Skill-Powered ADK Agent
    - Requirements: Python 3.10+, Google AI API key, terminal and text editor

- **Closing: Building Your Own Optimized Agents**
    - References and further reading
    - Community resources and next steps

## Key Takeaways

- TLDL (Too Long Didn't Listen): short context = better quality, lower cost, faster responses
- Progressive disclosure loads knowledge in layers — L1 metadata always, L2 instructions on demand, L3 resources only when needed
- SKILL.md structure: YAML frontmatter (name + description) for routing, Markdown body for instructions, `references/` for deep resources
- SkillToolset automatically generates three tools that implement progressive disclosure: `list_skills`, `load_skill`, `load_skill_resource`
- Four skill patterns for different needs: Inline (quick), File-Based (production), External (community), Meta (self-extending)
- Skills follow the agentskills.io spec — portable across any compatible agent or toolchain that supports the specification

## References

- [Developer's Guide to Building ADK Agents with Skills](https://developers.googleblog.com/developers-guide-to-building-adk-agents-with-skills/)
- [ADK Agent Skills: Progressive Disclosure with SkillToolset](https://lavinigam.com/posts/adk-agent-skills-part1/)
- [Skills for ADK Agents](https://adk.dev/skills/)
- [AgentSkills Specification](https://agentskills.io/specification)
- [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Lost in the Middle: How Language Models Use Long Contexts](https://cs.stanford.edu/~nfliu/papers/lost-in-the-middle.arxiv2023.pdf)
