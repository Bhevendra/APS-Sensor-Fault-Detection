import sys, os

def error_message_detail(error,error_details:sys):
    _,_,exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occurred python script name[{0}] line no [{1}] error message[{2}]".format(file_name,exc_tb.tb_lineno, str(error))

    return error_message




class SensorException(Exception):

    def __init__(self,error_message,error_details:sys):
        ''' 
        : param error_message : error message in string format
        '''
        super().__init__(error_message)

        self.error_message = error_message_detail(error, error_details=error_details)

    def __str__(Self):
        return self.error_message

        