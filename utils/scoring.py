def score_leads(df):
    def score(row):
        score = 0
        if row['industry'] in ['AI', 'SaaS']: score += 4
        if row['employee_range'] in ['11-50', '51-200']: score += 3
        if row['location'] == 'US': score += 2
        return score

    df['score'] = df.apply(score, axis=1)
    return df
