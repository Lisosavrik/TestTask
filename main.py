import requests


def parsing_page():
    url= f"https://search.worldbank.org/api/v2/projects?format=json&rows=200&fct=projectfinancialtype_exact,status_exact,regionname_exact,themev2_level1_exact,themev2_level2_exact,themev2_level3_exact,sector_exact,countryshortname_exact,cons_serv_reqd_ind_exact,esrc_ovrl_risk_rate_exact&fl=id,regionname,countryname,projectstatusdisplay,project_name,countryshortname,pdo,impagency,cons_serv_reqd_ind,url,boardapprovaldate,closingdate,projectfinancialtype,curr_project_cost,ibrdcommamt,idacommamt,totalamt,grantamt,borrower,lendinginstr,envassesmentcategorycode,esrc_ovrl_risk_rate,sector1,sector2,sector3,theme1,theme2,%20%20status,totalcommamt,proj_last_upd_date,curr_total_commitment,curr_ibrd_commitment,curr_ida_commitment,last_stage_reached_name,theme_list,ida_cmt_usd_amt,cmt_usd_amt,projectcost&apilang=en&os=0"
    response = requests.get(url)
    obj = response.json()
    for project in obj['projects']:
        project_dict = obj['projects'][project]
        prj_id = project_dict['id']
        title = project_dict['project_name']
        location = project_dict['regionname']
        status = project_dict['projectstatusdisplay']
        date = project_dict['proj_last_upd_date']
        amount = project_dict['curr_total_commitment']
        # prj_type = project_dict['projectfinancialtype']
        sector = project_dict['lendinginstr']

        print( prj_id, title, location, status, date, amount, sector)
        
# prj_id,title, location, status, date, amount,
parsing_page()


