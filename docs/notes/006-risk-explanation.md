# Risk Explanation

Domain: fintech compliance

This note records an implementation detail for AML Case Queue. The current operating
threshold is `0.73` and review should happen within `48` hours
for records above that level.

## Checks

- confirm input fields are present
- verify score ordering is stable
- compare high exposure records against the review queue
