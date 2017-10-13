import pandas as pd
import numpy as np
import nvd3
from d_func import dd,linechart,dd2_alpha
from d_html import header,body,footer

nvd3.ipynb.initialize_javascript(use_remote=True)

data=pd.read_csv('DATA')
data1=data.set_index(data.Date.values)


from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    div_close="</div>"
    charts=[]
    for i in data1.keys()[1:-1]:
        div_open="<div name="+i+" class="+i+">"
        vis=linechart(data1['Date'],data1[i])
        charts.append(div_open+vis+div_close)
       
        
    header_text=header()
    body_text=body()
    footer_text=footer()    
    return header_text+body_text+''.join(charts)+footer_text
        
    

@app.route("/favicon.ico")
def favicon():
    return "Uhoh"

if __name__ == "__main__":
    app.run()