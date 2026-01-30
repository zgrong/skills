# Dark Atmospheric Style

Cinematic, immersive style with dramatic dark backgrounds.

## Overview

| Property | Value |
|----------|-------|
| Texture | Clean with subtle depth |
| Mood | Dark, dramatic, immersive |
| Typography | Bold editorial, high contrast |
| Density | Balanced to minimal |

## Design Aesthetic

Cinematic and immersive with deep dark backgrounds and glowing accents. Creates drama and focus through contrast. Perfect for impactful presentations that need to capture attention and create memorable moments.

## Color Palette

| Role | Name | Hex | Usage |
|------|------|-----|-------|
| Background | Deep Space | `#0F172A` | Primary background |
| Background Alt | Dark Slate | `#1E293B` | Cards, sections |
| Primary Text | Ice White | `#F8FAFC` | Headlines |
| Secondary Text | Cool Gray | `#94A3B8` | Body text |
| Primary Accent | Electric Blue | `#38BDF8` | Key highlights |
| Secondary Accent | Purple Glow | `#A78BFA` | Secondary accents |
| Tertiary | Neon Pink | `#F472B6` | Special highlights |
| Border | Dark Border | `#334155` | Subtle dividers |

## Typography

### Headlines
- Style: Bold, high-contrast sans-serif
- Visual: Impactful, dramatic, modern
- Weight: 700-800 (Bold to Extra Bold)
- Letter-spacing: -0.02em

### Body
- Style: Clean sans-serif, light weight
- Visual: Readable on dark backgrounds
- Weight: 300-400 (Light to Regular)
- Line-height: 1.8

## Visual Elements

- **Gradient backgrounds**: Subtle dark gradients
- **Glow effects**: Soft glows on accents
- **Light lines**: Thin accent lines
- **Glass morphism**: Frosted glass cards
- **Icons**: Outlined with glow
- **Data viz**: Glowing, neon-style

## Density Guidelines

- **Content per slide**: 2-4 key points
- **Whitespace**: Strategic dark space
- **Element focus**: One hero element per slide
- **Contrast**: Maximum text/background contrast

## Style Rules

### DO
- Use dark gradients for depth
- Apply subtle glow effects on accents
- Maintain high text contrast
- Use glass-morphism for cards
- Create dramatic focal points

### DON'T
- Use pure black backgrounds
- Add too many competing glows
- Use low-contrast text
- Include bright daylight imagery
- Overcrowd with elements

## CSS Variables

```css
:root {
  --color-bg: #0F172A;
  --color-bg-alt: #1E293B;
  --color-text-primary: #F8FAFC;
  --color-text-secondary: #94A3B8;
  --color-accent-primary: #38BDF8;
  --color-accent-secondary: #A78BFA;
  --color-accent-tertiary: #F472B6;
  --color-border: #334155;
}
```

## Example CSS

```css
.slide--dark {
  background: linear-gradient(135deg, var(--color-bg) 0%, var(--color-bg-alt) 100%);
  color: var(--color-text-primary);
  padding: 64px;
}

.slide--dark .title {
  font-weight: 800;
  letter-spacing: -0.02em;
  text-shadow: 0 0 40px rgba(56, 189, 248, 0.3);
}

.slide--dark .accent {
  color: var(--color-accent-primary);
  text-shadow: 0 0 20px rgba(56, 189, 248, 0.5);
}

.slide--dark .glass-card {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
}
```

## Glow Effects

```css
.glow-blue {
  box-shadow: 0 0 30px rgba(56, 189, 248, 0.4);
}

.glow-purple {
  box-shadow: 0 0 30px rgba(167, 139, 250, 0.4);
}

.glow-text {
  text-shadow: 0 0 20px currentColor;
}
```

## Best For

- Product launches
- Gaming presentations
- Entertainment content
- Tech keynotes
- Creative showcases
- Night/evening events
