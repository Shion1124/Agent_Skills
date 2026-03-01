---
name: decision-example
description: Example decision structure (delete after reading)
---

# Decision: Tool Selection for E2E Testing

**Date**: 2026-02-15  
**Status**: ACCEPTED  
**Decision Makers**: @team-lead  

## Context
Team needs to choose E2E testing framework. Options: Playwright, Cypress, Selenium.

## Decision
Use Playwright for:
1. Multi-browser support (Chrome, Firefox, Safari)
2. Better performance (~3x faster)
3. Active maintenance and modern tooling

## Consequences
- Team learning curve (~2 days)
- CI/CD adds browser dependencies
- Better long-term maintainability

## Alternatives Considered
- Cypress: Good DX but limited to Chrome
- Selenium: Too verbose for modern web

## Related Patterns
- pattern-010: Playwright Best Practices

## Follow-up
- [ ] Train team on Playwright (Week 1)
- [ ] Review after 2 sprints (2026-04-15)

---

This is a template. Edit and customize for your decisions.
