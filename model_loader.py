# model_loader.py
import json
import importlib


import importlib

def get_class_by_name(full_class_string):
    """
    Return a class object from a string like 'module.submodule.ClassName'.
    """
    parts = full_class_string.split('.')
    module_path = '.'.join(parts[:-1])  # Extract the module path
    class_name = parts[-1]             # Extract the class name

    # Import the module dynamically
    try:
        module = importlib.import_module(module_path)
    except ModuleNotFoundError as e:
        raise ImportError(f"Module '{module_path}' could not be found: {e}")

    # Get the class from the module
    try:
        clazz = getattr(module, class_name)
    except AttributeError as e:
        raise AttributeError(f"Class '{class_name}' not found in module '{module_path}': {e}")

    return clazz

def load_model_classes(config_path):
    """
    Load model classes from a JSON configuration file.

    Args:
        config_path (str): Path to the configuration file.

    Returns:
        dict: A dictionary mapping model names to class objects.
    """
    with open(config_path, 'r') as f:
        config = json.load(f)
    model_classes = {}
    for model_info in config['models']:
        model_name = model_info['name']
        class_full_name = model_info['class']
        try:
            clazz = get_class_by_name(class_full_name)
            model_classes[model_name] = clazz
        except (ImportError, AttributeError) as e:
            print(f"Error loading class '{class_full_name}' for model '{model_name}': {e}")
    return model_classes
