from swine_lca.resource_manager.models import print_livestock_data, load_livestock_data
from swine_lca.resource_manager.animal_data import AnimalData as ad
import pandas as pd


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

    animals = load_livestock_data(livestock_data_frame)

    print_livestock_data(animals)

    cohorts = livestock_data_frame.cohort.unique()

    print(cohorts)

    for cohort in cohorts:
        animal = getattr(animals[2018]["animals"], cohort)
        print(f"{cohort}: bought: {ad.get_animal_bought(animal)}")
        print(f"{cohort}: sold: {ad.get_animal_sold(animal)}")
        print(f"{cohort}: population: {ad.get_animal_population(animal)}")
        print(f"{cohort}: weight: {ad.get_animal_weight(animal)}")
        print(f"{cohort}: daily milk: {ad.get_animal_daily_milk(animal)}")
        print(f"{cohort}: grazing: {ad.get_animal_grazing(animal)}")
        print(f"{cohort}: t outdoors: {ad.get_animal_t_outdoors(animal)}")

        print(f"{cohort}: t indoors: {ad.get_animal_t_indoors(animal)}")
        print(f"{cohort}: t stabled: {ad.get_animal_t_stabled(animal)}")
        print(f"{cohort}: mm storage: {ad.get_animal_mm_storage(animal)}")
        print(f"{cohort}: forage: {ad.get_animal_forage(animal)}")
        print(f"{cohort}: concentrate type: {ad.get_animal_concentrate_type(animal)}")
        print(f"{cohort}: concentrate amount: {ad.get_animal_concentrate_amount(animal)}")
        print(f"{cohort}: year: {ad.get_animal_year(animal)}")
        print(f"{cohort}: cohort: {ad.get_animal_cohort(animal)}")


if __name__ == '__main__':
    main()
