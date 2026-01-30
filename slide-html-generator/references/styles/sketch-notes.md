# Sketch Notes Style

Hand-drawn, educational style with warmth and personality.

## Overview

| Property | Value |
|----------|-------|
| Texture | Organic, paper-like |
| Mood | Warm, friendly, approachable |
| Typography | Handwritten headlines, humanist body |
| Density | Balanced |

## Design Aesthetic

Approachable and educational with hand-drawn charm. Feels like visual notes from an engaging workshop. Warm colors and organic shapes create a welcoming, non-intimidating atmosphere perfect for learning.

## Color Palette

| Role | Name | Hex | Usage |
|------|------|-----|-------|
| Background | Cream Paper | `#FDF6E3` | Slide background |
| Primary Text | Warm Black | `#2D3748` | Headlines |
| Secondary Text | Warm Gray | `#4A5568` | Body text |
| Primary Accent | Coral | `#E53E3E` | Key highlights |
| Secondary Accent | Teal | `#319795` | Secondary accents |
| Tertiary | Warm Yellow | `#F6E05E` | Highlight fills |
| Sketch Lines | Dark Brown | `#744210` | Hand-drawn elements |

## Typography

### Headlines
- Style: Hand-drawn marker appearance
- Visual: Energetic, slightly imperfect, friendly
- Weight: Bold with organic variation
- Letter-spacing: Normal

### Body
- Style: Humanist sans-serif
- Visual: Friendly, readable, warm
- Weight: 400 (Regular)
- Line-height: 1.8

## Visual Elements

- **Hand-drawn borders**: Slightly wobbly lines
- **Organic shapes**: Imperfect circles, flowing forms
- **Sketch icons**: Illustrated, not geometric
- **Doodles**: Arrows, underlines, circles
- **Highlights**: Marker-style fills
- **Connectors**: Flowing curves, hand-drawn arrows

## Density Guidelines

- **Content per slide**: 3-4 key points
- **Whitespace**: Generous but casual
- **Element placement**: Organic, not grid-strict
- **Visual notes**: Annotations and callouts welcome

## Style Rules

### DO
- Use hand-drawn line styles (2-3px, slightly uneven)
- Include organic shapes and doodles
- Apply marker-style highlights
- Use warm, approachable colors
- Add visual annotations and arrows

### DON'T
- Use perfect geometric shapes
- Apply rigid grid layouts
- Use cold or corporate colors
- Include photographic elements
- Make it too polished or perfect

## CSS Variables

```css
:root {
  --color-bg: #FDF6E3;
  --color-text-primary: #2D3748;
  --color-text-secondary: #4A5568;
  --color-accent-primary: #E53E3E;
  --color-accent-secondary: #319795;
  --color-accent-tertiary: #F6E05E;
  --color-sketch: #744210;
}
```

## Example CSS

```css
.slide--sketch {
  background: var(--color-bg);
  padding: 48px;
}

.slide--sketch .title {
  font-family: 'Comic Neue', cursive, sans-serif;
  font-weight: 700;
  color: var(--color-text-primary);
}

.slide--sketch .highlight {
  background: var(--color-accent-tertiary);
  padding: 2px 8px;
  border-radius: 4px;
}

.slide--sketch .hand-drawn-box {
  border: 3px solid var(--color-sketch);
  border-radius: 12px;
  /* Slightly irregular border effect */
}
```

## Visual Effects

### Hand-drawn border (CSS approximation)

```css
.hand-drawn {
  border: 3px solid var(--color-sketch);
  border-radius: 255px 15px 225px 15px/15px 225px 15px 255px;
}
```

### Marker highlight

```css
.marker-highlight {
  background: linear-gradient(
    to bottom,
    transparent 50%,
    var(--color-accent-tertiary) 50%
  );
}
```

## Best For

- Educational content
- Training materials
- Workshop presentations
- Tutorials and how-tos
- Informal team presentations
- Creative brainstorming
