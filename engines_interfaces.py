
#we expect to implement the frame clas
"""
TO-DO
- test the frame def
1. how to save a frame in a db! 
"""

class PipeModule():
    fxn_name = ''
    input_dims = ()
    output_dims = ()

    def __init__(self):
        pass
    
    def run_mod(self):
        #all functions will nd to inherit this 
        raise NotImplementedError



class PipeFrame():

    def __init__(self, frame_input_dims = (), 
                modules = [], module_parameters = [], 
                frame_output_dims =(), 
                **kwarg):
        """
        frame_input_dims & frame_output_dims: tuple of strings
        e.g. ( 'trial', 'time')

        modules: (list of functions? classes  that implement the PipeModule interface)
        module: list of dictionaries (PipeModule.name: dictionary)
        """
        #process frame init settings
        self._frame_input_dims = frame_input_dims
        self._frame_output_dims = frame_output_dims

        #init the seq to process
        self._modules = modules 
        self._module_params = module_parameters
        #set up mod of operation default to serial
        self._frame_mode  = kwarg['frame_mode'] if 'frame_mode' in kwarg.keys() else 'serial'

        #set up additional info lk
        self._frame_name = kwarg['frame_name'] if 'frame_name' in kwarg.keys() else 'a aolab proc frame'
        
        #for print out
        self._frame_desc = kwarg['frame_desc'] if 'frame_desc' in kwarg.keys() else self._frame_name

    def run_frame(self):

        if self._frame_mode == 'serial':

            for mod_i, mod in enumerate(self._modules):
                mod.run_mod(self.self._module_params[mod_i])

        elif self._frame_mode == 'parallel':
            raise NotImplementedError

            


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

