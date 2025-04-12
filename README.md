# Loan ranger

Rapide module pour calculer différents paramètres
d'un emprunt immobilier.

## Dépendances

- `python>3.10`
- `numpy`
- `scipy`

(For more details see `pyproject.toml` file or the Dev stuff below)

## Utilisation

### Short version

Aller dans le répertoire ou le repo a été cloné.
Executer le module.

```shell
cd loan_ranger
python -m loan_ranger
```

Et c'est tout.

### Long version

Importer le module dans une une console python.
Appeler la fonction "full_simu".
Et voilà.

```python
import loan_ranger

loan_ranger.full_simu()
```

## Structure

All code lives in `loan_ranger` folder.

- `common_objects`: Rapide structure pour stocker input et résultat (plus propre que de balader des tuples à rallonge)
- `core_functions`: Sexy stuff, là ou sont les calculs "compliqué
- `shell_interface`: Fonctions pour faire l'interface user: prompting, printing, regrouper le tout, etc

## Development stuff

- Project managed with uv, run `uv sync` to install project and dependencies
- Use ruff as a formatter, included in dev dependencies (`uv sync --all-extras` to install dev dependencies)
- First version developped in a single file, docstrings and refactoring courtesy of Claude.ai
