#### Needs to be updated, currently not working ########

import unittest
import pandas as pd
import os
from swine_lca.resource_manager.models import load_livestock_data, print_livestock_data
import io
from contextlib import redirect_stdout


def capture_stdout(function, *args, **kwargs):
    f = io.StringIO()
    with redirect_stdout(f):
        function(*args, **kwargs)

    return f.getvalue()


def read_expected_output(filename, path):
    with open(os.path.join(path, filename), "r") as file:
        return file.read()


class DatasetLoadingTestCase(unittest.TestCase):
    def setUp(self):
        self.txt_path = "./data_swine"
        # Create the DataFrame with the provided data
        data = [
            ["ireland",2018,2018,"boars",900,225,0,"average","pasture","concentrate",2.75,
             0,24,0,0,"solid","broadcast",0,0,],
            ["ireland", 2018, 2018, "gilts_in_pig", 17200, 160, 0, "average", "pasture", "concentrate", 2.64,
             0, 24, 0, 0, "solid", "broadcast", 0, 0, ],
            ["ireland", 2018, 2018, "sows_in_pig", 73500, 200, 0, "average", "pasture", "concentrate", 2.64,
             0, 24, 0, 0, "solid", "broadcast", 0, 0, ],
            ["ireland", 2018, 2018, "pigs_over_20kg", 1056350, 58, 0, "average", "pasture", "concentrate", 1.4,
             0, 24, 0, 0, "solid", "broadcast", 0, 0, ],
            ["ireland", 2018, 2018, "gilts_not_yet_served", 14750, 120, 0, "average", "pasture", "concentrate", 2.42,
             0, 24, 0, 0, "solid", "broadcast", 0, 0, ],
            ["ireland", 2018, 2018, "other_sows_for_breeding", 26000, 210, 0, "average", "pasture", "concentrate", 7.11,
             0, 24, 0, 0, "solid", "broadcast", 0, 0, ],
            ["ireland", 2018, 2018, "pigs_under_20kg", 413900, 13.5, 0, "average", "pasture", "concentrate", 3.03,
             0, 24, 0, 0, "solid", "broadcast", 0, 0, ]
        ]

        columns = [
            "ef_country",
            "farm_id",
            "year",
            "cohort",
            "pop",
            "weight",
            "daily_milk",
            "forage",
            "grazing",
            "con_type",
            "con_amount",
            "t_outdoors",
            "t_indoors",
            "wool",
            "t_stabled",
            "mm_storage",
            "daily_spreading",
            "n_sold",
            "n_bought",
        ]

        self.data_frame = pd.DataFrame(data, columns=columns)

    def test_data_set_creation(self):
        # Perform assertions or tests on the loaded DataFrame
        self.assertEqual(len(self.data_frame), 7)  # Example assertion

    def test_output_livestock(self):
        self.maxDiff = None  # Allow displaying the full diff
        data = load_livestock_data(self.data_frame)
        output = capture_stdout(print_livestock_data, data)

        # Validate the output
        expected_output = read_expected_output("livestock.txt", self.txt_path)
        self.assertEqual(output.strip(), expected_output.strip())


if __name__ == "__main__":
    unittest.main()
