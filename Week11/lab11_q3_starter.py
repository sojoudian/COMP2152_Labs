class Report:
    def __init__(self, team_name):
        self.team_name = team_name
        self.findings = []

    def add_finding(self, finding):
        self.findings.append(finding)
        print(f"  Added: {finding}")

    def get_by_severity(self, severity):
        # List comprehension to filter the findings list
        return [f for f in self.findings if f.severity == severity]

    def summary(self):
        print(f"  Team: {self.team_name}")
        print(f"  Total findings: {len(self.findings)}")
        
        # Pull counts based on severity
        print(f"  HIGH:   {len(self.get_by_severity('HIGH'))}")
        print(f"  MEDIUM: {len(self.get_by_severity('MEDIUM'))}")
        print(f"  LOW:    {len(self.get_by_severity('LOW'))}")
        print("-" * 40)
        
        # Python automatically calls __str__ for each 'f'
        for f in self.findings:
            print(f"  {f}")
