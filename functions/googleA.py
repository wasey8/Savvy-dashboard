from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange
from google.analytics.data_v1beta.types import Dimension
from google.analytics.data_v1beta.types import Metric
from google.analytics.data_v1beta.types import RunRealtimeReportRequest,RunReportResponse,RunReportRequest



def sample_run_report(property_id):
    client = BetaAnalyticsDataClient()

    request = RunRealtimeReportRequest(
        property=f"properties/{property_id}",
        metrics=[Metric(name="activeUsers")]
    )
    response = client.run_realtime_report(request)

    response=str(response)
    response=response.replace('row_count: 1','').replace('metric_headers','').replace('kind: "analyticsData#runRealtimeReport"','').replace('{','').replace('}','').replace('metric_values ','').replace(' type_: TYPE_INTEGER','').replace('  name: "activeUsers"','').replace('rows ','').replace('value','').replace(':','').replace('"','')
    response=response.strip()
    if response:
        return (str(response))
    else:
        return str(0)


def sample_run_report_crash(property_id="YOUR-GA4-PROPERTY-ID"):
    client = BetaAnalyticsDataClient()

    request = RunReportRequest(
        property=f"properties/{property_id}",
        metrics=[Metric(name="crashFreeUsersRate")],
        date_ranges=[DateRange(start_date="2020-03-31", end_date="today")],


    )
    response = client.run_report(request)
    response=str(response)
    response=response.replace('row_count: 1','').replace('metric_headers','').replace('kind: "  name crashFreeUsersRate"','').replace('{','').replace('}','').replace('metric_values ','').replace(' type_: TYPE_INTEGER','').replace('  name: "activeUsers"','').replace('rows ','').replace('value','').replace(':','').replace('"','').replace('kind analyticsData#runReport','').replace('time_zone America/Los_Angeles','').replace('  currency_code USD','').replace('metadata','').replace('name crashFreeUsersRate','')
    return (int(response))

   

def sample_run_report_lastDay(property_id="YOUR-GA4-PROPERTY-ID"):
    client = BetaAnalyticsDataClient()

    request = RunReportRequest(
        property=f"properties/{property_id}",
        metrics=[Metric(name="active1DayUsers")],
        date_ranges=[DateRange(start_date="yesterday", end_date="today")],


    )
    response = client.run_report(request)
    response=str(response)
    response=response.replace('row_count: 1','').replace('metric_headers','').replace('kind: "  name crashFreeUsersRate"','').replace('{','').replace('}','').replace('metric_values ','').replace(' type_: TYPE_INTEGER','').replace('  name: "activeUsers"','').replace('rows ','').replace('value','').replace(':','').replace('"','').replace('kind analyticsData#runReport','').replace('time_zone America/Los_Angeles','').replace('  currency_code USD','').replace('metadata','').replace('name crashFreeUsersRate','').replace('name active1DayUsers','')
    return int(response)




