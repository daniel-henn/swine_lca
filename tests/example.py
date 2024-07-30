import pandas as pd
from swine_lca.resource_manager.models import load_livestock_data, load_farm_data
from swine_lca.lca import ClimateChangeTotals, Energy


def main():
    # Instantiate ClimateChange Totals Class, passing Ireland as the emissions factor country
    climatechange = ClimateChangeTotals("ireland")
    energy = Energy("ireland")

    # Create a dictionary to store results
    index = -1
    emissions_dict = climatechange.create_emissions_dictionary([index])

    # Create some data to generate results

    livestock_data = {
        "ef_country": [
            "ireland",
            "ireland",
            "ireland",
            "ireland",
            "ireland",
            "ireland",
            "ireland",
        ],
        "farm_id": [2018, 2018, 2018, 2018, 2018, 2018, 2018],
        "year": [2018, 2018, 2018, 2018, 2018, 2018, 2018],
        "cohort": [
            "boars",
            "gilts_in_pig",
            "sows_in_pig",
            "pigs_over_20kg",
            "gilts_not_yet_served",
            "other_sows_for_breeding",
            "pigs_under_20kg",
        ],
        "pop": [
            900,
            17200,
            73500,
            1056350,
            14750,
            26000,
            413900,
        ],
        "weight": [225, 160, 200, 58, 120, 210, 13.5],
        "forage": [
            "average",
            "average",
            "average",
            "average",
            "average",
            "average",
            "average",
        ],
        "grazing": [
            "pasture",
            "pasture",
            "pasture",
            "pasture",
            "pasture",
            "pasture",
            "pasture",
        ],
        "con_type": [
            "concentrate",
            "concentrate",
            "concentrate",
            "concentrate",
            "concentrate",
            "concentrate",
            "concentrate",
        ],
        "con_amount": [2.75, 2.64, 2.64, 1.4, 2.42, 7.11, 3.03],
        "t_outdoors": [0, 0, 0, 0, 0, 0, 0 ],
        "t_indoors": [24, 24, 24, 24, 24, 24, 24],
        "t_stabled": [0, 0, 0, 0, 0, 0, 0],
        "mm_storage": [
            "solid",
            "solid",
            "solid",
            "solid",
            "solid",
            "solid",
            "solid",
        ],
        "daily_spreading": [
            "broadcast",
            "broadcast",
            "broadcast",
            "broadcast",
            "broadcast",
            "broadcast",
            "broadcast",
        ],
        "n_sold": [0, 0, 0, 0, 0, 0, 0],
        "n_bought": [0, 0, 0, 0, 0, 0, 0],
    }

    livestock_data_frame = pd.DataFrame(livestock_data)

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

    # load the dataframes
    animals = load_livestock_data(livestock_data_frame)
    farms = load_farm_data(farm_dataframe)

    animals_loc = list(animals.keys())[0]
    farm_loc = list(farms.keys())[0]



    # generate results and store them in the dictionary

    emissions_dict["enteric_ch4"][index] += climatechange.CH4_enteric_ch4(
        animals[animals_loc]["animals"]
    )

    emissions_dict["manure_management_N2O"][index] += climatechange.Total_storage_N2O(
        animals[animals_loc]["animals"]
    )

    emissions_dict["manure_management_CH4"][
        index
    ] += climatechange.CH4_manure_management(animals[animals_loc]["animals"])

    emissions_dict["manure_applied_N"][index] += 0

    emissions_dict["N_direct_fertiliser"][index] = climatechange.N2O_direct_fertiliser(
        farms[farm_loc].urea_n_fert,
        farms[farm_loc].total_urea_abated,
        farms[farm_loc].an_n_fert,
    )

    emissions_dict["N_indirect_fertiliser"][
        index
    ] += climatechange.N2O_fertiliser_indirect(
        farms[farm_loc].urea_n_fert,
        farms[farm_loc].total_urea_abated,
        farms[farm_loc].an_n_fert,
    )
    emissions_dict["soils_CO2"][index] += climatechange.CO2_soils_GWP(
        farms[farm_loc].total_urea_kg,
        farms[farm_loc].total_lime_kg,
    )

    # Add the totals
    emissions_dict["soil_organic_N_direct"][index] = (
        emissions_dict["manure_applied_N"][index]
        + emissions_dict["N_direct_PRP"][index]
    )
    emissions_dict["soil_organic_N_indirect"][index] = emissions_dict["N_indirect_PRP"][
        index
    ]

    emissions_dict["soil_inorganic_N_direct"][index] = emissions_dict[
        "N_direct_fertiliser"
    ][index]
    emissions_dict["soil_inorganic_N_indirect"][index] = emissions_dict[
        "N_indirect_fertiliser"
    ][index]

    emissions_dict["soil_N_direct"][index] = (
        emissions_dict["soil_organic_N_direct"][index]
        + emissions_dict["soil_inorganic_N_direct"][index]
    )

    emissions_dict["soil_N_indirect"][index] = (
        emissions_dict["soil_inorganic_N_indirect"][index]
        + emissions_dict["soil_organic_N_indirect"][index]
    )

    emissions_dict["soils_N2O"][index] = (
        emissions_dict["soil_N_direct"][index]
        + emissions_dict["soil_N_indirect"][index]
    )

    # Print the emission results dictionary
    print(emissions_dict)

if __name__ == "__main__":
    main()
