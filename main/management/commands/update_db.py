from django.core.management.base import BaseCommand
from main.models import Projects
import requests

def fetch_projects():
    url= f"https://search.worldbank.org/api/v2/projects?format=json&rows=200&fct=projectfinancialtype_exact,status_exact,regionname_exact,themev2_level1_exact,themev2_level2_exact,themev2_level3_exact,sector_exact,countryshortname_exact,cons_serv_reqd_ind_exact,esrc_ovrl_risk_rate_exact&fl=id,regionname,countryname,projectstatusdisplay,project_name,countryshortname,pdo,impagency,cons_serv_reqd_ind,url,boardapprovaldate,closingdate,projectfinancialtype,curr_project_cost,ibrdcommamt,idacommamt,totalamt,grantamt,borrower,lendinginstr,envassesmentcategorycode,esrc_ovrl_risk_rate,sector1,sector2,sector3,theme1,theme2,%20%20status,totalcommamt,proj_last_upd_date,curr_total_commitment,curr_ibrd_commitment,curr_ida_commitment,last_stage_reached_name,theme_list,ida_cmt_usd_amt,cmt_usd_amt,projectcost&apilang=en&os=0"
    response = requests.get(url)
    obj = response.json()

    all_data = Projects.objects.all()
    # print(f"Before {all_data.count()}")
    all_data.delete()
    # print(f"AfterDelete {Projects.objects.all().count()}")
    

    for project in obj['projects']:
        project_dict = obj['projects'][project]

        prj_id = project_dict['id']
        title = project_dict['project_name']
        date = project_dict['proj_last_upd_date']
        status = project_dict['projectstatusdisplay']
        sector = project_dict['lendinginstr']
        location = project_dict['regionname']
        amount = project_dict['curr_total_commitment']

        Projects.objects.create(
            project_id=prj_id,
            title=title,
            date=date,
            status=status,
            sector=sector,
            location=location,
            amount=amount
            )
    
    # print(f'After Create: {Projects.objects.all().count()}')


class Command(BaseCommand):

    def handle(self, *args, **options):
        fetch_projects()
        # print(f'Done: {Projects.objects.all().count()}')

