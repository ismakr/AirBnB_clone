#!/usr/bin/python3
""" contains the entry point of
the command interprete"""
import cmd


class HBNBCommand(cmd.Cmd):
    """command interpreter"""

    prompt = "(hbnb)"

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """quit command to exit the program"""
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
