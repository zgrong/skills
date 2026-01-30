# HTML Template

Standard HTML structure for 1280x720 slide generation.

## Base HTML Structure

```html
<!DOCTYPE html>
<html lang="{language}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=1280">
  <title>{Slide Title} - {Deck Title}</title>
  <style>
    {CSS_VARIABLES}
    {BASE_STYLES}
    {LAYOUT_STYLES}
    {COMPONENT_STYLES}
  </style>
</head>
<body>
  <div class="slide">
    {SLIDE_CONTENT}
  </div>
</body>
</html>
```

## CSS Variables (from STYLE_INSTRUCTIONS)

```css
:root {
  /* Dimensions */
  --slide-width: 1280px;
  --slide-height: 720px;
  
  /* Colors - from STYLE_INSTRUCTIONS */
  --color-bg: {Background Hex};
  --color-grid: {Grid/Texture Hex};
  --color-text-primary: {Primary Text Hex};
  --color-accent-primary: {Primary Accent Hex};
  --color-accent-secondary: {Secondary Accent Hex};
  --color-accent-tertiary: {Tertiary Hex};
  
  /* Typography */
  --font-headline: system-ui, -apple-system, sans-serif;
  --font-body: Georgia, serif;
  --font-mono: 'SF Mono', monospace;
  
  /* Spacing */
  --spacing-xs: 8px;
  --spacing-sm: 16px;
  --spacing-md: 24px;
  --spacing-lg: 48px;
  --spacing-xl: 64px;
  
  /* Typography Sizes */
  --text-xs: 14px;
  --text-sm: 16px;
  --text-base: 18px;
  --text-lg: 24px;
  --text-xl: 32px;
  --text-2xl: 40px;
  --text-3xl: 48px;
  --text-4xl: 64px;
}
```

## Base Styles

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: var(--font-body);
  font-size: var(--text-base);
  line-height: 1.6;
  color: var(--color-text-primary);
  background: #f0f0f0;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

.slide {
  width: var(--slide-width);
  height: var(--slide-height);
  background: var(--color-bg);
  position: relative;
  overflow: hidden;
  padding: var(--spacing-xl);
}

/* Grid texture overlay (for blueprint style) */
.slide--grid::before {
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

## Layout Styles

### Title Hero (Cover)

```css
.layout-title-hero {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  height: 100%;
}

.layout-title-hero .title {
  font-family: var(--font-headline);
  font-size: var(--text-4xl);
  font-weight: 700;
  color: var(--color-text-primary);
  margin-bottom: var(--spacing-md);
  letter-spacing: -0.02em;
}

.layout-title-hero .subtitle {
  font-size: var(--text-xl);
  color: var(--color-accent-secondary);
  max-width: 800px;
}

.layout-title-hero .visual {
  margin-top: var(--spacing-xl);
}
```

### Split Content

```css
.layout-split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--spacing-xl);
  height: 100%;
  align-items: center;
}

.layout-split .content {
  padding: var(--spacing-lg);
}

.layout-split .visual {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

### Grid Four

```css
.layout-grid-four {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.layout-grid-four .header {
  text-align: center;
  margin-bottom: var(--spacing-lg);
}

.layout-grid-four .grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: var(--spacing-lg);
  flex: 1;
}

.layout-grid-four .grid-item {
  background: rgba(255, 255, 255, 0.5);
  border: 1px solid var(--color-grid);
  border-radius: 8px;
  padding: var(--spacing-md);
}
```

### Data Visualization

```css
.layout-data-viz {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.layout-data-viz .header {
  margin-bottom: var(--spacing-lg);
}

.layout-data-viz .chart-container {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.layout-data-viz .data-points {
  display: flex;
  gap: var(--spacing-lg);
  justify-content: center;
  margin-top: var(--spacing-lg);
}
```

### Process Flow

```css
.layout-process {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.layout-process .header {
  text-align: center;
  margin-bottom: var(--spacing-lg);
}

.layout-process .steps {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  flex: 1;
}

.layout-process .step {
  flex: 1;
  text-align: center;
  padding: var(--spacing-md);
  position: relative;
}

.layout-process .step::after {
  content: '→';
  position: absolute;
  right: -20px;
  top: 50%;
  transform: translateY(-50%);
  font-size: var(--text-xl);
  color: var(--color-accent-primary);
}

.layout-process .step:last-child::after {
  display: none;
}
```

### Triptych (Three Columns)

```css
.layout-triptych {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.layout-triptych .header {
  text-align: center;
  margin-bottom: var(--spacing-lg);
}

.layout-triptych .columns {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--spacing-lg);
  flex: 1;
}

.layout-triptych .column {
  background: rgba(255, 255, 255, 0.3);
  border: 1px solid var(--color-grid);
  border-radius: 8px;
  padding: var(--spacing-md);
}

.layout-triptych .column-header {
  font-family: var(--font-headline);
  font-size: var(--text-lg);
  font-weight: 600;
  color: var(--color-accent-primary);
  margin-bottom: var(--spacing-sm);
  padding-bottom: var(--spacing-sm);
  border-bottom: 2px solid var(--color-accent-primary);
}
```

### Centered Content

```css
.layout-centered {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  height: 100%;
}

.layout-centered .title {
  font-family: var(--font-headline);
  font-size: var(--text-3xl);
  font-weight: 700;
  margin-bottom: var(--spacing-md);
}

.layout-centered .content {
  max-width: 900px;
}

.layout-centered .points {
  text-align: left;
  display: inline-block;
}
```

## Component Styles

```css
/* Headlines */
.headline {
  font-family: var(--font-headline);
  font-weight: 700;
  letter-spacing: -0.02em;
}

.headline--xl { font-size: var(--text-4xl); }
.headline--lg { font-size: var(--text-3xl); }
.headline--md { font-size: var(--text-2xl); }
.headline--sm { font-size: var(--text-xl); }

/* Subtitles */
.subtitle {
  font-size: var(--text-lg);
  color: var(--color-accent-secondary);
  margin-top: var(--spacing-xs);
}

/* Body text */
.body-text {
  font-size: var(--text-base);
  line-height: 1.8;
}

/* Lists */
.key-points {
  list-style: none;
  padding: 0;
}

.key-points li {
  position: relative;
  padding-left: var(--spacing-lg);
  margin-bottom: var(--spacing-sm);
}

.key-points li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 10px;
  width: 8px;
  height: 8px;
  background: var(--color-accent-primary);
  border-radius: 50%;
}

/* Data highlights */
.stat {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.stat__value {
  font-family: var(--font-headline);
  font-size: var(--text-3xl);
  font-weight: 700;
  color: var(--color-accent-primary);
}

.stat__label {
  font-size: var(--text-sm);
  color: var(--color-accent-secondary);
  text-transform: uppercase;
  letter-spacing: 0.1em;
}

/* Cards */
.card {
  background: rgba(255, 255, 255, 0.5);
  border: 1px solid var(--color-grid);
  border-radius: 8px;
  padding: var(--spacing-md);
}

.card__title {
  font-family: var(--font-headline);
  font-size: var(--text-lg);
  font-weight: 600;
  color: var(--color-accent-primary);
  margin-bottom: var(--spacing-sm);
}

.card__content {
  font-size: var(--text-base);
}

/* Icons (SVG placeholders) */
.icon {
  width: 48px;
  height: 48px;
  fill: var(--color-accent-primary);
}

.icon--sm { width: 24px; height: 24px; }
.icon--lg { width: 64px; height: 64px; }
```

## Style Variations

### Blueprint Style

```css
/* Additional blueprint-specific styles */
.slide--blueprint {
  background: #FAF8F5;
}

.slide--blueprint::before {
  background-image: 
    linear-gradient(#E5E5E5 1px, transparent 1px),
    linear-gradient(90deg, #E5E5E5 1px, transparent 1px);
  background-size: 40px 40px;
}

.slide--blueprint .accent-line {
  border-color: #2563EB;
}
```

### Minimal Style

```css
.slide--minimal {
  background: #FFFFFF;
  padding: var(--spacing-xl) calc(var(--spacing-xl) * 1.5);
}

.slide--minimal .title {
  font-weight: 300;
  letter-spacing: 0.05em;
}
```

### Dark Atmospheric Style

```css
.slide--dark {
  background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
  color: #F8FAFC;
}

.slide--dark .subtitle {
  color: #94A3B8;
}

.slide--dark .accent {
  color: #38BDF8;
}
```

## Complete Example

```html
<!DOCTYPE html>
<html lang="zh">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=1280">
  <title>封面 - AI对未来工作的影响</title>
  <style>
    :root {
      --slide-width: 1280px;
      --slide-height: 720px;
      --color-bg: #FAF8F5;
      --color-grid: #E5E5E5;
      --color-text-primary: #334155;
      --color-accent-primary: #2563EB;
      --color-accent-secondary: #1E3A5F;
      --color-accent-tertiary: #BFDBFE;
      --font-headline: system-ui, -apple-system, sans-serif;
      --font-body: Georgia, serif;
      --spacing-md: 24px;
      --spacing-lg: 48px;
      --spacing-xl: 64px;
      --text-xl: 32px;
      --text-4xl: 64px;
    }
    
    * { margin: 0; padding: 0; box-sizing: border-box; }
    
    body {
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      background: #f0f0f0;
    }
    
    .slide {
      width: var(--slide-width);
      height: var(--slide-height);
      background: var(--color-bg);
      position: relative;
      overflow: hidden;
      padding: var(--spacing-xl);
    }
    
    .slide::before {
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
    
    .layout-title-hero {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      height: 100%;
      position: relative;
      z-index: 1;
    }
    
    .title {
      font-family: var(--font-headline);
      font-size: var(--text-4xl);
      font-weight: 700;
      color: var(--color-text-primary);
      margin-bottom: var(--spacing-md);
      letter-spacing: -0.02em;
    }
    
    .subtitle {
      font-size: var(--text-xl);
      color: var(--color-accent-secondary);
      max-width: 800px;
    }
  </style>
</head>
<body>
  <div class="slide">
    <div class="layout-title-hero">
      <h1 class="title">人工智能对未来工作的影响</h1>
      <p class="subtitle">自动化浪潮下的劳动力市场重构</p>
    </div>
  </div>
</body>
</html>
```
