"""Test d'interopérabilité Polars -> DuckDB.

Vérifie que DuckDB sait interroger directement un DataFrame Polars
(« replacement scan »), sans export intermédiaire.
"""

import duckdb
import polars as pl


def test_duckdb_queries_polars_dataframe() -> None:
    """Un DataFrame Polars est requêtable en SQL par DuckDB."""
    # DuckDB résout le DataFrame par son nom de variable au moment de la requête
    # (« replacement scan »), donc `df` est utilisé sans l'être en Python.
    df = pl.DataFrame(  # noqa: F841
        {
            "station": ["Brest", "Marseille", "Brest"],
            "temperature": [12.5, 21.0, 9.5],
        }
    )

    rows = duckdb.sql(
        """
        SELECT station, COUNT(*) AS n, ROUND(AVG(temperature), 2) AS moyenne
        FROM df
        GROUP BY station
        ORDER BY station
        """
    ).fetchall()

    assert rows == [("Brest", 2, 11.0), ("Marseille", 1, 21.0)]
