import unittest
import pandas as pd
from swine_lca.resource_manager.models import load_livestock_data, load_farm_data
from swine_lca.lca import AirQualityTotals
import matplotlib.pyplot as plt
import os


class EmissionCalculationTestCase(unittest.TestCase):
    def setUp(self):
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

        farm_data = {
            "ef_country": ["ireland"],
            "farm_id": [2018],
            "year": [2018],
            "total_urea": [0],
            "total_urea_abated": [0],
            "total_n_fert": [0],
            "total_p_fert": [0],
            "total_k_fert": [0],
            "diesel_kg": [0],
            "elec_kwh": [0],
        }

        self.farm_dataframe = pd.DataFrame(farm_data)

        self.baseline_index = -1

        self.airquality = AirQualityTotals("ireland")
        self.emissions_dict = self.airquality.create_emissions_dictionary([self.baseline_index])

    def test_emissions(self):
        past_animals = load_livestock_data(self.data_frame)
        past_farms = load_farm_data(self.farm_dataframe)

        past_animals_loc = list(past_animals.keys())[0]
        past_farm_loc = list(past_farms.keys())[0]

        self.emissions_dict["manure_management"][
            self.baseline_index
        ] += self.airquality.total_manure_NH3_AQ(past_animals[past_animals_loc]["animals"])

        self.emissions_dict["soils"][
            self.baseline_index
        ] += self.airquality.total_fertiliser_soils_NH3_AQ(
            past_farms[past_farm_loc].total_urea,
            past_farms[past_farm_loc].total_urea_abated,
            past_farms[past_farm_loc].total_n_fert,
        )

        print(self.emissions_dict)

        path = "data"
        labels = self.emissions_dict.keys()
        values = [self.emissions_dict[label][self.baseline_index] for label in labels]

        plt.bar(labels, values)
        plt.xticks(rotation=90)
        plt.ylabel('Values')
        plt.xlabel('Categories')
        plt.title('Bar Chart')
        plt.tight_layout()

        plt.savefig(os.path.join(path, "air_quality_emissions_test.png"))


if __name__ == "__main__":
    unittest.main()
