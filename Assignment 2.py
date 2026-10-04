def report_header(func):
    def wrapper(*args, **kwargs):
        print("-" * 55)
        print("MONTHLY REPORT")
        print("-" * 55)

        func(*args, **kwargs)

        print("-" * 55)
        print("REPORT COMPLETED")
        print("-" * 55)

    return wrapper


class Report:
    company_name = "TechNova Solutions Pvt. Ltd."

    def __init__(self, heading, writer):
        self.heading = heading
        self.writer = writer
        self.details = []

    def add_detail(self, text):
        self.details.append(text)

    @classmethod
    @report_header
    def show_report(cls, report):
        print("Company :", cls.company_name)
        print("Title   :", report.heading)
        print("Author  :", report.writer)
        print("Details :")

        for number, item in enumerate(report.details, 1):
            print(f"  {number}. {item}")


def assignment2():
    report = Report("Monthly Performance", "Padmaraj")
    report.add_detail("Sales increased by 12%")
    report.add_detail("New service introduced")
    Report.show_report(report)


assignment2()
