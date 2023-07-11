import random 
import time
import multiprocessing  # the multiprocessing module provides support for parallelism

MEC_list = [
    {'id': 1, 'location': 0, 'cpu': 0, 'sticker_id': [1,2,3,4,5,6]},
    {'id': 2, 'location': 1, 'cpu': 1, 'sticker_id': [1,2,3,4,5,6]},
    {'id': 3, 'location': 2, 'cpu': 2, 'sticker_id': [1,2,3,4,5,6]},
    {'id': 4, 'location': 3, 'cpu': 3, 'sticker_id': [1,2,3,4,5,6]}
]

class TaskType():
    def __init__(self, task_inf_list):        
        self.req_u2e_size = 300 * 300 * 3 * 1
        self.process_loading = 300 * 300 * 3 * 4
        self.req_e2u_size = 4 * 4 + 20 * 4
        # migration
        self.migration_size = 2e9

        #===================================
        self.task_inf_list = task_inf_list
        self.task_process_time = 0
        self.task_size = 0       
        


    def find_MEC(self):        
        if self.task_inf_list['task_name'] == 'Capture':
            return None
        elif self.task_inf_list['task_name'] == 'Tracking':            
            for MEC in range(MEC_list):
                distance = self.task_inf_list['task_location'] - MEC['location']
                volume = MEC['cpu'] 
                if distance > 0 and volume > 0:                    
                    return MEC
                break    
            return None
        elif self.task_inf_list['task_name'] == 'AR_sticker':
            done = False
            for MEC in range(MEC_list):
                distance = self.task_inf_list['task_location'] - MEC['location']
                volume = MEC['cpu'] 
                if distance > 0 and volume > 0:
                    for sticker_id in range(MEC['sticker_id']):
                        if self.task_inf_list.User_sticker_id == sticker_id:
                            done = True
                            return MEC
                        break
                    if done:
                        break
            return None
        elif self.task_inf_list['task_name'] == 'Video_creator':
            for MEC in range(MEC_list):
                distance = self.task_inf_list['task_location'] - MEC['location']
                volume = MEC['cpu'] 
                if distance > 0 and volume > 0:
                    return MEC
            return None
        elif self.task_inf_list['task_name'] == 'Display':
            return None

    def handle_task(self):
        if self.task_inf_list['task_name'] == 'Capture':
            start_time = time.time()            
            task_size = round(random.uniform(0, 1),2)
            task_process_time = 0
            end_time = time.time()
            task_process_time = end_time - start_time
            print("Capture task done!!")
            results = [task_size, task_process_time]
            return results
        elif self.task_inf_list['task_name'] == 'Tracking':
            start_time = time.time()
            task_size = round(random.uniform(0, 1),2)
            task_process_time = 0
            end_time = time.time()
            task_process_time = end_time - start_time
            results = [task_size, task_process_time]
            return results
        elif self.task_inf_list['task_name'] == 'AR_sticker':
            start_time = time.time()
            task_size = round(random.uniform(0, 1),2)
            task_process_time = 0
            end_time = time.time()
            task_process_time = end_time - start_time
            results = [task_size, task_process_time]
            return results
        elif self.task_inf_list['task_name'] == 'Video_creator':
            start_time = time.time()
            task_size = round(random.uniform(0, 1),2)
            task_process_time = 0
            end_time = time.time()
            task_process_time = end_time - start_time
            results = [task_size, task_process_time]
            return results
        elif self.task_inf_list['task_name'] == 'Display':
            start_time = time.time()
            task_size = round(random.uniform(0, 1),2)
            task_process_time = 0
            end_time = time.time()
            task_process_time = end_time - start_time
            results = [task_size, task_process_time]
            return results

    


    