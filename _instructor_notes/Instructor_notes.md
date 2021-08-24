# Setting Up a Development Environment: Instructor Notes

By the end of this workshop, students will be able to:
1. Recognize the role of a development environment and source code editor in computer programming
2. Become familiar with the [Visual Studio Code](https://code.visualstudio.com/) interface and tools
3. Run codes and debug in Visual Studio Code environment (in Python) 
4. Employ Extensions to connect Visual Studio Code with other development tools such as SSH, Git, and Docker

## Preparing to Teach

- My goal for this workshop was to present them a set of tools for streamlining code development and VS Code as the integrator.
- Uninstall VS Code and Python, make sure that you uninstall extensions and settings by deleting the whole folder in `%UserFolder%\AppData\Roaming\Code` and deleting extension folder in `%UserFolder%\. vscode`
- Follow the pattern of "Why someone wants to do a thing?" and then "How to do it?"
-  If there is enough time, show examples of what extensions do, via screenshots or clickthrough
- Tell people how to answer a question (via chat, unmute, ...)


## Steps during the workshop:

1. Introduction
2. What is a Development Environment? Have you any installed on your system and how you are using it right now
3. Tools of Development environment and code editors
4. What is VS Code? VS Code and Python installation on your system (20 mins)
5. VS Code interface
6. VS Code shortcuts (using multi curser for two exercises)
	a. Build one exercise with several columns and ask them to delete commas 
	b. Build another one in which they use special search for replacing words and then use multi curser
7. VS Code themes and settings (30 mins)
	a. "editor.rulers": [80,120] or menu>preferences>settings> search for ruler
8. Talk about extensions and how to look for extensions in VS Code
	a. What makes an extension good? (well maintained, used by a lot of people) 
	b. Talk about settings sync (for example, in a research project, all colleagues can sync their development environment while working on different machines)
	c. Show format on save for prettier
9. Install Python and introduce python extension + run/debug/ and test
	a. Talk about choosing the interpreter and virtual environment
	
	"python.formatting.provider": "black",
	
	b. Exercises on debugging and testing

10. Terminal -> changing the terminal and installing different terminal interpreters
11. Source Control -> link with UBC workshop (git and github) -> link with source control extension in VS Code
	a. Install Git and show how to add the files to Git
	b. Comparison of files using right click
12. Virtual environments, containerization, docker workshop by UBC, managing containers and ssh into containers

## Extra resources

- Install and customize (user interface, setup, keyboard shortcuts and key binding extensions): [https://code.visualstudio.com/docs/introvideos/basics](https://code.visualstudio.com/docs/introvideos/basics)

- Using keyboard extensions for editing and viewing code: [https://code.visualstudio.com/docs/editor/codebasics](https://code.visualstudio.com/docs/editor/codebasics)

- [Version control in VS Code](https://code.visualstudio.com/docs/editor/versioncontrol)

- [Container extension in VS Code](https://code.visualstudio.com/docs/containers/overview)

- [Setting up a Python development environment in VS Code](https://www.youtube.com/watch?v=-nh9rCzPJ20)