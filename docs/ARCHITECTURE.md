# DoodleTurtleAI Architecture

## Overview

DoodleTurtleAI is designed as a modular educational platform that combines software engineering, structured knowledge, and artificial intelligence to create meaningful learning experiences for children.

The architecture emphasizes simplicity, maintainability, and clear separation of responsibilities. Every major component has a single purpose and communicates with other components through well-defined interfaces.

---

# Architectural Philosophy

Project Genesis follows several core engineering principles:

* One responsibility per class.
* One responsibility per module.
* Structure before implementation.
* Design before optimization.
* Knowledge remains separate from application code.
* Documentation evolves alongside the software.

These principles guide every architectural decision.

---

# Current System Components

## Startup Engine

Responsible for:

* Loading configuration
* Initializing logging
* Initializing the Turtle Brain
* Running startup health checks

---

## Turtle Brain

The Turtle Brain manages structured memory.

Current responsibilities include:

* Database initialization
* Project storage
* Repository pattern
* Service layer
* Future persistent memory

---

## Knowledge Library

The Knowledge Library contains the permanent knowledge and guiding principles of DoodleTurtleCo.

Current sections include:

* Constitution
* Mission
* Vision
* Child First
* Teaching Principles
* Finn

Knowledge is stored as Markdown documents to remain human-readable and easily maintained.

---

## Knowledge Integration

The Knowledge Integration subsystem connects the application to the Knowledge Library.

Current components:

* KnowledgeLoader
* KnowledgeLibrary

Its responsibility is to discover, organize, and provide access to knowledge documents.

---

# Repository Structure

```text
docs/
    Technical documentation

knowledge/
    Permanent organizational knowledge

src/
    Python application

scripts/
    Development and testing utilities

data/
    Local runtime data

tests/
    Automated testing (future)
```

---

# Current Data Flow

```text
User
   │
   ▼
Startup
   │
   ▼
Application
   │
   ├────────► Turtle Brain
   │
   └────────► Knowledge Library
```

---

# Future Architecture

As Project Genesis grows, additional systems are expected to include:

* Character Management
* Story Engine
* Lesson Engine
* Conversation Engine
* Illustration Services
* AI Agents
* Learning Analytics

Each future subsystem will be documented as it is designed and implemented.

---

# Living Document

This document describes the current architecture of DoodleTurtleAI.

It is intended to evolve alongside the software.

Architectural changes should be reflected here as part of the development process.
