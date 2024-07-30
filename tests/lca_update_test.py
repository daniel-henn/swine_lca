import pandas as pd
from swine_lca.resource_manager.models import load_livestock_data, load_farm_data
from swine_lca.lca import ClimateChangeTotals


def main():
    # Create some data to generate results

    livestock_data = [
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

    columns = ['ef_country', 'farm_id', 'year', 'cohort', 'pop', 'weight', 'daily_milk', 'forage', 'grazing',
               'con_type', 'con_amount', 't_outdoors', 't_indoors', 'wool', 't_stabled', 'mm_storage',
               'daily_spreading', 'n_sold', 'n_bought']

    livestock_data_frame = pd.DataFrame(livestock_data, columns=columns)

    farm_data = {
        'ef_country': ['ireland'],
        'farm_id': [2018],
        'year': [2018],
        'total_urea_kg': [0],
        'total_lime_kg': [0],
        'an_n_fert': [0],
        'urea_n_fert': [0],
        'total_urea_abated': [0],
        'total_p_fert': [0],
        'total_k_fert': [0],
        'diesel_kg': [0],
        'elec_kwh': [0]
    }

    farm_dataframe = pd.DataFrame(farm_data)

    # Instantiate ClimateChange Totals Class, passing Ireland as the emissions factor country
    climatechange = ClimateChangeTotals("ireland")

    # Create a dictionary to store results
    index = -1
    emissions_dict = climatechange.create_emissions_dictionary([index])

    # load the dataframes
    animals = load_livestock_data(livestock_data_frame)
    farms = load_farm_data(farm_dataframe)

    animals_loc = list(animals.keys())[0]
    farm_loc = list(farms.keys())[0]

    # generate results and store them in the dictionary

    emissions_dict["enteric_ch4"][index] += (
        climatechange.CH4_enteric_ch4(
            animals[animals_loc]["animals"]
        )
    )
    emissions_dict["manure_management_N2O"][index] += (
        climatechange.Total_storage_N2O(
            animals[animals_loc]["animals"]
        )
    )
    emissions_dict["manure_management_CH4"][index] += (
        climatechange.CH4_manure_management(
            animals[animals_loc]["animals"]
        )

    )

    # Print the emission results dictionary
    print(emissions_dict)


if __name__ == "__main__":
    main()
