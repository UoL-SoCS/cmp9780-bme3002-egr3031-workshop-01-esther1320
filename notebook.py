import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import pickle
import chardet


def get_expected_values():
    with open('expected_values.pkl', 'rb') as file:
        expected_values = pickle.load(file)
    return expected_values


def get_file_encoding(notebook_path):
    with open(notebook_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result["encoding"]


def execute_notebook(notebook_path):
    encoding = get_file_encoding(notebook_path)
    with open(notebook_path, encoding=encoding) as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

    try:
        ep.preprocess(nb, {'metadata': {'path': './'}})
    except Exception as e:
        print(f"Error executing notebook: {e}")
        raise

    return nb


def extract_variable_value(cell, expected_values):
    code = ''.join(cell['source'])
    exec(code, globals())
    return {key: globals().get(key) for key in expected_values.keys() if key in code}


def get_computed_values(notebook_path, expected_values):
    notebook = execute_notebook(notebook_path)

    computed_values = {}

    for cell in notebook.cells:
        if cell.cell_type == 'code':
            variable_values = extract_variable_value(cell, expected_values)
            computed_values.update(variable_values)

    return computed_values


# expected_values and computed_values as global values
expected_values = get_expected_values()
computed_values = get_computed_values("notebook_template.ipynb", expected_values)


# =======================================
# Functions below here will be tested
# ========================================
def common_parameters():
    variables = ["Fs", "dt", "L", "t", "A", "w"]

    required_computed_values, required_expected_values = {}, {}

    if computed_values:
        # Grade based on the computed values
        for key in variables:
            required_computed_values[key] = {'value': computed_values.get(key)}
            required_expected_values[key] = {'value': expected_values[key]['value'], 'atol': expected_values[key]['atol']}

    return required_computed_values, required_expected_values


def signals():
    variables = ["S"]

    required_computed_values, required_expected_values = {}, {}

    if computed_values:
        # Grade based on the computed values
        for key in variables:
            required_computed_values[key] = {'value': computed_values.get(key)}
            required_expected_values[key] = {'value': expected_values[key]['value'], 'atol': expected_values[key]['atol']}

    return required_computed_values, required_expected_values


def signals_second():
    variables = ["signal", "fs", "fs_above", "fs_below", "signal_above", "signal_below"]

    required_computed_values, required_expected_values = {}, {}

    if computed_values:
        # Grade based on the computed values
        for key in variables:
            print(key)
            required_computed_values[key] = {'value': computed_values.get(key)}
            required_expected_values[key] = {'value': expected_values[key]['value'], 'atol': expected_values[key]['atol']}

    return required_computed_values, required_expected_values

# if __name__ == "__main__":
