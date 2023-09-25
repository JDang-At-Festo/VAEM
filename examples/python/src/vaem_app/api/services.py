from datetime import datetime
from driver.VaemDriver import vaemDriver
from .models import Status, VaemState

# We assume that:
# VAEM device has already been successfully configued and is operational 
# Status data will be returned as a python dict from read_status()
# use middleware when any API endpoint is accessed to log and then produce the data
def vaem_middleware(get_response):
    def middleware(request):
        data = vaem_status()

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

        translator = data['transferTranslator']
        decoder = translator['decoder']

        vaem_state  = VaemState(
                                status = decoder(data['transferValue'], *translator['Status']),
                                error = decoder(data['transferValue'], *translator['Error']),
                                readiness = decoder(data['transferValue'], *translator['Readiness']),
                                operating_mode = decoder(data['transferValue'], *translator['OperatingMode']),
                                valve1 = decoder(data['transferValue'], *translator['Valve1']),
                                valve2 = decoder(data['transferValue'], *translator['Valve2']),
                                valve3 = decoder(data['transferValue'], *translator['Valve3']),
                                valve4 = decoder(data['transferValue'], *translator['Valve4']),
                                valve5 = decoder(data['transferValue'], *translator['Valve5']),
                                valve6 = decoder(data['transferValue'], *translator['Valve6']),
                                valve7 = decoder(data['transferValue'], *translator['Valve7']),
                                valve8 = decoder(data['transferValue'], *translator['Valve8']),
                                timestamp = datetime.now()
                                )
        vaem_state.save()

        resp = get_response(request)
        return resp
    return middleware

def vaem_status():
    vaem = vaemDriver(["0.0.0.0", 502, 0]) # necessary but non-functional arguments here
    data = vaem.read_status()
 
    return data
