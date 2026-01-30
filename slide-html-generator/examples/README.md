# Example: AI对未来工作的影响

This example demonstrates the complete workflow from a topic to HTML slides.

## Topic Input

```
创建一个关于人工智能对未来工作影响的演示文稿，涵盖自动化、工作岗位流失、
新的职位创造以及技能再培训的需求等主题。演示文稿应当具有吸引力和信息量，
拥有清晰的视觉效果和简洁的文本内容。
```

## Generated Files

```
ai-future-work/
├── source.md           # Step 1: Collected information
├── analysis.md         # Step 2: Content analysis
├── outline.md          # Step 4: Detailed outline with STYLE_INSTRUCTIONS
├── prompts/            # Step 5: Individual slide scripts
│   ├── 01-slide-cover.md
│   ├── 02-slide-contents.md
│   ├── 03-slide-automation-rise.md
│   ├── 04-slide-automation-impact.md
│   ├── 05-slide-job-loss-data.md
│   ├── 06-slide-affected-industries.md
│   ├── 07-slide-new-jobs.md
│   ├── 08-slide-growth-trends.md
│   ├── 09-slide-key-skills.md
│   ├── 10-slide-reskilling-path.md
│   ├── 11-slide-human-ai-collaboration.md
│   ├── 12-slide-key-insights.md
│   ├── 13-slide-summary.md
│   └── 14-slide-back-cover.md
├── slides/             # Step 6: Generated HTML slides
│   ├── 01-slide-cover.html
│   └── ... (14 files)
└── index.html          # Preview page
```

## Workflow Steps

### Step 1: Information Gathering

Agent executes web searches:
- `web_search "人工智能 未来工作 自动化 影响"`
- `web_search "AI job displacement statistics 2024"`
- `web_search "reskilling workforce AI era"`
- `web_search "新兴AI职业 2024"`

Results saved to `source.md`.

### Step 2: Content Analysis

Agent analyzes collected content and creates `analysis.md`:
- Identifies core themes
- Recommends style (blueprint - technical analysis content)
- Recommends slide count (14)
- Maps visual opportunities

### Step 3: User Confirmation

Agent confirms with user:
- Style: blueprint ✓
- Slides: 14 ✓
- Audience: experts/professionals ✓

### Step 4: Generate Outline

Agent creates `outline.md` with:
- Complete STYLE_INSTRUCTIONS block
- 14 slide definitions with types, layouts, content

### Step 5: Generate Slide Scripts

Agent creates individual prompt files:
- Each slide has its own .md file
- Contains type, layout, title, subtitle, key points, visual description

### Step 6: Generate HTML Slides

Agent generates HTML for each slide:
- Reads STYLE_INSTRUCTIONS for consistent styling
- Applies blueprint color palette and grid texture
- Creates 1280x720 responsive slides

### Step 7: Output Summary

```
✅ Slide Deck Complete!

Topic: AI对未来工作的影响
Style: blueprint
Location: slide-deck/ai-future-work/
Slides: 14 total

Files:
├── 01-slide-cover.html - Cover
├── 02-slide-contents.html - Table of Contents
├── 03-slide-automation-rise.html - 自动化的崛起
├── 04-slide-automation-impact.html - 自动化的影响范围
├── 05-slide-job-loss-data.html - 工作岗位流失预测
├── 06-slide-affected-industries.html - 受影响最严重的行业
├── 07-slide-new-jobs.html - AI时代的新兴职业
├── 08-slide-growth-trends.html - 新职位的增长趋势
├── 09-slide-key-skills.html - 未来工作的关键技能
├── 10-slide-reskilling-path.html - 技能再培训路径
├── 11-slide-human-ai-collaboration.html - 人机协作的未来
├── 12-slide-key-insights.html - 关键洞察与行动建议
├── 13-slide-summary.html - 总结
└── 14-slide-back-cover.html - Back Cover
```
