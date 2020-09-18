def COVID_Analysis():
    import pandas as pd
    import datetime
    import matplotlib.pyplot as plt
    import lxml
    import numpy as np

    # Setting display options
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 10000)

    # Reading and filtering data for covid dataset
    covid = pd.read_csv("covid.csv")
    covid['deaths_per_cases'] = covid['total_deaths'] / covid['total_cases']
    covid['date'] = pd.to_datetime(covid['date'])
    covid = covid[covid['date'] == datetime.datetime(2020, 7, 25)]
    covid = covid[['location', 'deaths_per_cases']]
    covid.columns = ['Country', 'Deaths Per Cases']
    print(covid)

    # Reading healthcare index dataset
    url = 'https://www.numbeo.com/health-care/rankings_by_country.jsp'
    hlth = pd.DataFrame(columns=['Country', 'Health Care Index'])
    hlt = pd.read_html(url)
    hlt = hlt[1]
    hlt = hlt[['Country', 'Health Care Index']]
    print(hlt.head())

    # Merging datasets
    merge = hlt.merge(covid, left_on='Country', right_on='Country', how='inner')
    merge = merge.set_index('Country')
    print(merge)
    x = merge['Health Care Index']
    y = merge['Deaths Per Cases']
    y1 = y[y > 0.1].sort_values(ascending=False)
    z = merge.index

    # Plotting information into multi-graph
    plt.figure()
    ax1 = plt.subplot(131)
    ax2 = plt.subplot(132)
    ax3 = plt.subplot(133)
    ax1.scatter(x, y, s=5, c='black')
    ax1.set_title("Country Health Care Rating  \nvs Current Covid Death Rates")
    ax1.set_xlabel('Health Care Index')
    ax1.set_ylabel('% Deaths Per Cases')
    ax2.boxplot(y)
    ax2.set_title('Covid Death Rate Distribution')
    ax2.set_xticks([])
    ax2.tick_params(labelleft=False)
    ax3.bar(y1.index, y1, color='red')
    ax3.set_xlabel('Countries')
    for tick in ax3.get_xticklabels():
        tick.set_rotation(90)
    ax3.tick_params(labelleft=False)
    ax3.set_title('Countries with Highest Fatality Ratio')
    plt.show()
    plt.show()

COVID_Analysis()