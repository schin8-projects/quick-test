'''
Template code
'''


class Main:
    ''' Main class for template '''
    code = 0

    def __init__(self, msg, code) -> None:
        Main.code += code
        self.msg = f"Hello {msg}"

    def get_message(self):
        ''' Simple getter '''
        return self.msg

    def set_message(self, msg) -> None:
        ''' Simple setter '''
        self.msg = msg
