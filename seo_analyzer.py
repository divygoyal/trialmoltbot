import json

def analyze_gsc(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    recommendations = []
    
    for entry in data:
        query = entry['query']
        pos = entry['position']
        ctr = entry['ctr']
        imp = entry['impressions']
        
        # 1. Striking Distance Logic (Positions 11-20)
        if 11 <= pos <= 20:
            recommendations.append({
                "type": "STRIKING_DISTANCE",
                "query": query,
                "current_pos": pos,
                "impact": "HIGH",
                "suggestion": f"Keywords '{query}' is on Page 2 (Pos {pos:.1f}). Add this to an H2 tag and internal links to push to Page 1."
            })
            
        # 2. CTR Healer Logic (Pos < 10 but CTR < 2%)
        if pos < 10 and ctr < 0.02:
            recommendations.append({
                "type": "CTR_HEALER",
                "query": query,
                "current_ctr": f"{ctr*100:.1f}%",
                "impact": "MEDIUM",
                "suggestion": f"High impressions ({imp}) for '{query}' but low CTR. Rewrite the Meta Title to be more 'clicky'."
            })
            
    return recommendations

if __name__ == "__main__":
    results = analyze_gsc('gsc_data.json')
    print(json.dumps(results, indent=2))
