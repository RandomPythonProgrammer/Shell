import cmd
import os
import subprocess
import shutil
from zipfile import ZipFile

os.system("")


class style:
    YELLOW = '\033[33m'
    WHITE = '\033[37m'
    RESET = '\033[0m'


class Shell(cmd.Cmd):
    intro = "Bad shell by RandomPythonProgrammer:"
    style = style.YELLOW
    current_directory = "C:\\"
    prompt = style + f"{current_directory}>"

    def postcmd(self, stop, line):
        self.style = style.YELLOW
        self.prompt = self.style + f"{self.current_directory}>"
        return stop

    def precmd(self, line):
        self.style = style.RESET
        line = line.replace("/", "\\")
        return line

    def do_dir(self, line):
        """Show current working directory"""
        print(self.style + "\n".join(os.listdir(self.current_directory)))

    def do_cd(self, line):
        """Change directory"""
        if line == "..":
            os.chdir("..")
            self.current_directory = os.getcwd()
        else:
            try:
                os.chdir(line)
                self.current_directory = os.getcwd()
            except FileNotFoundError as e:
                try:
                    os.chdir("\\" + line)
                    self.current_directory = os.getcwd()
                except FileNotFoundError as e:
                    print(style.RESET, e)
                except OSError as e:
                    print(style.RESET, e)

    def do_del(self, line):
        """Deletes file"""
        try:
            os.remove(line)

            print(self.style + "File removed")
        except FileNotFoundError as e:
            try:
                os.remove("\\" + line)

                print(self.style + "File removed")
            except FileNotFoundError as e:
                print(style.RESET, e)
            except OSError as e:
                print(style.RESET, e)

    def do_ren(self, line):
        """Rename file"""
        file, name = tuple(line.split(" "))
        try:
            os.rename(file, file.replace(os.path.basename(file), name))

            print(self.style + "File renamed")
        except FileNotFoundError as e:
            try:
                os.rename("\\" + file, "\\" + file.replace(os.path.basename(file), name))

                print(self.style + "File renamed")
            except FileNotFoundError as e:
                print(style.RESET, e)
            except OSError as e:
                print(style.RESET, e)

    def do_mkdir(self, line):
        "Creates directory"
        try:
            os.mkdir(line)

            print(self.style + "Directory created")
        except FileNotFoundError as e:
            try:
                os.mkdir("\\" + line)

                print(self.style + "Directory created")
            except FileNotFoundError as e:
                print(style.RESET, e)
            except OSError as e:
                print(style.RESET, e)

    def do_echo(self, line):
        "Creates file"
        try:
            with open(line, "x") as file:
                pass

            print(self.style + "File created")
        except FileNotFoundError as e:
            try:
                with open("\\" + line, "x") as file:
                    pass

                print(self.style + "File created")
            except FileNotFoundError as e:
                print(style.RESET, e)
            except OSError as e:
                print(style.RESET, e)

    def do_rd(self, line):
        "Deletes directory"
        try:
            os.rmdir(line)

            print(self.style + "Directory removed")
        except FileNotFoundError as e:
            try:
                os.rmdir("\\" + line)

                print(self.style + "Directory removed")
            except FileNotFoundError as e:
                print(style.RESET, e)
            except OSError as e:
                print(style.RESET, e)

    def do_move(self, line):
        "Moves file"
        start, end = tuple(line.split(" "))
        try:
            shutil.move(start, f"{end}\\{os.path.basename(start)}")

            print(self.style + "File moved")
        except FileNotFoundError as e:
            try:
                shutil.move("\\" + start, f"\\{end}\\{os.path.basename(start)}")

                print(self.style + "File moved")
            except FileNotFoundError as e:
                print(style.RESET, e)
            except OSError as e:
                print(style.RESET, e)

    def do_moves(self, line):
        "Moves all files from directory"
        start, end = tuple(line.split(" "))
        try:
            for file in os.listdir(start):
                shutil.move(f"{start}\\{file}", f"{end}\\{file})")

            print(self.style + "Files moved")
        except FileNotFoundError as e:
            try:
                for file in os.listdir(start):
                    shutil.move(f"\\{start}\\{file}", f"\\{end}\\{file}")

                print(self.style + "Files moved")
            except FileNotFoundError as e:
                print(style.RESET, e)
            except OSError as e:
                print(style.RESET, e)

    def do_start(self, line):
        "Runes file"
        try:
            subprocess.Popen(line)

            print(self.style + "File started")
        except FileNotFoundError as e:
            try:
                subprocess.Popen("\\" + line)

                print(self.style + "File started")
            except FileNotFoundError as e:
                print(style.RESET, e)
            except OSError as e:
                print(style.RESET, e)

    def do_zip(self, line):
        "Creates zip file"
        try:
            try:
                filepath, location = tuple(line.split(" "))
            except:
                filepath = line
                location = self.current_directory

            try:
                with ZipFile(f"{location}\\{filepath}.zip", "x") as zip_file:
                    for file in os.listdir(filepath):
                        zip_file.write(f"{filepath}\\{file}")

                print(self.style + "Files zipped")
            except (FileNotFoundError, OSError) as e:
                try:
                    with ZipFile(f"\\{location}\\{filepath}.zip", "x") as zip_file:
                        for file in os.listdir(filepath):
                            zip_file.write(f"\\{filepath}\\{file}")

                    print(self.style + "Files zipped")
                except (FileNotFoundError, OSError) as e:
                    try:
                        print(filepath)
                        file_ = filepath.split("\\")[-1]
                        print(file_)
                        with ZipFile(f"{location}\\{file_}.zip", "x") as zip_file:
                            for file in os.listdir(filepath):
                                zip_file.write(f"{filepath}\\{file}")

                    except FileNotFoundError as e:
                        print(style.RESET, e)
                    except OSError as e:
                        print(style.RESET, e)
        except FileNotFoundError:
           pass

    def do_extract(self, line):
        "Extracts zip file"
        try:
            file, location = tuple(line.split(" "))
        except:
            file = line
            location = self.current_directory
        try:
            with ZipFile(file + ".zip") as zip_file:
                zip_file.extractall(location)

            print(self.style + "Files extracted")
        except FileNotFoundError as e:
            try:
                with ZipFile(f"\\{file}.zip") as zip_file:
                    zip_file.extractall(location)

                print(self.style + "Files extracted")
            except FileNotFoundError as e:
                print(style.RESET, e)
            except OSError as e:
                print(style.RESET, e)

    def do_exit(self, line):
        "Exits"
        return True

    def do_info(self, line):
        "Information"
        print("Github page: https://github.com/RandomPythonProgrammer/BadShell")


if __name__ == '__main__':
    Shell().cmdloop()
