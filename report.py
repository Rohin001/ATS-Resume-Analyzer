def generate_report(results):

    report = f"""
ATS RESUME ANALYSIS REPORT
=========================

ATS Score: {results['score']}/100

Detected Skills:
{chr(10).join(results['skills'])}

Suggestions:
{chr(10).join(results['suggestions'])}
"""

    return report