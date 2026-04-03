---
id: T6
title: "From Code to Cloud with Containers and CI/CD Workflows"
summary: "A talk covering the fundamentals of containerization and CI/CD pipelines, and how Google Cloud tools like Cloud Build, Artifact Registry, and Cloud Deploy tie it all together into a secure, modern software supply chain."
type: Talk
category: DevOps
status: Delivered
level: Intermediate
duration: 25
language: English
tags: ["containers","docker","kubernetes","gke","cloud-run","ci-cd","cloud-build","devops","software-supply-chain","binary-authorization"]

# Event history for Impact Analytics
events:
  - name: "CS Expo 2025"
    organizer: "FEU Institute of Technology"
    date: 2025-11-12
    location: "FEU Tech Innovation Center (FTIC), Manila, Philippines"
    attendees: 100
    url:
      name: "Event Page"
      link: "https://csexpo2025.tech"
    slides:
      name: "Slide Deck"
      link: "https://docs.google.com/presentation/d/13EKeblrVUMC0mHHFmEalZkn5OGOqdkQGAkMyrjbohcA/edit?usp=sharing"

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
qr_code: "https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=https://smatoto.github.io/content-hub/2025/T6%20-%20Containers%20and%20CICD/"
---

## Abstract

Modern applications are no longer deployed as single monolithic blobs running on pre-provisioned VMs. Today's systems are dynamic, scalable, and resilient: built on microservices, packaged as containers, and shipped through automated pipelines. But how do all these pieces actually fit together?

This talk starts from first principles: what containerization is, why it beats VMs and shared hosts for most workloads, and how Kubernetes (and specifically GKE) brings orchestration to the picture. It then walks through CI/CD: what it means, how it maps onto the SDLC, and what a real-world pipeline looks like using Google Cloud's own software supply chain tooling: Cloud Build, Artifact Registry, Cloud Deploy, and Binary Authorization. By the end, participants will have a clear mental model of how code travels from a developer's commit all the way to a running container in production: securely, automatically, and reliably.


## Outline

- From monoliths to microservices: why containers
- Containers vs. VMs vs. shared hosts: what's actually different
- Kubernetes and GKE: orchestration explained from first principles
- CI/CD and the SDLC: what automation actually looks like
- Google Cloud's supply chain: Cloud Build → Artifact Registry → Cloud Deploy
- Binary Authorization: the final security gate
- End-to-end: tracing a commit all the way to a running production container

## Key Takeaways

- Containers solve "works on my machine" by packaging the app and its runtime together
- GKE handles scaling, self-healing, and scheduling - so your team doesn't have to
- CI/CD is a discipline, not just automation - it enforces quality at every commit
- Cloud Build + Artifact Registry + Cloud Deploy form a complete, managed supply chain on GCP
- Binary Authorization is the enforcement layer: no unverified image ever reaches production
