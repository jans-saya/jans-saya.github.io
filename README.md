# Zhansaya AI Portfolio

A multi-page static portfolio for GitHub Pages.

## Publish

1. Download and unzip the folder.
2. Copy **everything inside** the folder into the root of your `jans-saya.github.io` repository.
3. Open a terminal inside that folder and run:

```bash
git add .
git commit -m "Update portfolio language"
git push
```

4. In GitHub, open **Settings → Pages** and select **Deploy from a branch → main → /(root)**.

## Pages

- `index.html` — home, selected projects, awards, certificates, and contact
- `ray.html` — Project RAY and the external-memory benchmark
- `sign-language.html` — sign-language translator case study
- `glove.html` — gesture-controlled smart glove case study
- `doit.html` — DOIT web-app case study
- `resume.html` — web résumé and PDF download

## Writing style

Personal introductions, decisions, and lessons use first person. Methodology, architecture, and numerical results remain neutral and technical.

## Contact information

The site publicly displays the email and phone number supplied by Zhansaya. Edit or remove them from the HTML files if needed.

## Editing

Most text is inside the HTML files. Shared appearance is in `assets/css/site.css`; behavior is in `assets/js/site.js`.

## No build step

This is plain HTML, CSS, and JavaScript. It works directly on GitHub Pages.
