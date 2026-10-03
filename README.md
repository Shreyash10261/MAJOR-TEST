# Mock Repository for Testing HealingCI

This repository is designed to intentionally trigger a failed pipeline run so that you can see your RCA Engine and ML Preflight risk assessor in action on the `HealingCI` dashboard.

### How to use this:
1. Go to your GitHub account and create a new, empty private repository (e.g., `mock-repo-test`).
2. Make sure you install the `GoHeal-app-test` GitHub App on this new repository!
3. Push this folder to that new repository by running these commands in your terminal:

```bash
cd /Users/shreyashshivhare/Desktop/major/codebase/mock-repo-test
git init
git add .
git commit -m "Initial commit with intentionally failing tests"
git branch -M main
git remote add origin https://github.com/Shreyash10261/<YOUR-NEW-REPO-NAME>.git
git push -u origin main
```

### What will happen:
- As soon as you push, GitHub Actions will detect the `.github/workflows/ci.yml` file and start a pipeline run.
- The pipeline will intentionally **FAIL** because of a ZeroDivisionError in `test_app.py`.
- **HealingCI Backend** will receive the `workflow_run` webhooks via Smee.
- **ML Preflight** will assign it a risk score.
- **RCA Engine** will detect the failure, try to fix it, and generate an Incident Report which will immediately show up on your frontend dashboard at `http://localhost:5173/dashboard`!
