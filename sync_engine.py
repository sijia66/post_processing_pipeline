#sync source def
import socket
import os

"""
how to mirror remote counter part
"""
#generic player  all members are going to inherit

PLAYER_TYPES = ('general', 'source', 'server', 'sink')

class SyncPlayer():
    def __init__(self, player_type = 'general', ip_addr =  "localhost"):
        """
        ip_addr:str
        """
        
        if player_type in PLAYER_TYPES:
            self.player_type = player_type
        else:
            raise Exception(f'unrecognized player type:{player_type} \n only support {PLAYER_TYPES}')
        
        self.ip_addr = ip_addr
        self._socket = None

    def shake_hand_with(self, another_player):
        if another_player.ip_addr == "localhost": return True 
        pass

    def connect_to_another_player(self, another_player):
        
        """
        ASSUME the following connections:
        - 
        - client connects to  server
        - sink connects to  server
        -  client to sink, as  server,  assume 1 client to 1 server at a time. 
        otherwise, there are too many poss
        
        """
        
        if another_player.ip_addr == "localhost": return True 
        
        #connect to server
        print(f'connect to {another_player.__name__}')
        
        try: 
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._socket.connect(another_player.ip_address, 
                                 123) #ASSUM pre-determined  port number between computers 
            return True
            
        except:
            raise Exception(f'cannot connect to another player {str(another_player)}')
            
    def transfer_file_to(self, another_player, source_file_path, dest_file_path):
        #whr w interface wz singile file handler. 
        raise NotImplementedError

    def check_file_exist(self):
        """
        return T or False 
        """
        return False
            
    def __str__(self):
        self.desc = ''
        return    self.desc

    
class SyncSource():
    def __init__(self):
        pass

class SyncSink(SyncPlayer):
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        
        
class SyncServer(SyncPlayer):


    def __init__(self, list_of_sources, list_of_sink, 
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def accept_clients(self):
        pass


#thiz can be plugged into a pipeline 
"""
chck if thy all all syncPlayers
"""
class SyncSess():
    """
    thiz is whr t sync haps
    """
    def __init__(self, list_of_sources, sync_server, list_of_sinks):
        self._list_of_sources = list_of_sources
        self._sync_server = sync_server
        self._list_of_sinks = list_of_sinks
        self.list_of_letters = list()
        pass

    def add_a_letter(self, job_source, source_file_path, job_dest, dest_dir):
        sync_letter = (job_source, source_file_path, job_dest, dest_dir)

        if job_source.shake_hand_with(job_dest):
            #if file path exist A dest dir exists

        else:
            raise Exception(f'{str(job_source)} can not shake hand with {str(job_dest)}')
        
        #chcked all errors, can add the letter
        self.list_of_letters.append(sync_letter)
        

    





