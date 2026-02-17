# Python Training Repository

This repository contains Python training materials, including basics, intermediate concepts, and Jupyter notebooks.

## Prerequisites

- Python 3.12 or higher

## Setup

It is recommended to use a virtual environment to manage dependencies.

### 1. Create a Virtual Environment

Run the following command to create a virtual environment named `venv`:

```bash
python -m venv venv
```

### 2. Activate the Virtual Environment

- **Linux/macOS:**

    ```bash
    source venv/bin/activate
    ```

- **Windows:**

    ```bash
    .\venv\Scripts\activate
    ```

### 3. Install Dependencies

With the virtual environment activated, install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

### Running Jupyter Notebooks

To start the Jupyter Notebook server:

```bash
jupyter notebook
```

This will open the Jupyter interface in your web browser. You can then navigate to the `jupyter/` directory to explore the notebooks.

### Running Python Scripts

To run any of the Python scripts (e.g., in `basics/` or `intermediate/`), simply direct Python to the file:

```bash
python basics/simple_types.py
```
