---
id: T1
title: "Securing the CI/CD pipelines on Google Cloud"
summary: "Securing the software supply chain by implementing security best practices in CI/CD pipelines on Google Cloud."
type: Talk
category: DevOps
status: Delivered
level: Advanced
duration: 40
language: English
tags: ["devops","cicd","security","slsa","software-supply-chain","binary-authorization","cloud-build","artifact-registry","gke","cloud-run"]

# Event history for Impact Analytics
events:
  - name: "Hiver's Connect Manila 2023"
    organizer: "Design Hive"
    date: 2023-09-23
    location: "Asia Pacific College, Makati, Philippines"
    attendees: 50
    url:
      name: "Event Page"
      link: "https://luma.com/hiversconnectmnl?tk=n6YjkH"
    slides:
      name: "Slide Deck"
      link: "https://docs.google.com/presentation/d/e/2PACX-1vRV0M9n1r37UrcVwNrNKLPiqpmbDXK9SwStA69SEV4fE5gJjR-I0ziZj0-F2Bx11Lv0qZn8TsDB-nZS/pub?start=false&loop=false&delayms=3000"

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
qr_code: "https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=https://smatoto.dev/2023/securing-ci-cd-pipelines/"
---

## Abstract

As organizations accelerate their digital transformation, the software development life cycle (SDLC) has become a primary target for sophisticated cyberattacks. From the SolarWinds breach to the Log4Shell vulnerability, the security of the software supply chain is now a critical priority for DevOps and Security teams alike. This session explores the fundamental concepts of Continuous Integration and Continuous Delivery (CI/CD) through the lens of security, introducing the "Shift Left" philosophy to identify and mitigate risks as early as the development phase.

This talk dives deep into Google Cloud's holistic approach to securing the software supply chain (S3C). Participants will learn how to leverage tools like Cloud Workstations for managed development environments, Assured Open Source Software for curated and scanned dependencies, and Cloud Build for achieving SLSA Level 3 compliance with automated build provenance. The session also discusses how Binary Authorization acts as a gatekeeper, ensuring only trusted and verified artifacts are deployed to GKE or Cloud Run. By the end of this talk, attendees will have a clear roadmap and architectural blueprint for building resilient, tamper-evident, and secure CI/CD pipelines that protect an organization's most valuable software assets.

## Outline

- The growing threat to software supply chains (SolarWinds, Log4Shell)
- Shift Left: catching vulnerabilities at the source
- Google Cloud's S3C approach: an end-to-end framework
- Cloud Workstations: secure managed development environments
- Assured OSS + Cloud Build: verified dependencies and SLSA Level 3 provenance
- Binary Authorization: the final deployment gatekeeper
- Architecture blueprint for a resilient, tamper-evident CI/CD pipeline

## Key Takeaways

- CI/CD pipelines are now a primary attack surface in the modern SDLC
- "Shift Left" means baking security into development, not bolting it on at deployment
- SLSA Level 3 with Cloud Build provides cryptographic, tamper-evident build provenance
- Binary Authorization ensures only verified, signed artifacts are ever deployed to GKE or Cloud Run
- Google Cloud's S3C tools compose into a complete, layered supply chain security posture
