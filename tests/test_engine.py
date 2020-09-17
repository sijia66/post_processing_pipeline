import pytest
import numpy as np
import xarray as xr


from engines_interfaces import PipeModule

class DataRelayterFor1D(PipeModule):
    """
    relay data to output
    """
    input_dims = ('time')
    output_dims = ('time')
    _params_name_ordered = ('data')

    def run_mod(self):
        self._da_xarray = xr.DataArray(self._params_val_dict['Data'])



class TestDataRelay():
    relay = DataRelayterFor1D()

    def test_assign_para_values(self):
        arr = np.array([1,2,3])
        params_dict = {'data': arr}
        self.relay.assign_params_value(params_dict)

        assert 'data' in self.relay._params_val_dict.keys()

        




