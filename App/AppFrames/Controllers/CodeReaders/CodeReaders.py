import logging


def import_honeywell(params):
    from .Honeywell3320g import BarCodeReader
    try:
        return BarCodeReader(params)
    except Exception as e:
        logging.error(str(e))
        return BarCodeReader()
        


def get_code_readers():
    code_reader = {
        "Honeywell": {
            "import": import_honeywell
        }
    }
    return code_reader