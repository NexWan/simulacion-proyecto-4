# User Story – Exercise 4: Quality Control Inspection Simulation

## Story
As a **quality inspector**, I want to simulate the random inspection of boxes and the detection of defects so that I can estimate the **average number of defective boxes detected**.

## Acceptance Criteria
- Probability of selecting a box for inspection: 30%.
- If a box is inspected:
  - Inspect 1 product → 50% chance.
  - Inspect 2 products → 30% chance.
  - Inspect 3 products → 20% chance.
- Probability that a box contains one or more defective products: 2%.
- The simulation must run for **100 boxes**.
- For each box, the system must record at least:
  - Whether it was inspected or not.
  - How many products were inspected (if any).
  - Whether the box is defective and whether a defect was detected.
- The system must generate a **CSV file** in the folder `output/problema4/` that:
  - Contains one row per box.
  - Includes all variables used (inspection decision, number of items, defect flags).
- The system must generate an **Excel file** in `output/problema4/` that:
  - Contains the same data table as the CSV.
  - Includes at least one embedded chart, for example:
    - bar chart of inspected vs. not inspected boxes,
    - bar chart or pie chart of defective vs. non-defective boxes detected.
- The output must include the average number of defective boxes detected and any other requested statistics.

## Definition of Done
- Simulation reflects all probabilistic sampling rules as described.
- Detection logic is correctly applied and traceable via the CSV/Excel.
- The folder `output/problema4/` exists and contains:
  - CSV with all simulation variables.
  - Excel workbook with data and embedded charts.
