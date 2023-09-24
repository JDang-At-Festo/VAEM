from datetime import datetime
from driver.VaemDriver import vaemDriver
from .models import Status

# We assume that:
# VAEM device has already been successfully configued and is operational 
# Status data will be returned as a python dict from read_status()
# use middleware when any API endpoint is accessed to log and then produce the data
def vaem_middleware(get_response):
    def middleware(request):
        data = vaem_status()
        print(data)
        status = Status(
                        access = data['access'],
                        data_type = data['dataType'],
                        param_index = data['paramIndex'],
                        param_sub_index = data['paramSubIndex'],
                        error_returned = data['errorRet'],
                        transfer_value= data['transferValue'],
                        timestamp = datetime.now()
                        )
        status.save()
        resp = get_response(request)
        return resp
    return middleware

def vaem_status():
    vaem = vaemDriver(["0.0.0.0", 502, 0]) # necessary but non-functional arguments here
    data = vaem.read_status()
 
    return data
