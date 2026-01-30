---
name: slide-html-generator
description: Generate professional slide deck HTML from a topic. Creates structured outlines, collects information via web search, and generates 1280x720 HTML slides. Use when user asks to "create slides", "make a presentation", "generate deck", "slide deck", or "PPT".
---

# Slide HTML Generator

Transform a topic into professional slide deck HTML files.

## Usage

```bash
# User provides a topic
"创建一个关于人工智能对未来工作影响的演示文稿"

# Or with options
--style blueprint    # Visual style preset
--slides 12          # Target slide count
--audience experts   # Target audience
--lang zh            # Output language
```

## Quick Start

1. User provides topic (e.g., "人工智能对未来工作的影响")
2. Agent collects information via web search
3. Agent analyzes content and recommends style/slides
4. Agent generates outline with STYLE_INSTRUCTIONS
5. Agent generates HTML slides (1280x720)

## Workflow

Copy this checklist and check off items as you complete them:

```
Slide HTML Progress:
- [ ] Step 1: Information Gathering
- [ ] Step 2: Content Analysis
- [ ] Step 3: User Confirmation (optional)
- [ ] Step 4: Generate Outline
- [ ] Step 5: Generate Slide Scripts
- [ ] Step 6: Generate HTML Slides
- [ ] Step 7: Output Summary
```

### Step 1: Information Gathering

**Purpose**: Collect comprehensive information about the topic.

**Actions**:
1. Parse topic keywords (both Chinese and English)
2. Execute multiple web searches
3. Organize results into structured content
4. Save to `source.md`

```bash
# Example web searches for "AI对未来工作的影响"
web_search "人工智能 未来工作 自动化 影响"
web_search "AI job displacement statistics 2024"
web_search "reskilling workforce AI era"
web_search "新兴AI职业 2024"
```

**Output**: `slide-deck/{topic-slug}/source.md`

```markdown
# Source: {Topic}

## Search Keywords
- [keyword 1]
- [keyword 2]
- ...

## Collected Information

### Section 1
- Key point 1
- Key point 2
- Statistics and data

### Section 2
...
```

### Step 2: Content Analysis

**Purpose**: Analyze collected content and recommend presentation structure.

**Actions**:
1. Extract core messages
2. Identify target audience
3. Map visual opportunities
4. Recommend style and slide count
5. Save to `analysis.md`

**Reference**: See `references/analysis-framework.md` for detailed framework.

**Output**: `slide-deck/{topic-slug}/analysis.md`

```markdown
# Analysis: {Topic}

**Topic:** {Full topic description}
**Slug:** {topic-slug}
**Language:** {zh/en}
**Style:** {recommended preset}
**Audience:** {target audience}
**Slide Count:** {N-M}

## Core Messages
1. [Main takeaway 1]
2. [Main takeaway 2]
...

## Content Themes
- [Theme 1]
- [Theme 2]
...

## Recommended Structure
1. Cover
2. Contents
3. [Content sections]
...
N. Back Cover
```

### Step 3: User Confirmation (Optional)

**Purpose**: Confirm style, slides, and audience with user.

**Display**:
```
📊 Analysis Complete

Topic: {topic}
Recommended Style: {preset} - {description}
Recommended Slides: {N}
Target Audience: {audience}

Options:
1. Proceed with recommendations
2. Change style to: [preset options]
3. Adjust slide count
4. Change audience
```

### Step 4: Generate Outline

**Purpose**: Create detailed outline with STYLE_INSTRUCTIONS.

**Actions**:
1. Read style definition from `references/styles/{preset}.md`
2. Build STYLE_INSTRUCTIONS block
3. Define each slide structure
4. Save to `outline.md`

**Reference**: See `references/outline-template.md` for structure.

**Output**: `slide-deck/{topic-slug}/outline.md`

### Step 5: Generate Slide Scripts

**Purpose**: Create detailed script for each slide.

**Actions**:
1. For each slide in outline:
   - Extract slide type, title, key points
   - Add visual description
   - Define layout
2. Save to `prompts/{NN}-slide-{slug}.md`

**Output**: `slide-deck/{topic-slug}/prompts/*.md`

### Step 6: Generate HTML Slides

**Purpose**: Generate 1280x720 HTML for each slide.

**Actions**:
1. Read STYLE_INSTRUCTIONS from outline
2. For each prompt file:
   - Parse slide content
   - Apply style variables
   - Generate complete HTML with CSS
3. Save to `slides/{NN}-slide-{slug}.html`

**Reference**: See `references/html-template.md` for HTML structure.

**Output**: `slide-deck/{topic-slug}/slides/*.html`

### Step 7: Output Summary

**Purpose**: Summarize generated files and provide preview.

**Actions**:
1. Generate `index.html` for preview
2. List all generated files
3. Report completion

**Output**:
```
✅ Slide Deck Complete!

Topic: {topic}
Style: {preset}
Location: slide-deck/{topic-slug}/

Files:
├── source.md
├── analysis.md
├── outline.md
├── prompts/
│   ├── 01-slide-cover.md
│   └── ... ({N} files)
├── slides/
│   ├── 01-slide-cover.html
│   └── ... ({N} files)
└── index.html (preview)
```

## Output Directory Structure

```
slide-deck/{topic-slug}/
├── source.md           # Collected information
├── analysis.md         # Analysis configuration
├── outline.md          # Outline with STYLE_INSTRUCTIONS
├── prompts/            # Slide scripts
│   ├── 01-slide-cover.md
│   ├── 02-slide-contents.md
│   └── ...
├── slides/             # HTML slides (1280x720)
│   ├── 01-slide-cover.html
│   ├── 02-slide-contents.html
│   └── ...
└── index.html          # Preview page
```

## Style System

### Presets

| Preset | Characteristics | Best For |
|--------|-----------------|----------|
| `blueprint` | Grid texture, technical lines, cool blue | Architecture, system design, technical docs |
| `minimal` | Clean white, geometric, lots of whitespace | Executive briefings, summaries |
| `corporate` | Professional navy/gold, balanced density | Investor decks, business proposals |
| `sketch-notes` | Hand-drawn feel, warm colors, organic | Education, tutorials, training |
| `dark-atmospheric` | Deep backgrounds, cinematic, glowing accents | Entertainment, gaming, product launches |

### Auto Style Selection

| Content Signals | Preset |
|-----------------|--------|
| technical, architecture, system, data, analysis | `blueprint` |
| executive, briefing, summary, minimal | `minimal` |
| business, investor, corporate, quarterly | `corporate` |
| education, tutorial, learn, training | `sketch-notes` |
| entertainment, gaming, launch, product | `dark-atmospheric` |
| Default | `blueprint` |

### Style Specifications

Full specifications in `references/styles/{preset}.md`:
- Design aesthetic description
- Background texture and color
- Typography (visual descriptions, not font names)
- Color palette with hex codes
- Visual elements
- Density guidelines
- Do/Don't rules

## Sandbox Tools Usage

### write

Create and save files:

```bash
write source.md [content]
write analysis.md [content]
write outline.md [content]
write prompts/01-slide-cover.md [content]
write slides/01-slide-cover.html [content]
```

### read

Read existing files:

```bash
read outline.md
read prompts/01-slide-cover.md
```

### command / web_search

Execute web searches:

```bash
web_search "search query"
```

### run_code

Execute Python scripts if needed:

```python
# run_code: generate-html.py
python scripts/generate-html.py
```

## Slide Count Guidelines

| Content Length | Recommended Slides |
|----------------|-------------------|
| Brief topic | 5-8 |
| Standard topic | 10-14 |
| Comprehensive topic | 15-20 |
| Extensive topic | 20-25 (consider splitting) |

## Language Handling

- Detect language from user input
- Generate all content in detected language
- Technical terms (file paths, code) remain in English

## References

| File | Content |
|------|---------|
| `references/analysis-framework.md` | Content analysis methodology |
| `references/outline-template.md` | Outline structure and format |
| `references/html-template.md` | HTML generation template |
| `references/layouts.md` | Layout options |
| `references/styles/*.md` | Style preset definitions |

## Notes

- HTML slides are 1280x720 pixels
- Each slide is self-contained with inline CSS
- Use CSS variables for consistent theming
- Maintain visual hierarchy and whitespace
- One clear message per slide
