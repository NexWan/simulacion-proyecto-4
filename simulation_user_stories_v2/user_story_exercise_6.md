# User Story – Exercise 6: Random Box Selection in Quality Control

## Story
As a **quality control analyst**, I want to simulate which boxes get inspected and whether they contain defects so that I can estimate the **expected number of defective boxes encountered**.

## Acceptance Criteria
- Probability of selecting a box for inspection: 30%.
- If selected, the number of inspected items must follow:
  - 1 item → 50%,
  - 2 items → 30%,
  - 3 items → 20%.
- Probability that a box contains at least one defective item: 2%.
- The simulation must run for **100 boxes**.
- For each box, the system must record:
  - selection decision,
  - number of items inspected,
  - defect presence,
  - whether a defect was detected.
- The system must generate a **CSV file** in the folder `output/problema6/` that:
  - Contains one row per box.
  - Includes all variables used (selection, count of inspected items, defect flags).
- The system must generate an **Excel file** in `output/problema6/` that:
  - Contains the same data table as the CSV.
  - Includes at least one embedded chart, for example:
    - distribution of inspected vs. non-inspected boxes,
    - distribution of defective vs. non-defective boxes.
- The output must include the empirical defect rate and average defective boxes encountered.

## Definition of Done
- Simulation faithfully implements the sampling and defect probabilities.
- All decisions and outcomes are traceable via the CSV/Excel.
- The folder `output/problema6/` exists and contains:
  - CSV with all simulation variables.
  - Excel workbook with data and embedded charts.
