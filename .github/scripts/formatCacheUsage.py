import sys
# import js2py

# js = """
# var coll = document.getElementsByClassName("collapsible");
# var i;

# for (i = 0; i < coll.length; i++) {
#   coll[i].addEventListener("click", function() {
#     this.classList.toggle("active");
#     var content = this.nextElementSibling;
#     if (content.style.display === "block") {
#       content.style.display = "none";
#     } else {
#       content.style.display = "block";
#     }
#   });
# }
# """.replace("document.write", "return ")
# result = js2py.eval_js(js)

style = """
.collapsible {
  background-color: #777;
  color: white;
  cursor: pointer;
  padding: 18px;
  width: 100%;
  border: none;
  text-align: left;
  outline: none;
  font-size: 15px;
}

.active, .collapsible:hover {
  background-color: #555;
}

.content {
  padding: 0 18px;
  display: none;
  overflow: hidden;
  background-color: #f1f1f1;
} """

def generate_cache_usage_html():
    html = f"<html><head><style>{style}</style></head>"
    html += "<body><h1>Performance Profiling</h1>" \
            "<button type='button' class='collapsible'>Cache Memory Usage</button><div class='content'>"
    current_module = table_list[0].split("#")[0].split(":")[-1]
    html += f"<button type='button' class='collapsible'>{current_module}</button><div class='content'>" \
            "<table><tr><th>Action in test-app</th><th>Cache usage</th></tr>"
    
    for line in table_list:
        if "CacheSize:" in line:
            # Split the line by "," to separate key and value
            key_value_pair = line.split(",")
            # Extract key and value
            key = key_value_pair[0].split(":")[-1]
            value = key_value_pair[1].split()[0]

            html += f"<tr><td>{key}</td><td>{value[0:-1]} KB</td></tr>"
    
    html += f"</table></div></div></body></html>"

    print(f"HTML = {html}")

    with open("cache_usage_report.html", "w") as file:
        file.write(html)

logFile = open(sys.argv[1], "r")
table_data = logFile.read().strip()
logFile.close()
table_list = table_data.split('\n')
print(f"Table lines = \n{table_list}")

generate_cache_usage_html()
