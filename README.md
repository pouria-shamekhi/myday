
# MyDay - A To-Do List Application with Calendar

## Overview
**MyDay** is a PyQt5-based desktop application that combines a simple to-do list with a customizable calendar. Users can organize their tasks, manage daily schedules, and customize the application's theme (dark mode or light mode). The application is designed to provide a seamless user experience with a clean and modern interface.

## Features
- **To-Do List Management**:
  - Add, edit, and delete tasks.
  - Mark tasks as completed or uncompleted.
  - Automatically save tasks to a JSON file.
  
- **Integrated Calendar**:
  - Navigate through months using arrow buttons.
  - Highlight the current day.
  - Select any day to view or manage tasks for that date.

- **Customization**:
  - Switch between dark mode and light mode through the settings dialog.
  - Persistent theme preferences saved in a `settings.json` file.

- **Modern User Interface**:
  - Built with PyQt5 for a sleek and responsive design.
  - Sidebar toggle for better focus.

## Requirements
To run the project, you need the following:

- **Python**: 3.7 or later
- **Libraries**:
  - PyQt5

Install the required libraries using:
```bash
pip install PyQt5
```

## How to Run
1. Clone or download the repository.
2. Navigate to the project directory.
3. Run the main Python file:
   ```bash
   python main.py
   ```

## Project Structure
```
project/
├── main.py          # Main entry point of the application
├── pyx1.py          # Dark mode implementation
├── pyx1_light.py    # Light mode implementation
├── settings.py      # Settings dialog and theme management
├── settings.json    # Stores user preferences (theme)
├── icons/           # Contains application icons
│   ├── Notebook.png
│   ├── Notebookl.png
│   └── trash_icon.png
└── todos.json       # Stores user tasks
```

## Customization
- **Change Theme**:
  Open the settings dialog from the main application window and choose between "Dark Mode" or "Light Mode".

- **Modify Icons**:
  Replace files in the `icons/` folder with your preferred images.

## Building the Application
To convert the application into a standalone executable file:
1. Install **PyInstaller**:
   ```bash
   pip install pyinstaller
   ```
2. Build the executable:
   ```bash
   pyinstaller --onefile --noconsole --icon="icons/Notebook.ico" main.py
   ```
3. The executable will be located in the `dist/` folder.

## Known Issues
- Ensure that `settings.json` and `todos.json` are writable; otherwise, changes may not persist.
- Some systems might require clearing the icon cache to properly display the custom application icon.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- **PyQt5** for providing a robust framework for GUI development.
- Community contributions for code optimization and feedback.

---

Feel free to suggest improvements or report bugs via the project's issue tracker.

