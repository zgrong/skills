#!/usr/bin/env python3
"""
Slide HTML Generator Script

This script generates HTML slides from outline and prompt files.
It can be used by the agent via run_code to batch generate slides.

Usage:
    python generate-html.py <slide-deck-dir>
    python generate-html.py slide-deck/ai-future-work

The script will:
1. Read outline.md for STYLE_INSTRUCTIONS
2. Read each prompt file in prompts/
3. Generate corresponding HTML in slides/
4. Create index.html for preview
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional

# Default style variables (blueprint)
DEFAULT_STYLE = {
    'color_bg': '#FAF8F5',
    'color_grid': '#E5E5E5',
    'color_text_primary': '#334155',
    'color_accent_primary': '#2563EB',
    'color_accent_secondary': '#1E3A5F',
    'color_accent_tertiary': '#BFDBFE',
}


def parse_style_instructions(outline_content: str) -> Dict[str, str]:
    """Extract style variables from STYLE_INSTRUCTIONS block."""
    style = DEFAULT_STYLE.copy()
    
    # Extract color palette
    color_patterns = [
        (r'Background:.*?#([A-Fa-f0-9]{6})', 'color_bg'),
        (r'Grid:.*?#([A-Fa-f0-9]{6})', 'color_grid'),
        (r'Primary Text:.*?#([A-Fa-f0-9]{6})', 'color_text_primary'),
        (r'Primary Accent:.*?#([A-Fa-f0-9]{6})', 'color_accent_primary'),
        (r'Secondary Accent:.*?#([A-Fa-f0-9]{6})', 'color_accent_secondary'),
        (r'Tertiary:.*?#([A-Fa-f0-9]{6})', 'color_accent_tertiary'),
    ]
    
    for pattern, key in color_patterns:
        match = re.search(pattern, outline_content, re.IGNORECASE)
        if match:
            style[key] = f'#{match.group(1)}'
    
    # Extract style name
    style_match = re.search(r'\*\*Visual Style:\*\*\s*(\w+)', outline_content)
    if style_match:
        style['style_name'] = style_match.group(1).lower()
    else:
        style['style_name'] = 'blueprint'
    
    return style


def parse_prompt_file(prompt_content: str) -> Dict[str, str]:
    """Parse a prompt file to extract slide content."""
    slide = {
        'type': 'Content',
        'layout': 'centered-content',
        'title': '',
        'subtitle': '',
        'content': '',
    }
    
    # Extract type
    type_match = re.search(r'\*\*Type:\*\*\s*(.+)', prompt_content)
    if type_match:
        slide['type'] = type_match.group(1).strip()
    
    # Extract layout
    layout_match = re.search(r'\*\*Layout:\*\*\s*(.+)', prompt_content)
    if layout_match:
        slide['layout'] = layout_match.group(1).strip()
    
    # Extract title
    title_match = re.search(r'\*\*Title:\*\*\s*(.+)', prompt_content)
    if title_match:
        slide['title'] = title_match.group(1).strip()
    
    # Extract subtitle
    subtitle_match = re.search(r'\*\*Subtitle:\*\*\s*(.+)', prompt_content)
    if subtitle_match:
        slide['subtitle'] = subtitle_match.group(1).strip()
    
    # Extract key points
    points = re.findall(r'^-\s+(.+)$', prompt_content, re.MULTILINE)
    if points:
        slide['points'] = points[:6]  # Limit to 6 points
    
    return slide


def generate_base_css(style: Dict[str, str]) -> str:
    """Generate base CSS from style variables."""
    return f'''
:root {{
  --slide-width: 1280px;
  --slide-height: 720px;
  --color-bg: {style['color_bg']};
  --color-grid: {style['color_grid']};
  --color-text-primary: {style['color_text_primary']};
  --color-accent-primary: {style['color_accent_primary']};
  --color-accent-secondary: {style['color_accent_secondary']};
  --color-accent-tertiary: {style['color_accent_tertiary']};
  --font-headline: system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
  --font-body: Georgia, 'Times New Roman', serif;
  --spacing-sm: 16px;
  --spacing-md: 24px;
  --spacing-lg: 48px;
  --spacing-xl: 64px;
}}

* {{ margin: 0; padding: 0; box-sizing: border-box; }}

body {{
  font-family: var(--font-body);
  font-size: 18px;
  line-height: 1.6;
  color: var(--color-text-primary);
  background: #e0e0e0;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}}

.slide {{
  width: var(--slide-width);
  height: var(--slide-height);
  background: var(--color-bg);
  position: relative;
  overflow: hidden;
  padding: var(--spacing-xl);
}}

.slide--grid::before {{
  content: '';
  position: absolute;
  inset: 0;
  background-image: 
    linear-gradient(var(--color-grid) 1px, transparent 1px),
    linear-gradient(90deg, var(--color-grid) 1px, transparent 1px);
  background-size: 40px 40px;
  opacity: 0.5;
  pointer-events: none;
}}

.title {{
  font-family: var(--font-headline);
  font-size: 48px;
  font-weight: 700;
  color: var(--color-text-primary);
  letter-spacing: -0.02em;
  margin-bottom: var(--spacing-md);
}}

.title--xl {{ font-size: 64px; }}
.title--lg {{ font-size: 48px; }}
.title--md {{ font-size: 36px; }}

.subtitle {{
  font-size: 24px;
  color: var(--color-accent-secondary);
}}

.key-points {{
  list-style: none;
  padding: 0;
  margin-top: var(--spacing-lg);
}}

.key-points li {{
  position: relative;
  padding-left: 32px;
  margin-bottom: var(--spacing-sm);
  font-size: 20px;
}}

.key-points li::before {{
  content: '';
  position: absolute;
  left: 0;
  top: 10px;
  width: 8px;
  height: 8px;
  background: var(--color-accent-primary);
  border-radius: 50%;
}}

.layout-title-hero {{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  height: 100%;
  position: relative;
  z-index: 1;
}}

.layout-centered {{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  height: 100%;
  position: relative;
  z-index: 1;
}}

.layout-content {{
  display: flex;
  flex-direction: column;
  height: 100%;
  position: relative;
  z-index: 1;
}}

.layout-content .header {{
  margin-bottom: var(--spacing-lg);
}}

.layout-content .body {{
  flex: 1;
}}
'''


def generate_slide_html(slide: Dict, style: Dict[str, str], lang: str = 'zh') -> str:
    """Generate complete HTML for a single slide."""
    css = generate_base_css(style)
    
    # Determine layout class
    layout_class = 'layout-content'
    slide_class = 'slide'
    
    if style.get('style_name') == 'blueprint':
        slide_class += ' slide--grid'
    
    if slide['type'] == 'Cover':
        layout_class = 'layout-title-hero'
    elif slide['type'] == 'Back Cover':
        layout_class = 'layout-centered'
    
    # Build content
    content_html = ''
    
    if slide['type'] in ['Cover', 'Back Cover']:
        content_html = f'''
    <div class="{layout_class}">
      <h1 class="title title--xl">{slide['title']}</h1>
      <p class="subtitle">{slide.get('subtitle', '')}</p>
    </div>
'''
    else:
        points_html = ''
        if slide.get('points'):
            points_items = '\n'.join([f'        <li>{p}</li>' for p in slide['points']])
            points_html = f'''
      <ul class="key-points">
{points_items}
      </ul>
'''
        
        content_html = f'''
    <div class="{layout_class}">
      <div class="header">
        <h1 class="title title--lg">{slide['title']}</h1>
        <p class="subtitle">{slide.get('subtitle', '')}</p>
      </div>
      <div class="body">
{points_html}
      </div>
    </div>
'''
    
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=1280">
  <title>{slide['title']}</title>
  <style>
{css}
  </style>
</head>
<body>
  <div class="{slide_class}">
{content_html}
  </div>
</body>
</html>
'''


def generate_index_html(slides: List[Dict], deck_dir: Path, style: Dict[str, str]) -> str:
    """Generate index.html for slide preview."""
    slides_list = '\n'.join([
        f'    <li><a href="slides/{s["filename"]}">{s["title"]}</a></li>'
        for s in slides
    ])
    
    return f'''<!DOCTYPE html>
<html lang="zh">
<head>
  <meta charset="UTF-8">
  <title>Slide Deck Preview</title>
  <style>
    body {{
      font-family: system-ui, sans-serif;
      max-width: 800px;
      margin: 40px auto;
      padding: 20px;
      background: #f5f5f5;
    }}
    h1 {{
      color: {style['color_text_primary']};
      border-bottom: 3px solid {style['color_accent_primary']};
      padding-bottom: 10px;
    }}
    ul {{
      list-style: none;
      padding: 0;
    }}
    li {{
      margin: 10px 0;
    }}
    a {{
      color: {style['color_accent_primary']};
      text-decoration: none;
      font-size: 18px;
    }}
    a:hover {{
      text-decoration: underline;
    }}
    .meta {{
      color: #666;
      font-size: 14px;
      margin-bottom: 20px;
    }}
  </style>
</head>
<body>
  <h1>Slide Deck Preview</h1>
  <div class="meta">
    Style: {style.get('style_name', 'blueprint')} | 
    Slides: {len(slides)}
  </div>
  <ul>
{slides_list}
  </ul>
</body>
</html>
'''


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate-html.py <slide-deck-dir>")
        print("Example: python generate-html.py slide-deck/ai-future-work")
        sys.exit(1)
    
    deck_dir = Path(sys.argv[1])
    
    if not deck_dir.exists():
        print(f"Error: Directory not found: {deck_dir}")
        sys.exit(1)
    
    outline_path = deck_dir / 'outline.md'
    prompts_dir = deck_dir / 'prompts'
    slides_dir = deck_dir / 'slides'
    
    # Check required files
    if not outline_path.exists():
        print(f"Error: outline.md not found in {deck_dir}")
        sys.exit(1)
    
    if not prompts_dir.exists():
        print(f"Error: prompts/ directory not found in {deck_dir}")
        sys.exit(1)
    
    # Create slides directory
    slides_dir.mkdir(exist_ok=True)
    
    # Parse outline for style
    print(f"Reading outline from {outline_path}...")
    outline_content = outline_path.read_text(encoding='utf-8')
    style = parse_style_instructions(outline_content)
    print(f"  Style: {style.get('style_name', 'blueprint')}")
    
    # Process each prompt file
    prompt_files = sorted(prompts_dir.glob('*.md'))
    slides_info = []
    
    print(f"\nGenerating {len(prompt_files)} slides...")
    
    for prompt_file in prompt_files:
        print(f"  Processing {prompt_file.name}...")
        
        prompt_content = prompt_file.read_text(encoding='utf-8')
        slide = parse_prompt_file(prompt_content)
        
        # Generate HTML filename
        html_filename = prompt_file.stem + '.html'
        html_path = slides_dir / html_filename
        
        # Generate and save HTML
        html_content = generate_slide_html(slide, style)
        html_path.write_text(html_content, encoding='utf-8')
        
        slides_info.append({
            'filename': html_filename,
            'title': slide['title'] or prompt_file.stem,
        })
    
    # Generate index.html
    print("\nGenerating index.html...")
    index_html = generate_index_html(slides_info, deck_dir, style)
    (deck_dir / 'index.html').write_text(index_html, encoding='utf-8')
    
    print(f"\n✅ Generation complete!")
    print(f"   Output: {slides_dir}")
    print(f"   Preview: {deck_dir / 'index.html'}")


if __name__ == '__main__':
    main()
