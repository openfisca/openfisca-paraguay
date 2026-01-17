import os

from openfisca_core.taxbenefitsystems import TaxBenefitSystem

from openfisca_paraguay.entities import entities


class ParaguayTaxBenefitSystem(TaxBenefitSystem):
    def __init__(self):
        super().__init__(entities)
        param_path = os.path.join(os.path.dirname(__file__), "parameters")
        self.load_parameters(param_path)

        var_path = os.path.join(os.path.dirname(__file__), "variables")
        self.add_variables_from_directory(var_path)
