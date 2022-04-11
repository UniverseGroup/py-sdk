name: Test

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [ 3.6, 3.7, 3.8, 3.9 ]

  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install dependencies
        run: |
          python -m pip install -U pip
          pip install -r requirements.txt
          pip install pytest pytest-cov
      - name: Test with pytest(cov)
        run: |
          pytest --cov=universelist --cov-report=xml
      - name: Codecov
        uses: codecov/codecov-action@v1
