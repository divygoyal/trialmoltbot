import json
import os

def analyze_gsc(file_path):
    # Try multiple paths for robustness during development
    paths_to_check = [file_path, os.path.join(os.path.dirname(__file__), "..", file_path), "gsc_data.json"]
    
    data = None
    for p in paths_to_check:
        if os.path.exists(p):
            with open(p, 'r') as f:
                data = json.load(f)
            break
            
    if data is None:
        raise FileNotFoundError(f"Could not find GSC data file in {paths_to_check}")
    
    recommendations = []
    for entry in data:
        query = entry['query']
        pos = entry['position']
        ctr = entry['ctr']
        imp = entry['impressions']
        
        if 11 <= pos <= 20:
            recommendations.append({
                "type": "STRIKING_DISTANCE",
                "query": query,
                "current_pos": pos,
                "impact": "HIGH",
                "suggestion": f"Keywords '{query}' is on Page 2 (Pos {pos:.1f}). Add this to an H2 tag."
            })
        if pos < 10 and ctr < 0.02:
            recommendations.append({
                "type": "CTR_HEALER",
                "query": query,
                "current_ctr": f"{ctr*100:.1f}%",
                "impact": "MEDIUM",
                "suggestion": f"High impressions ({imp}) for '{query}' but low CTR. Rewrite the Title."
            })
            
    return recommendations
