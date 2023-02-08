import plotly.express as px
import plotly.io as io

io.renderers.default = "chrome"


cases_deaths = px.scatter(covid_table,
                          x = "total_cases",
                          y = "total_deaths",
                          trendline = "ols")
cases_deaths.show()
