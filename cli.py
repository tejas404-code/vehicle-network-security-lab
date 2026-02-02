from ingest import load_can_log
from profile import profile_ids
from anomaly import detect_unknown_ids
from rules import apply_rules

baseline = load_can_log('data/baseline_can_log.csv')
test = load_can_log('data/sample_can_log.csv')

baseline_ids = profile_ids(baseline).index
anomalies = detect_unknown_ids(test, baseline_ids)
alerts = apply_rules(anomalies)

print(alerts)
