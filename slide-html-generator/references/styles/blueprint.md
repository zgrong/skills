# Blueprint Style

Technical, analytical style with engineering precision.

## Overview

| Property | Value |
|----------|-------|
| Texture | Grid with technical paper overlay |
| Mood | Cool, analytical, professional |
| Typography | Geometric sans-serif headlines, clean serif body |
| Density | Balanced |

## Design Aesthetic

Clean, technical precision reminiscent of engineering blueprints. Emphasizes structure, data clarity, and professional authority. Grid-based layouts with geometric precision and restrained color palette.

## Color Palette

| Role | Name | Hex | Usage |
|------|------|-----|-------|
| Background | Blueprint Paper | `#FAF8F5` | Slide background |
| Grid | Light Gray | `#E5E5E5` | Grid overlay, borders |
| Primary Text | Deep Slate | `#334155` | Headlines, body text |
| Primary Accent | Engineering Blue | `#2563EB` | Key highlights, icons |
| Secondary Accent | Navy Blue | `#1E3A5F` | Subtitles, secondary text |
| Tertiary | Light Blue | `#BFDBFE` | Backgrounds, fills |
| Warning/Highlight | Amber | `#F59E0B` | Callouts, alerts |

## Typography

### Headlines
- Style: Bold geometric sans-serif
- Visual: Clean, precise letterforms with perfect geometry
- Weight: 700 (Bold)
- Letter-spacing: -0.02em (tight)

### Body
- Style: Clean serif with technical feel
- Visual: Readable, professional, timeless
- Weight: 400 (Regular)
- Line-height: 1.6-1.8

### Code/Technical
- Style: Monospace
- Visual: Even character width, technical precision

## Visual Elements

- **Grid overlay**: Subtle 40px grid pattern
- **Technical lines**: Precise stroke weights (1-2px)
- **Schematics**: Clean vector graphics, engineering diagram style
- **Icons**: Geometric, outlined, consistent stroke
- **Charts**: Minimal decoration, data-focused
- **Connectors**: Straight lines, 90-degree angles
- **Shapes**: Geometric precision, clean edges

## Density Guidelines

- **Content per slide**: 3-5 key points maximum
- **Whitespace**: Generous margins (64px minimum)
- **Element spacing**: Consistent grid-based spacing
- **Visual hierarchy**: Clear through size and color

## Style Rules

### DO
- Maintain consistent line weights throughout
- Use grid alignment for all elements
- Keep color palette restrained and unified
- Create clear visual hierarchy through scale
- Use geometric precision for all shapes
- Apply technical annotation style for callouts

### DON'T
- Use hand-drawn or organic shapes
- Add decorative flourishes
- Use curved connection lines (except for data)
- Include photographic elements
- Add slide numbers, footers, or logos
- Use gradient backgrounds

## CSS Variables

```css
:root {
  --color-bg: #FAF8F5;
  --color-grid: #E5E5E5;
  --color-text-primary: #334155;
  --color-accent-primary: #2563EB;
  --color-accent-secondary: #1E3A5F;
  --color-accent-tertiary: #BFDBFE;
  --color-warning: #F59E0B;
}
```

## Grid Overlay CSS

```css
.slide--blueprint::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image: 
    linear-gradient(var(--color-grid) 1px, transparent 1px),
    linear-gradient(90deg, var(--color-grid) 1px, transparent 1px);
  background-size: 40px 40px;
  opacity: 0.5;
  pointer-events: none;
}
```

## Best For

- Architecture and system design presentations
- Technical documentation
- Data analysis reports
- Engineering proposals
- Research presentations
- Technology briefings
