"""Test de fumée : vérifie que le paquet s'installe et s'importe.

Il existe seulement pour que la CI ait quelque chose à exécuter dès le premier commit.
Les vrais tests arriveront avec les fonctionnalités.
"""

import nami


def test_package_exposes_version() -> None:
    assert nami.__version__
