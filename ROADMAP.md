# Verification Roadmap: Legislation (Focus)

This document details the strategy to ensure that the OpenFisca Paraguay model faithfully reflects the legislation.
We focus here exclusively on validation against the law (Parameters and Variables).

---

## 🎯 Objective
**Achieve a "Legally Accurate" Model.**
Every parameter must be sourced. Every formula must correspond to the law.

---

## 📋 Action Plan

### Phase 1: Static Audit
*Action: Review and validate existing code.*

1. **Parameters (YAML)**
   - Verify values and history in `parameters/`.
   - **Mandatory**: Every YAML file must include a `reference` metadata structured by date for each value change.
     ```yaml
     metadata:
       reference:
         2024-01-01: # Effective date
           title: "Decree N°..." # Title of the law/decree
           href: "https://..." # Link to Decree/Law
     ```
   - *Priority Targets*: Minimum Wages, IPS Contributions, IRP/IRE Brackets.

2. **Variables (Python)**
   - Verify variable logic in `variables/`.
   - **Legislative History**: If a formula changed over time, cite the law corresponding to the modification in the docstring or code.
   - Ensure exemptions and deductions are correctly coded.

### Phase 2: Dynamic Validation (Tests)
*Action: Prove the calculations are correct.*

1. **Test Cases (Profiles)**
   - Define 3-5 "specific" profiles (e.g., Minimum Wage Worker, Tekoporã Family, Independent).
   - Simulate these profiles manually (Excel/Paper) to obtain reference results.

2. **Integration Tests**
   - Implement these profiles in `tests/test_case_types.py`.
   - Verify that `OpenFisca Result == Excel Result` (exact match / < 1 PYG).

---

## ⚙️ Mode of Action & Best Practices

To collaborate effectively between Business (Ernesto) and Tech (Benjello), here is the recommended workflow:

### 1. The Golden Rule: "One Task = One Branch"
Never modify the entire codebase at once. Work subject by subject.
*Example: Do not fix Minimum Wage and Income Tax in the same Pull Request.*

### 2. Correction Workflow (The Cycle)
1. **Detection**: Spot an error in a parameter or formula.
2. **Branch**: Create an explicit branch.
   - *Good*: `fix/minimum-wage-2023`, `chore/ips-source`
   - *Bad*: `ernesto-test`, `correction`
3. **Correction & Proof**:
   - Modify the value.
   - **Add the source**:
     - *Parameters (YAML)*: `metadata` / `reference` / `date` structure.
     - *Variables (Python)*: Comment or Docstring citing the article of law.
4. **Pull Request (PR)**: Open the PR on GitHub.
   - *Title*: Explicit (e.g., "Fix minimum wage history 2020-2024").
   - *Description*: "Based on Decree N°1234 (link)".
5. **Review**:
   - **Benjello** checks: YAML/Python syntax, Indentation, Breaking tests.
   - **Ernesto** checks: Compliance with the law.
6. **Merge**: Once validated by the other party, merge.

### 3. Handling Doubts
If a law is ambiguous or hard to code:
- Do not block.
- Create a GitHub **Issue** with label `question` or `legislation-check`.
- Copy the ambiguous text of the law there for discussion.
