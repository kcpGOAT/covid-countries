# With only pandas

import pandas as pd
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
    
# With pandas and polars

import pandas as pd
import polars as pl

covid_table = pd.DataFrame(data = covid_table, columns = ["id", "country", "total_cases", "new_cases",
                                                          "total_deaths", "new_deaths", "total_recovered",
                                                          "new_recovered", "active_cases", "active_critical_cases", 
                                                          "total_cases_per_mill", "deaths_per_mill", "total_tests",
                                                          "tests_per_mill", "population", "continent",
                                                          "1_case_per_X_ppl", "1_death_per_X_ppl", "1_test_per_X_ppl",
                                                          "new_cases_per_mill", "new_deaths_per_mill", "active_cases_per_mill"])

covid_df = pl.from_pandas(covid_table)
numeric_col = covid_df.drop(columns = ["country", "continent"]).columns

covid_df = (
    covid_df.lazy()
    .select(
        pl.when(pl.col(pl.Utf8).is_in(["N/A", ""])).then(None).otherwise(pl.col(pl.Utf8)).keep_name()
    )
    .drop(columns = list(covid_table.filter(regex = "new|X")))
    .drop_nulls()
    .with_columns(pl.col(pl.Utf8).str.replace_all(",", ""))
    .with_columns(pl.col(numeric_col).cast(pl.Float64))
)
