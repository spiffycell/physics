""" The electromagnetic tensor and its properties."""
# imports
from pydantic import BaseModel
from typing import list

# macros
COL_DIMENSION = 4
ROW_DIMENSION = 4
TENSOR_DIMENSION = [COL_DIMENSION, ROW_DIMENSION]

# objects
class ElecromagneticTensor(BaseModel):
    """ Object for EM Tensor."""
    F: List[List[float]]

    @classmethod
    def gauss_electricity_law(self, F, J):
        """ Gauss's Law for Electricity."""
        return [sum(F[i][j] * J[j] for j in range(TENSOR_DIMENSION[1])) for i in range(TENSOR_DIMENSION)]

    @classmethod
    def gauss_magnetism_law(self, F_dual):
        """ Gauss's Law for Magnetism."""
        return [sum(F_dual[i][j] for j in range(TENSOR_DIMENSION[1])) for i in range(TENSOR_DIMENSION)]

    @classmethod
    def faraday_induction_law(self, F):
        """ Faraday's Law of Induction."""
        result = []
        for i in range(TENSOR_DIMENSION[0]):
            row_sum = sum(F[i][j] + F[j][i] + F[i][j] for j in range(TENSOR_DIMENSION[1]))
            result.append(row_sum)
        return result

    @classmethod
    def ampere_maxwell_law(self, F_dual, J):
        """ Ampere's Law with Maxwell's Additions."""
        result = []
        for i in range(TENSOR_DIMENSION[0]):
            row_sum = sum(F[i][j] for j in range(TENSOR_DIMENSION[1])) - J[i]
            result.append(row_sum)
        return result
