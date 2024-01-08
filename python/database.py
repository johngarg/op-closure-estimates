#!/usr/bin/env python3

from limits import get_loop_level_records, get_tree_level_records
import pandas as pd

tree_level_records = get_tree_level_records()
get_tree_level_dataframe = lambda: pd.DataFrame.from_records(tree_level_records)

loop_level_records = get_loop_level_records()
get_loop_level_dataframe = lambda: pd.DataFrame.from_records(loop_level_records)
