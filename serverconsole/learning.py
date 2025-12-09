# serverconsole/learning.py

LINUX_PATH = {
    "id": "linux_basics",
    "title": "Linux for Absolute Beginners",
    "tagline": "Learn Linux from scratch — no experience required.",
    "levels": [

        # -------------------------------------------------------
        # LEVEL 1
        # -------------------------------------------------------
        {
            "id": "level1",
            "title": "Level 1 · Getting Comfortable",
            "summary": "Learn what the terminal is and how to run commands.",
            "lessons": [

                {
                    "slug": "intro-terminal",
                    "title": "What is the Linux terminal?",
                    "goal": "Understand what the terminal is and what it is used for.",
                    "tasks": [
                        {"id": "l1_t1", "title": "Meet the terminal",
                         "instruction": "Just type: `echo Hello Linux` and press Enter.",
                         "check_type": "manual"}
                    ]
                },

                {
                    "slug": "first-commands",
                    "title": "Your first Linux commands",
                    "goal": "Run simple commands and clear the terminal screen.",
                    "tasks": [
                        {"id": "l1_t2", "title": "Print text",
                         "instruction": "Run: `echo I love Linux`",
                         "check_type": "manual"},
                        {"id": "l1_t3", "title": "Clear the screen",
                         "instruction": "Run: `clear`",
                         "check_type": "manual"},
                    ]
                },

                {
                    "slug": "getting-help",
                    "title": "Getting help",
                    "goal": "Learn to use built-in help like man pages.",
                    "tasks": [
                        {"id": "l1_t4", "title": "Read help",
                         "instruction": "Run: `ls --help` or `man ls`",
                         "check_type": "manual"},
                        {"id": "l1_t5", "title": "View command history",
                         "instruction": "Run: `history`",
                         "check_type": "manual"},
                    ]
                },
            ]
        },

        # -------------------------------------------------------
        # LEVEL 2
        # -------------------------------------------------------
        {
            "id": "level2",
            "title": "Level 2 · Finding Your Way",
            "summary": "Learn how to navigate folders and explore files.",
            "lessons": [

                {
                    "slug": "where-am-i",
                    "title": "Where am I?",
                    "goal": "Find your current location.",
                    "tasks": [
                        {"id": "l2_t1",
                         "title": "Print working directory",
                         "instruction": "Run: `pwd`",
                         "check_type": "manual"}
                    ]
                },

                {
                    "slug": "listing-files",
                    "title": "Listing files and folders",
                    "goal": "Learn how to see what exists.",
                    "tasks": [
                        {"id": "l2_t2",
                         "title": "Simple list",
                         "instruction": "Run: `ls`",
                         "check_type": "manual"},
                        {"id": "l2_t3",
                         "title": "Detailed list",
                         "instruction": "Run: `ls -la`",
                         "check_type": "manual"},
                    ]
                },

                {
                    "slug": "changing-directories",
                    "title": "Moving between folders",
                    "goal": "Navigate properly using cd.",
                    "tasks": [
                        {"id": "l2_t4",
                         "title": "Move to root",
                         "instruction": "Run: `cd /` then `pwd`",
                         "check_type": "manual"},
                        {"id": "l2_t5",
                         "title": "Move back home",
                         "instruction": "Run: `cd ~`",
                         "check_type": "manual"},
                    ]
                },

                {
                    "slug": "tab-history",
                    "title": "Tab completion & history",
                    "goal": "Use keyboard shortcuts effectively.",
                    "tasks": [
                        {"id": "l2_t6",
                         "title": "Use TAB",
                         "instruction": "Type `cd D` then press TAB to auto-complete.",
                         "check_type": "manual"},
                        {"id": "l2_t7",
                         "title": "Use arrow keys",
                         "instruction": "Press UP arrow to recall previous commands.",
                         "check_type": "manual"},
                    ]
                },

            ]
        },

        # -------------------------------------------------------
        # LEVEL 3
        # -------------------------------------------------------
        {
            "id": "level3",
            "title": "Level 3 · Creating & Managing Files",
            "summary": "Learn to manipulate real files safely.",
            "lessons": [

                {
                    "slug": "create-files",
                    "title": "Creating files",
                    "goal": "Create files using touch.",
                    "tasks": [
                        {"id": "l3_t1",
                         "title": "Create file",
                         "instruction": "Run: `touch practice.txt`",
                         "check_type": "manual"},
                    ]
                },

                {
                    "slug": "writing-files",
                    "title": "Writing text files",
                    "goal": "Put text inside a file.",
                    "tasks": [
                        {"id": "l3_t2",
                         "title": "Write text",
                         "instruction": "Run: `echo Linux rocks > practice.txt`",
                         "check_type": "manual"},
                        {"id": "l3_t3",
                         "title": "Read file",
                         "instruction": "Run: `cat practice.txt`",
                         "check_type": "manual"},
                    ]
                },

                {
                    "slug": "copy-move",
                    "title": "Copying & renaming",
                    "goal": "Duplicate and rename files safely.",
                    "tasks": [
                        {"id": "l3_t4",
                         "title": "Make a copy",
                         "instruction": "Run: `cp practice.txt backup.txt`",
                         "check_type": "manual"},
                        {"id": "l3_t5",
                         "title": "Rename a file",
                         "instruction": "Run: `mv backup.txt notes.txt`",
                         "check_type": "manual"},
                    ]
                },

                {
                    "slug": "deletion",
                    "title": "Deleting safely",
                    "goal": "Remove files without mistakes.",
                    "tasks": [
                        {"id": "l3_t6",
                         "title": "Delete a file",
                         "instruction": "Run: `rm -i notes.txt` (confirm the prompt)",
                         "check_type": "manual"},
                    ]
                },
            ],
        },

        # -------------------------------------------------------
        # LEVEL 4
        # -------------------------------------------------------
        {
            "id": "level4",
            "title": "Level 4 · Understanding the System",
            "summary": "Understand users, permissions, running programs, and resources.",
            "lessons": [

                {
                    "slug": "permissions",
                    "title": "File permissions",
                    "goal": "Learn how Linux protects files.",
                    "tasks": [
                        {"id": "l4_t1",
                         "title": "View permissions",
                         "instruction": "Run: `ls -l`",
                         "check_type": "manual"},
                        {"id": "l4_t2",
                         "title": "Change permissions",
                         "instruction": "Run: `chmod +x practice.txt`",
                         "check_type": "manual"},
                    ]
                },

                {
                    "slug": "processes",
                    "title": "Running processes",
                    "goal": "View and manage running tasks.",
                    "tasks": [
                        {"id": "l4_t3",
                         "title": "List processes",
                         "instruction": "Run: `ps aux | head`",
                         "check_type": "manual"},
                        {"id": "l4_t4",
                         "title": "Open live process view",
                         "instruction": "Run: `top` (Press q to quit)",
                         "check_type": "manual"},
                    ]
                },

                {
                    "slug": "system-info",
                    "title": "System information",
                    "goal": "Gather system resource data.",
                    "tasks": [
                        {"id": "l4_t5",
                         "title": "Who am I?",
                         "instruction": "Run: `whoami`",
                         "check_type": "manual"},
                        {"id": "l4_t6",
                         "title": "Check uptime",
                         "instruction": "Run: `uptime`",
                         "check_type": "manual"},
                        {"id": "l4_t7",
                         "title": "Check disk usage",
                         "instruction": "Run: `df -h`",
                         "check_type": "manual"},
                    ]
                },
            ]
        },

    ],
}
