# Layout Options

Available layouts for slide content organization.

## Layout Gallery

| Layout | Description | Best For |
|--------|-------------|----------|
| `title-hero` | Large centered title with optional visual | Cover slides |
| `split-content` | Left/right content split | Comparisons, dual concepts |
| `grid-four` | 2x2 grid layout | Categories, features |
| `grid-six` | 2x3 grid layout | More detailed categories |
| `data-visualization` | Chart-focused layout | Statistics, trends |
| `process-flow` | Sequential flow diagram | Workflows, steps |
| `triptych` | Three-column layout | Comparisons, categories |
| `full-visual` | Visual-dominant layout | Impact slides |
| `centered-content` | Centered text/visual | Summaries, closings |
| `quote` | Large quote with attribution | Testimonials, insights |

## Layout Details

### title-hero

**Use for**: Cover slides, section dividers

**Structure**:
- Centered title (large)
- Subtitle below
- Optional hero visual/graphic

**HTML Structure**:
```html
<div class="layout-title-hero">
  <h1 class="title">{Title}</h1>
  <p class="subtitle">{Subtitle}</p>
  <div class="visual">{Optional visual}</div>
</div>
```

### split-content

**Use for**: Comparisons, contrasts, dual concepts

**Structure**:
- Left side: Text content or visual
- Right side: Complementary content
- Can swap sides based on flow

**Variations**:
- `split-content-left`: Text left, visual right
- `split-content-right`: Visual left, text right

**HTML Structure**:
```html
<div class="layout-split">
  <div class="content">
    <h2 class="title">{Title}</h2>
    <p class="subtitle">{Subtitle}</p>
    <ul class="key-points">
      <li>{Point 1}</li>
      <li>{Point 2}</li>
    </ul>
  </div>
  <div class="visual">
    {Visual content}
  </div>
</div>
```

### grid-four

**Use for**: Features, categories, steps (up to 4)

**Structure**:
- Header with title
- 2x2 grid of content cards
- Equal sizing for balance

**HTML Structure**:
```html
<div class="layout-grid-four">
  <div class="header">
    <h2 class="title">{Title}</h2>
  </div>
  <div class="grid">
    <div class="grid-item">
      <div class="item-icon">{Icon}</div>
      <h3 class="item-title">{Item 1 Title}</h3>
      <p class="item-desc">{Description}</p>
    </div>
    <!-- Repeat for items 2-4 -->
  </div>
</div>
```

### grid-six

**Use for**: More detailed feature lists, comprehensive categories

**Structure**:
- Header with title
- 2x3 or 3x2 grid
- Smaller cards than grid-four

**HTML Structure**:
```html
<div class="layout-grid-six">
  <div class="header">
    <h2 class="title">{Title}</h2>
  </div>
  <div class="grid">
    <!-- 6 grid items -->
  </div>
</div>
```

### data-visualization

**Use for**: Statistics, charts, data stories

**Structure**:
- Title and context
- Central chart/visualization
- Optional data callouts

**Chart Types**:
- Bar chart (horizontal/vertical)
- Line chart
- Pie/donut chart
- Progress bars
- Number highlights

**HTML Structure**:
```html
<div class="layout-data-viz">
  <div class="header">
    <h2 class="title">{Title}</h2>
    <p class="subtitle">{Data context}</p>
  </div>
  <div class="chart-container">
    {Chart or data visualization}
  </div>
  <div class="data-points">
    <div class="stat">
      <span class="stat__value">{Value}</span>
      <span class="stat__label">{Label}</span>
    </div>
    <!-- More stats -->
  </div>
</div>
```

### process-flow

**Use for**: Workflows, step-by-step processes, timelines

**Structure**:
- Title
- Sequential steps with connectors
- Optional icons per step

**Variations**:
- Horizontal flow (default)
- Vertical flow
- Circular/cycle flow

**HTML Structure**:
```html
<div class="layout-process">
  <div class="header">
    <h2 class="title">{Process Title}</h2>
    <p class="subtitle">{Process description}</p>
  </div>
  <div class="steps">
    <div class="step">
      <div class="step-number">1</div>
      <h3 class="step-title">{Step 1}</h3>
      <p class="step-desc">{Description}</p>
    </div>
    <!-- More steps with connector arrows -->
  </div>
</div>
```

### triptych

**Use for**: Three-way comparisons, categories, before/during/after

**Structure**:
- Title
- Three equal columns
- Column headers with content lists

**HTML Structure**:
```html
<div class="layout-triptych">
  <div class="header">
    <h2 class="title">{Title}</h2>
    <p class="subtitle">{Subtitle}</p>
  </div>
  <div class="columns">
    <div class="column">
      <h3 class="column-header">{Column 1}</h3>
      <ul class="column-items">
        <li>{Item 1}</li>
        <li>{Item 2}</li>
      </ul>
    </div>
    <!-- Columns 2 and 3 -->
  </div>
</div>
```

### full-visual

**Use for**: Impact moments, visual stories, emotional appeal

**Structure**:
- Large background visual
- Minimal text overlay
- High visual dominance (80%+ visual)

**HTML Structure**:
```html
<div class="layout-full-visual">
  <div class="visual-bg">
    {Background visual}
  </div>
  <div class="text-overlay">
    <h2 class="title">{Short title}</h2>
    <p class="message">{Key message}</p>
  </div>
</div>
```

### centered-content

**Use for**: Summaries, key takeaways, closing slides

**Structure**:
- Centered title
- Centered content block
- Balanced whitespace

**HTML Structure**:
```html
<div class="layout-centered">
  <h2 class="title">{Title}</h2>
  <p class="subtitle">{Subtitle}</p>
  <div class="content">
    <ul class="points">
      <li>{Point 1}</li>
      <li>{Point 2}</li>
    </ul>
  </div>
</div>
```

### quote

**Use for**: Testimonials, expert quotes, key insights

**Structure**:
- Large quote text
- Attribution (name, title, organization)
- Optional visual accent

**HTML Structure**:
```html
<div class="layout-quote">
  <blockquote class="quote-text">
    "{Quote text}"
  </blockquote>
  <div class="attribution">
    <span class="name">{Person name}</span>
    <span class="title">{Title/Organization}</span>
  </div>
</div>
```

## Layout Selection Guide

### By Content Type

| Content Type | Recommended Layout |
|--------------|-------------------|
| Introduction/Title | `title-hero` |
| Table of Contents | `grid-four`, `grid-six` |
| Key Statistics | `data-visualization` |
| Process/Steps | `process-flow` |
| Comparisons | `triptych`, `split-content` |
| Feature List | `grid-four`, `grid-six` |
| Conclusion | `centered-content` |
| Call to Action | `centered-content`, `full-visual` |
| Expert Quote | `quote` |

### By Slide Position

| Position | Common Layouts |
|----------|---------------|
| Slide 1 (Cover) | `title-hero` |
| Slide 2 (Contents) | `grid-four` |
| Middle slides | Varies by content |
| Final slide (Back Cover) | `centered-content`, `title-hero` |

### By Information Density

| Density Level | Suitable Layouts |
|---------------|-----------------|
| Minimal (1 point) | `title-hero`, `full-visual`, `quote` |
| Low (2-3 points) | `centered-content`, `split-content` |
| Medium (4-6 points) | `grid-four`, `triptych` |
| High (6+ points) | `grid-six`, `data-visualization` |
