def success_response(data=None, msg='Operation Success'):
    return {
        'success': True,
        'message': msg,
        'data': data
    }


def failure_response(data=None, msg='Operation Failure'):
    return {
        'success': False,
        'message': msg,
        'data': data
    }
