# Outline Template

Standard structure for slide deck outlines with style instructions.

## Outline Format

```markdown
# {Topic} - Slide Deck Outline

**Topic**: {topic description}
**Style**: {preset name}
**Audience**: {target audience}
**Language**: {output language}
**Slide Count**: {N} slides
**Generated**: {YYYY-MM-DD HH:mm}

---

## STYLE_INSTRUCTIONS

{Complete style block - see below}

---

## Slide 1: Cover
{slide definition}

---

## Slide 2: Contents
{slide definition}

---

## Slide 3: {Title}
{slide definition}

...

## Slide N: Back Cover
{slide definition}
```

## STYLE_INSTRUCTIONS Block

The STYLE_INSTRUCTIONS block is the SINGLE SOURCE OF TRUTH for style information.

```markdown
## STYLE_INSTRUCTIONS

**Visual Style:** {preset name}
**Texture:** {texture description}
**Mood:** {mood description}
**Typography:** {typography style}
**Density:** {density level}

**Color Palette:**
- Background: {Name} ({Hex})
- Grid/Texture: {Name} ({Hex})
- Primary Text: {Name} ({Hex})
- Primary Accent: {Name} ({Hex})
- Secondary Accent: {Name} ({Hex})
- Tertiary: {Name} ({Hex})

**Visual Elements:**
- {Element 1 with rendering guidance}
- {Element 2 with rendering guidance}
- {Element 3}

**Style Rules - DO:**
- {Guideline 1}
- {Guideline 2}
- {Guideline 3}

**Style Rules - DON'T:**
- {Anti-pattern 1}
- {Anti-pattern 2}
- {Anti-pattern 3}
```

## Slide Definition Templates

### Cover Slide

```markdown
## Slide 1: Cover
**Type:** Cover
**Layout:** title-hero

**Title:** {Main title}
**Subtitle:** {Supporting tagline}

**Visual:** {Detailed visual description - composition, elements, mood}

**Notes:** {Any special considerations}
```

### Contents Slide

```markdown
## Slide 2: Contents
**Type:** Table of Contents
**Layout:** grid-four

**Title:** {Contents title, e.g., "内容概览"}

**Sections:**
1. {Section 1 name}
2. {Section 2 name}
3. {Section 3 name}
4. {Section 4 name}

**Visual:** {Visual treatment for contents}
```

### Content Slide

```markdown
## Slide X: {Slide Title}
**Type:** Content
**Layout:** {layout name}

**Title:** {Main headline}
**Subtitle:** {Supporting context}

**Key Points:**
- {Point 1}
- {Point 2}
- {Point 3}

**Visual:** {Detailed visual description}

**Data:** {If applicable - statistics, charts}
```

### Data Visualization Slide

```markdown
## Slide X: {Slide Title}
**Type:** Content
**Layout:** data-visualization

**Title:** {Main headline}
**Subtitle:** {Data context}

**Data Points:**
- {Metric 1}: {Value} ({context})
- {Metric 2}: {Value} ({context})
- {Metric 3}: {Value} ({context})

**Chart Type:** {bar/line/pie/etc.}

**Visual:** {Chart styling and composition}
```

### Process Flow Slide

```markdown
## Slide X: {Slide Title}
**Type:** Content
**Layout:** process-flow

**Title:** {Process name}
**Subtitle:** {Process description}

**Steps:**
1. **{Step 1 name}**
   - {Detail 1}
   - {Detail 2}

2. **{Step 2 name}**
   - {Detail 1}
   - {Detail 2}

3. **{Step 3 name}**
   - {Detail 1}
   - {Detail 2}

**Visual:** {Flow diagram styling}
```

### Comparison Slide

```markdown
## Slide X: {Slide Title}
**Type:** Content
**Layout:** triptych

**Title:** {Comparison title}
**Subtitle:** {Comparison context}

**Columns:**
1. **{Column 1 header}**
   - {Item 1}
   - {Item 2}
   - {Item 3}

2. **{Column 2 header}**
   - {Item 1}
   - {Item 2}
   - {Item 3}

3. **{Column 3 header}**
   - {Item 1}
   - {Item 2}
   - {Item 3}

**Visual:** {Column styling and icons}
```

### Back Cover Slide

```markdown
## Slide N: Back Cover
**Type:** Back Cover
**Layout:** centered-content

**Title:** {Closing statement}
**Subtitle:** {Optional secondary text}

**Closing Message:** {Memorable closing or call-to-action}

**Visual:** {Clean, minimal closing visual}
```

## Layout Options

| Layout | Description | Best For |
|--------|-------------|----------|
| `title-hero` | Large centered title with visual | Cover slides |
| `split-content` | Left/right content split | Comparisons, dual concepts |
| `grid-four` | 2x2 grid layout | Categories, features |
| `data-visualization` | Chart-focused layout | Statistics, trends |
| `process-flow` | Sequential flow diagram | Workflows, steps |
| `triptych` | Three-column layout | Comparisons, categories |
| `full-visual` | Visual-dominant layout | Impact slides |
| `centered-content` | Centered text/visual | Summaries, closings |

## Slide Numbering

- Cover is always Slide 1
- Contents is typically Slide 2
- Content slides use sequential numbers
- Back Cover is always final slide (N)

## Filename Conventions

Format: `{NN}-slide-{slug}.{ext}`

| Slide Type | Filename Pattern | Example |
|------------|------------------|---------|
| Cover | `01-slide-cover` | `01-slide-cover.html` |
| Contents | `02-slide-contents` | `02-slide-contents.html` |
| Content | `{NN}-slide-{topic-slug}` | `03-slide-automation-rise.html` |
| Back Cover | `{NN}-slide-back-cover` | `14-slide-back-cover.html` |

Slug rules:
- Kebab-case (lowercase, hyphens)
- Derived from slide title
- Maximum 30 characters
- Unique within deck

## Example Outline

```markdown
# AI对未来工作的影响 - Slide Deck Outline

**Topic**: 人工智能对未来工作的影响
**Style**: blueprint
**Audience**: experts/professionals
**Language**: zh
**Slide Count**: 14 slides
**Generated**: 2024-01-15 10:30

---

## STYLE_INSTRUCTIONS

**Visual Style:** blueprint
**Texture:** grid with subtle technical engineering paper overlay
**Mood:** cool, analytical, professional
**Typography:** geometric sans-serif for headlines, clean serif for body
**Density:** balanced

**Color Palette:**
- Background: Blueprint Paper (#FAF8F5)
- Grid: Light Gray (#E5E5E5)
- Primary Text: Deep Slate (#334155)
- Primary Accent: Engineering Blue (#2563EB)
- Secondary Accent: Navy Blue (#1E3A5F)
- Tertiary: Light Blue (#BFDBFE)

**Visual Elements:**
- Precise technical line work with consistent stroke weights
- Engineering schematics and clean vector graphics
- Grid-based layouts with geometric precision
- Clean data visualization with minimal charts

**Style Rules - DO:**
- Maintain consistent line weights throughout
- Use grid alignment for all elements
- Keep color palette restrained and unified

**Style Rules - DON'T:**
- Use hand-drawn or organic shapes
- Add decorative flourishes
- Include photographic elements

---

## Slide 1: Cover
**Type:** Cover
**Layout:** title-hero

**Title:** 人工智能对未来工作的影响
**Subtitle:** 自动化浪潮下的劳动力市场重构

**Visual:** Abstract blueprint schematic of interconnected gears and circuits representing AI and human workforce integration

---

## Slide 2: Contents
**Type:** Table of Contents
**Layout:** grid-four

**Title:** 内容概览

**Sections:**
1. 自动化的崛起
2. 工作岗位的变迁
3. 新兴职业机会
4. 技能再培训策略

**Visual:** Clean grid layout with blueprint-style icons

---

...
```
