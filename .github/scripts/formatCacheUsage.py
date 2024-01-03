import sys
def generate_cache_usage_html():
    html = "<html>"
    html += "<body><h1>Performance Profiling</h1><details><summary style='padding:0px;'><h3 style='display:inline;'>Cache Memory Usage</h3></summary><ul>"
    current_module = table_list[0].split("#")[0].split(":")[-1]
    html += f"<li><details><summary style='padding:0px;'><h3 style='display:inline;'>{current_module}</h3></summary>" \
            "<table><tr><th>Action in test-app</th><th>Cache usage</th></tr>"
    
    for line in table_list:
        if "CacheSize:" in line:
            # Split the line by "," to separate key and value
            key_value_pair = line.split(",")
            # Extract key and value
            key = key_value_pair[0].split(":")[-1]
            value = key_value_pair[1].split()[0]

            html += f"<tr><td>{key}</td><td>{value[0:-1]} KB</td></tr>"
    
    html += "</table></details></li></ul></details></body></html>"

    print(f"HTML = {html}")

    with open("cache_usage_report.html", "w") as file:
        file.write(html)

logFile = open(sys.argv[1], "r")
table_data = logFile.read().strip()
logFile.close()
table_list = table_data.split('\n')
print(f"Table lines = \n{table_list}")

generate_cache_usage_html()

