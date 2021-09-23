# Magalix Action Testing Repository

This repository contains end to end tests to test magalix action.

The tests run every day at 12:00 AM UTC on both `dev` and `main`
- `dev` branch uses `magalix-action@dev` and kubeguard from `dev` environment  
- `main` branch uses `magalix-action@main` and kubeguard from `prod` environment

## Test Scenario
- Asserts that the number of scanned entities, entities with violations and fixed entities by auto remediation are correct.
- Checks that the auto-remediation pull request is created.

## Testing Accounts

- `DEV` Environment:

    username: `test+e2e@magalix.com`

    password: `magalix@testing`

- `PROD` Environment:

    username: `test+e2e@magalix.com`
    
    password: `magalix@testing`
