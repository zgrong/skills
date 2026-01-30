# Minimal Style

Clean, sophisticated style with maximum whitespace.

## Overview

| Property | Value |
|----------|-------|
| Texture | Clean, pure solid colors |
| Mood | Neutral, sophisticated, calm |
| Typography | Geometric sans-serif, light weights |
| Density | Minimal |

## Design Aesthetic

Extreme simplicity and elegance. Maximum whitespace, minimal elements, and refined typography. Each slide focuses on one clear message with nothing extraneous. Inspired by Apple and high-end luxury brands.

## Color Palette

| Role | Name | Hex | Usage |
|------|------|-----|-------|
| Background | Pure White | `#FFFFFF` | Slide background |
| Primary Text | Charcoal | `#1F2937` | Headlines |
| Secondary Text | Slate | `#6B7280` | Body text, subtitles |
| Accent | Slate Blue | `#3B82F6` | Minimal highlights |
| Border | Light Gray | `#E5E7EB` | Subtle dividers |

## Typography

### Headlines
- Style: Light geometric sans-serif
- Visual: Thin, elegant, modern
- Weight: 300-400 (Light to Regular)
- Letter-spacing: 0.05em (slightly wide)

### Body
- Style: Clean sans-serif
- Visual: Highly readable, modern
- Weight: 400 (Regular)
- Line-height: 1.8

## Visual Elements

- **No grid or texture**: Pure solid backgrounds
- **Generous whitespace**: 80px+ margins
- **Subtle lines**: 1px borders only when necessary
- **Icons**: Single-line, ultra-minimal
- **Charts**: Data points only, no decoration
- **Shapes**: Perfect geometry, no fills

## Density Guidelines

- **Content per slide**: 1-2 key points maximum
- **Whitespace**: Dominant (60%+ of slide)
- **Element count**: Maximum 3-4 elements
- **Visual hierarchy**: Through size only

## Style Rules

### DO
- Embrace empty space
- Use single focal point per slide
- Keep typography light and elegant
- Maintain absolute consistency
- Use subtle, thin borders if needed

### DON'T
- Add decorative elements
- Use bold or heavy typography
- Include multiple competing elements
- Use backgrounds or textures
- Add shadows or effects

## CSS Variables

```css
:root {
  --color-bg: #FFFFFF;
  --color-text-primary: #1F2937;
  --color-text-secondary: #6B7280;
  --color-accent: #3B82F6;
  --color-border: #E5E7EB;
}
```

## Example CSS

```css
.slide--minimal {
  background: var(--color-bg);
  padding: 80px 100px;
}

.slide--minimal .title {
  font-weight: 300;
  letter-spacing: 0.05em;
  color: var(--color-text-primary);
}

.slide--minimal .subtitle {
  font-weight: 400;
  color: var(--color-text-secondary);
}
```

## Best For

- Executive briefings
- High-level summaries
- Luxury brand presentations
- Investor updates
- Keynote highlights
- Minimalist product launches
