---
id: T9
title: "Building Full-Stack Apps with Google AI Studio, Cloud Run, & Cloud SQL"
summary: "A live-built talk that takes a running club app from a single natural-language prompt to a public URL: Google AI Studio generates the frontend, the backend, and a real Cloud SQL for PostgreSQL schema, features get added by chat, and one click publishes it to Cloud Run."
type: Talk
category: App Dev
status: Delivered
level: Beginner
duration: 45
tags: ["AI - Generative AI", "AI - Gemini", "Cloud - AI Tools", "Cloud - App Development", "Cloud - Serverless & Containers", "Google Cloud", "Google I/O Extended"]

# Event history for Impact Analytics
events:
  - name: "Google I/O Extended Cloud Manila 2026"
    organizer: "GDG Cloud Manila"
    date: 2026-09-12
    location: "Virtual"
    attendees: 111
    url:
      name: "Event Page"
      link: "https://gdg.community.dev/events/details/google-gdg-cloud-manila-presents-gdg-cloud-manila-io-extended-2026/"
    slides:
      name: "Slide Deck"
      link: "https://docs.google.com/presentation/d/e/2PACX-1vR8FHUzbzeKKRfRPdu2OHHXoGmIjMB8iWLYpmaGr_VwvaeQVqDFnOGGtJVtK3WIxc8GUFTYmyMihZzS/pub?start=false&loop=false&delayms=3000"

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
qr_code: "https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=https://smatoto.dev/2026/full-stack-apps-with-ai-studio/"
---

## Abstract

Shipping a full-stack app with real persistence is still assumed to be days of work: design the schema, write the backend, provision a database, wire up auth, then figure out hosting. This session argues the assumption is out of date, and proves it by building an app live, on stage, starting from nothing.

Using Google AI Studio's Build mode, a single sentence produces a working running club web app: Google Sign-In, a relational schema on Cloud SQL for PostgreSQL, and a frontend that actually reads and writes real rows. From there the app grows by conversation. One chat prompt adds a route library, and AI Studio evolves the schema and wires the foreign key to the existing runs table. Another adds RSVPs, attendee counts, and a shareable invite link. A browser refresh proves the data is in a real database, not component state. A final click on Publish deploys the same app, with the same schema and the same data, to Cloud Run at a public URL the audience can open while the talk is still running.

Along the way the session covers where the generated code stops being a prototype and starts being something to review, own, and extend. Attendees leave with a repeatable prompt-driven path from idea to a live, database-backed app on Google Cloud, and a codelab to walk the same path themselves.

This session is for developers at any level who have shipped a frontend but hesitate at the backend, and for experienced engineers who want an honest look at how far prompt-driven full-stack generation has actually come.

## Outline

- The myth: full-stack apps with real persistence take days of backend and schema work
- Google AI Studio Build mode: describe the app, get the app
- One prompt, one full-stack app: Google Sign-In, a Cloud SQL for PostgreSQL schema, a working frontend
- The generated schema: `users`, `runs`, `comments`, and why it is relational rather than a document dump
- Iterating by chat: adding a route library, and watching the schema grow a foreign key on its own
- Adding RSVPs, attendee counts, and invite links without touching the database by hand
- Proving persistence: refresh the browser, and the data is still there in Cloud SQL
- Publish: one click from AI Studio to a live Cloud Run URL, same schema, same data, no separate deploy step
- The full picture: AI Studio to Cloud Run to Cloud SQL, and where a human still has to own the code

## Key Takeaways

- Google AI Studio generates a real backend and a real relational schema on Cloud SQL, not a mockup with local state
- Features are added by conversation - the schema evolves, relationships get wired, and no migration is written by hand
- A browser refresh is the honest test of persistence, and it passes because the data is in PostgreSQL
- Publish to Cloud Run is a button, not a pipeline: preview and production share the same schema and data, so there is no environment drift
- Generated code is a starting point, not a finished system - review it, own it, and know what is running before it carries real users
- The full path is reproducible at home via the "Build a Database-Backed Web App with Google AI Studio and Cloud SQL" codelab
