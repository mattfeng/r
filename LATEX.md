# LaTeX Cheatsheet

## Packages

```bash
sudo tlmgr install mhchem
sudo tlmgr install siunitx
```

---

## General

### Text on top of symbols

```latex
\stackrel{over}{symbol}
```

## Chemistry

### Abbreviations/Commands

```tex
\newcommand{\pH}{\text{pH}}
\newcommand{\pK}[1]{\text{pK}_{#1}}
```

### siunitx

```tex
\unit{}  % standalone unit
\num{}   % number
\SI{}{}  % physical unit
\DeclareSIUnit{\micron}{\micro\m}
```

