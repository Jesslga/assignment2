"""Cleans the Data"""
def filter_us_public_stations(df):
    """Filters the Data to only include US Public Stations"""
    return df[(df['Country'] == 'US') | (df['EV Workplace Charging'] == "False")]

def summarize_station_data(df):
    """Summarizes the Station Data"""
    summary = df.groupby('State').agg(
        num_EV_charge_stations=('ID', 'count'),
        num_EV_Level1=('EV Level1 EVSE Num', 'sum'),
        num_EV_Level2=('EV Level2 EVSE Num', 'sum'),
        num_EV_DC_Fast=('EV DC Fast Count', 'sum')
    )
    summary['num_Total_EV_Ports'] = (
        summary['num_EV_Level1'] + summary['num_EV_Level2'] + summary['num_EV_DC_Fast']
    )
    summary['Avg_Ports per Station'] = (
        summary['num_Total_EV_Ports'] / summary['num_EV_charge_stations']
    )
    summary.reset_index(inplace=True)
    return summary
