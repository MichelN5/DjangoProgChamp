from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from Challenges.models import Category, Challenge


class Command(BaseCommand):
    help = "Seed starter ProgChamp categories and challenges."

    def handle(self, *args, **options):
        author, _ = User.objects.get_or_create(
            username="seed_admin",
            defaults={"email": "seed@example.com", "is_staff": True, "is_superuser": True},
        )
        author.is_staff = True
        author.is_superuser = True
        author.set_password("admin12345")
        author.save()

        python, _ = Category.objects.update_or_create(
            id=1,
            defaults={"CategoryName": "PY", "slug": "python"},
        )
        Category.objects.update_or_create(
            id=2,
            defaults={"CategoryName": "JS", "slug": "javascript"},
        )
        cpp, _ = Category.objects.update_or_create(
            id=3,
            defaults={"CategoryName": "C++", "slug": "cpp"},
        )

        challenges = [
            {
                "category": python,
                "slug": "hello-world",
                "title": "Hello World",
                "description": "Write a function named hello_world that prints or returns the string Hello World.",
                "solution": "def hello_world():\n    print(\"Hello World\")",
                "default_code": "def hello_world():\n    # write your code here\n    pass",
                "tests": (
                    "import contextlib\n"
                    "import io\n"
                    "_output = io.StringIO()\n"
                    "with contextlib.redirect_stdout(_output):\n"
                    "    _result = hello_world()\n"
                    "assert _result == \"Hello World\" or _output.getvalue().strip() == \"Hello World\"\n"
                    "print(\"All checks passed.\")"
                ),
            },
            {
                "category": python,
                "slug": "add-two-numbers",
                "title": "Add Two Numbers",
                "description": "Write a function named add that returns the sum of two numbers.",
                "solution": "def add(a, b):\n    return a + b",
                "default_code": "def add(a, b):\n    # write your code here\n    pass",
                "tests": "assert add(2, 3) == 5\nassert add(-1, 4) == 3\nprint(\"All checks passed.\")",
            },
            {
                "category": python,
                "slug": "is-even",
                "title": "Is Even",
                "description": "Write a function named is_even that returns True when a number is even.",
                "solution": "def is_even(number):\n    return number % 2 == 0",
                "default_code": "def is_even(number):\n    # write your code here\n    pass",
                "tests": "assert is_even(2) is True\nassert is_even(7) is False\nprint(\"All checks passed.\")",
            },
            {
                "category": cpp,
                "slug": "cpp-hello-world",
                "title": "C++ Hello World",
                "description": "Write a function named hello_world that returns the string Hello World.",
                "solution": "#include <string>\nstd::string hello_world() {\n    return \"Hello World\";\n}",
                "default_code": "#include <string>\nstd::string hello_world() {\n    // write your code here\n    return \"\";\n}",
                "tests": (
                    "#include <cassert>\n#include <iostream>\nint main() {\n"
                    "    assert(hello_world() == \"Hello World\");\n"
                    "    std::cout << \"All checks passed.\\n\";\n    return 0;\n}"
                ),
            },
            {
                "category": cpp,
                "slug": "cpp-add-two-numbers",
                "title": "C++ Add Two Numbers",
                "description": "Write a function named add that returns the sum of two integers.",
                "solution": "int add(int a, int b) {\n    return a + b;\n}",
                "default_code": "int add(int a, int b) {\n    // write your code here\n    return 0;\n}",
                "tests": (
                    "#include <cassert>\n#include <iostream>\nint main() {\n"
                    "    assert(add(2, 3) == 5);\n    assert(add(-1, 4) == 3);\n"
                    "    std::cout << \"All checks passed.\\n\";\n    return 0;\n}"
                ),
            },
            {
                "category": cpp,
                "slug": "cpp-is-even",
                "title": "C++ Is Even",
                "description": "Write a function named is_even that returns true when a number is even.",
                "solution": "bool is_even(int number) {\n    return number % 2 == 0;\n}",
                "default_code": "bool is_even(int number) {\n    // write your code here\n    return false;\n}",
                "tests": (
                    "#include <cassert>\n#include <iostream>\nint main() {\n"
                    "    assert(is_even(2) == true);\n    assert(is_even(7) == false);\n"
                    "    std::cout << \"All checks passed.\\n\";\n    return 0;\n}"
                ),
            },
        ]

        for challenge in challenges:
            Challenge.objects.update_or_create(
                slug=challenge["slug"],
                defaults={
                    "Category": challenge["category"],
                    "Title": challenge["title"],
                    "Created_by": author,
                    "Description": challenge["description"],
                    "Solution": challenge["solution"],
                    "default_code": challenge["default_code"],
                    "testcases_code": challenge["tests"],
                },
            )

        self.stdout.write(self.style.SUCCESS("Seeded starter challenges."))
