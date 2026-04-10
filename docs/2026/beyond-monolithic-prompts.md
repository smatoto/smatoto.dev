---
id: W5
title: "Beyond Monolithic Prompts: Optimizing Agent Context with Progressive Disclosure"
summary: "Learn how to build efficient AI agents using ADK SkillToolset and progressive disclosure instead of massive system prompts. Discover how to reduce token consumption while optimizing agent context through layered knowledge architecture."
type: Talk
category: AI
status: Draft # Draft, Upcoming, or Delivered
level: Intermediate
duration: 40
language: English
tags: ["google-cloud", "gde", "google-developer-expert"]

# Delivery history for Impact Analytics
deliveries:
  - event: "Build with AI Manila 2026: Beyond the Prompt"
    organizer: "GDG Manila"
    date: 2026-04-11
    location: "Accenture People Hub, Uptown Mall, Taguig, Philippines"
    attendees: 0
    url:
      name: "Event Page"
      link: "https://gdg.community.dev/events/details/google-gdg-manila-presents-build-with-ai-manila-2026-beyond-the-prompt/"
    slides:
      name: "Slide Deck"
      link: "https://docs.google.com/presentation/d/e/2PACX-1vRlfYmnGdoakSThoE1QwpmSKVeBH4BqLDvGsSOxP0LO3e0VQuo3hRn-J7N75IXavGnenm9UXMsKW6fa/pub?start=false&loop=false&delayms=3000"

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
qr_code: "https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=https://smatoto.dev/2026/beyond-monolithic-prompts/"
---

## Abstract

As AI agents take on more tasks, developers often rely on massive, token-heavy system prompts to provide domain knowledge. This session presents a highly efficient alternative using the ADK SkillToolset. By breaking knowledge down into L1 metadata, L2 instructions, and L3 resources, we can implement progressive disclosure to drastically reduce token consumption. We will walk through building inline, file-based, and external skills, culminating in a demonstration of a fully optimized agent that pulls in community-driven expertise exactly when a task requires it.

## Outline

- **The Problem: Monolithic Prompts**
  - Token explosion: loading all knowledge upfront into massive system prompts
  - Context window limitations: real-world constraints vs. theoretical models
  - Cost implications: token consumption directly impacts API costs
  - Why context engineering matters for scalable agent development

- **Progressive Disclosure: The Solution**
  - Three-tier architecture: L1 Metadata, L2 Instructions, L3 Resources
  - How progressive disclosure reduces token consumption by ~90%
  - Why modular knowledge matters for agent scalability
  - The "lost in the middle" problem and how progressive disclosure mitigates it

- **Skill Patterns: From Basic to Advanced**
  - **Inline Skills** — Hardcoded Python objects for simple, stable rules
  - **File-Based Skills** — Directory structure with SKILL.md and references for reusability
  - **External Skills** — Community-sourced skills via agentskills.io specification
  - **Skill Factory** — Self-extending agents that generate capabilities at runtime
  - When to use each pattern: prototyping vs. production vs. ecosystem

- **Building & Demonstrating Optimized Agents**
  - Repository structure and SKILL.md anatomy
  - Semantic routing: how agents discover and activate skills
  - Live demonstration: executing a real task with progressive disclosure
  - Token metrics and efficiency gains in practice
  - Best practices: semantic descriptions, scoped instructions, static vs. dynamic separation

- **Closing: Building Your Own Optimized System**
  - How to evaluate your current agent architecture
  - Roadmap for migrating from monolithic to progressive disclosure
  - Resources for implementing skills and SkillToolset patterns
  - Next steps: Antigravity codelabs and advanced patterns

## Key Takeaways

- Monolithic prompts are inefficient — progressive disclosure reduces token consumption by ~90%
- ADK SkillToolset provides a standardized approach to modular agent knowledge architecture
- Start with inline skills for prototyping, then evolve to file-based and external skills for production
- The three-tier structure (L1 metadata, L2 instructions, L3 resources) enables efficient context window management
- Self-extending agents (Skill Factory pattern) represent the future of scalable AI systems
- Community-driven skills via agentskills.io specification enable knowledge sharing across organizations

## References

- [Developers Guide to Building ADK Agents with Skills](https://developers.googleblog.com/developers-guide-to-building-adk-agents-with-skills/)
- [Skills for ADK Agents](https://adk.dev/skills/)
- [AgentSkills Specification](https://agentskills.io/specification)
- [ADK Samples](https://github.com/google/adk-samples)
- [Agent Skills Tutorial](https://github.com/google/adk-samples/tree/main/python/agents/agent-skills-tutorial)
- [ADK Agent Skills: Progressive Disclosure with SkillToolset](https://lavinigam.com/posts/adk-agent-skills-part1/)
- [Guide to Context Engineering](https://blog.bytebytego.com/p/a-guide-to-context-engineering-for)
- [Lost in the Middle: How Language Models Use Long Contexts](https://cs.stanford.edu/~nfliu/papers/lost-in-the-middle.arxiv2023.pdf)
