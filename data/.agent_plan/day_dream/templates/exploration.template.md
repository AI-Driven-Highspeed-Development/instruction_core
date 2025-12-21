---
topic: "{Topic Name}"
status: ACTIVE
created: "{YYYY-MM-DD}"
expires: "{YYYY-MM-DD}"  # created + 14 days
synthesized_to: null
superseded_by: null
---

# {Topic} Exploration

> **Parent Vision:** [vision.md](../vision.md) *(or "N/A — pre-vision research")*  
> **Created:** {YYYY-MM-DD}  
> **Expires:** {YYYY-MM-DD}

---

## Decision Context

**Question:** What specific decision does this exploration answer?

<!-- 
Be precise. Not "how should we build X" but "should we use approach A or B for X".
If you can't phrase it as a choice between options, this may not need an exploration.
-->

{The specific question this exploration will answer.}

**Constraints:**
- {Hard constraint 1}
- {Hard constraint 2}

**Timeline:** {When must this decision be made?}

---

## Options Considered

### Option A: {Name}

**Description:** {1-2 sentences explaining this approach.}

| Pros | Cons |
|------|------|
| {Pro 1} | {Con 1} |
| {Pro 2} | {Con 2} |

**Difficulty:** `[KNOWN]` | `[EXPERIMENTAL]` | `[RESEARCH]`

**Effort Estimate:** {Rough estimate if chosen}

---

### Option B: {Name}

**Description:** {1-2 sentences.}

| Pros | Cons |
|------|------|
| {Pro 1} | {Con 1} |
| {Pro 2} | {Con 2} |

**Difficulty:** `[KNOWN]` | `[EXPERIMENTAL]` | `[RESEARCH]`

**Effort Estimate:** {Rough estimate}

---

### Option C: {Name} *(if applicable)*

{Same structure as above. Remove if only 2 options.}

---

## Evaluation Criteria

<!-- 
Weight: High (must have), Medium (important), Low (nice to have)
Score each option: ⭐ (poor), ⭐⭐ (adequate), ⭐⭐⭐ (good)
-->

| Criterion | Weight | Option A | Option B |
|-----------|--------|----------|----------|
| {e.g., Complexity} | High | ⭐⭐⭐ | ⭐⭐ |
| {e.g., Maintainability} | Medium | ⭐⭐ | ⭐⭐⭐ |
| {e.g., Performance} | Low | ⭐⭐ | ⭐⭐ |

---

## Recommendation

**Chosen Option:** {A | B | C | None — needs more research}

**Rationale:** {2-3 sentences explaining why this option was chosen.}

**Unresolved Risks:**
- {Risk 1 that remains even with chosen option}
- {Risk 2}

---

## Synthesis Notes

<!-- 
Fill this section when integrating insights into vision.md.
Then change status in frontmatter to SYNTHESIZED.
-->

- **Integrated to:** `vision.md#{section-anchor}`
- **Key points carried over:**
  - {Point 1}
  - {Point 2}
- **Points deferred to implementation:**
  - {Detail 1}
  - {Detail 2}

---

## Appendix: Research Notes

<!-- 
OPTIONAL: Raw notes, links, code snippets gathered during exploration.
Keep brief — this is not a knowledge base, just working notes.
-->

### Links
- {URL 1}: {Why relevant}
- {URL 2}: {Why relevant}

### Code Snippets
```python
# Example if testing something
```

### Rejected Alternatives
- {Alternative X}: Rejected because {reason}

---

<!--
EXPLORATION DOCUMENT RULES:

WHEN TO CREATE:
- Choosing between 2+ architectural approaches
- Evaluating external API/library options  
- Complex algorithm design (ML, data pipeline)

WHEN NOT TO CREATE:
- Standard CRUD features → just write in vision.md
- Implementation details → HyperArch's domain
- "Understanding X" → that's learning, not planning

LITMUS TEST: "Would this decision fundamentally change the vision?"
If yes → exploration. If no → defer to implementation.

CONSTRAINTS:
- Max 3 active explorations (soft cap)
- 200 lines max (forces synthesis)
- 14-day expiration (passive warning)
- Never delete — archive when done

STATUS LIFECYCLE:
ACTIVE → working on it
SYNTHESIZED → insights moved to vision.md → archive to _archive/
ABANDONED → rejected or superseded → keep with status marked
EXPIRED → >14 days old → needs decision (synthesize, abandon, or extend)

AFTER SYNTHESIS:
1. Update status to SYNTHESIZED
2. Fill Synthesis Notes section
3. Move file to _archive/{date}_{topic}.md
4. Add entry to implementation.md ## Exploration Log
-->
