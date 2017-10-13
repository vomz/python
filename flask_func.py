import numpy as np
import nvd3

def linechart(x,y):
    chart = nvd3.lineChart(name=y.name, height=200, width=350)
    chart.add_serie(y=y.tolist(),x=np.arange(len(y)),name=y.name)
    
    chart.buildcontent()
    chart_html = chart.htmlcontent
    return chart_html

