"""
schemas.py: Schemas for the BiqQuery tables where the enriched data is
stored.
"""

__author__ = "Jason Wolosonovich <jason@avaland.io>"
__license__ = "BSD 3 clause"

from google.cloud import bigquery as bq

# mobile friendly test
MOBILE_FRIENDLY_SCHEMA = [
    bq.SchemaField(name="refinery_company_id",
                   field_type="string",
                   mode="required"),
    bq.SchemaField(name="refined_at",
                   field_type="timestamp",
                   mode="required"),
    bq.SchemaField(name="refined_date",
                   field_type="date",
                   mode="required"),
    bq.SchemaField(name="domain",
                   field_type="string",
                   mode="required"),
    bq.SchemaField(name="url",
                   field_type="string",
                   mode="required"),
    bq.SchemaField(name="test_results",
                   field_type="string",
                   mode="required")
]

# clearbit tag history
TAGS_HISTORY_SCHEMA = [
    bq.SchemaField(name="refinery_company_id",
                   field_type="string",
                   mode="required"),
    bq.SchemaField(name="refined_at",
                   field_type="timestamp",
                   mode="required"),
    bq.SchemaField(name="refined_date",
                   field_type="date",
                   mode="required"),
    bq.SchemaField(name="domain",
                   field_type="string",
                   mode="required"),
    bq.SchemaField(name="url",
                   field_type="string",
                   mode="required"),
    bq.SchemaField(name="tag",
                   field_type="string",
                   mode="required")
]

# clearbit tech history
TECH_HISTORY_SCHEMA = [
    bq.SchemaField(name="refinery_company_id",
                   field_type="string",
                   mode="required"),
    bq.SchemaField(name="refined_at",
                   field_type="timestamp",
                   mode="required"),
    bq.SchemaField(name="refined_date",
                   field_type="date",
                   mode="required"),
    bq.SchemaField(name="domain",
                   field_type="string",
                   mode="required"),
    bq.SchemaField(name="url",
                   field_type="string",
                   mode="required"),
    bq.SchemaField(name="tech",
                   field_type="string",
                   mode="required")
]

# crawler asset history
CRAWLER_TECH_HISTORY_SCHEMA = [
    bq.SchemaField(name="refinery_company_id",
                   field_type="string",
                   mode="required"),
    bq.SchemaField(name="refined_at",
                   field_type="timestamp",
                   mode="required"),
    bq.SchemaField(name="refined_date",
                   field_type="date",
                   mode="required"),
    bq.SchemaField(name="domain",
                   field_type="string",
                   mode="required"),
    bq.SchemaField(name="url",
                   field_type="string",
                   mode="required"),
    bq.SchemaField(name="asset",
                   field_type="string",
                   mode="required"),
    bq.SchemaField(name="type",
                   field_type="string",
                   mode="required")
]

# crawler payload
CRAWLER_SCHEMA = [
    bq.SchemaField(name="refinery_company_id",
                   field_type="string",
                   mode="required"),
    bq.SchemaField(name="refined_at",
                   field_type="timestamp",
                   mode="required"),
    bq.SchemaField(name="refined_date",
                   field_type="date",
                   mode="required"),
    bq.SchemaField(name="refinery_person_id",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="sfdc_lead_id",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="sfdc_contact_id",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="sfdc_asset_id",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="domain",
                   field_type="string",
                   mode="required"),
    bq.SchemaField(name="url",
                   field_type="string",
                   mode="required"),
    bq.SchemaField(name="all_links",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="internal_links",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="external_links",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="href_emails",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="href_phones",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="href_socials",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="meta_keywords",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="meta_description",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="tier1_classification",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="tier2_classification",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="tier3_classification",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="classification_likelihood",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="html_string",
                   field_type="string",
                   mode="nullable"),
]

# clearbit person
CLEARBIT_PERSON_SCHEMA = [
    bq.SchemaField(name="refinery_person_id",
                   field_type="string",
                   mode="required"),
    bq.SchemaField(name="refined_at",
                   field_type="timestamp",
                   mode="required"),
    bq.SchemaField(name="refined_date",
                   field_type="date",
                   mode="required"),
    bq.SchemaField(name="refinery_company_id",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="sfdc_lead_id",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="sfdc_contact_id",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="sfdc_asset_id",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="domain",
                   field_type="string",
                   mode="required"),
    bq.SchemaField(name="url",
                   field_type="string",
                   mode="required"),
    bq.SchemaField(name="clearbit_person_id",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="clearbit_indexed_at",
                   field_type="timestamp",
                   mode="nullable"),
    bq.SchemaField(name="full_name",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="first_name",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="last_name",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="email",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="location",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="time_zone",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="utc_offset",
                   field_type="integer",
                   mode="nullable"),
    bq.SchemaField(name="city",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="state",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="state_code",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="country",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="country_code",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="latitude",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="longitude",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="bio",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="site",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="avatar",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="employment_domain",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="employment_name",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="employment_title",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="employment_role",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="employment_seniority",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="facebook_handle",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="github_handle",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="github_avatar",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="github_company",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="github_blog",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="github_followers",
                   field_type="integer",
                   mode="nullable"),
    bq.SchemaField(name="github_following",
                   field_type="integer",
                   mode="nullable"),
    bq.SchemaField(name="twitter_handle",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="twitter_id",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="twitter_bio",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="twitter_followers",
                   field_type="integer",
                   mode="nullable"),
    bq.SchemaField(name="twitter_following",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="twitter_location",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="twitter_site",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="twitter_avatar",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="linkedin_handle",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="googleplus_handle",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="gravatar_handle",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="gravatar_url_titles",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="gravatar_urls",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="gravatar_avatar",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="gravatar_avatar_types",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="gravatar_avatar_urls",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="fuzzy_match",
                   field_type="boolean",
                   mode="nullable"),
    bq.SchemaField(name="is_email_provider",
                   field_type="string",
                   mode="nullable")
]

# clearbit company
CLEARBIT_COMPANY_SCHEMA = [
    bq.SchemaField(name="refinery_company_id",
                   field_type="string",
                   mode="required"),
    bq.SchemaField(name="refined_at",
                   field_type="timestamp",
                   mode="required"),
    bq.SchemaField(name="refined_date",
                   field_type="date",
                   mode="required"),
    bq.SchemaField(name="refinery_person_id",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="sfdc_lead_id",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="sfdc_contact_id",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="sfdc_asset_id",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="domain",
                   field_type="string",
                   mode="required"),
    bq.SchemaField(name="url",
                   field_type="string",
                   mode="required"),
    bq.SchemaField(name="clearbit_company_id",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="clearbit_indexed_at",
                   field_type="timestamp",
                   mode="nullable"),
    bq.SchemaField(name="company_name",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="legal_name",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="company_domain",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="domain_aliases",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="phone_numbers",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="email_addresses",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="industry",
                   field_type="integer",
                   mode="nullable"),
    bq.SchemaField(name="industry_group",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="sub_industry",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="sector",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="sic_code",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="naics_code",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="description",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="year_founded",
                   field_type="integer",
                   mode="nullable"),
    bq.SchemaField(name="location",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="street_number",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="street_name",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="sub_premise",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="city",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="state",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="state_code",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="postal_code",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="country",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="country_code",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="latitude",
                   field_type="float",
                   mode="nullable"),
    bq.SchemaField(name="longitude",
                   field_type="float",
                   mode="nullable"),
    bq.SchemaField(name="time_zone",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="utc_offset",
                   field_type="integer",
                   mode="nullable"),
    bq.SchemaField(name="company_phone",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="number_of_employees",
                   field_type="integer",
                   mode="nullable"),
    bq.SchemaField(name="number_of_employees_range",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="fiscal_year_ends",
                   field_type="integer",
                   mode="nullable"),
    bq.SchemaField(name="market_cap",
                   field_type="integer",
                   mode="nullable"),
    bq.SchemaField(name="total_raised",
                   field_type="integer",
                   mode="nullable"),
    bq.SchemaField(name="company_type",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="ticker_symbol",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="tax_ein",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="annual_revenue",
                   field_type="integer",
                   mode="nullable"),
    bq.SchemaField(name="estimated_annual_revenue",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="company_logo",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="crunchbase_handle",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="alexa_us_rank",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="alexa_global_rank",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="parent_domain",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="facebook_handle",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="facebook_likes",
                   field_type="integer",
                   mode="nullable"),
    bq.SchemaField(name="linkedin_handle",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="twitter_handle",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="twitter_avatar",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="twitter_bio",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="twitter_follower_count",
                   field_type="integer",
                   mode="nullable"),
    bq.SchemaField(name="twitter_following_count",
                   field_type="integer",
                   mode="nullable"),
    bq.SchemaField(name="twitter_id",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="twitter_location",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="twitter_site_url",
                   field_type="string",
                   mode="nullable"),
    bq.SchemaField(name="is_email_provider",
                   field_type="boolean",
                   mode="nullable"),
]