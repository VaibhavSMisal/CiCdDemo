import sys
def generate_cache_usage_html():
    html = "<html>"
    html += "<body><h1>Performance Profiling</h1><details><summary><h2 style=\"display:inline;\">Cache Memory Usage</h2></summary>"
    current_module = None
    
    for line in table_list:
        if "CacheSize:" in line:
            # Extract module name from the line
            module = line.split("#")[0].split(":")[-1].strip()
            # If the module changes, print it and the header
            if current_module != module:
                if current_module != None:
                    html += "</table></details>"
                current_module = module
                html += f"<details><summary><h3 style=\"display:inline;\">{current_module}</h3></summary>"
                html += "<table><tr><th>Action in test-app</th><th>Cache usage</th></tr>"
            # Split the line by "=" to separate key and value
            key_value_pair = line.split("=")
            # Extract key and value
            key = key_value_pair[0].split(":")[-1].strip()
            value = key_value_pair[1].split()[0].strip()

            html += f"<tr><td>{key}</td><td>{value}</td></tr>"
    
    html += "</table></details></details></body></html>"

    print(f"HTML = {html}")

    with open("cache_usage_report.html", "w") as file:
        file.write(html)

logFile = open(sys.argv[1], "r")
table_data = logFile.read().strip()
logFile.close()
table_list = table_data.split('\n')
print(f"Table lines = \n{table_list}")

generate_cache_usage_html()

