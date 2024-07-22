class Cart():
    def __init__(self, request):
        self.session = request.session
    
    #get the current session key
        cart = self.session.get('session_key')

    #if user is new no session key create some
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}


        #make sure site works on every app
        self.cart = cart