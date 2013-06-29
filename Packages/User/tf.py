import sublime, sublime_plugin
import subprocess


class CheckoutCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.insert(edit, 0, "Hello, World!")
        tf_path = 'c:\\Program Files (x86)\\Microsoft Visual Studio 11.0\\Common7\\IDE\\TF.exe'
        try:
            subprocess.check_call([tf_path, "out", self.view.file_name()], stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            sublime.messageBox(e.output)
