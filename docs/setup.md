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

Deux branches permanentes :

- `dev` : branche d'intégration, où arrive chaque issue terminée ;
- `main` : branche par défaut, qui ne contient que des versions stables.

Pour chaque issue :

1. Partir de `dev` à jour : `git switch dev && git pull`
2. Créer la branche : `git switch -c feat/<n°>-<slug>`
3. Coder et tester, en committant par petites étapes (`feat:`, `fix:`, `test:`, `docs:`, `chore:`)
4. Pousser : `git push -u origin feat/<n°>-<slug>`
5. Ouvrir la PR vers `dev` : `gh pr create --base dev --fill`, puis vérifier que la CI est verte
6. Merger, puis revenir sur `dev` : `git switch dev && git pull`

À chaque version stable :

1. Ouvrir la PR : `gh pr create --base main --head dev --title "Version <x.y>"`
2. Lister dans sa description les issues livrées, une par ligne : `Closes #<n°>`
3. CI verte, puis merger avec un commit de merge (`gh pr merge --merge`), sans squash : sinon
   l'historique de `main` diverge de celui de `dev`.

GitHub ne ferme une issue via `Closes #<n°>` que lorsque la PR est mergée dans la branche par
défaut. Une PR vers `dev` ne ferme donc pas son issue : c'est la PR `dev` → `main` qui s'en
charge.
