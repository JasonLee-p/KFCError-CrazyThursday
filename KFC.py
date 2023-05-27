class KFCError(Exception):
    def __init__(self, message="\nKFC crazy thursday Whoever gives me 50 CNY,\nI will Thank him!"):
        self.message = message

    def __str__(self):
        return self.message
