class Person:
    APPROVED_JOBS = ["Sales", "ITC", "Manager", "Teacher"]

    def __init__(self, name=None, job=None):
        # Validate job FIRST (because tests call Person(job="...") with no name)
        if job is not None and job not in Person.APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
            return

        # Validate name ONLY if provided
        if name is not None:
            if not isinstance(name, str) or len(name) == 0 or len(name) > 25:
                print("Name must be string between 1 and 25 characters.")
                return

        # Save values
        self.name = name.title() if isinstance(name, str) else name
        self.job = job

    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")
