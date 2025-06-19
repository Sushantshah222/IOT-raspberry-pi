
    ```
2.  **Create the virtual environment:**
    ```bash
    python3 -m venv venv
    ```
    This command creates a new directory named `venv` (you can choose a different name) inside your current directory, containing a copy of the Python interpreter and `pip`.

3.  **Activate the virtual environment:**
    ```bash
    source venv/bin/activate
    ```
    You will see `(venv)` at the beginning of your terminal prompt, indicating the virtual environment is active. All subsequent `pip` commands will install packages into this isolated environment.

#### Install Python Dependencies

Once your virtual environment is active, install all required Python libraries listed in `requirements.txt`:

```bash
pip install -r requirements.txt
