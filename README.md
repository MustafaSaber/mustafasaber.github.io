# Mustafa Saber — personal website

A minimal Hugo site with a horizontal Arabic identity, IBM Plex Mono English typography, and a warm ivory and forest green palette. No theme, JavaScript framework, npm, or Ruby dependencies.

## Run locally

Install Hugo **0.170.0 or newer** (`brew install hugo` on macOS), then:

```sh
hugo server
```

Open the URL printed by Hugo, normally http://localhost:1313.

```sh
hugo --minify --panicOnWarning
```

The production site is generated in `public/` (ignored by Git).

## Content

- `content/_index.md`: About homepage, including the professional introduction and personal bio.
- `content/thoughts/`: Markdown articles; `externalURL` links a listing directly to an external publication.
- `layouts/home.html`: minimal About homepage layout.
- `hugo.toml`: title, description, domain, and social links.
- `assets/css/main.css`: typography, responsive layout, and light/dark color tokens.
- `layouts/_partials/mark.html` and `static/images/mark.svg`: vector monogram adapted from the brand board.

Create a post with `hugo new content thoughts/my-post.md`. Set `draft: false` to publish it. The original Magento post keeps its old `/2020/06/16/magento-dockercompose/` URL through an alias. The old unpublished welcome post remains a draft.

## Deploy to GitHub Pages

The workflow validates pull requests and deploys pushes to `master` or `main`. In repository **Settings → Pages**, select **GitHub Actions** as the build source. The domain `msaber.dev` is preserved in `static/CNAME`; retain the existing DNS settings. No deployment happens until the changes are pushed.

## Fonts and branding

IBM Plex Mono (regular, medium, bold, and italic styles) for all English text and code, and the Noto Kufi Arabic fallback are self-hosted in `static/fonts/`, with their licenses. The monogram is a clean vector adaptation of the selected Kufic direction. The Arabic name uses an outlined SVG rendered from the official Thmanyah Serif Display Medium font. Font binaries for Thmanyah are not bundled with the site. Update both monogram SVG files together when final artwork changes.

## Arabic wordmark

The header uses a horizontal bilingual lockup. `layouts/_partials/wordmark.html` uses an outlined Arabic wordmark from `assets/branding/arabic-wordmark.svg` when available. The checked-in wordmark uses the official Thmanyah Serif Display Medium font. If the SVG is removed, the partial falls back to accessible Arabic text in Noto Kufi Arabic.

For Thmanyah, obtain the official font package from https://font.thmanyah.com/ and render the name to an SVG with outlined glyphs. Do not commit or serve Thmanyah font binaries: the official terms prohibit making font files available for download. See https://font.thmanyah.com/licenses.

Regenerate the Arabic wordmark on macOS from your own official font download:

```sh
python3 scripts/create-arabic-wordmark.py \
  "$HOME/Downloads/Thmanyah-Font-Family/thmanyah typeface/thmanyahserifdisplay/otf/thmanyahserifdisplay-Medium.otf" \
  assets/branding/arabic-wordmark.svg
```

The exporter uses HarfBuzz (`brew install harfbuzz`) to shape the Arabic name and exports only vector paths for the wordmark. It does not copy or embed the font software.

## Minimal layout

The homepage is the About page: a short professional introduction followed by a personal bio. Articles live on the separate Thoughts page. `/about/` redirects to `/`, and the header logo links home. Navigation includes Thoughts, the public Resume, and the theme switch. The resume URL is configured in `hugo.toml`. The footer provides GitHub, LinkedIn, and RSS links. `/writing/` and the existing published article URLs redirect to `/thoughts/`; the original 2020 article URL is also preserved.
