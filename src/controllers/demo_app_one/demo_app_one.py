from flask import Flask, request, jsonify

class DemoAppOne: 

    def __init__(self):
        pass
    
    def testGet(self):
        return jsonify({
            "status": True,
            "message": 'Successfully running'
        })
    def testPost(self):
        print('testPost request', request.data)
        payload = request.get_json()
        print("json >>>>>", payload)
        return jsonify(payload)
    
    def getQueryParams(self):
        print('getQueryParams', request.args)
        return 'request query params'
    
    def getPathParams(self, id) :
        # print('request', id)
        return jsonify({ 
            'status': bool(request.view_args['id']),
            'data': request.view_args['id'],
            'messsage': 'Get getPathParams'
        })
