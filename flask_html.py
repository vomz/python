def header():
####################################Creation of Header#################################################################
    style='<style>\n\
    /* The switch - the box around the slider */\n\
    .switch { position: relative;\n\
              display: inline-block;\n\
              width: 30px;\n\
              height: 17px;\n\
            }\n\
    /* Hide default HTML checkbox */\n\
    .switch input {display:none;}\n\
    /* The slider */\n\
    .slider { position: absolute;\n\
              cursor: pointer; top: 0;\n\
              left: 0;\n\
              right: 0;\n\
              bottom: 0;\n\
              background-color: #ccc;\n\
              -webkit-transition: .4s;\n\
              transition: .4s;\n\
            }\n\
    .slider:before { position: absolute;\n\
                     content: "";\n\
                     height: 13px;\n\
                     width: 13px;\n\
                     left: 2px;\n\
                     bottom: 2px;\n\
                     background-color: white;\n\
                     -webkit-transition: .4s;\n\
                     transition: .4s;\n\
                  }\n\
    input:checked + .slider { background-color: #2196F3;}\n\
    input:focus + .slider { box-shadow: 0 0 0.5px #2196F3;}\n\
    input:checked + .slider:before { -webkit-transform: translateX(13px);\n\
                                     -ms-transform: translateX(13px);\n\
                                     transform: translateX(13px);\n\
                                   }\n\
    /* Rounded sliders */\n\
    .slider.round { border-radius: 17px;}\n\
    .slider.round:before { border-radius: 50%;}\n\
    .switch_box{ vertical-align: top;\n\
                 display: inline-block;\n\
                 *display: inline;\n\
               }\n\
</style>'
    header_text='<!DOCTYPE html><html lang="en"><head><meta charset="utf-8" /><link href="https://cdnjs.cloudflare.com/ajax/libs/nvd3/1.7.1/nv.d3.min.css" rel="stylesheet" /><script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.5/d3.min.js"></script><script src="https://cdnjs.cloudflare.com/ajax/libs/nvd3/1.7.1/nv.d3.min.js"></script><script src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.2.1.min.js"></script>'+style+'</head>'
    return header_text

def body():
####################################Creation of Body#################################################################
    buttons='<div id="placeholder1">\
    		<div class="switch_box">\
    			<!-- Rounded switch -->\
    			<label class="switch">\
    			  <input type="checkbox" onclick="chartSelection();" id="_box" name="slider" value="placeholder">\
    			  <span class="slider round"></span>\
    			</label>\
    			<span>PLACEHOLDER</span>\
    		</div>'
    		
    
    body_text=buttons
    
    return body_text


def footer():
####################################Creation of Footer#################################################################
    footer_text='</div></body></html>'
    jsvars='<script>\n\
            PLACEHOLDER\n\
            </script>\n'
    jsfunc='<script>\n\
    function HideAllFast(){\n\
     $(\'.PLACEHOLDER\').hide();\n\
    };\n\
    \n\
    \n\
    $(document).ready(function(){\n\
     HideAllFast();});\n\
     <!--Chart Selected-->\n\
    function chartSelection(){\n\
     HideAllFast();\n\
     placeholder=[]\n\
     placeholder1=[]\n\
     place=$(\'input[name=slider]:checked\').each(function(){placeholder.push($(this).val());});\n\
     place1=$(\'input[name=xslider]:checked\').each(function(){placeholder1.push($(this).val());});\n\
     if (placeholder.length == 0){\n\
      for (i in placeholder1){\n\
       $(\'div[class$=_\'+placeholder1[i]+\']\').show();\n\
     }}\n\
     else if (placeholder1.length == 0){\n\
           for (i in placeholder){\n\
            $(\'div[class^=\'+placeholder[i]+\']\').show();\n\
     }}\n\
     else if (placeholder.length != 0 && placeholder1.length != 0){\n\
           for (i in placeholder1){\n\
            for (j in placeholder){\n\
             $(\'div[class^=\'+placeholder[j]+\'][class$=_\'+placeholder1[i]+\']\').show();\n\
     }}}\n\
     else{}\n\
     $(\'div[class^=selection]\').show();\n\
    };\n\
    \n\
    \n\
    </script>'
    
    footer_text=footer_text+jsvars+jsfunc
    return footer_text