import plotly.express as px
import plotly.io as io

io.renderers.default = "chrome"

cases_deaths = px.scatter(covid_table,
                          x = "total_cases",
                          y = "total_deaths",
                          trendline = "ols")
cases_deaths.show()

tests_cases = px.scatter(covid_table,
                         x = "total_tests",
                         y = "total_cases",
                         trendline = "ols")
tests_cases.show()

hist_cases_per_mill = px.histogram(covid_table, 
                                   x = "total_cases_per_mill")
hist_cases_per_mill.show()

