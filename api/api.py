import justpy as jp
import definition
import json
class Api:
    """ Handles request at /api?w=word"""
    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        word = req.query_params.get("w")
        defin = definition.Definition(word).get()

        response = {
            "word" : word,
            "defintion" : defin
        }
        wp.html = json.dumps(response)
        #jp.Div(a=wp, text=word.title())
        return(wp)

jp.Route("/", Api.serve)

jp.justpy()