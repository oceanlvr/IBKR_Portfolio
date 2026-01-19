import xml.etree.ElementTree as ET
import pandas as pd
from utils.func import to_datetime


def transform_node(attrib, mapping):
    """
    pure func：mapping XML attributes to target dict based on mapping rules
    """

    def apply_mapping(xml_key, mapping_target):
        value = attrib.get(xml_key)
        # A: array -> return multiple key-value pairs
        if isinstance(mapping_target, list):
            return {target_col: value for target_col in mapping_target}
        # B: dict -> apply transformation
        if isinstance(mapping_target, dict):
            target_name = mapping_target.get("name", xml_key)
            transform_func = mapping_target.get("transform", lambda x: x)
            return {target_name: transform_func(value)}
        # C: string -> direct rename
        return {mapping_target: value}

    return {
        k: v
        for xml_key, target in mapping.items()
        if xml_key in attrib
        for k, v in apply_mapping(xml_key, target).items()
    }


def parse_advanced_mapping_functional(file_path, node_tag, root_tag, field_mapping):
    # 1. load and mapping (XML -> Dicts -> DataFrame)
    tree = ET.parse(file_path)

    root = tree.findall(f".//{root_tag}")[0]
    if root is None:  # make sure root exists
        raise ValueError(f"Root tag '{root_tag}' not found in the XML file.")
    extracted_data = [
        transform_node(node.attrib, field_mapping)
        for node in root.findall(f".//{node_tag}")
    ]

    df = pd.DataFrame(extracted_data)

    # 2. Dynamically identify date columns from mapping
    # if the transform function is to_datetime, then that column needs to be date-ized
    date_cols = [
        target["name"] if isinstance(target, dict) else target
        for xml_key, target in field_mapping.items()
        if isinstance(target, dict) and target.get("transform") == to_datetime
    ]

    # 3. Pipeline-style processing
    return (
        # A. process numeric columns
        df.pipe(lambda d: d.apply(pd.to_numeric, errors="ignore"))
        .assign(
            **{
                # Dynamically process date columns
                col: pd.to_datetime(df[col], errors="coerce")
                for col in date_cols
                if col in df.columns
            }
        )
        .convert_dtypes()  # C. process String and NULL columns
    )
