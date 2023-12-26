import sys
def generate_cache_usage_html():
    html = "<html>"
    html += "<body><h1>Bidder Token Generation Time</h1>"
    html += "<table>"
    html += f"<tr><th>App Startup Mode</th><th>Valid Bidder Token in Cache</th><th>Generation time (90th percentile)</th></tr>"

    for i in range(0, len(table_list), 3):
        html += f"<tr><td>{table_list[i]}</td>" \
                f"<td>{table_list[i+1]}</td>" \
                f"<td>{format_time(table_list[i+2])}</td></tr>"

    html += "</table>"
    html += "<br><i>*refer all the App Startup modes <a href='https://developer.android.com/topic/performance/vitals/launch-time#startup-state'>here</a>.</i>"
    html += "</body></html>"

    with open("token_gen_time_report.html", "w") as file:
        file.write(html)

def format_time(time):
        return f"{time} sec"

table_data = sys.argv[1]
table_list = table_data.split(",")

generate_cache_usage_html()