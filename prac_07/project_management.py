import datetime
from project import Project

FILENAME = 'projects.txt'

def load_projects(filename=FILENAME):
    """Load projects from a file."""
    projects = []
    with open(filename, 'r') as file:
        file.readline()  # skip the header
        for line in file:
            parts = line.strip().split('\t')
            project = Project(*parts)
            projects.append(project)
    return projects


def save_projects(projects, filename=FILENAME):
    """Save projects to a file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                       f"{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    """Display all projects, separated by completion status."""
    incomplete = [project for project in projects if not project.is_complete()]
    complete = [project for project in projects if project.is_complete()]

    print("Incomplete projects:")
    for project in sorted(incomplete):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted(complete):
        print(f"  {project}")


def filter_projects_by_date(projects, date_string):
    """Filter projects by start date."""
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date > date]
    for project in sorted(filtered_projects, key=lambda p: p.start_date):
        print(project)


def add_new_project(projects):
    """Add a new project to the list."""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: ")
    completion_percentage = input("Percent complete: ")
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)


def update_project(projects):
    """Update an existing project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = int(input("Project choice: "))
    chosen_project = projects[project_choice]
    print(chosen_project)
    completion_percentage = input("New Percentage: ")
    priority = input("New Priority: ")
    chosen_project.update(completion_percentage or None, priority or None)

def main():
    """Main function to run the project management program."""
    projects = load_projects()

    MENU = """
    - (L)oad projects  
    - (S)ave projects  
    - (D)isplay projects  
    - (F)ilter projects by date
    - (A)dd new project  
    - (U)pdate project
    - (Q)uit
    """

    print("Welcome to Pythonic Project Management")
    while True:
        print(MENU)
        choice = input(">>> ").lower()
        if choice == 'l':
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Filename: ")
            save_projects(projects, filename)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date_string = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, date_string)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save = input(f"Would you like to save to {FILENAME}? (yes/no): ").lower()
            if save == 'yes':
                save_projects(projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()
