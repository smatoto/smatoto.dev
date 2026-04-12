---
id: W4
title: "Deploy a Secure MCP Server on Cloud Run"
summary: "A workshop and codelab walking developers through the concepts of agentic AI, the Model Context Protocol (MCP), and how to deploy a secure MCP server on Cloud Run: making it easy to connect AI agents to external tools and databases at scale."
type: Workshop
category: AI
status: Delivered
level: Intermediate
duration: 40
language: English
tags: ["Cloud - Serverless & Containers", "AI - LLM", "AI - Gemini", "Google Cloud", "DevFest", "AI - Gemini CLI"]

# Event history for Impact Analytics
events:
  - name: "DevFest Bacolod 2025"
    organizer: "GDG Bacolod"
    date: 2025-11-22
    location: "University of St. La Salle, Bacolod City, Philippines"
    attendees: 109
    url:
      name: "Event Page"
      link: "https://gdg.community.dev/events/details/google-gdg-bacolod-presents-devfest-bacolod-2025-1/"
    slides:
      name: "Slide Deck"
      link: "https://docs.google.com/presentation/d/e/2PACX-1vSTUueUaymgzATs5gU9SU4s0joXZ00sVtnM1-JxnzfPWEVFl1lBvs-4-Xv-NcaJXOLDwNACwyWKS_mQ/pub?start=false&loop=false&delayms=3000"

# Links for the Portfolio Site
resources:
  github:
    name: "GitHub Repository"
    link: "https://github.com/smatoto/mcp-server-cloud-run"
  blog:
    name: "Blog Post"
    link: ""
  recording:
    name: "Session Recording"
    link: ""

# Dynamic QR code (construct based on path)
qr_code: "https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=https://smatoto.dev/2025/mcp-server-on-cloud-run/"
---

## Abstract

As AI agents become a core part of how modern software operates, the challenge shifts from building a single capable model to connecting many agents reliably to the external world: databases, APIs, and services. The Model Context Protocol (MCP) addresses this directly: it standardizes how AI agents discover and call tools, reducing the boilerplate of tool-calling code and improving the reliability and reusability of agent integrations.

This workshop starts with the fundamentals of agentic AI: what agents are, how tools and function-calling work, and how the ecosystem has evolved from simple LLM prompts to multi-agent systems. It then introduces MCP: what it is, why it matters, and how Google's open-source MCP Toolbox for Databases fits into the picture. The second half of the workshop dives into Cloud Run as the ideal serverless runtime for hosting MCP servers: covering its architecture, benefits for AI workloads, and design patterns for GenAI apps and agents. The workshop concludes with a live codelab where attendees deploy their own secure MCP server on Cloud Run.


## Agenda

- Agentic AI fundamentals: agents, tools, and how function calling works
- The integration problem: reliably connecting agents to databases, APIs, and services
- What is MCP? Protocol overview and why standardization matters
- Google's MCP Toolbox for Databases: simplifying agent-to-database connections
- Cloud Run as the ideal serverless runtime for MCP servers
- Design patterns for GenAI apps and multi-agent systems
- Codelab: Deploying your own secure MCP server on Cloud Run

## Key Takeaways

- MCP standardizes tool discovery and calling - eliminating custom glue code across every agent project
- A well-designed MCP server is reusable across multiple agents and use cases simultaneously
- Cloud Run's serverless model is a natural fit for MCP servers: scalable, secure, and pay-per-use
- Google's MCP Toolbox removes the hardest part of connecting agents to production databases
- Security is built into Cloud Run by design - auth, HTTPS, and IAM are handled for you
