import random

def enrich_data(df):
    industries = ['AI', 'FinTech', 'SaaS', 'Healthcare', 'E-Commerce']
    sizes = ['1-10', '11-50', '51-200', '201-500', '500+']
    locations = ['US', 'India', 'Germany', 'UK', 'Canada']

    df['industry'] = [random.choice(industries) for _ in range(len(df))]
    df['employee_range'] = [random.choice(sizes) for _ in range(len(df))]
    df['location'] = [random.choice(locations) for _ in range(len(df))]

    return df
