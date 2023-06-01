import unittest
import pandas as pd
from cattle_lca.models import load_livestock_data, load_farm_data
from cattle_lca.lca import ClimateChangeTotals
import matplotlib.pyplot as plt
import os


class EmissionCalculationTestCase(unittest.TestCase):
    def setUp(self):
        # Create the DataFrame with the provided data
        data = [
            [
                "ireland",
                2018,
                2018,
                "dairy_cows",
                175298,
                538,
                14.953,
                "irish_grass",
                "pasture",
                "concentrate",
                2.992828296,
                13.5890411,
                10.4109589,
                0,
                0,
                "tank liquid",
                "broadcast",
                0,
                0,
            ],
            [
                "ireland",
                2018,
                2018,
                "suckler_cows",
                30587,
                600,
                1.410958904,
                "irish_grass",
                "pasture",
                "concentrate",
                0.842751605,
                12.2739726,
                11.7260274,
                0,
                0,
                "tank liquid",
                "broadcast",
                0,
                0,
            ],
            [
                "ireland",
                2018,
                2018,
                "DxD_heifers_more_2_yr",
                384.1446311,
                122.125,
                0,
                "irish_grass",
                "pasture",
                "concentrate",
                0,
                12.98630137,
                11.01369863,
                0,
                0,
                "tank liquid",
                "broadcast",
                0,
                0,
            ],
            [
                "ireland",
                2018,
                2018,
                "DxB_heifers_more_2_yr",
                0,
                94.75,
                0,
                "irish_grass",
                "pasture",
                "concentrate",
                0,
                12.98630137,
                11.01369863,
                0,
                0,
                "tank liquid",
                "broadcast",
                0,
                0,
            ],
            [
                "ireland",
                2018,
                2018,
                "BxB_heifers_more_2_yr",
                0,
                103.875,
                0,
                "irish_grass",
                "pasture",
                "concentrate",
                0,
                12.38356164,
                11.61643836,
                0,
                0,
                "tank liquid",
                "broadcast",
                0,
                0,
            ],
            [
                "ireland",
                2018,
                2018,
                "DxD_heifers_less_2_yr",
                49298.56099,
                395.875,
                0,
                "irish_grass",
                "pasture",
                "concentrate",
                0,
                11.56164384,
                12.43835616,
                0,
                0,
                "tank liquid",
                "broadcast",
                0,
                0,
            ],
            [
                "ireland",
                2018,
                2018,
                "DxB_heifers_less_2_yr",
                30347.42586,
                346.6,
                0,
                "irish_grass",
                "pasture",
                "concentrate",
                0,
                11.56164384,
                12.43835616,
                0,
                0,
                "tank liquid",
                "broadcast",
                0,
                0,
            ],
            [
                "ireland",
                2018,
                2018,
                "BxB_heifers_less_2_yr",
                14763.98982,
                412.3,
                0,
                "irish_grass",
                "pasture",
                "concentrate",
                0,
                11.56164384,
                12.43835616,
                0,
                0,
                "tank liquid",
                "broadcast",
                0,
                0,
            ],
            [
                "ireland",
                2018,
                2018,
                "DxD_steers_less_2_yr",
                37646.17385,
                463.475,
                0,
                "irish_grass",
                "pasture",
                "concentrate",
                0,
                11.56164384,
                12.43835616,
                0,
                0,
                "tank liquid",
                "broadcast",
                0,
                0,
            ],
            [
                "ireland",
                2018,
                2018,
                "DxB_steers_less_2_yr",
                29323.04018,
                474.425,
                0,
                "irish_grass",
                "pasture",
                "concentrate",
                0,
                11.56164384,
                12.43835616,
                0,
                0,
                "tank liquid",
                "broadcast",
                0,
                0,
            ],
            [
                "ireland",
                2018,
                2018,
                "BxB_steers_less_2_yr",
                14327.92261,
                479.9,
                0,
                "irish_grass",
                "pasture",
                "concentrate",
                0,
                11.56164384,
                12.43835616,
                0,
                0,
                "tank liquid",
                "broadcast",
                0,
                0,
            ],
            [
                "ireland",
                2018,
                2018,
                "DxD_steers_more_2_yr",
                5506.073046,
                140.45,
                0,
                "irish_grass",
                "pasture",
                "concentrate",
                0,
                18.73972603,
                5.260273973,
                0,
                0,
                "tank liquid",
                "broadcast",
                0,
                0,
            ],
            [
                "ireland",
                2018,
                2018,
                "DxB_steers_more_2_yr",
                4225.590942,
                129.5,
                0,
                "irish_grass",
                "pasture",
                "concentrate",
                0,
                18.73972603,
                5.260273973,
                0,
                0,
                "tank liquid",
                "broadcast",
                0,
                0,
            ],
            [
                "ireland",
                2018,
                2018,
                "BxB_steers_more_2_yr",
                2273.779022,
                162.35,
                0,
                "irish_grass",
                "pasture",
                "concentrate",
                0,
                18.73972603,
                5.260273973,
                0,
                0,
                "tank liquid",
                "broadcast",
                0,
                0,
            ],
            [
                "ireland",
                2018,
                2018,
                "DxD_calves_f",
                46993.69321,
                149.575,
                0,
                "irish_grass",
                "pasture",
                "concentrate",
                1,
                7.945205479,
                16.05479452,
                0,
                0,
                "tank liquid",
                "broadcast",
                0,
                0,
            ],
            [
                "ireland",
                2018,
                2018,
                "DxB_calves_f",
                33164.48649,
                116.725,
                0,
                "irish_grass",
                "pasture",
                "concentrate",
                1,
                7.945205479,
                16.05479452,
                0,
                0,
                "tank liquid",
                "broadcast",
                0,
                0,
            ],
            [
                "ireland",
                2018,
                2018,
                "BxB_calves_f",
                13985.29837,
                175.125,
                0,
                "irish_grass",
                "pasture",
                "concentrate",
                1,
                7.945205479,
                16.05479452,
                0,
                0,
                "tank liquid",
                "broadcast",
                0,
                0,
            ],
            [
                "ireland",
                2018,
                2018,
                "DxD_calves_m",
                32140.1008,
                122.2,
                0,
                "irish_grass",
                "pasture",
                "concentrate",
                1,
                7.945205479,
                16.05479452,
                0,
                0,
                "tank liquid",
                "broadcast",
                0,
                0,
            ],
            [
                "ireland",
                2018,
                2018,
                "DxB_calves_m",
                31755.95617,
                118.55,
                0,
                "irish_grass",
                "pasture",
                "concentrate",
                1,
                7.945205479,
                16.05479452,
                0,
                0,
                "tank liquid",
                "broadcast",
                0,
                0,
            ],
            [
                "ireland",
                2018,
                2018,
                "BxB_calves_m",
                13424.64053,
                178.775,
                0,
                "irish_grass",
                "pasture",
                "concentrate",
                1,
                7.945205479,
                16.05479452,
                0,
                0,
                "tank liquid",
                "broadcast",
                0,
                0,
            ],
            [
                "ireland",
                2018,
                2018,
                "bulls",
                4641.388771,
                773,
                0,
                "irish_grass",
                "pasture",
                "concentrate",
                0.654140961,
                11.56164384,
                12.43835616,
                0,
                0,
                "tank liquid",
                "broadcast",
                0,
                0,
            ],
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
            "total_urea": [2072487.127],
            "total_urea_abated": [0],
            "total_n_fert": [17310655.18],
            "total_p_fert": [1615261.859],
            "total_k_fert": [3922778.8],
            "diesel_kg": [0],
            "elec_kwh": [0],
        }

        self.farm_dataframe = pd.DataFrame(farm_data)

        self.baseline_index = -1

        self.climatechange = ClimateChangeTotals("ireland")
        self.emissions_dict = self.climatechange.create_expanded_emissions_dictionary([self.baseline_index])

    def test_emissions(self):
        
        past_animals = load_livestock_data(self.data_frame)
        past_farms = load_farm_data(self.farm_dataframe)

        past_animals_loc = list(past_animals.keys())[0]
        past_farm_loc = list(past_farms.keys())[0]

        self.emissions_dict["enteric_ch4"][
            self.baseline_index
        ] += self.climatechange.CH4_enteric_ch4(past_animals[past_animals_loc]["animals"]) * 28
        self.emissions_dict["manure_management_N2O"][
            self.baseline_index
        ] += self.climatechange.Total_storage_N2O(past_animals[past_animals_loc]["animals"]) *298
        self.emissions_dict["manure_management_CH4"][
            self.baseline_index
        ] += self.climatechange.CH4_manure_management(
            past_animals[past_animals_loc]["animals"]
        )*28
        self.emissions_dict["manure_applied_N"][
            self.baseline_index
        ] += self.climatechange.Total_N2O_Spreading(
            past_animals[past_animals_loc]["animals"]
        )*298
        self.emissions_dict["N_direct_PRP"][
            self.baseline_index
        ] += self.climatechange.N2O_total_PRP_N2O_direct(
            past_animals[past_animals_loc]["animals"]
        )*298

        self.emissions_dict["N_indirect_PRP"][
            self.baseline_index
        ] += self.climatechange.N2O_total_PRP_N2O_indirect(
            past_animals[past_animals_loc]["animals"]
        )*298
        self.emissions_dict["N_direct_fertiliser"][
            self.baseline_index
        ] = self.climatechange.N2O_direct_fertiliser(
            past_farms[past_farm_loc].total_urea,
            past_farms[past_farm_loc].total_urea_abated,
            past_farms[past_farm_loc].total_n_fert,
        )*298

        self.emissions_dict["N_indirect_fertiliser"][
            self.baseline_index
        ] += self.climatechange.N2O_fertiliser_indirect(
            past_farms[past_farm_loc].total_urea,
            past_farms[past_farm_loc].total_urea_abated,
            past_farms[past_farm_loc].total_n_fert,
        )*298
        self.emissions_dict["soils_CO2"][
            self.baseline_index
        ] += self.climatechange.CO2_soils_GWP(
            past_farms[past_farm_loc].total_urea,
            past_farms[past_farm_loc].total_urea_abated,
        )

        self.emissions_dict["upstream_fuel_fert"][
            self.baseline_index
        ] += self.climatechange.upstream_and_inputs_and_fuel_co2(
            past_farms[past_farm_loc].diesel_kg,
            past_farms[past_farm_loc].elec_kwh,
            past_farms[past_farm_loc].total_n_fert,
            past_farms[past_farm_loc].total_urea,
            past_farms[past_farm_loc].total_urea_abated,
            past_farms[past_farm_loc].total_p_fert,
            past_farms[past_farm_loc].total_k_fert,
        )

        self.emissions_dict["upstream_feed"][
            self.baseline_index
        ] += self.climatechange.co2_from_concentrate_production(
            past_animals[past_animals_loc]["animals"]
        )


        # Totals
        self.emissions_dict["upstream"][self.baseline_index
        ] = (self.emissions_dict["upstream_feed"][
            self.baseline_index
        ]+self.emissions_dict["upstream_fuel_fert"][
            self.baseline_index
        ])
        self.emissions_dict["soil_organic_N_direct"][self.baseline_index] = (
            self.emissions_dict["manure_applied_N"][self.baseline_index]
            + self.emissions_dict["N_direct_PRP"][self.baseline_index]
        )
        self.emissions_dict["soil_organic_N_indirect"][
            self.baseline_index
        ] = self.emissions_dict["N_indirect_PRP"][self.baseline_index]

        self.emissions_dict["soil_inorganic_N_direct"][
            self.baseline_index
        ] = self.emissions_dict["N_direct_fertiliser"][self.baseline_index]
        self.emissions_dict["soil_inorganic_N_indirect"][
            self.baseline_index
        ] = self.emissions_dict["N_indirect_fertiliser"][self.baseline_index]

        self.emissions_dict["soil_N_direct"][self.baseline_index] = (
            (self.emissions_dict["soil_organic_N_direct"][self.baseline_index]
            + self.emissions_dict["soil_inorganic_N_direct"][self.baseline_index])
        )

        self.emissions_dict["soil_N_indirect"][self.baseline_index] = (
            (self.emissions_dict["soil_inorganic_N_indirect"][self.baseline_index]
            + self.emissions_dict["soil_organic_N_indirect"][self.baseline_index])
        )

        self.emissions_dict["soils_N2O"][self.baseline_index] = (
            self.emissions_dict["soil_N_direct"][self.baseline_index]
            + self.emissions_dict["soil_N_indirect"][self.baseline_index]
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

        plt.savefig(os.path.join(path,"emissions_test.png"))


if __name__ == "__main__":
    unittest.main()
