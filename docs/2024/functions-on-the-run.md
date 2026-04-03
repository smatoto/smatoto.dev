---
id: T4
title: "Functions on the Run: Unified Serverless Platform"
summary: "Exploring the unified serverless platform on Google Cloud with Cloud Functions and Cloud Run."
type: Talk
category: DevOps
status: Delivered
level: Intermediate
duration: 30
language: English
tags: ["serverless","cloud-run","cloud-functions","ai","gpu","gemma","genkit","devops","containers","llm"]

# Event history for Impact Analytics
events:
  - name: "DevFest Cloud Manila 2024"
    organizer: "GDG Cloud Manila"
    date: 2024-10-05
    location: "JY Campos Hall B, Bayanihan Center, Pasig, Philippines"
    attendees: 80
    url:
      name: "Event Page"
      link: "https://gdg.community.dev/events/details/google-gdg-cloud-manila-presents-devfest-cloud-manila-2024/"
    slides:
      name: "Slide Deck"
      link: "https://docs.google.com/presentation/d/1FVsUozz7RJYnrvsVLEDVbqgEO4sPm9RJakm7RIg-toM/edit?usp=sharing"

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
qr_code: "https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=https://smatoto.github.io/content-hub/2024/T4%20-%20Functions%20on%20the%20Run/"
---

## Abstract

The serverless landscape on Google Cloud has reached a major milestone with the unification of its flagship products. Cloud Functions has officially been rebranded to **Cloud Run functions**, creating a single, powerful platform for both event-driven snippets and containerized microservices. This session dives into the implications of this change and explores how developers can now enjoy the best of both worlds: the simplicity of Functions-as-a-Service (FaaS) combined with the flexibility and advanced features of Cloud Run.

This session explores the technical benefits of this unified platform, including access to high-performance NVIDIA L4 GPUs for AI inference, custom volume mounts for Cloud Storage and Filestore, and advanced cost-optimization strategies like "Always-on CPU" and Committed Use Discounts (CUDs). The talk features a live demo building an AI-powered text summarization application using **Gemma 2**, **Firebase Genkit**, and **Cloud Run**, highlighting how to scale LLMs to zero when not in use. Whether participants are managing legacy Cloud Functions or building new AI-native applications, this session will provide a roadmap to master the next generation of serverless on Google Cloud.

## Outline

- The evolution: Cloud Functions → Cloud Run functions
- What changed, what stayed the same
- New capabilities: GPU inference, volume mounts, Committed Use Discounts
- Cost optimization: Always-on CPU and scale to zero
- Live demo: AI text summarization with Gemma 2 + Firebase Genkit on Cloud Run
- Migration path for existing Cloud Functions workloads

## Key Takeaways

- Cloud Functions is now Cloud Run functions - one unified serverless platform on Google Cloud
- FaaS simplicity and container flexibility are no longer a trade-off
- NVIDIA L4 GPU access enables on-demand AI inference without managing any infrastructure
- Scale-to-zero keeps LLM hosting costs near zero during idle periods
- CUDs make serverless economically competitive with always-on alternatives at scale
