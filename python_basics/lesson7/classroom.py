# my_dict = {
#     "apple": "olma",
#     "ism": "ali",
#     "yoshi": 18,
#     "username": "ali",
#     1: "bir",
#     True: "true",
#     2.3: "ikki butun uch",
#     (1, 2, 3, 4): "Tuple"
#     #[1, 2, 3]: "listda ishlamaydi"
#     #{"simpl": "oddiy"}: "dict ishlamaydi"
# }

# print(my_dict[(1, 2, 3, 4)])

# my_dict["apple"] = "Bu olma hisoblanadi."


# for key in my_dict:
#     print(f"{key}: {my_dict[key]}")



# my_self_dict = {
#     "ism": "Elmurod",
#     "togilgan yil": 2005,
#     "yosh": 20
# }

dict1 = {
  "id": 390491994,
  "parent_id": 390491994,
  "created_at": "2017-07-24T08:36:51.000Z",
  "updated_at": "2025-12-01T05:24:46.222410Z",
  "checked_at": "2025-12-01T05:24:46.222410Z",
  "changed_at": "2025-12-01T05:24:46.222410Z",
  "experience_change_last_identified_at": None,
  "is_deleted": 0,
  "is_parent": 1,
  "public_profile_id": 551832805,
  "linkedin_url": "https://www.linkedin.com/in/jessie-liauw-a-fong-831983134",
  "linkedin_shorthand_names": [
    "jcb-liauw-a-fong",
    "jessie-liauw-a-fong-831983134"
  ],
  "historical_ids": [
    390491994
  ],
  "full_name": "Jessie Liauw A Fong",
  "first_name": "Jessie",
  "first_name_initial": "J",
  "middle_name": "Liauw A",
  "middle_name_initial": "L",
  "last_name": "Fong",
  "last_name_initial": "F",
  "headline": "Full stack developer",
  "summary": None,
  "picture_url": "https://media.licdn.com/dms/image/v2/D4E03AQF100dDA61SLw/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1727001238451?e=2147483647&v=beta&t=0sTUvW1-9TYr3d_oJWfl9x95yuEw0xKZyhKI5xyQnz4",
  "location_country": "Netherlands",
  "location_country_iso2": "NL",
  "location_country_iso3": "NLD",
  "location_full": "Amsterdam, North Holland, Netherlands",
  "location_regions": [
    "Europe",
    "Western Europe",
    "EMEA",
    "EU"
  ],
  "location_city": "Amsterdam",
  "location_state": "North Holland",
  "interests": [],
  "inferred_skills": [
    "software",
    "devops",
    "technology"
  ],
  "historical_skills": [
    "microsoft office",
    "javascript",
    "jquery",
    "scrum",
    "json",
    "es6",
    "kotlin",
    "mysql",
    "customer service",
    "html",
    "java",
    "nuxtjs",
    "vuejs",
    "python",
    "php",
    "cascading style sheets (css)",
    "git",
    "web development"
  ],
  "connections_count": 469,
  "followers_count": 477,
  "services": None,
  "primary_professional_email": None,
  "primary_professional_email_status": None,
  "professional_emails_collection": [],
  "is_working": 1,
  "active_experience_company_id": 8697858,
  "active_experience_title": "Software Engineer",
  "active_experience_description": None,
  "active_experience_department": "Engineering and Technical",
  "active_experience_management_level": "Specialist",
  "is_decision_maker": 0,
  "total_experience_duration_months": 93,
  "total_experience_duration_months_breakdown_department": [
    {
      "department": "Engineering and Technical",
      "total_experience_duration_months": 113
    },
    {
      "department": "C-Suite",
      "total_experience_duration_months": 37
    }
  ],
  "total_experience_duration_months_breakdown_management_level": [
    {
      "management_level": "Intern",
      "total_experience_duration_months": 4
    },
    {
      "management_level": "Founder",
      "total_experience_duration_months": 29
    },
    {
      "management_level": "C-Level",
      "total_experience_duration_months": 8
    },
    {
      "management_level": "Specialist",
      "total_experience_duration_months": 105
    }
  ],
  "experience": 
    {
      "active_experience": 1,
      "position_title": "Software Engineer",
      "department": "Engineering and Technical",
      "management_level": "Specialist",
      "location": "Amsterdam, North Holland, Netherlands",
      "description": None,
      "date_from": "January 2024",
      "date_from_year": 2024,
      "date_from_month": 1,
      "date_to": None,
      "date_to_year": None,
      "date_to_month": None,
      "duration_months": 23,
      "company_id": 8697858,
      "company_name": "Aareon NL",
      "company_type": "Privately Held",
      "company_founded_year": 1979,
      "company_followers_count": 4603,
      "company_website": "https://www.aareon.nl",
      "company_facebook_url": [
        "https://www.facebook.com/aareon-353807094777486"
      ],
      "company_twitter_url": [
        "https://www.twitter.com/aareonnl"
      ],
      "company_linkedin_url": "https://www.linkedin.com/company/aareon-nl",
    }

}


empty_keys = []
for key in dict1:
    if not dict1[key]:
        empty_keys[key] = "Bu bo'sh"

print(empty_keys)
print(len(empty_keys))










