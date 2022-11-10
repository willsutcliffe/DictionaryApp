import justpy as jp
from webapp import layout
from webapp import page
class Documentation(page.Page):
    path = "/doc"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)
        div = jp.Div(a=container, classes=  "bg-gray-200 h-screen")
        jp.Div(a=div, text="API Documentation", classes = "text-4xl m-2")
        jp.Div(a=div, text = """
        Get defintions of words
        """, classes= "text-lg")
        jp.Hr(a=div)
        jp.Div(a=div, text="www.example.com/api?w=moon")
        jp.Hr(a=div)
        jp.Div(a=div, text = """
        {"word": "moon", "defintion": ["A natural satellite of a planet."
        , "A month, particularly a lunar month (approximately 28 days)."
        , "To fuss over adoringly or with great affection.", "Deliberately
         show ones bare ass (usually to an audience, or at a place, where
          this is not expected or deemed appropriate).", 
          "To be lost in phantasies or be carried away by some internal 
          vision, having temorarily lost (part of) contact to reality."]}
        """, classes= "text-lg")
        return wp
