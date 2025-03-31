from loaders import get_google_drive_csv_specified_columns, get_google_drive_csv, load_json_google_drive
from cleaners import filter_us_public_stations, summarize_station_data

if __name__ == "__main__":
    keep_columns = [
        'Fuel Type Code', 'ID', 'City', 'State', 'Status Code', 'Access Days Time',
        'EV Level1 EVSE Num', 'EV Level2 EVSE Num', 'EV DC Fast Count', 'Latitude', 'Longitude',
        'Open Date', 'EV Connector Types', 'Country', 'Access Code', 'Facility Type',
        'EV Pricing', 'EV On-Site Renewable Source', 'Restricted Access', 'EV Workplace Charging'
    ]

    col_data_type = {
        'Fuel Type Code': str, 'ID': str, 'City': str, 'State': str, 'Status Code': str,
        'Access Days Time': str, 'Latitude': float, 'Longitude': float, 'Open Date': str,
        'EV Connector Types': str, 'Country': str, 'Access Code': str, 'Facility Type': str,
        'EV Pricing': str, 'EV On-Site Renewable Source': str, 'Restricted Access': str,
        'EV Workplace Charging': str
    }

    afs_df = get_google_drive_csv_specified_columns('1UhsY-GB1JwII_OnYaAB5nJSCZsbaZDdE', keep_columns, col_data_type)
    afs_us = filter_us_public_stations(afs_df)
    charge_summary = summarize_station_data(afs_us)

    ev_charting_data = load_json_google_drive('1y0Ai_KF5pF-1xqyCrjR7r8QrL_Y0gvna')
    state_abbr = get_google_drive_csv('15PZ3jX0qtQdnLd0Yi2enFTXFN31wcMs3')
    state_abbr.rename(columns={'State': 'State name', 'Abbreviation': 'state_abbr'}, inplace=True)

    charge_summary = charge_summary.rename(columns={'State': 'state_abbr'})
    charge_summary = charge_summary.merge(state_abbr, how='left', on='state_abbr')

    state_coords = get_google_drive_csv('1uM_0XCsZUa8vufOrTvqQAjlh8phDy3PT')
    state_coords.rename(columns={'state': 'State name'}, inplace=True)

    charge_summary = charge_summary.merge(state_coords, how='left', on='State name')
    charge_summary.describe()