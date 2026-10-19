# Installation et lancement

## Prérequis

| Outil | Version | Installation |
|---|---|---|
| Git | 2.40+ | Inclus sur macOS avec les Xcode Command Line Tools |
| uv | 0.13+ | `curl -LsSf https://astral.sh/uv/install.sh \| sh`, puis `uv self update` pour mettre à jour |

Python n'a pas besoin d'être installé à part : uv télécharge la version indiquée dans
`.python-version` si elle manque.

## Installer le projet

```bash
git clone https://github.com/wanakin1/nami-data-platform.git
cd nami-data-platform
uv sync
```

`uv sync` crée l'environnement virtuel `.venv/` et y installe exactement les versions figées
dans `uv.lock`, y compris le paquet `nami` lui-même en mode éditable : tes modifications dans
`src/` sont prises en compte sans réinstaller.

## Commandes du quotidien

| Commande | Effet |
|---|---|
| `uv run pytest` | Lance tous les tests |
| `uv run pytest tests/test_smoke.py -v` | Lance un seul fichier, en mode détaillé |
| `uv run ruff check .` | Lint : erreurs et mauvaises pratiques |
| `uv run ruff check . --fix` | Corrige automatiquement ce qui peut l'être |
| `uv run ruff format .` | Formate le code |
| `uv add <paquet>` | Ajoute une dépendance (met à jour `pyproject.toml` et `uv.lock`) |
| `uv add --dev <paquet>` | Ajoute une dépendance de développement |
| `uv run python` | Ouvre un interpréteur dans l'environnement du projet |

`uv run` exécute une commande dans `.venv/` sans avoir à l'activer.

## Avant de pousser

Ce sont les mêmes vérifications que la CI :

```bash
uv run ruff check . && uv run ruff format --check . && uv run pytest
```

## Cycle de travail

1. Choisir une issue et créer la branche : `git switch -c feat/<n°>-<slug>`
2. Coder et tester, en committant par petites étapes (`feat:`, `fix:`, `test:`, `docs:`, `chore:`)
3. Pousser : `git push -u origin feat/<n°>-<slug>`
4. Ouvrir la PR : `gh pr create --fill`, puis vérifier que la CI est verte
5. Merger, puis revenir sur `main` : `git switch main && git pull`
