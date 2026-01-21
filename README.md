# OpenFisca Paraguay

This repository contains the OpenFisca model for the Paraguayan tax and benefit system.

## Setup

This project uses `uv` for dependency management.

### Installation

```bash
uv pip install -e .
```

## Usage

### Running Tests

```bash
uv run openfisca-run-test tests/test_ips.yaml -c openfisca_paraguay
```

### Checking Parameters

You can inspect the parameters using the OpenFisca CLI (ensure it is installed/accessible):

```bash
uv run openfisca-paraguay show-parameters
```

## Structure

- `openfisca_paraguay/paramaters`: Tax and benefit system parameters (rates, thresholds, etc.), organized by domain.
- `openfisca_paraguay/variables`: Python variables defining the logic of the tax and benefit system.
- `tests`: YAML tests to verify the logic.

## Legislation

The model implements legislation based on:
- Law No. 6380/2019 (Tax Modernization)
- Decree Law No. 1860/1950 (Social Security)
- Various other laws and decrees defining social benefits (Tekoporã, PAAM, Hambre Cero).

## Roadmap

To verify and improve the model, please refer to our roadmap:
- [Roadmap (English)](ROADMAP.md)
- [Hoja de Ruta (Español)](ROADMAP_ES.md)
