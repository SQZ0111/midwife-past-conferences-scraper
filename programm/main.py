from web_utils import fetch_past_conferences_page,get_soup_from_url,extract_conference_details
from data_storage import save_to_csv

def main():
    # Fetch the past conferences page URL using Selenium
    past_conferences_url = fetch_past_conferences_page()
    
    # Get the soup of the page
    html_soup = get_soup_from_url(past_conferences_url)
    
    # Extract conference details
    years = html_soup.find_all('h3')
    conferences_list = []
    for year in years:
        default_time = year.get_text()
        ul_tag = year.find_next('ul')
        for li in ul_tag.find_all('li'):
            conference_detail = extract_conference_details(li, default_time)
            if conference_detail:  # Check if the details are not None
                conferences_list.append(conference_detail)
    
    
    # Save the data to a CSV file
    save_to_csv(conferences_list, '../data/conferences.csv')
    


if __name__ == "__main__":
    main()
    
