---
id: T2
title: "Process Automation using Application Integration"
summary: "Connecting applications and services efficiently using Google Cloud's Application Integration services."
type: Talk
category: DevOps
status: Delivered
level: Advanced
duration: 30
language: English
tags: ["Cloud - App Development", "Google Cloud", "Google I/O Extended"]

# Event history for Impact Analytics
events:
  - name: "Google I/O Extended Cloud Manila 2023"
    organizer: "GDG Cloud Manila"
    date: 2023-08-12
    location: "De La Salle University, Manila, Philippines"
    attendees: 120
    url:
      name: "Event Page"
      link: "https://gdg.community.dev/events/details/google-gdg-cloud-manila-presents-google-io-extended-2023-gdg-cloud-manila/"
    slides:
      name: "Slide Deck"
      link: "https://docs.google.com/presentation/d/e/2PACX-1vS7XjoDTkLRLfbqasdYQ6k1mlxNfYDe5WHmnw_D9uTO7IZ9lIQheAA_Qb-kqG7KFfFG-8qC0E-Rxma-/pub?start=false&loop=false&delayms=3000"

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
qr_code: "https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=https://smatoto.dev/2023/application-integration/"
---

## Abstract

In today's cloud-first world, organizations are managing more SaaS applications and data sources than ever before. Traditional point-to-point integrations are fragile, difficult to scale, and often require extensive custom code. This session introduces Google Cloud's **Application Integration**, a managed iPaaS (Integration Platform as a Service) that enables users to connect applications and services using an intuitive, low-code visual designer.

This session explores how Application Integration simplifies the orchestration of complex business processes. From the 75+ built-in connectors for Google and third-party apps to versatile triggers and data mapping tasks, attendees will learn the core building blocks needed to build robust, scalable integration flows. The talk includes a practical walkthrough of an e-commerce backend scenario, demonstrating how to handle API payloads, apply conditional logic, and integrate with external vendors. Whether participants are a business analyst looking to automate workflows or a developer aiming to reduce boilerplate integration code, this session will demonstrate how to leverage Google's infrastructure to connect an ecosystem efficiently.

## Outline

- The integration problem: why point-to-point integrations break at scale
- What is Application Integration? iPaaS on Google Cloud
- Core building blocks: triggers, connectors, data mapping tasks
- Demo walkthrough: e-commerce backend - API payloads, conditional logic, external vendors
- Developer vs. business analyst use cases
- When to reach for Application Integration vs. custom code

## Key Takeaways

- Point-to-point integrations are fragile and don't scale - a managed iPaaS solves this
- 75+ pre-built connectors eliminate most custom integration boilerplate
- The low-code visual designer makes integration accessible to business analysts and developers alike
- Conditional logic and data mapping handle complex business rules without writing glue code
- Application Integration fits naturally into a Google Cloud-first architecture
