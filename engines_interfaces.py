
#TO-DO
#try import 
import xarray as xr
#
from itertools import permutations

#we expect to implement the frame clas
"""
TO-DO
- test the frame def
1. how to save a frame in a db! 
2. how to use a factory  dsgn pat and gen module frm other sources
3. a gen lnk tool to lnk two things into one th. all of the same type.  
"""

"""
TO-TK
- wt wd b advan t compost vs. to inheirt. no ide
"""

"""
To-DO
-get ordered array
arg = [params_dict[i] for i in self._params_name_ordered]
"""

class PipeModule():
    fxn_name = ''
    input_dims = ()
    output_dims = ()

    _params_name_ordered = ()
    _params_name_KW = ()
    _params_val_ordered_dict = dict()
    _params_val_KW_dict = dict()
    #_da_xarray = xarray()

    def __init__(self):
        #in case we need a long time,
        #the larger structure need to have a way to know if data is avail
        self._data_available = False 
    
    def check_ordered_args_exist(self, params_name):
        unlisted_args = list()
        for name_ordered in self._params_name_ordered: 
            if  name_ordered not in params_name:
                unlisted_args.append(name_ordered)
        
        return (True, None) if len(unlisted_args) == 0 else (False, unlisted_args)

    
    def assign_params_value(self,params_dict):
        #assign ordered param val
        
        #sort into argument
        self._params_val_dict = params_dict

        for arg_name in self._params_name_ordered:
            self._params_val_ordered_dict[arg_name] = params_dict[arg_name]

        #assign the rest to a self.kw args
        for arg_name in params_dict.keys():

            #do not repeat arg in kwargs
            if arg_name in self._params_name_ordered: continue

            self._params_val_KW_dict[arg_name] = params_dict[arg_name]

    


    def run_mod(self):
        #all functions will nd to inherit this 
        # expect to assign this to self._data
        self._data_available = False
        raise NotImplementedError

    def get_data_xarray(self):
        if self._data_available:
            return xr.DataArray(self._data, dims = self.output_dims)

        raise Exception('data is not available yet')


"""
TO-DO
- nd a function to check if the input parameters match eh? 
- nd a function to dist t frames
- nd a function to cal input A output dims
"""

class PipeFrame():

    def __init__(self, frame_type = 'proc', modules = [], module_parameters = dict(), 
                **kwarg):
        """
        frame_input_dims & frame_output_dims: tuple of strings
        e.g. ( 'trial', 'time')

        modules: (list of functions? classes  that implement the PipeModule interface)
        module_parameters: list of dictionaries (PipeModule.name: dictionary)
        """
        #frame type
        self._type = frame_type

        #check if modules is not empty
        if not modules:
            raise Exception('Empty module list!')
        
        #oherwise, just assign the modulees
        self._modules = modules 
        self._module_params = module_parameters

        #process frame init settings
        self._frame_input_dims = self._modules[0].input_dims
        self._frame_output_dims = self._modules[-1].input_dims


        #set up mod of operation default to serial
        self._frame_mode  = kwarg['frame_mode'] if 'frame_mode' in kwarg.keys() else 'serial'

        #set up additional info lk
        self._frame_name = kwarg['frame_name'] if 'frame_name' in kwarg.keys() else 'a aolab proc frame'
        
        #for print out
        self._frame_desc = kwarg['frame_desc'] if 'frame_desc' in kwarg.keys() else self._frame_name


    
    def run_frame(self):

        if self._frame_mode == 'serial':

            for mod_i, mod in enumerate(self._modules):
                mod.run_mod(self._module_params[mod_i])

        elif self._frame_mode == 'parallel':
            raise NotImplementedError

    @classmethod
    def orient_dims(cls,xr_array:xr.DataArray, mat_dims):
        """
        accepts a xr_array with definitions of dims in dims.
        xr_array (xr.DataArray):  has dims
        mat_dims (iterable, list or tuple):  matching dimensions:
        must be a permutated set of xr_array.dims 
        
        ASSUME"
        1. assume dims small. i.e. no permutation of 

        return a new xr_array 
        """
        #type checking
        if not isinstance(xr_array, xr.DataArray): raise TypeError('xr_array should be a xr_array')

        #checking matching dims
        curr_dims = xr_array.dims
        if not mat_dims in list(permutations(curr_dims)):
            raise Exception(f'{mat_dims} is not a permutation of {curr_dims}')

        return xr_array.transpose(*mat_dims)
        



    def wrap_up_frame(self):
        """
        depending config, this function would
        1. off load the intermediate parameters
        2. notify user
        3. note down time.
        4. save meta data. 

        """
        pass

            


"""
TO-DO
1. can chck compat when adding the frame. 
2. refact the method into checking two frames. 
3. can we suggest ways to improve the pipline
"""
class PipeLine():
    _frames = list()

    def __init__(self):
        self.num_of_frames = 0


    
    def add_frame(self, frame_to_add):
        #raise exception if the object is not a PipeFrame
        if not isinstance(frame_to_add, PipeFrame):
            raise Exception(f'would rather not add this frame to the pipeline: {PipeFrame}')

        #if yes, append to te frame list
        self._frames.append(frame_to_add)
        #increment the cnter
        self.num_of_frames += 1

    def add_frame_list(self, frame_list):
        pass

    def delete_last_frame(self):
        raise NotImplementedError
        #mem to dec t number of frames

    def check_frame_compat(self):
        """
        check if the input of the first frame eq to the output of the second frame
        ret a tuple of (True or False, )
        """

        for i in range(self.num_of_frames - 1):
            #get the dims 
            first_output_dims = self._frames[i]._frame_output_dims
            second_input_dims = self._frames[i+1]._frame_input_dims

            if  not first_output_dims == second_input_dims:
                return {'compat_result': False, 
                'problem_frames': (self._frames[i], self._frames[i+1])
                }

        
        return {'compat_result': True, 
                'problem_frames': None
                }
    
    @staticmethod
    def check_2_frames(pipeframe_1, pipeframe_2):
        raise NotImplementedError

    def plot_ppl(self):
        NotImplementedError
    
    def run_ppl(self):
        """
        loop through the frames
        for each frame, call its internal run_frame
        """
        #can we analyze the pipeline, do a bit of analysis
        compat_result_dic  = self.check_frame_compat()
        #wil return True for comp and False for non
        if compat_result_dic['compat_result']:
            raise Exception(f"Not compatible for these frames {compat_result_dic['problem_frames']}")

        #now, we know the pipeline compatibie
        for ppl_frame in self._frames:
            ppl_frame.run_frame()

