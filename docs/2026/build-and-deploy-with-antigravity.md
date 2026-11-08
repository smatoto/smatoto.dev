---
id: W7
title: "Plan, Build, Ship: A Serverless Pipeline on Google Cloud with Antigravity"
summary: "A hands-on workshop where attendees use Google Antigravity to plan, generate, deploy, and verify an event-driven document pipeline on Google Cloud, built on Cloud Storage, Pub/Sub, Cloud Run, and BigQuery, while keeping a human in the loop at every step."
type: Workshop
category: AI
status: Draft
level: Intermediate
duration: 90
tags: ["AI - Agents", "AI - Gemini", "Cloud - AI Tools", "Cloud - Serverless & Containers", "Google Cloud", "Developer Tools"]

# Event history for Impact Analytics
events: []

# Links for the Portfolio Site
resources:
  codelab:
    name: "Codelab"
    link: "https://codelabs.developers.google.com/build-and-deploy-gcp-with-antigravity"
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
qr_code: "https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=https://smatoto.dev/2026/build-and-deploy-with-antigravity/"
---

## Abstract

Coding agents are good at writing code, but the harder part is everything around it: agreeing on an architecture, provisioning infrastructure, deploying, and proving it works. In this hands-on workshop, attendees use Google Antigravity to take a serverless, event-driven document pipeline through that whole path on Google Cloud. Files uploaded to Cloud Storage trigger a Pub/Sub push to a Python service on Cloud Run, which streams extracted metadata into BigQuery. Before any code exists, Antigravity's `/grill-me` command questions the design, and attendees review the resulting Implementation Plan. The agent then generates the service, deployment scripts, Terraform, and tests, deploys the pipeline, and verifies it with live BigQuery queries recorded in a Walkthrough, while the "Always Ask" review policy keeps the developer approving every step.

The session closes by reviewing the generated code critically and hardening the prototype with authenticated push, dead letter topics, and Secret Manager. It is for developers who know the basics of Google Cloud and want a repeatable, reviewable way to go from an idea to a deployed, verified system with an agent.

## Agenda

- Beyond code completion: where agents help across plan, build, deploy, and verify
- A tour of Google Antigravity: the editor, the Agent Manager, and artifacts
- The target architecture: Cloud Storage, Pub/Sub, Cloud Run, and BigQuery
- Setup: Antigravity, `gcloud` authentication, and the "Always Ask" review policy
- Lab 1: Planning the architecture with `/grill-me` and approving the Implementation Plan
- Lab 2: Generating the service, deployment scripts, Terraform, and local tests
- Lab 3: Deploying the pipeline to Cloud Run with Cloud Storage and Pub/Sub
- Lab 4: Verifying end to end with live BigQuery queries and the Walkthrough artifact
- Reviewing the generated code as if it were a teammate's PR
- Hardening the prototype: authenticated push, dead letter topics, and Secret Manager
- Cleaning up resources and next steps

## Key Takeaways

- Start with the design, not the code: `/grill-me` turns a vague prompt into explicit decisions you can review
- An Implementation Plan reviewed before generation is cheaper to fix than generated code reviewed after
- An agent can own the full loop, from code and infrastructure to deployment and verification, but "Always Ask" keeps you in charge of every step
- A Walkthrough artifact is evidence: it records what was built, how it was tested, and what the live system actually returned
- Event-driven building blocks fit together cleanly: Cloud Storage notifications to Pub/Sub push to Cloud Run to BigQuery streaming inserts
- Generated code is a starting point: an unauthenticated prototype needs authentication, dead letter handling, and secrets management before it carries real data

## References

- [Build and Deploy to Google Cloud with Antigravity (Codelab)](https://codelabs.developers.google.com/build-and-deploy-gcp-with-antigravity)
- [Google Antigravity](https://antigravity.google/)
- [Pub/Sub notifications for Cloud Storage](https://cloud.google.com/storage/docs/pubsub-notifications)
- [Triggering Cloud Run from Pub/Sub push](https://cloud.google.com/run/docs/triggering/pubsub-push)
- [Streaming data into BigQuery](https://cloud.google.com/bigquery/docs/streaming-data-into-bigquery)
