---
id: W2
title: "Build AI Agents with ADK and Gemini"
summary: "A workshop introducing the Agent Development Kit (ADK): Google's open-source framework for building production-ready AI agents with Gemini: covering agentic AI concepts, ADK architecture, multi-agent design, and deployment options on Google Cloud."
type: Workshop
category: AI
status: Delivered
level: Intermediate
duration: 45
language: English
tags: ["adk","agent-development-kit","ai-agents","agentic-ai","gemini","vertex-ai","vertex-ai-agent-engine","multi-agent","function-calling","generative-ai"]

# Event history for Impact Analytics
events:
  - name: "Google I/O Extended Bacolod 2025"
    organizer: "GDG Bacolod"
    date: 2025-08-02
    location: "Negros Women for Tomorrow Foundation (NWTF) Head Office, Bacolod, Philippines"
    attendees: 80
    url:
      name: "Event Page"
      link: "https://gdg.community.dev/events/details/google-gdg-bacolod-presents-google-io-extended-2025-bacolod/"
    slides:
      name: "Slide Deck"
      link: "https://docs.google.com/presentation/d/14k3SEyEOiTmrcy7xXoPdCar9ettMrilGD59CaQGrOpE/edit?usp=sharing"

# Links for the Portfolio Site
resources:
  github:
    name: "GitHub Repository"
    link: "https://bit.ly/iox-adk-foundation"
  blog:
    name: "Blog Post"
    link: ""
  recording:
    name: "Session Recording"
    link: ""

# Dynamic QR code (construct based on path)
qr_code: "https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=https://smatoto.github.io/content-hub/2025/W2%20-%20ADK%20and%20Gemini/"
---

## Abstract

AI agents represent the next major shift in how software is built: moving from static, deterministic systems to dynamic applications that reason, plan, and act. But building agents that are reliable, extensible, and production-ready is a different challenge altogether.

This workshop unpacks what AI agents actually are, how they've evolved from simple LLM prompts to complex multi-agent systems, and when (and when not) to reach for an agentic architecture. It then introduces the Agent Development Kit (ADK): Google's open-source framework designed to give developers a powerful, flexible foundation for building complex agents with Gemini: with minimal boilerplate, a built-in dev UI for debugging, and native support for multimodal streaming. The session covers the full agent-building toolkit available on Google Cloud: from no-code Conversational Agents to full-code ADK with Vertex AI Agent Engine: and close with a practical look at how to deploy ADK agents to Cloud Run or Vertex AI Agent Engine, with codelabs attendees can follow along with live.


## Agenda

- What are AI agents? Evolution from prompts to multi-agent systems
- When (and when not) to reach for an agentic architecture
- Google's agent spectrum: Conversational Agents → ADK → Agent Engine
- ADK architecture: models, tools, sessions, memory, and callbacks
- Codelab: Building your first agent with ADK and Gemini
- Debugging with ADK's built-in dev UI
- Deploying your agent to Cloud Run or Vertex AI Agent Engine

## Key Takeaways

- Agents reason and act dynamically - they are fundamentally different from prompt-response chatbots
- ADK minimizes boilerplate while giving you full programmatic control over agent behavior
- Google Cloud's agent spectrum lets you choose the right abstraction for your complexity and scale
- ADK's built-in dev UI makes it practical to debug and observe multi-agent flows
- Production deployment - to Cloud Run or Agent Engine - is a first-class feature, not an afterthought
