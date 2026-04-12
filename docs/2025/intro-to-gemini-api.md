---
id: W1
title: "Getting Started with the Gemini API in Vertex AI with cURL / REST API"
summary: "A hands-on workshop that walks developers through calling the Gemini API on Vertex AI using cURL and REST: covering text generation, multimodal inputs, function calling, controlled generation, and more."
type: Workshop
category: AI
status: Delivered
level: Intermediate
duration: 40
language: English
tags: ["AI - Vertex AI", "AI - Gemini", "Build with AI"]

# Event history for Impact Analytics
events:
  - name: "Build with AI Cloud Manila 2025"
    organizer: "GDG Cloud Manila"
    date: 2025-04-24
    location: "Greenfield Tower, Mandaluyong, Philippines"
    attendees: 100
    url:
      name: "Event Page"
      link: "https://gdg.community.dev/events/details/google-gdg-cloud-manila-presents-gdg-cloud-manila-build-with-ai-2025/"
    slides:
      name: "Slide Deck"
      link: "https://docs.google.com/presentation/d/e/2PACX-1vTYAn48ZuSLm0AfLNRVnEe6JwXzPXHXfo9ySBT9oz8NLLD5ZON4XtBdAS10yHpsmsTmNCfG_k7R1X5m/pub?start=false&loop=false&delayms=3000"
  - name: "Build with AI Zamboanga 2025"
    organizer: "GDG Zamboanga"
    date: 2025-04-25
    location: "Rosal Hall, Universidad de Zamboanga (UZ), Zamboanga City, Philippines"
    attendees: 127
    url:
      name: "Event Page"
      link: "https://gdg.community.dev/events/details/google-gdg-zamboanga-presents-build-with-ai-zamboanga/"
    slides:
      name: "Slide Deck"
      link: "https://docs.google.com/presentation/d/e/2PACX-1vRZ1Nfg89AUZGKriGnCGsXCvpFxWQ27w9MsQpZ-jO0dBWKOfzwd00fY58As6mjcKGORcJrlzQb_W6D-/pub?start=false&loop=false&delayms=3000"

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
qr_code: "https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=https://smatoto.dev/2025/intro-to-gemini-api/"
---

## Abstract

> _The full talk abstract: the version submitted to CFPs and shared with event organizers._

In this hands-on workshop, developers will get started with the Gemini API in Vertex AI using nothing but cURL and REST: no SDKs required. Starting from the basics of the Vertex AI API surface, participants will learn how to authenticate, structure requests, and call Gemini models directly via HTTP. Through a series of guided labs, attendees will explore key capabilities including text generation, streaming, multi-turn chat, function calling, multimodal inputs (images and video), controlled generation with JSON schemas, and using Google Search as a grounding tool. By the end of the session, developers will have a working mental model of how the Gemini API works under the hood: knowledge that transfers directly to any language or SDK they choose to use in their projects.


## Agenda

- Introduction: Vertex AI API surface and Gemini model overview
- Lab 1: Authenticating and making your first API call with cURL
- Lab 2: Text generation and streaming responses
- Lab 3: Multi-turn chat conversations
- Lab 4: Function calling basics
- Lab 5: Multimodal inputs - sending images and video
- Lab 6: Controlled generation with JSON schemas
- Lab 7: Grounding responses with Google Search

## Key Takeaways

- The Gemini API is plain HTTP - no SDK needed to get started, just cURL
- Understanding the raw API makes you a better developer regardless of which SDK you use later
- Streaming, multi-turn chat, and function calling are all first-class, built-in API features
- Multimodal inputs (text, image, video) are supported natively in a single API request
- Google Search grounding reduces hallucinations by anchoring responses in real-time, factual data
