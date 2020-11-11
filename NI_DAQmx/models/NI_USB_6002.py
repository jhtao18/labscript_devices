#####################################################################
#                                                                   #
# /NI_DAQmx/models/_subclass_template.py                            #
#                                                                   #
# Copyright 2018, Christopher Billington                            #
#                                                                   #
# This file is part of the module labscript_devices, in the         #
# labscript suite (see http://labscriptsuite.org), and is           #
# licensed under the Simplified BSD License. See the license.txt    #
# file in the root of the project for the full license.             #
#                                                                   #
#####################################################################

#####################################################################
#     WARNING                                                       #
#                                                                   #
# This file is auto-generated, any modifications may be             #
# overwritten. See README.txt in this folder for details            #
#                                                                   #
#####################################################################


from labscript_devices.NI_DAQmx.labscript_devices import NI_DAQmx

CAPABILITIES = {
    'AI_range': [-10.0, 10.0],
    'AI_start_delay': 0, #manually =0 because get_capabilities failed
    'AO_range': [-10.0, 10.0],
    'max_AI_multi_chan_rate': 50000.0,
    'max_AI_single_chan_rate': 50000.0,
    'max_AO_sample_rate': 5000.0,
    'acquisition_rate': 25000.0,
    'max_DO_sample_rate': None,
    'min_semiperiod_measurement': None,
    'num_AI': 8,
    'num_AO': 2,
    'num_CI': 1,
    'ports': {
        'port0': {'num_lines': 8, 'supports_buffered': False},
        'port1': {'num_lines': 4, 'supports_buffered': False},
        'port2': {'num_lines': 1, 'supports_buffered': False},
    },
    'supports_buffered_AO': True,
    'supports_buffered_DO': False,
    'supports_semiperiod_measurement': False,
}


class NI_USB_6002(NI_DAQmx):
    description = 'NI-USB-6002'

    def __init__(self, *args, **kwargs):
        # Any provided kwargs take precedent over capabilities
        combined_kwargs = CAPABILITIES.copy()
        combined_kwargs.update(kwargs)
        NI_DAQmx.__init__(self, *args, **combined_kwargs)