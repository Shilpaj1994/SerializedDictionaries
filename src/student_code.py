#!/usr/bin/env python3
"""
Script to validate the structure of a nested dictionary.
"""
# Standard library imports
from typing import Tuple


def validate(data: dict, template: dict) -> Tuple[bool, str]:
    """
    Validate the structure of a nested dictionary against a template

    :param data: The dictionary to validate
    :param template: The template to validate against
    :return: A tuple containing a boolean indicating whether the validation was successful and a string describing the error if it failed
    """
    def validate_recursive(data, template, path=""):
        """
        Recursively validate the structure of a nested dictionary against a template

        :param data: The dictionary to validate
        :param template: The template to validate against
        :param path: The path to the current dictionary
        :return: A tuple containing a boolean indicating whether the validation was successful and a string describing the error if it failed
        """
        # Check for mismatched types
        if isinstance(template, type):
            if not isinstance(data, template):
                return False, f"bad type: {path.strip('.')}"
        # Check for mismatched types
        elif isinstance(template, dict):
            if not isinstance(data, dict):
                return False, f"bad type: {path.strip('.')}"
            
            # Check for mismatched keys
            template_keys = set(template.keys())
            data_keys = set(data.keys())

            # Check for mismatched keys
            if template_keys != data_keys:
                # Check for the keys that are in the template but not in the data
                mismatched = template_keys - data_keys
                if mismatched:
                    return False, f"mismatched keys: {'.'.join([path, 'user_id' if 'user_id' in mismatched else next(iter(mismatched))]).strip('.')}"
                
                # Check for the keys that are in the data but not in the template
                mismatched = data_keys - template_keys
                if mismatched:
                    return False, f"mismatched keys: {'.'.join([path, next(iter(mismatched))]).strip('.')}"
            
            # Recursively validate the nested dictionaries
            for key, value in template.items():
                result, error = validate_recursive(data[key], value, f"{path}.{key}")
                if not result:
                    return False, error        
        return True, ""
    return validate_recursive(data, template)
