# Corporate Style

Professional, trustworthy style for business presentations.

## Overview

| Property | Value |
|----------|-------|
| Texture | Clean with subtle structure |
| Mood | Professional, authoritative, warm |
| Typography | Geometric sans-serif, medium weights |
| Density | Balanced |

## Design Aesthetic

Polished and professional with a balance of authority and approachability. Navy and gold accents convey trust and premium quality. Structured layouts with clear hierarchy suitable for stakeholder presentations.

## Color Palette

| Role | Name | Hex | Usage |
|------|------|-----|-------|
| Background | Off White | `#FAFAFA` | Slide background |
| Primary Text | Navy | `#1E3A5F` | Headlines |
| Secondary Text | Slate | `#475569` | Body text |
| Primary Accent | Royal Blue | `#1D4ED8` | Key highlights |
| Secondary Accent | Gold | `#D97706` | Premium accents |
| Tertiary | Light Navy | `#DBEAFE` | Card backgrounds |
| Border | Silver | `#CBD5E1` | Dividers, cards |

## Typography

### Headlines
- Style: Bold geometric sans-serif
- Visual: Strong, confident, professional
- Weight: 600-700 (Semi-bold to Bold)
- Letter-spacing: -0.01em

### Body
- Style: Clean sans-serif
- Visual: Professional, readable
- Weight: 400 (Regular)
- Line-height: 1.7

## Visual Elements

- **Subtle backgrounds**: Light gradient or solid
- **Professional icons**: Filled or outlined, consistent
- **Charts**: Business-appropriate, labeled clearly
- **Cards**: Subtle shadows, rounded corners
- **Lines**: Clean separators, navy accents
- **Shapes**: Rounded rectangles, professional feel

## Density Guidelines

- **Content per slide**: 3-5 key points
- **Whitespace**: Balanced (40-50% of slide)
- **Element spacing**: Generous but efficient
- **Visual hierarchy**: Clear through color and weight

## Style Rules

### DO
- Use navy for authority, gold for highlights
- Maintain consistent card styling
- Include clear data labels
- Use professional icon style
- Apply subtle shadows for depth

### DON'T
- Use playful or casual elements
- Include hand-drawn graphics
- Use bright or neon colors
- Add excessive decoration
- Mix too many accent colors

## CSS Variables

```css
:root {
  --color-bg: #FAFAFA;
  --color-text-primary: #1E3A5F;
  --color-text-secondary: #475569;
  --color-accent-primary: #1D4ED8;
  --color-accent-secondary: #D97706;
  --color-accent-tertiary: #DBEAFE;
  --color-border: #CBD5E1;
}
```

## Example CSS

```css
.slide--corporate {
  background: var(--color-bg);
  padding: 64px;
}

.slide--corporate .card {
  background: white;
  border: 1px solid var(--color-border);
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  padding: 24px;
}

.slide--corporate .highlight {
  color: var(--color-accent-secondary);
  font-weight: 600;
}
```

## Best For

- Investor presentations
- Quarterly reports
- Business proposals
- Corporate communications
- Strategy presentations
- Stakeholder updates
