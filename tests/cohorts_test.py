import unittest
from swine_lca.resource_manager.swine_lca_data_manager import LCADataManager  # Import your actual class module
from swine_lca.resource_manager.data_loader import Loader


class TestDataStructureIntegrity(unittest.TestCase):

    def setUp(self):

        # Initialize your LCADataManager which should load your new data structure
        self.manager = LCADataManager("ireland")

        self.test_data = self.manager.cohorts_data

        self.loader_class = Loader("ireland")

        self.Gross_energy = {
            "boars": self.loader_class.emissions_factors.get_ef_Gross_energy_boars(),
            "gilts_in_pig": self.loader_class.emissions_factors.get_ef_Gross_energy_gilts_in_pig(),
            "sows_in_pig": self.loader_class.emissions_factors.get_ef_Gross_energy_sows_in_pig(),
            "pigs_over_20kg": self.loader_class.emissions_factors.get_ef_Gross_energy_pigs_over_20kg(),
            "gilts_not_yet_served": self.loader_class.emissions_factors.get_ef_Gross_energy_gilts_not_yet_served(),
            "other_sows_for_breeding": self.loader_class.emissions_factors.get_ef_Gross_energy_other_sows_for_breeding(),
            "pigs_under_20kg": self.loader_class.emissions_factors.get_ef_Gross_energy_pigs_under_20kg(),
        }

        self.N_excretion = {
            "boars": self.loader_class.emissions_factors.get_ef_N_excretion_boars(),
            "gilts_in_pig": self.loader_class.emissions_factors.get_ef_N_excretion_gilts_in_pig(),
            "sows_in_pig": self.loader_class.emissions_factors.get_ef_N_excretion_sows_in_pig(),
            "pigs_over_20kg": self.loader_class.emissions_factors.get_ef_N_excretion_pigs_over_20kg(),
            "gilts_not_yet_served": self.loader_class.emissions_factors.get_ef_N_excretion_gilts_not_yet_served(),
            "other_sows_for_breeding": self.loader_class.emissions_factors.get_ef_N_excretion_other_sows_for_breeding(),
            "pigs_under_20kg": self.loader_class.emissions_factors.get_ef_N_excretion_pigs_under_20kg(),
        }

        self.direct_n2o = {
            "boars": self.loader_class.emissions_factors.get_ef3__cpp_pasture_range_paddock_sheep_direct_n2o,
            "gilts_in_pig": self.loader_class.emissions_factors.get_ef3__cpp_pasture_range_paddock_sheep_direct_n2o,
            "sows_in_pig": self.loader_class.emissions_factors.get_ef3__cpp_pasture_range_paddock_sheep_direct_n2o,
            "pigs_over_20kg": self.loader_class.emissions_factors.get_ef3__cpp_pasture_range_paddock_sheep_direct_n2o,
            "gilts_not_yet_served": self.loader_class.emissions_factors.get_ef3__cpp_pasture_range_paddock_sheep_direct_n2o,
            "other_sows_for_breeding": self.loader_class.emissions_factors.get_ef3__cpp_pasture_range_paddock_sheep_direct_n2o,
            "pigs_under_20kg": self.loader_class.emissions_factors.get_ef3__cpp_pasture_range_paddock_sheep_direct_n2o,
        }

        self.atmospheric_deposition = {
            "boars": self.loader_class.emissions_factors.get_ef_indirect_n2o_atmospheric_deposition_to_soils_and_water,
            "gilts_in_pig": self.loader_class.emissions_factors.get_ef_indirect_n2o_atmospheric_deposition_to_soils_and_water,
            "sows_in_pig": self.loader_class.emissions_factors.get_ef_indirect_n2o_atmospheric_deposition_to_soils_and_water,
            "pigs_over_20kg": self.loader_class.emissions_factors.get_ef_indirect_n2o_atmospheric_deposition_to_soils_and_water,
            "gilts_not_yet_served": self.loader_class.emissions_factors.get_ef_indirect_n2o_atmospheric_deposition_to_soils_and_water,
            "other_sows_for_breeding": self.loader_class.emissions_factors.get_ef_indirect_n2o_atmospheric_deposition_to_soils_and_water,
            "pigs_under_20kg": self.loader_class.emissions_factors.get_ef_indirect_n2o_atmospheric_deposition_to_soils_and_water,
        }

        self.leaching = {
            "boars": self.loader_class.emissions_factors.get_ef_indirect_n2o_from_leaching_and_runoff,
            "gilts_in_pig": self.loader_class.emissions_factors.get_ef_indirect_n2o_from_leaching_and_runoff,
            "sows_in_pig": self.loader_class.emissions_factors.get_ef_indirect_n2o_from_leaching_and_runoff,
            "pigs_over_20kg": self.loader_class.emissions_factors.get_ef_indirect_n2o_from_leaching_and_runoff,
            "gilts_not_yet_served": self.loader_class.emissions_factors.get_ef_indirect_n2o_from_leaching_and_runoff,
            "other_sows_for_breeding": self.loader_class.emissions_factors.get_ef_indirect_n2o_from_leaching_and_runoff,
            "pigs_under_20kg": self.loader_class.emissions_factors.get_ef_indirect_n2o_from_leaching_and_runoff,
        }

    def test_cohort_Gross_energy_data_integrity(self):
        # Loop through each cohort in the old coefficient data structure
        for cohort, expected_value in self.Gross_energy.items():
            with self.subTest(cohort=cohort, attribute='Gross_energy'):
                # Check if the cohort exists in the new data structure
                self.assertIn(cohort, self.test_data, f"{cohort} is missing in new data structure")

                # Now check if 'coefficient' exists for this cohort in new data structure
                self.assertIn('Gross_energy', self.test_data[cohort], f"'Gross_energy' data is missing for {cohort}")

                # Retrieve the actual value from the new data structure
                actual_value = self.test_data[cohort]['Gross_energy']

                # Now assert the actual value matches the expected value from the old structure
                self.assertEqual(actual_value, expected_value, f"Mismatch in 'Gross_energy' for {cohort}")

    def test_cohort_N_excretion_data_integrity(self):
        # Loop through each cohort in the old coefficient data structure
        for cohort, expected_value in self.N_excretion.items():
            with self.subTest(cohort=cohort, attribute='N_excretion'):
                # Check if the cohort exists in the new data structure
                self.assertIn(cohort, self.test_data, f"{cohort} is missing in new data structure")

                # Now check if 'coefficient' exists for this cohort in new data structure
                self.assertIn('N_excretion', self.test_data[cohort], f"'weight_gain' data is missing for {cohort}")

                # Retrieve the actual value from the new data structure
                actual_value = self.test_data[cohort]['N_excretion']

                # Now assert the actual value matches the expected value from the old structure
                self.assertEqual(actual_value, expected_value, f"Mismatch in 'N_excretion' for {cohort}")

    def test_cohort_direct_n2o_emissions_factors_data_integrity(self):
        # Loop through each cohort in the old coefficient data structure
        for cohort, expected_value in self.direct_n2o.items():
            with self.subTest(cohort=cohort, attribute='direct_n2o'):
                # Check if the cohort exists in the new data structure
                self.assertIn(cohort, self.test_data, f"{cohort} is missing in new data structure")

                # Now check if 'coefficient' exists for this cohort in new data structure
                self.assertIn('direct_n2o', self.test_data[cohort],
                              f"'direct_n2o' data is missing for {cohort}")

                # Retrieve the actual value from the new data structure
                actual_value = self.test_data[cohort]['direct_n2o']

                # Now assert the actual value matches the expected value from the old structure
                self.assertEqual(actual_value(), expected_value(),
                                 f"Mismatch in 'direct_n2o' for {cohort}")

    def test_cohort_atmospheric_deposition_data_integrity(self):
        # Loop through each cohort in the old coefficient data structure
        for cohort, expected_value in self.atmospheric_deposition.items():
            with self.subTest(cohort=cohort, attribute='atmospheric_deposition'):
                # Check if the cohort exists in the new data structure
                self.assertIn(cohort, self.test_data, f"{cohort} is missing in new data structure")

                # Now check if 'coefficient' exists for this cohort in new data structure
                self.assertIn('atmospheric_deposition', self.test_data[cohort],
                              f"'atmospheric_deposition' data is missing for {cohort}")

                # Retrieve the actual value from the new data structure
                actual_value = self.test_data[cohort]['atmospheric_deposition']

                # Now assert the actual value matches the expected value from the old structure
                self.assertEqual(actual_value(), expected_value(), f"Mismatch in 'atmospheric_deposition' for {cohort}")

    def test_cohort_leaching_data_integrity(self):
        # Loop through each cohort in the old coefficient data structure
        for cohort, expected_value in self.leaching.items():
            with self.subTest(cohort=cohort, attribute='leaching'):
                # Check if the cohort exists in the new data structure
                self.assertIn(cohort, self.test_data, f"{cohort} is missing in new data structure")

                # Now check if 'coefficient' exists for this cohort in new data structure
                self.assertIn('leaching', self.test_data[cohort], f"'leaching' data is missing for {cohort}")

                # Retrieve the actual value from the new data structure
                actual_value = self.test_data[cohort]['leaching']

                # Now assert the actual value matches the expected value from the old structure
                self.assertEqual(actual_value(), expected_value(), f"Mismatch in 'leaching' for {cohort}")


if __name__ == '__main__':
    unittest.main()
