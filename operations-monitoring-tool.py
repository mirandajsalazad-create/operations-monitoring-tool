
def collect_incidents():
    """Collect incident data from the user and return a list of incidents."""
    incidents = []
    total_incidents = int(input("How many incidents do you want to enter? "))

    for _ in range(total_incidents):
        name = input("Enter system name: ")
        issue = input("Enter issue description: ")
        severity = input("Enter severity (low / medium / high): ").lower()
        downtime = int(input("Enter downtime in minutes: "))
        resolved = input("Is the incident resolved? (yes/no): ").lower()

        incident = {
            "name": name,
            "issue": issue,
            "severity": severity,
            "downtime": downtime,
            "resolved": resolved
        }

        incidents.append(incident)

    return incidents


def analyze_incidents(incidents):
    """Analyze incident data and return summary statistics and open incidents."""
    total_incidents = len(incidents)
    unresolved_incidents = 0
    high_severity = 0
    total_downtime = 0
    open_incidents = []

    for incident in incidents:
        total_downtime += incident["downtime"]

        if incident["severity"] == "high":
            high_severity += 1

        if incident["resolved"] == "no":
            unresolved_incidents += 1
            open_incidents.append(incident)

    average_downtime = total_downtime / total_incidents if total_incidents > 0 else 0

    stats = {
        "total_incidents": total_incidents,
        "unresolved_incidents": unresolved_incidents,
        "high_severity_incidents": high_severity,
        "average_downtime": average_downtime
    }

    return stats, open_incidents


def print_report(stats, open_incidents):
    """Print the operations status report."""
    print("\n=== OPERATIONS STATUS REPORT ===")
    print(f"Total Incidents: {stats['total_incidents']}")
    print(f"Open Incidents: {stats['unresolved_incidents']}")
    print(f"High Severity Incidents: {stats['high_severity_incidents']}")
    print(f"Average Downtime: {stats['average_downtime']:.1f} minutes")

    if not open_incidents:
        print("\nNo open incidents 🎉")
        return

    print()
    for incident in open_incidents:
        if incident["severity"] == "high":
            icon = "🚨"
        elif incident["severity"] == "medium":
            icon = "⚠️"
        else:
            icon = "ℹ️"

        print(
            f"{icon} {incident['name']} | "
            f"{incident['issue']} | "
            f"{incident['severity']} | "
            f"{incident['downtime']} min"
        )


def main():
    incidents = collect_incidents()
    stats, open_incidents = analyze_incidents(incidents)
    print_report(stats, open_incidents)


main()











