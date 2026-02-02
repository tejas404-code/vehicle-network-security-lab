def detect_unknown_ids(df, baseline_ids):
    return df[~df['can_id'].isin(baseline_ids)]
