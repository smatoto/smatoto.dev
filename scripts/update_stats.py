import os
import re
from datetime import date

def update_stats():
    total_sessions = 0
    total_attendees = 0
    years_with_sessions = set()

    # Directories to scan
    years = ['2023', '2024', '2025', '2026']
    # Resolve root_dir relative to this script's location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(script_dir)

    for year in years:
        year_path = os.path.join(root_dir, 'docs', year)
        if not os.path.exists(year_path):
            continue

        for filename in os.listdir(year_path):
            if filename.endswith('.md') and filename != 'template.md':
                total_sessions += 1
                years_with_sessions.add(year)
                file_path = os.path.join(year_path, filename)

                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                        # Extract YAML front matter
                        match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
                        if match:
                            yaml_content = match.group(1)
                            # Look for attendees: [number]
                            # Since it's in a list under deliveries, we can find all occurrences
                            attendees_matches = re.findall(r'attendees:\s*(\d+)', yaml_content)
                            for count in attendees_matches:
                                total_attendees += int(count)
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    # Calculate years speaking (count of unique years with sessions)
    years_speaking = len(years_with_sessions)

    # Format the stats block
    today = date.today().isoformat()
    # Use the format requested by the user
    stats_block = f"""<!-- STATS:START -->
- **Total Sessions:** {total_sessions}
- **Total Developers Reached:** {total_attendees:,}+
- **Last Updated:** {today}
<!-- STATS:END -->"""

    # Update docs/index.md
    readme_path = os.path.join(root_dir, 'docs', 'index.md')
    if os.path.exists(readme_path):
        try:
            with open(readme_path, 'r', encoding='utf-8') as f:
                readme_content = f.read()

            # Update the markdown stats block
            new_readme_content = re.sub(
                r'<!-- STATS:START -->.*?<!-- STATS:END -->',
                stats_block,
                readme_content,
                flags=re.DOTALL
            )

            # Update the stat card for Sessions
            new_readme_content = re.sub(
                r'(<div class="stat-number">)\d+(<\/div>\s*<div class="stat-label">Sessions<\/div>)',
                r'\g<1>' + str(total_sessions) + r'\g<2>',
                new_readme_content
            )

            # Update the stat card for Developers Reached (with or without + symbol)
            new_readme_content = re.sub(
                r'(<div class="stat-number">)[0-9,]+\+?(<\/div>\s*<div class="stat-label">Developers Reached<\/div>)',
                r'\g<1>' + f'{total_attendees:,}+' + r'\g<2>',
                new_readme_content
            )

            # Update the stat card for Years Speaking
            new_readme_content = re.sub(
                r'(<div class="stat-number">)\d+(<\/div>\s*<div class="stat-label">Years Speaking<\/div>)',
                r'\g<1>' + str(years_speaking) + r'\g<2>',
                new_readme_content
            )

            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(new_readme_content)
            print(f"Successfully updated docs/index.md with {total_sessions} sessions, {total_attendees} attendees, and {years_speaking} years speaking.")
        except Exception as e:
            print(f"Error updating docs/index.md: {e}")
    else:
        print(f"docs/index.md not found at {readme_path}")

if __name__ == "__main__":
    update_stats()
