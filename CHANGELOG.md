# Changelog

## 0.2.0 [#PR_NUMBER](https://github.com/openfisca/openfisca-paraguay/pull/PR_NUMBER)

* **Enhancements**:
    * Added `parameters/units.yaml` with definitions for Guaraní currency, percentages, and years.
    * Updated monetary parameters (minimum wages, bonuses, thresholds) to use `unit: currency`.
    * Cleaned up variables by removing proxy formulas (e.g., estimated IVA, assumed IRP taxable base) to ensure strict adherence to legislation.
* **Documentation**:
    * Added `CONTRIBUTING.md` and `CONTRIBUTING_ES.md` (Spanish translation) to guide contributors.
* **Infrastructure**:
    * Fixed CI workflows to use correct package name and Python version (3.11).
    * Configured `ruff` and `isort` for code quality, matching `openfisca-nouvelle-caledonie` standards.

## 0.1.0

* Initial release of OpenFisca Paraguay.
* Implemented core structure mimicking `openfisca-france`.
* Parameters defined for:
    * Labor: Minimum Wage.
    * Taxes: IRP (Personal Income Tax) for Services and Capital, VAT (simplified).
    * Social Security: IPS contributions.
    * Benefits: Tekoporã, PAAM (Senior Citizens), Disability Pension, School Meals (Hambre Cero).
* Basic logic implemented for IRP, IPS, and listed benefits.
