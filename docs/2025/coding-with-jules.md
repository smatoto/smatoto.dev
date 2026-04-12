---
id: T5
title: "From Prompt to PR: Autonomous Coding with Jules"
summary: "A talk exploring Jules, Google's experimental AI-powered async coding agent: how it works, what it can do, and how developers can start using it to write tests, fix bugs, build features, and ship code directly to GitHub."
type: Talk
category: AI
status: Delivered
level: Intermediate
duration: 30
language: English
tags: ["AI - Agents", "AI - Generative AI", "AI - Gemini", "Google I/O Extended"]

# Event history for Impact Analytics
events:
  - name: "Google I/O Extended Manila 2025"
    organizer: "GDG Manila"
    date: 2025-07-26
    location: "Accenture People Hub, Uptown Mall, Taguig, Philippines"
    attendees: 150
    url:
      name: "Event Page"
      link: "https://gdg.community.dev/events/details/google-gdg-manila-presents-google-io-extended-manila-2025/"
    slides:
      name: "Slide Deck"
      link: "https://docs.google.com/presentation/d/e/2PACX-1vQ98JmoNfHq67BlwxbQzAue8iiuB1TjQj-jwLOrKPdTryrCaeNqWyC1k-t90OpsU83iNHLZSc6n8XUI/pub?start=false&loop=false&delayms=3000"

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
qr_code: "https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=https://smatoto.dev/2025/coding-with-jules/"
---

## Abstract

In an era where AI agents are reshaping how software gets built, Jules stands out as a uniquely practical tool: an asynchronous, agentic coding assistant that lives directly inside GitHub workflow. Unlike copilots that require developers to stay in the loop for every line, Jules works in the background: it clones a repository into a secure Google Cloud VM, reasons over the full codebase, executes a visible plan, and surfaces a diff for review: all without switching context.

This session covers what Jules is, how it fits into Google's broader AI agent ecosystem (Vertex AI, ADK, Agent Engine), and what makes it different from other AI coding tools. The talk walks through the full workflow: from writing an effective prompt and reviewing Jules' plan, to approving changes and creating a pull request: and close with a live demo showing Jules fix a bug and build a feature from scratch. Whether participants are skeptical of AI-generated code or already all-in on agentic development, this talk will provide a clear, practical picture of where autonomous coding is headed.


## Outline

- The agentic coding shift: from copilots to autonomous agents
- What Jules is and how it works: GitHub-native, async, VM-isolated
- How Jules fits in Google's AI ecosystem (Vertex AI, ADK, Agent Engine)
- Jules vs. other AI coding tools: what makes it different
- The full workflow: prompt → plan → diff → PR
- Live demo: Jules fixing a bug and building a feature from scratch

## Key Takeaways

- Jules works asynchronously - you write the prompt, it works in the background while you do something else
- Full codebase reasoning in an isolated Google Cloud VM produces more reliable, context-aware results
- Every change is transparent: you review a visible plan and a diff before anything is merged
- Jules fits directly into GitHub - no new tool, dashboard, or workflow to adopt
- Agentic coding is about removing grunt work, not replacing developers
