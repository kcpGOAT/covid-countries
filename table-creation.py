covid_table = pd.DataFrame(data = covid_table, columns = ["id", "country", "total_cases", "new_cases",
                                                          "total_deaths", "new_deaths", "total_recovered",
                                                          "new_recovered", "active_cases", "active_critical_cases", 
                                                          "total_cases_per_mill", "deaths_per_mill", "total_tests",
                                                          "tests_per_mill", "population", "continent",
                                                          "1_case_per_X_ppl", "1_death_per_X_ppl", "1_test_per_X_ppl",
                                                          "new_cases_per_mill", "new_deaths_per_mill", "active_cases_per_mill"])
covid_table = covid_table.iloc[9:]
covid_table.index = [""] * len(covid_table)
covid_table = (
        covid_table
        .drop(columns = list(covid_table.filter(regex = "new|X")))
        .replace(['', "N/A"], pd.NA)
        .dropna()
        .apply(lambda x: x.str.replace(',', ''))
    )
numeric_cols = covid_table.drop(columns = ["country", "continent"]).columns
for i in numeric_cols:
    covid_table[i] = covid_table[i].astype(float)
