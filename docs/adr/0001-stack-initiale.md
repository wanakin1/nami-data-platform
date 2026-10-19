# ADR 0001 : stack initiale

- **Date** : 2026-10-16
- **Statut** : acceptée

## Contexte

Le volume visé (quelques villes, plusieurs dizaines d'années de données quotidiennes) se
compte en millions de lignes au plus : il tient largement sur une seule machine. Le projet doit
rester simple à installer, rapide à tester en local et en CI, et sans infrastructure à
maintenir.

## Décision

| Besoin | Choix | Alternative écartée | Raison |
|---|---|---|---|
| Dépendances | **uv** | pip + venv, Poetry | Un seul outil, lockfile reproductible, très rapide |
| Transformations | **Polars** | pandas, Spark | API expressive et typée, moteur lazy, multi-cœur, sans JVM |
| SQL analytique | **DuckDB** | PostgreSQL, SQLite | Embarqué, en colonnes, lit le Parquet sans chargement préalable |
| Stockage | **Parquet** | CSV, JSON | Typé, compressé, en colonnes, lisible par tous les outils |
| Qualité du code | **Ruff** | flake8 + black + isort | Lint et format en un seul outil |
| Tests | **pytest** | unittest | Fixtures, syntaxe concise, standard de fait |
| CI | **GitHub Actions** | — | Intégrée au repo |

## Conséquences

- Pas de cluster ni de service à lancer : `uv sync` suffit.
- Si le volume ou les besoins changent (orchestration, transformations SQL versionnées,
  visualisation), on ajoutera un outil par un nouvel ADR, seulement quand le besoin sera réel.
