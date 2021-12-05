import web
from web import form
from web.template import Render
import Video_Fetch

urls = ('/', 'index')



class index:
    
    def POST(self):
        data = web.input()
        print(data.URL)
        path = Video_Fetch.DownloadVideo(data.URL)
    
    def GET(self):
        render = web.template.render('templates/')
        path = ""
        visible = "true"
        return render.FileInput(path, visible)

    

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()  
