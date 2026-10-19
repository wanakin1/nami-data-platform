# Roadmap

Chaque jalon correspond à une [milestone GitHub](https://github.com/wanakin1/nami-data-platform/milestones).
Le détail vit dans les issues.

| Jalon | Objectif | Ce qu'on apprend |
|---|---|---|
| **M0 Fondations** | Squelette, CI verte, backlog | uv, Git, cycle issue → branche → PR |
| **M1 Bronze** | Ingérer les données brutes d'Open-Meteo en Parquet partitionné, de façon idempotente | HTTP, `pathlib`, Parquet, tests sans réseau |
| **M2 Silver** | Nettoyer, typer, dédupliquer et valider avec Polars | Polars, schémas, qualité de données |
| **M3 Gold** | Tables analytiques en SQL DuckDB | DuckDB, modélisation analytique |
| **M4 Pipeline** | CLI `nami run`, chargement incrémental, logs, contrôles qualité bloquants | Conception de pipeline, gestion d'erreurs |
| **M5 Vitrine** | Exécution planifiée, résultats présentés dans le README | Industrialisation, valorisation du projet |

## Hors périmètre pour l'instant

Orchestrateur (Dagster, Airflow), dbt, cloud, dashboard. On les envisagera par un ADR quand un
besoin concret apparaîtra.
